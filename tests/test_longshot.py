"""长图：哪些快讯要截图。截图本身要用浏览器，只在定时任务里跑，这里不测。"""

from __future__ import annotations

from wta import longshot


def test_targets_are_new_or_edited_issues(tmp_path):
    for name in ("weekly/2026-W41.html", "weekly/2026-W42.html", "daily/2026/2026-10-20-kuaixun.html"):
        (tmp_path / name).parent.mkdir(parents=True, exist_ok=True)
        (tmp_path / name).write_text("<p>快讯</p>", encoding="utf-8")
    (tmp_path / "weekly/2026-W41.jpg").write_bytes(b"jpg")
    (tmp_path / "weekly/2026-W42.jpg").write_bytes(b"jpg")
    (tmp_path / "daily/2026/2026-10-20.md").write_text("日报", encoding="utf-8")  # 日报本身不截图

    found = longshot.targets(tmp_path, set())
    assert [page.relative_to(tmp_path).as_posix() for page in found] == ["daily/2026/2026-10-20-kuaixun.html"]
    edited = {(tmp_path / "weekly/2026-W42.html").resolve()}
    assert len(longshot.targets(tmp_path, edited)) == 2  # 改过的也要重新截


def test_list_prints_relative_paths(tmp_path, capsys, monkeypatch):
    (tmp_path / "weekly").mkdir()
    (tmp_path / "weekly/2026-W42.html").write_text("<p>快讯</p>", encoding="utf-8")
    monkeypatch.setattr(longshot, "edited", lambda root: set())
    assert longshot.main(["--root", str(tmp_path), "--list"]) == 0
    assert capsys.readouterr().out == "weekly/2026-W42.html\n"
