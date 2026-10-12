"""热门模型：Hugging Face 和魔搭 ModelScope 上正在上升的模型。

两个平台的接口都不需要密钥。Hugging Face 的热门榜里有大量第三方重新打包的量化版
和“去审查”版本，这里过滤掉，只留原始发布。国内访问 Hugging Face 不稳定，
所以每条都附一个镜像站链接；魔搭的链接国内可以直接打开。
"""

from __future__ import annotations

from typing import Any

from ..models import Item
from ..textutil import log_scale
from .base import Context

NAME = "hot_models"
TITLE = "热门模型"

HF_API = "https://huggingface.co/api/models"
MODELSCOPE_API = "https://modelscope.cn/openapi/v1/models"
_UNWANTED = ("uncensored", "abliterat", "nsfw", "heretic", "not-for-all-audiences", "face-swap", "faceswap")
_TASKS = {
    "text-generation": "文本生成",
    "image-text-to-text": "图文理解",
    "any-to-any": "多模态",
    "text-to-image": "文生图",
    "image-to-image": "图像编辑",
    "text-to-video": "文生视频",
    "image-to-video": "图生视频",
    "text-to-speech": "语音合成",
    "automatic-speech-recognition": "语音识别",
    "feature-extraction": "向量表示",
    "sentence-similarity": "向量表示",
    "text-to-audio": "音频生成",
    "robotics": "机器人",
}


def _describe(task: str, licence: str) -> str:
    parts = [f"{_TASKS.get(task, task)}模型" if task else "", f"许可证 {licence}" if licence else ""]
    return "，".join(p for p in parts if p)


def expand(config: dict[str, Any]) -> list[tuple[str, str, dict[str, Any]]]:
    """两个平台分开抓、分开记录，一个不通不影响另一个。"""
    return [
        (f"{NAME}:{site}", title, {**config, "site": site})
        for site, title in (("huggingface", "Hugging Face 热门模型"), ("modelscope", "魔搭 ModelScope 热门模型"))
        if config.get(site, True)
    ]


def _huggingface(config: dict[str, Any], ctx: Context) -> list[Item]:
    want = int(config.get("max_items", 8))
    models = ctx.http.get_json(HF_API, params={"sort": "trendingScore", "limit": want * 3 + 10})
    if not isinstance(models, list) or not models:
        raise RuntimeError("接口没有返回模型列表")
    items: list[Item] = []
    for model in models:
        model_id = model.get("id") or ""
        tags = model.get("tags") or []
        owner = model_id.split("/")[0]
        quantized_from = next((t.split(":", 2)[2] for t in tags if t.startswith("base_model:quantized:")), "")
        if quantized_from and quantized_from.split("/")[0] != owner:
            continue  # 别人模型的量化重打包；同一作者自己发的量化版往往就是官方版本，保留
        if not model_id or any(word in " ".join([model_id, *tags]).lower() for word in _UNWANTED):
            continue
        licence = next((t.split(":", 1)[1] for t in tags if t.startswith("license:")), "")
        likes = int(model.get("likes") or 0)
        trending = model.get("trendingScore") or 0
        items.append(
            Item(
                title=model_id,
                url=f"https://huggingface.co/{model_id}",
                source=NAME,
                section="opensource",
                via="Hugging Face 热门模型",
                # 不填发布时间：上榜的“新”不等于建库时间，和 GitHub Trending 一样按中间值算新鲜度
                summary=_describe(model.get("pipeline_tag") or "", licence),
                heat=log_scale(trending, 3000) if trending else log_scale(likes, 2000),
                metrics={"likes": likes, "downloads": int(model.get("downloads") or 0)},
                extra={"links": [["国内镜像", f"https://hf-mirror.com/{model_id}"]]},
            )
        )
        if len(items) >= want:
            break
    return items


def _modelscope(config: dict[str, Any], ctx: Context) -> list[Item]:
    data = ctx.http.get_json(MODELSCOPE_API, params={"page_size": 20, "sort": "default"})
    models = ((data or {}).get("data") or {}).get("models")
    if not data or not data.get("success") or not models:
        raise RuntimeError(f"接口返回异常：{str(data)[:120]}")
    items: list[Item] = []
    for model in models[: int(config.get("max_items", 8))]:
        model_id = model.get("id") or ""
        if not model_id or any(word in model_id.lower() for word in _UNWANTED):
            continue
        likes = int(model.get("likes") or 0)
        task = (model.get("tasks") or [""])[0]
        items.append(
            Item(
                title=model_id,
                url=f"https://www.modelscope.cn/models/{model_id}",
                source=NAME,
                section="opensource",
                via="魔搭 ModelScope 热门模型",
                summary=model.get("description") or _describe(task if isinstance(task, str) else "", ""),
                heat=log_scale(likes, 2000),
                metrics={"likes": likes, "downloads": int(model.get("downloads") or 0)},
            )
        )
    return items


def fetch(config: dict[str, Any], ctx: Context) -> list[Item]:
    items = _modelscope(config, ctx) if config.get("site") == "modelscope" else _huggingface(config, ctx)
    weight = float(config.get("weight", 0.5))
    for item in items:
        item.weight = weight
    return items
