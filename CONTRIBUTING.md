# 参与贡献

欢迎一起维护这个项目。最适合上手的第一件事是**加一个信息来源**。

## 准备环境

需要 Python 3.11 或更高版本。

```bash
git clone https://github.com/game-life04/weekly-tech-agent.git
cd weekly-tech-agent
python -m venv .venv                 # 建一个虚拟环境，装的东西不会影响系统
source .venv/bin/activate            # Windows 上是 .venv\Scripts\activate
pip install -r requirements-dev.txt
python -m pytest                     # 跑测试（不访问网络，一两秒跑完）
ruff check . && ruff format .
```

在中国大陆访问境外来源需要代理，设置环境变量 `HTTPS_PROXY`。读取 GitHub 接口建议设置 `GITHUB_TOKEN`，否则每小时只有 60 次额度。

## 加一个 RSS 订阅（不用写代码）

1. 找到网站的订阅地址。尽量用网站自己提供的，不要用第三方中转。
2. 在 `config.yaml` 的 `sources.rss.feeds` 里加一行。可用的选项写在 [wta/sources/rss.py](wta/sources/rss.py) 开头，常用的是：

   ```yaml
   - { name: 显示的名字, url: 'https://example.com/feed.xml', weight: 0.6, max_items: 2 }
   ```

   综合类媒体加上 `only_related: true`，只取和 AI 相关的条目；中文网站加上 `naive_offset: 8`。
3. 运行 `python -m wta check rss:显示的名字`，只测试这一个订阅。输出里每条都带发布时间（北京时间），确认它和网站上的一致。
   显示“0 条”通常是因为最近 48 小时没有新文章：把这个订阅的 `max_age_hours` 临时调大（比如 720）再跑一次，能看到内容就说明没问题。日期全部解析不了、订阅地址返回的是网页时，会直接显示失败原因。
4. 运行 `python -m pytest`。其中有一项测试专门读取 `config.yaml`，写错的地方（漏了 name、正则有误）会在这里报出来。

## 加一种新的来源（写一个文件）

1. 在 `wta/sources/` 下新建一个文件，照着 [base.py](wta/sources/base.py) 开头的约定提供 `NAME`、`TITLE` 和 `fetch(config, ctx)`。[qbitai.py](wta/sources/qbitai.py) 是最短的例子。
2. 在 `wta/sources/__init__.py` 里登记，在 `config.yaml` 的 `sources` 下加上它的配置和 `enabled: true`。
3. 在 `tests/test_sources.py` 里加测试：用 `fakes.context` 喂一份预设的返回内容，检查解析结果和出错时的行为。测试不能访问网络。
4. 运行 `python -m wta check 你的来源名` 看真实效果。

写来源时请注意：

- 优先用官方接口或官方订阅源，不要硬爬网页。
- 网络请求一律通过 `ctx.http`，它带有统一的标识、超时和重试。
- 抓不到内容时直接抛异常，不要悄悄返回空列表。调度器会记录失败并继续运行其他来源。
- 只取标题、链接、发布时间和简短的简介，不保存全文。
- 没有发布时间的内容不要当作新内容。
- `metrics` 的值必须是数字，`published` 用 `dates.to_iso(...)` 转换。字段约定写在 [wta/sources/base.py](wta/sources/base.py) 开头。

## 调整每周快讯（不用写代码）

快讯的设置在 `config.yaml` 的 `kuaixun` 下（`daily` 里的是每日快讯单独的设置）：`caps` 是每个栏目最多登几条，`policy.keywords` 决定哪些政策条目算相关，
`events.subjects` 和 `events.ranks` 决定预告哪些领域、哪几类的会议，`club.exclude` 是不计入俱乐部统计的仓库。
改完可以把 `data/` 复制到仓库外面的目录，用 `python -m wta --root 那个目录 kuaixun --no-llm`（每日快讯加 `--day 日期`）看效果。

## 提交规范

- 分支：`feat/…`、`fix/…`、`docs/…`、`ci/…`、`chore/…`，通过 PR 合并。
- 提交信息用英文，格式 `type(scope): summary`，例如 `feat(sources): add ModelScope trending models`。type 用 feat、fix、docs、refactor、test、chore、ci。
- 提交前确认 `python -m pytest`、`ruff check .` 和 `ruff format --check .` 都通过。
- `daily/`、`weekly/`、`data/` 和 README 里“最新一期”那一段由定时任务生成，不要手动修改。PR 里带了 `data/` 的改动，CI 会直接失败。
- `config.yaml` 里 `llm.providers` 的改动（服务地址、密钥变量名）按代码改动的标准来审：它决定密钥发往哪里。

## 使用 AI 工具

本项目遵循[华科开放原子开源俱乐部的 AI 使用准则](https://github.com/hust-open-atom-club/docs/blob/master/%E5%8D%8E%E7%A7%91%E5%BC%80%E6%94%BE%E5%8E%9F%E5%AD%90%E5%BC%80%E6%BA%90%E4%BF%B1%E4%B9%90%E9%83%A8AI%E4%BD%BF%E7%94%A8%E5%87%86%E5%88%99.md)：

- 用 AI 工具辅助完成的提交，在提交信息末尾加一行 `Assisted-by: <工具> + <模型>`，例如 `Assisted-by: Claude Code + Claude Opus 5.5`。
- AI 工具不添加 `Signed-off-by`；这一行只能由人自己添加。
- AI 生成的代码和文字，提交前要由人看过并确认。
