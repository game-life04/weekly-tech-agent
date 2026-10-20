"""把快讯的公众号排版版（.html）截成长图（同名的 .jpg），方便大家在 GitHub 上看、转发到微信。

由定时任务在生成快讯之后运行（见 .github/workflows/daily.yml）。截图要用 Chrome（或 Edge）、中文字体和 Pillow，
它们都不是项目本身的依赖：缺了的话这一步失败，但不影响日报和快讯照常提交。

    python -m wta.longshot --list   # 列出要截图的快讯：还没有长图的，加上这次改过的
    python -m wta.longshot          # 截图

截图的宽度是 720 像素（和公众号正文差不多宽），按 1.5 倍保存成 1080 像素宽的 JPEG（手机屏幕的宽度，
放大也看得清），每张约 0.4 MB，一年下来仓库大约多 170 MB。
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

WIDTH, SCALE, QUALITY = 720, 1.5, 72
HEIGHT = 9000  # 截图窗口的高度（CSS 像素）。一期快讯一般在 5000 以内，比这还长的只截前面这么多
BROWSERS = (
    "google-chrome",
    "google-chrome-stable",
    "chromium",
    "chromium-browser",
    "msedge",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
)


def pages(root: Path) -> list[Path]:
    """仓库里所有快讯的公众号排版版。"""
    return sorted(root.glob("weekly/*.html")) + sorted(root.glob("daily/*/*-kuaixun.html"))


def edited(root: Path) -> set[Path]:
    """这次运行改过（或新建）的 .html。不在 git 仓库里时返回空集合。"""
    try:
        out = subprocess.run(
            ["git", "status", "--porcelain", "-uall", "--", "daily", "weekly"],
            cwd=root,
            capture_output=True,
            text=True,
            check=True,
        ).stdout
    except (OSError, subprocess.CalledProcessError):
        return set()
    return {(root / line[3:].strip()).resolve() for line in out.splitlines() if line.strip().endswith(".html")}


def targets(root: Path, changed: set[Path]) -> list[Path]:
    """要截图的快讯：还没有长图的，和改过的。"""
    return [page for page in pages(root) if page.resolve() in changed or not page.with_suffix(".jpg").is_file()]


def browser() -> str | None:
    for name in BROWSERS:
        found = shutil.which(name) or (name if Path(name).is_file() else None)
        if found:
            return found
    return None


def shoot(page: Path, program: str) -> Path:
    """截一张长图，存成 page 旁边同名的 .jpg。"""
    from PIL import Image, ImageChops  # 只有截图时才需要

    out = page.with_suffix(".jpg")
    with tempfile.TemporaryDirectory() as folder:
        raw = Path(folder) / "raw.png"
        command = [
            program,
            "--headless=new",
            "--disable-gpu",
            "--hide-scrollbars",
            f"--force-device-scale-factor={SCALE}",
            f"--window-size={WIDTH},{HEIGHT}",
            f"--screenshot={raw}",
            page.resolve().as_uri(),
        ]
        try:
            subprocess.run(command, check=True, capture_output=True, timeout=120)
        except subprocess.CalledProcessError:
            # 有的 Linux（例如 Ubuntu 24.04）不让浏览器建沙箱。截的是自己生成的静态页面（没有脚本，
            # 外部文字都转义过），关掉沙箱再试一次
            subprocess.run([*command[:1], "--no-sandbox", *command[1:]], check=True, capture_output=True, timeout=120)
        with Image.open(raw) as shot:
            image = shot.convert("RGB")
    box = ImageChops.difference(image, Image.new("RGB", image.size, "white")).getbbox()
    bottom = image.size[1] if box is None else min(image.size[1], box[3] + int(40 * SCALE))  # 留一点白边
    if box and box[3] >= image.size[1] - 2:
        print(f"注意：{page} 比 {HEIGHT} 像素还长，长图只截了前面这么多", file=sys.stderr)
    image.crop((0, 0, image.size[0], bottom)).save(out, "JPEG", quality=QUALITY, optimize=True, progressive=True)
    return out


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python -m wta.longshot", description="把快讯截成长图")
    parser.add_argument("--root", type=Path, default=Path("."), help="仓库目录（默认是当前目录）")
    parser.add_argument("--list", action="store_true", help="只列出要截图的快讯，不截图")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    todo = targets(root, edited(root))
    if args.list:
        for page in todo:
            print(page.relative_to(root).as_posix())
        return 0
    if not todo:
        print("没有需要截图的快讯。")
        return 0
    program = browser()
    if program is None:
        print("找不到 Chrome 或 Edge，没法截图。", file=sys.stderr)
        return 1
    for page in todo:
        print(f"截图：{shoot(page, program).relative_to(root).as_posix()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
