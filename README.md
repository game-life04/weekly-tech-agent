# 每周科技收集 Agent

[![Daily digest](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml)
[![CI](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

每天自动收集 AI 和大模型领域值得看的动态、开源项目和论文，整理成一份日报，每周再汇总成周报。内容直接放在这个仓库里，打开就能看。

<!-- wta:latest:start -->

## 最新一期 · 2026-10-12（周一）

> 收录 **21** 条：🗞️ AI 动态 8 · 🛠️ 开源圈 8 · 📄 前沿论文 5<br>
> [本周周报](weekly/2026-W42.md) · [往期日报](daily/README.md) · [往期周报](weekly/README.md) · [单独打开这一期](daily/2026/2026-10-12.md)

### 🗞️ AI 动态

**1. [LLM 能力共识的差距正在扩大](https://twitter.com/karpathy/status/2109361546505966046)**<br><sub>Hacker News · 392 分 · 549 评论 · #行业动态 · 原题：The gap in shared understanding of LLM capability is widening · [讨论](https://news.ycombinator.com/item?id=50047422)</sub>

**2. [构建你自己的决策模型](https://nishtahir.com/build-your-own-decision-model/)**<br><sub>Hacker News · 455 分 · 102 评论 · #行业动态 · 原题：Build your own decision model · [讨论](https://news.ycombinator.com/item?id=50037949)</sub>

**3. [Talorys – Cloudflare 免费层上的自托管个人 AI 智能体](https://github.com/rociiu/talorys)**<br>在 Cloudflare 账户中部署个人 AI 智能体，支持聊天、记忆、任务和提醒，无需遥测数据。<br><sub>Hacker News · 783 ★ · 323 分 · 150 评论 · 同时见于 GitHub 新项目 · #智能体 #开源工具 · 原题：Talorys – A self-hosted personal AI agent on Cloudflare's free tier · [讨论](https://news.ycombinator.com/item?id=50031614)</sub>

**4. [华为AI靠RSI通关25款游戏！操作次数比人类少56%](https://www.qbitai.com/2026/10/502654.html)**<br>游戏打到21:0，AI甚至不用再调用大模型了<br><sub>量子位 · #游戏AI #华为 #RSI</sub>

**5. [500B tokens 后：让 AI 智能体反编译第一人称射击游戏](https://momo5502.com/posts/2026-10-09-game-decompilation/)**<br><sub>Hacker News · 189 分 · 137 评论 · #智能体 #行业动态 · 原题：500B tokens later: Letting AI agents decompile a first-person shooter · [讨论](https://news.ycombinator.com/item?id=50039092)</sub>

**6. [智谱新模型，490 tokens/s！](https://www.qbitai.com/2026/10/502649.html)**<br>GLM「速度仙人」来了？<br><sub>量子位 · #智谱 #模型发布 #推理速度</sub>

**7. [字节发现 DeepSeek 隐藏 Bug，加点空格，模型翻车](https://www.leiphone.com/category/yanxishe/zm33Zeu88CNbEPMx.html)**<br>字节团队发现 DeepSeek V4 模型存在“神鬼二象性”问题，因分块 KV Cache 压缩导致位置敏感，关键信息可能被忽略。<br><sub>雷峰网 · #模型发布 #Bug #行业动态</sub>

**8. [刚刚，AI圈爆出王炸！实现「万物共脑」，连大脑带具身越狱到现实](https://aiera.com.cn/2026/10/12/other/admin/118175/%e5%88%9a%e5%88%9a%ef%bc%8cai%e5%9c%88%e7%88%86%e5%87%ba%e7%8e%8b%e7%82%b8%ef%bc%81%e5%ae%9e%e7%8e%b0%e3%80%8c%e4%b8%87%e7%89%a9%e5%85%b1%e8%84%91%e3%80%8d%ef%bc%8c%e8%bf%9e%e5%a4%a7%e8%84%91%e5%b8%a6/)**<br>物理AI需要可靠大脑、执行系统和物理身体。<br><sub>新智元 · #物理AI #具身智能 #行业动态</sub>

### 🛠️ 开源圈

**1. [morluto/rea](https://github.com/morluto/rea)**<br>使用智能体从应用行为到原生二进制文件进行逆向工程。<br><sub>GitHub Trending · 今日 +25.6k ★ · 118.5k ★ · #开源工具 #智能体</sub>

**2. [Niko1221/Strata](https://github.com/Niko1221/Strata)**<br>在消费级硬件上运行 Qwen3.8-Flash-Next，支持本地 OpenAI/Anthropic API。<br><sub>GitHub 新项目 · 21.9k ★ · #开源工具 #推理加速</sub>

**3. [huggingface/transformers](https://github.com/huggingface/transformers)**<br>支持文本、视觉、音频和多模态模型推理与训练的模型定义框架。<br><sub>GitHub Trending · 今日 +501 ★ · 167.5k ★ · #开源工具 #框架</sub>

**4. [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio)**<br>完全本地化的 ElevenLabs 开源替代品，支持 646 种语言的语音克隆和视频配音。<br><sub>GitHub Trending · 今日 +1.2k ★ · 59.2k ★ · #开源工具 #语音</sub>

**5. [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)**<br>为 Claude Code、GitHub Copilot 等工具提供 44 种类型的编辑图表设计。<br><sub>GitHub Trending · 今日 +1.1k ★ · 51k ★ · #开源工具 #工具</sub>

**6. [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast)**<br>Fastest and cheapest web agent<br><sub>GitHub 新项目 · 22.7k ★</sub>

**7. [open-webui/open-webui v0.12.0](https://github.com/open-webui/open-webui/releases/tag/v0.12.0)**<br>次版本更新<br><sub>GitHub 版本发布 · #开源工具 #语音 #版本发布</sub>

**8. [xorbitsai/inference v4.0.0](https://github.com/xorbitsai/inference/releases/tag/v4.0.0)**<br>主版本更新<br><sub>GitHub 版本发布</sub>

### 📄 前沿论文

**1. [重新思考跨分词器的策略蒸馏：从对齐覆盖到监督可靠性](https://arxiv.org/abs/2610.08448)**<br>研究跨分词器策略蒸馏中，扩展对齐覆盖是否有助于提升学习效果。<br><sub>Hugging Face 热门论文 · 210 赞 · #论文 #模型蒸馏 · 原题：Rethinking Cross-Tokenizer On-Policy Distillation: From Alignment Coverage to Supervision Reliability</sub>

**2. [Kandinsky 6.0 Video：同步视频与音频生成模型](https://arxiv.org/abs/2610.05608)**<br>Kandinsky 6.0 Video 是一组用于同步文本到音频视频生成的扩散模型，包含 3B 和 29B 参数版本，支持 5 秒视频和 44 kHz 音频生成。<br><sub>Hugging Face 热门论文 · 169 赞 · #模型发布 #视频生成 #音频生成 · 原题：Kandinsky 6.0 Video: Foundation Models for Synchronized Video and Audio Generation · [代码](https://github.com/kandinskylab/kandinsky-6)</sub>

**3. [Long-WAM：扩展世界-动作模型的上下文](https://arxiv.org/abs/2610.10528)**<br>Long-WAM 是一个在实时控制约束下扩展因果世界-动作模型上下文的框架，发现更长历史在预训练自回归视频基础上效果更好。<br><sub>Hugging Face 热门论文 · 106 赞 · #论文 #机器人 #上下文扩展 · 原题：Long-WAM: Scaling the Context of World-Action Models · [代码](https://github.com/NVlabs/LongLive)</sub>

**4. [Learn2Play Bench：LLM智能体在陌生环境中的学习表现如何？](https://arxiv.org/abs/2610.08215)**<br>提出新基准测试，评估LLM智能体在动态陌生环境中的学习与适应能力。<br><sub>arXiv · 智能体 · 136 赞 · 同时见于 Hugging Face 热门论文 · #论文 #智能体 #评测 · 原题：Learn2Play Bench: How Well Do LLM Agents Learn from Experience in Unfamiliar Environments? · [代码](https://github.com/liushiliushi/Learn2Play-Bench)</sub>

**5. [nanoMuse：面向个人设备的开源个人智能体](https://arxiv.org/abs/2610.08699)**<br>定义个人智能体概念，探讨其在账户、设备、记忆和交互方面的实现。<br><sub>arXiv · 智能体 · 104 赞 · 同时见于 Hugging Face 热门论文、arXiv · 高效推理 · #论文 #智能体 · 原题：nanoMuse: An Open-Source Personal Agent for Every Device You Own · [代码](https://github.com/nano-muse/nanoMuse)</sub>

<sub>中文标题和摘要由 AI 生成（glm-4.7-flash），可能有误，请以原文为准。 本期候选来自：Hacker News 46、RSS 订阅 33（40 个源）、量子位 5、GitHub Trending 33、GitHub 新项目 274、GitHub 版本发布 4、热门模型 16（2 个源）、论文 34。 由[每周科技收集 Agent](https://github.com/game-life04/weekly-tech-agent)于 2026-10-12 14:36（北京时间）自动生成。</sub>

<!-- wta:latest:end -->

---

## 关于这个项目

### 收集什么

| 栏目 | 来源 |
| --- | --- |
| 🗞️ AI 动态 | Hacker News 上和 AI 相关的热帖；OpenAI、Anthropic、Google、Mistral 等的官方博客；量子位、新智元、InfoQ 等中文媒体；几位值得读的作者 |
| 🛠️ 开源圈 | GitHub Trending 里的 AI 项目；最近一个月涨星最快的新仓库；vLLM、Ollama、transformers 等三十多个重点项目的新版本；Hugging Face 和魔搭的热门模型 |
| 📄 前沿论文 | Hugging Face Daily Papers 上点赞最多的论文；长上下文与检索、智能体、语音、高效推理四个方向的 arXiv 新论文 |

日报每天每个栏目最多 8 / 8 / 5 条；周报从当周日报里按综合分再精选一次。登过的内容 120 天内不会重复出现。

每条内容只保留标题、链接和一两句摘要，原文版权归原作者所有。

### 怎么工作的

```
抓取（每个来源一个文件）
  → 去重（同一篇文章、同一篇论文在不同来源只算一条）
  → 打分（热度、来源权重、新鲜度）
  → 大模型打分并给入选内容写中文标题和摘要（可选）
  → 生成 daily/、weekly/ 下的 Markdown 和本页顶部的“最新一期”
  → 提交回仓库
```

整个流程由 GitHub Actions 每天定时运行（[.github/workflows/daily.yml](.github/workflows/daily.yml)），不需要服务器。GitHub 的定时任务经常晚到两三个小时，所以日报出现的时间不固定，一般在北京时间早上。

### 在本地运行

需要 Python 3.11 或更高版本。

```bash
pip install -r requirements.txt
python -m wta check hackernews    # 测试一个来源，打印条数、发布时间和样例
python -m wta check rss:量子位     # 只测试一个订阅
# 完整跑一遍，结果写到仓库外面的目录里看效果（不调用大模型）：
python -m wta --root ../wta-preview --config config.yaml run --no-llm
```

不要直接在仓库目录里运行 `python -m wta run`：它会改写 `data/`、`daily/`、`weekly/` 和 README 里的“最新一期”，这些文件由定时任务维护。不小心改了的话，提交前用 `git restore` 还原。

在中国大陆运行时，多数境外来源需要代理：设置环境变量 `HTTPS_PROXY` 即可。读取 GitHub 接口不带令牌每小时只有 60 次额度，本地调试建议设置 `GITHUB_TOKEN`。

### 配置

所有可调的东西都在 [config.yaml](config.yaml) 里：每个栏目放几条、关键词表、订阅列表、关注的仓库、论文的关注方向、用哪家大模型。改配置不需要改代码。

### 大模型是可选的

没有配置密钥时，流程照常运行，只是标题保持原文、没有中文摘要。要启用的话，在仓库的 Settings → Secrets and variables → Actions 里添加下面任意一个密钥：

| 密钥名 | 服务 | 说明 |
| --- | --- | --- |
| `ZHIPU_API_KEY` | 智谱 glm-4.7-flash | 免费，手机号注册即可，推荐 |
| `GEMINI_API_KEY` | Google Gemini | 有免费额度 |
| `DEEPSEEK_API_KEY` | DeepSeek | 付费，这个项目的用量很小 |
| `LLM_API_KEY` | 任何兼容 OpenAI 接口的服务 | 另需在 Variables 里设置 `LLM_BASE_URL` 和 `LLM_MODEL` |

配了多个时的顺序：设置了 `LLM_API_KEY` 就优先用它，其余按智谱、Gemini、DeepSeek 的顺序。前一个不可用（密钥失效、额度用完、模型下线，或接连两次请求失败）时自动换下一个。每次运行最多发 30 次请求、最多用 8 分钟，正常一天用 10 次左右。

### 加一个信息来源

- **加一个 RSS 订阅**：在 `config.yaml` 的 `sources.rss.feeds` 里加一行，不用写代码。
- **加一种新的来源**：在 [wta/sources/](wta/sources/) 下新建一个文件，提供 `NAME`、`TITLE` 和一个 `fetch(config, ctx)` 函数，然后在 `wta/sources/__init__.py` 里登记。约定写在 [wta/sources/base.py](wta/sources/base.py) 的开头，[qbitai.py](wta/sources/qbitai.py) 是最短的例子。

详细步骤见 [CONTRIBUTING.md](CONTRIBUTING.md)。

### 项目结构

```
config.yaml          配置
wta/                 程序
  sources/           每个来源一个文件
  collect.py         依次运行各个来源
  dedupe.py          去重
  rank.py            打分和选稿
  llm.py editor.py   大模型接口；打分、写中文摘要
  render.py          生成 Markdown
  publish.py         写文件
  cli.py             命令行入口
data/                每天的数据（JSON），页面都从这里生成
daily/  weekly/      日报和周报
tests/               测试（全部使用假数据，不访问网络）
```

### AI 使用说明

- 中文标题和摘要由大模型根据抓到的文字生成，页面上有标注，可能有误，请以原文为准。每条内容都附原文链接。
- 条目的链接、热度数字和来源名由程序根据抓到的数据写出，不经过大模型。来源自带的简介里如果有网址，GitHub 会自动把它显示成链接。
- 程序会核对大模型写的标题和摘要：出现了原文里没有的英文名称，或三位以上、带小数点或百分号的数字，就不采用。这只能降低出错的可能，中文写的论断核对不了。
- 本项目的代码在 AI 辅助下编写（Claude Code），相应的提交带有 `Assisted-by` 标注。

### 部署与交接

把这个项目搬到新的账号或组织时，注意下面几点：

- **不要给默认分支开“必须通过 PR 合并”**，否则机器人每天的提交会被拒绝，日报停更。确实需要保护分支的话，要改用 GitHub App 的令牌来推送。
- 定时任务失败的通知邮件只发给最后修改 cron 那一行的人。接手的人需要改一次 cron，或者把工作流停用再启用，才会收到通知。
- 仓库地址写在三个地方：`wta/__init__.py` 的 `REPO_URL`、本文件开头的徽章、CONTRIBUTING.md 里的 clone 地址。
- Secrets 会随仓库转移保留；确认 `LLM_BASE_URL`、`LLM_MODEL` 两个 Variables（如果用了）还在，并把个人的密钥换成组织自己的。
- Issue 模板用到的 `source` 标签需要手动创建。
- 公开仓库连续 60 天没有活动，GitHub 会停掉定时任务。机器人每天的提交算活动，所以正常运行时不会被停。

### 参与贡献

欢迎提 Issue 和 PR，尤其是新的信息来源。请先读 [CONTRIBUTING.md](CONTRIBUTING.md)。

### 致谢

设计上参考了 [Horizon](https://github.com/Thysrael/Horizon)、[agents-radar](https://github.com/duanyytop/agents-radar) 和 [AIHOT](https://github.com/KKKKhazix/AIHOT)。

### 许可证

[MIT](LICENSE)
