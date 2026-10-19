# 给 AI 编程助手的说明

这个仓库每天由 GitHub Actions 自动收集 AI / 大模型领域的内容并生成日报，每周一再生成上一周的快讯。动手前请先读 [README.md](README.md) 的“关于这个项目”和 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 必须遵守

- 提交信息用英文，格式 `type(scope): summary`；由 AI 辅助完成的提交在末尾加一行 `Assisted-by: <工具> + <模型>`。不要添加 `Signed-off-by`。
- 不要手动修改 `daily/`、`weekly/`、`data/` 和 README 里 `wta:latest` 两个标记之间的内容，它们由定时任务生成。
- 不要把任何密钥写进仓库。大模型密钥只通过环境变量读取。
- 改完代码后运行 `python -m pytest`、`ruff check .` 和 `ruff format .`，全部通过再提交。
- 测试不能访问网络：用 `tests/fakes.py` 里的假网络和假大模型。

## 代码约定

- Python 3.11+，依赖只有 requests 和 PyYAML。新增依赖要有充分理由。
- 注释和文档字符串用中文，写清楚“为什么”；标识符用英文。
- 外部来的文字（标题、简介、`wta/excerpt.py` 取的原文摘录、大模型的输出）一律当作不可信内容：进页面前经过 `render.md_escape` / `render.md_url`，大模型的输出经过 `editor.plain` 和 `editor.ungrounded`。
- 任何一个来源失败、大模型失败，都不能让当天的日报和每周的快讯出不来。
- 快讯（`wta/kuaixun.py`）里，大模型只写栏目、标题和正文；日期、链接、俱乐部统计和会议截稿时间由程序写。页面只凭 `data/weekly/` 里存的数据生成，`python -m wta render` 不需要网络。
