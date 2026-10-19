# 每周科技收集 Agent

[![Daily digest](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml)
[![CI](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

每天自动收集 AI 和大模型领域值得看的动态、开源项目和论文，整理成一份日报；每周一再参照《CCF开源快讯》的体例，把上一周的内容整理成一期 5 分钟速读的「每周快讯」，附一份能直接贴进公众号的排版版。内容直接放在这个仓库里，打开就能看。

<!-- wta:latest:start -->

## 每周快讯 · 10.12–10.18

> 上周 AI 与开源要闻 **25** 条，5 分钟速读。<br>
> [阅读全文](weekly/2026-W42.md) · [公众号排版版](weekly/2026-W42.html) · [往期快讯](weekly/README.md)

**俱乐部动态**<br>
✨ [开放原子开源俱乐部一周合并 34 个 PR、提交 75 次](https://osd.openatom.club/)<br>
✨ [pwn.hust.college 一周合并 13 个 PR](https://github.com/hust-open-atom-club/pwn.hust.college)<br>
✨ [hust-mail-cli 一周合并 4 个 PR](https://github.com/hust-open-atom-club/hust-mail-cli)<br>
✨ [hust-mirrors 一周合并 4 个 PR](https://github.com/hust-open-atom-club/hust-mirrors)<br>
✨ [俱乐部新建 nginx-oci-mirror 仓库](https://github.com/hust-open-atom-club/nginx-oci-mirror)

**政策动向**<br>
✨ [国务院常务会议听取人工智能进展汇报](https://www.gov.cn/yaowen/liebiao/202610/content_7083431.htm)

**国内动态**<br>
✨ [智谱发布GLM新模型](https://www.qbitai.com/2026/10/502649.html)<br>
✨ [面壁开源MiniCPM-V 4.7多模态模型](https://www.qbitai.com/2026/10/503109.html)<br>
✨ [DeepSeek-V4.1-Flash-1017 推理性能提升](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)

**海外动态**<br>
✨ [Meta发布Muse新模型](https://www.infoq.cn/article/2QXm6PqYYX57AOxTYyO0?utm_source=rss&utm_medium=article)<br>
✨ [Anthropic披露Claude动态工作流架构](https://www.infoq.cn/article/8La5gsJVOOF5BvFiLAUF?utm_source=rss&utm_medium=article)<br>
✨ [Gemini 4 Argon：解决最困难问题的前沿智能](https://deepmind.google/models/gemini/)<br>
✨ [Muse Spark Open 开源](https://research.meta.ai/blog/muse-spark-open)<br>
✨ [OpenAI 推出 Rosalind 学术计划](https://openai.com/index/introducing-the-rosalind-academic-plan)<br>
✨ [Google DeepMind 发布 Antigravity 科学工具](https://deepmind.google/blog/accelerating-antimicrobial-discovery/)

**开源项目**<br>
✨ [rea：用智能体做逆向工程](https://github.com/morluto/rea)<br>
✨ [Strata：在消费级硬件上运行Qwen3.8-Flash-Next](https://github.com/Niko1221/Strata)<br>
✨ [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)<br>
✨ [deepseek-ai/DeepSeek-V4.1-Flash](https://www.modelscope.cn/models/deepseek-ai/DeepSeek-V4.1-Flash)

**学术前沿**<br>
✨ [Agent-Reflex：训练智能体主动反思](https://arxiv.org/abs/2610.17953)<br>
✨ [大型语言模型如何通过线性映射存储信息](https://alexwang.ai/posts/associative-memory/)<br>
✨ [Google 研究将 AI 智能体落地生物实验室](https://research.google/blog/grounding-ai-agents-in-biological-reality-building-blocks-for-autonomous-wet-labs/)

**活动预告**<br>
✨ [WWW 2027 论文截稿](https://www2027.thewebconf.org/)<br>
✨ [RECOMB 2027 论文截稿](https://recomb.org/recomb2027/)<br>
✨ [CVPR 2027 论文截稿](https://cvpr.thecvf.com/Conferences/2027)

## 最新日报 · 2026-10-20（周二）

> 收录 **21** 条：🗞️ AI 动态 8 · 🛠️ 开源圈 8 · 📄 前沿论文 5<br>
> [往期日报](daily/README.md) · [每周快讯](weekly/README.md) · [单独打开这一期](daily/2026/2026-10-20.md)

### 🗞️ AI 动态

**1. [Hybrid Reasoning Agents：在潜在空间思考，通过文本行动](https://arxiv.org/abs/2610.18861)**<br>HybridAgents 动态在潜在推理和文本交互间切换，解决 LLM 代理在效率和透明度上的问题。<br><sub>Hacker News · 501 分 · 235 评论 · #智能体 #论文 · 原题：Hybrid Reasoning Agents: LLM agents that think in latent space, act through text · [讨论](https://news.ycombinator.com/item?id=50145337)</sub>

**2. [Timestral：Mistral 的时间序列基础模型](https://mistral.ai/news/timestral/)**<br>Timestral 是 Mistral 发布的时间序列基础模型，在 209M 参数下实现最先进的概率预测。<br><sub>Hacker News · 518 分 · 97 评论 · #模型发布 #时间序列 · 原题：Timestral: Mistral's time-series foundation models · [讨论](https://news.ycombinator.com/item?id=50150434)</sub>

**3. [Mercury 3：大规模扩散模型](https://www.inceptionlabs.ai/blog/introducing-mercury-3)**<br>Mercury 3 是目前最强大的扩散 LLM，在 1000+ tokens/秒的速度下超越 GPT-6 Luna 和 Claude Haiku 5.5。<br><sub>Hacker News · 205 分 · 80 评论 · #模型发布 #扩散模型 · 原题：Mercury 3: Diffusion at scale · [讨论](https://news.ycombinator.com/item?id=50155245)</sub>

**4. [OpenAI 提升低资源编程语言代码能力](https://openai.com/index/low-resource-programming-languages)**<br>OpenAI 改进了 ChatGPT 在低资源编程语言上的表现，新增了针对软件工程、SQLite 和 COBOL 迁移的评估。<br><sub>OpenAI · #模型发布 #编程 #评测 · 原题：Advancing Coding in Low-Resource Programming Languages</sub>

**5. [如果不运行自己的 LLM 代理，如何知道发生了什么？](https://jrdsgl.com/if-you-dont-run-your-own-llm-proxy-how-the-fuck-do-you-even-know-whats-going-on/)**<br><sub>Hacker News · 292 分 · 203 评论 · #行业动态 · 原题：If you don't run your own LLM proxy, how do you know whats going on? · [讨论](https://news.ycombinator.com/item?id=50145507)</sub>

**6. [微软称 AI 智能体如同内部威胁](https://techcrunch.com/2026/10/19/microsoft-says-ai-agents-are-like-insider-threats-as-frontier-models-cant-be-trusted/)**<br>微软警告企业需密切监控员工使用的智能体，因为前沿模型无法被完全信任。<br><sub>TechCrunch · #行业动态 #智能体 #安全 · 原题：Microsoft says AI agents are like insider threats as ‘frontier models can’t be trusted’</sub>

**7. [MiniMax M3.1 Flash 发布](https://zhidx.com/p/602354.html)**<br>MiniMax 发布 M3.1 Flash，定位为 Coding/Agent 优化轻量级模型，价格大幅降低。<br><sub>智东西 · #模型发布 #开源工具 #智能体 · 原题：正面硬刚DeepSeek！MiniMax M3.1 Flash发布，输出卷到200+TPS，价格砍到1/2</sub>

**8. [TorchNeuron 让在 AWS Trainium 上运行 HF 模型更简单](https://huggingface.co/blog/hf-torchneuron)**<br>TorchNeuron 为 PyTorch 提供了 Trainium 原生后端，支持 eager mode、torch.compile 和分布式 API。<br><sub>Hugging Face 博客 · #开源工具 #推理加速 #AWS · 原题：TorchNeuron: running HF models on AWS Trainium is easier than ever</sub>

### 🛠️ 开源圈

**1. [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI)**<br>ComfyUI 是最强大且模块化的扩散模型 GUI、API 和后端，拥有节点/图界面，是全球最快的本地推理引擎。<br><sub>GitHub Trending · 今日 +1k ★ · 139.7k ★ · #开源工具 #扩散模型</sub>

**2. [alchaincyf/huashu-motion](https://github.com/alchaincyf/huashu-motion)**<br>huashu-motion 是一个开源项目，能让 Agent 一键直出会作曲、能指着画面修改的商业级产品宣传片。<br><sub>GitHub 新项目 · 902 ★ · #开源工具 #智能体</sub>

**3. [Achieving near-zero-downtime scaling in Elastic Expert Parallelism](https://vllm.ai/blog/2026-10-19-elastic-ep-near-zero-downtime)**<br>通过异步准备和 NIXL EP 技术，vLLM 实现了弹性专家并行的近零停机扩展。<br><sub>vLLM 博客 · #开源工具 #推理加速 #分布式</sub>

**4. [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)**<br>ai-memory 解决了 Agent 编码 CLI 的长期记忆问题，并促进不同 Agent 供应商之间的交接。<br><sub>GitHub Trending · 今日 +666 ★ · 11.3k ★ · #开源工具 #智能体</sub>

**5. [google/artemis](https://github.com/google/artemis)**<br>ARTEMIS 能自动化端到端工作流，在 AndroidWorld 基准测试中达到 99%+ 的成功率。<br><sub>GitHub Trending · 今日 +526 ★ · 13k ★ · #开源工具 #自动化</sub>

**6. [How Numan Built an Eval-First AI Health Coach with LangGraph and LangSmith](https://www.langchain.com/blog/how-numan-built-an-eval-first-ai-health-coach-with-langgraph-and-langsmith)**<br>Numan 利用 LangGraph 和 LangSmith 构建了 AI 健康教练，包含分类评估、模拟对话和安全门控。<br><sub>LangChain 博客 · #开源工具 #智能体 #评测</sub>

**7. [koala73/worldmonitor](https://github.com/koala73/worldmonitor)**<br>worldmonitor 是一个 AI 驱动的实时全球情报仪表盘，提供新闻聚合、地缘政治监控和基础设施跟踪。<br><sub>GitHub Trending · 今日 +143 ★ · 88.8k ★ · #开源工具 #监控</sub>

**8. [OpenHands/OpenHands v1.28.0](https://github.com/OpenHands/OpenHands/releases/tag/v1.28.0)**<br>OpenHands 发布 v1.28.0 版本，新增了 Bahasa Indonesia 语言支持、对话模态请求密钥等功能。<br><sub>GitHub 版本发布 · #开源工具 #版本发布 #智能体</sub>

### 📄 前沿论文

**1. [GPT-6-Astra：具身智能的新突破](https://arxiv.org/abs/2610.22471)**<br>GPT-6-Astra 在机器人操作和导航任务中表现出色，挑战了传统专用模型范式。通过统一协议和上下文学习，它在多个基准测试中取得了前所未有的性能。<br><sub>Hugging Face 热门论文 · 236 赞 · #具身智能 #机器人 #大模型 · 原题：Has GPT-6-Astra Achieved Embodied Intelligence? · [代码](https://github.com/OpenSenseNova/SenseNova-RoboRSI)</sub>

**2. [DLite：无历史记录的推测解码](https://arxiv.org/abs/2610.23787)**<br>DLite 针对智能体工作负载中历史上下文导致的接受长度下降和系统开销问题，提出了一种无历史记录的推测解码框架。实验表明，它在通用、长上下文和智能体工作负载上实现了 2-6 的接受长度，并优于最先进方法。<br><sub>arXiv · 高效推理 · 20 赞 · #推理加速 #智能体 #大模型 · 原题：DLite: History-free Speculative Decoding for Agentic AI · [代码](https://github.com/SJTU-DAI-Sys/DLite)</sub>

**3. [Into the Unknown：开放科学问题的智能体评测](https://arxiv.org/abs/2610.19159)**<br>Into the Unknown 基准测试评估智能体在开放科学问题上的研究能力，要求其基于论文和方向撰写后续论文。实验发现，尽管智能体能生成看似合理的论文，但无一满足领域科学家的标准。<br><sub>arXiv · 智能体 · 130 赞 · #智能体 #评测 #科学 · 原题：Into the Unknown: Benchmarking AI agents on open scientific research problems · [代码](https://github.com/prometheus-eval/into-the-unknown)</sub>

**4. [RoTA-Bench：通过交互式投影对齐评估3D空间推理](https://arxiv.org/abs/2610.17665)**<br>RoTA-Bench 通过交互式 3D 到 2D 投影对齐任务，评估视觉语言模型将 2D 观察转化为支持精确动作的 3D 理解能力。实验发现，模型在任务完成率和精细控制方面与人类存在显著差距。<br><sub>Hugging Face 热门论文 · 196 赞 · #3D推理 #多模态 #评测 · 原题：RoTA-Bench: Evaluating 3D Spatial Reasoning through Interactive Projection Alignment · [代码](https://github.com/MAC-AutoML/RoTA-Bench)</sub>

**5. [VocalGrad：评估音频语言模型的声学感知](https://arxiv.org/abs/2610.23745)**<br>VocalGrad 专门评估大音频语言模型对低级声学变化的感知能力，将其定义为时间变化方向的二分类问题。结果显示，当前最先进的 LALMs 在声学感知上与人类 annotators 存在巨大差距。<br><sub>arXiv · 语音 · #语音 #声学感知 #评测 · 原题：VocalGrad: Evaluating Acoustic Perception in Audio Language Models</sub>

<sub>中文标题和摘要由 AI 生成（glm-4.7-flash），可能有误，请以原文为准。 本期候选来自：Hacker News 51、RSS 订阅 41（40 个源）、量子位 5、GitHub Trending 36、GitHub 新项目 299、GitHub 版本发布 2、热门模型 16（2 个源）、论文 31。 由[每周科技收集 Agent](https://github.com/game-life04/weekly-tech-agent)于 2026-10-20 06:54（北京时间）自动生成。</sub>

<!-- wta:latest:end -->

---

## 关于这个项目

### 收集什么

| 栏目 | 来源 |
| --- | --- |
| 🗞️ AI 动态 | Hacker News 上和 AI 相关的热帖；OpenAI、Anthropic、Google、Mistral 等的官方博客；量子位、新智元、InfoQ 等中文媒体；几位值得读的作者 |
| 🛠️ 开源圈 | GitHub Trending 里的 AI 项目；最近一个月涨星最快的新仓库；vLLM、Ollama、transformers 等三十多个重点项目的新版本；Hugging Face 和魔搭的热门模型 |
| 📄 前沿论文 | Hugging Face Daily Papers 上点赞最多的论文；长上下文与检索、智能体、语音、高效推理四个方向的 arXiv 新论文 |

日报每天每个栏目最多 8 / 8 / 5 条。登过的内容 120 天内不会重复出现。

每条内容只保留标题、链接和一两句摘要，原文版权归原作者所有。

### 每周快讯

每周一生成上周一到周日的一期，放在 [weekly/](weekly/README.md)，首页顶部是最新一期的速览。栏目和顺序参照《CCF开源快讯》：

| 栏目 | 内容从哪来 |
| --- | --- |
| 俱乐部动态 | [俱乐部开源仪表盘](https://osd.openatom.club/)（[Open-Source-Dashboard](https://github.com/hust-open-atom-club/Open-Source-Dashboard)）的周统计和最活跃的仓库，加上 GitHub 上这一周新建的仓库和新发布的版本。全部由程序根据接口数据写成，不经过大模型 |
| 政策动向 | 中国政府网“最新政策”和“要闻”里和人工智能、开源、软件有关的条目 |
| 国内动态、海外动态、开源项目、学术前沿、产业纵横 | 从这一周的日报里按综合分挑候选（中文媒体的报道另留名额），大模型负责分栏，把标题写成“主体+动作+对象”，再写一两句正文；讲同一件事的重复条目和分错的国内、海外公司由程序按名称纠正 |
| 活动预告 | 这一周新闻里预告的会议、论坛和比赛（日期要能在原文里找到）；接下来 45 天截稿的 CCF 推荐会议（人工智能、图形学与多媒体、人机交互、交叉综合四个领域的 A、B 类），数据来自 [CCFDDL](https://ccfddl.com/)，时间换算成北京时间 |

每期有两个文件：`weekly/<周>.md` 在 GitHub 上直接看；`weekly/<周>.html` 是公众号排版版，下载后用浏览器打开，全选、复制，粘贴到公众号编辑器即可，样式会一起带过去（公众号里外链点不了，来源直接写成网址，和《CCF开源快讯》一样）。

### 怎么工作的

```
抓取（每个来源一个文件）
  → 去重（同一篇文章、同一篇论文在不同来源只算一条）
  → 打分（热度、来源权重、新鲜度）
  → 大模型打分并给入选内容写中文标题和摘要（可选；没有简介的 AI 动态先到原文网页取一小段当资料）
  → 生成 daily/ 下的日报和本页顶部的“最新一期”
  → 每周一：把上周的日报，加上俱乐部统计、政策和会议截稿，整理成 weekly/ 下的快讯
  → 提交回仓库
```

整个流程由 GitHub Actions 每天定时运行（[.github/workflows/daily.yml](.github/workflows/daily.yml)），不需要服务器。GitHub 的定时任务经常晚到两三个小时，有时干脆不触发，所以一天设了三次（北京时间 03:17、05:47、09:17）：先跑到的那次负责抓取和出刊，后面的不重新抓取，只补上大模型之前没写成的中文摘要。日报出现的时间因此不固定，一般在北京时间早上。

快讯在周一第一次运行时生成；大模型没写完的条目由后面几次补上（已经写好的不会重写）。俱乐部仪表盘中午前后才更新到周日，所以周一 13:17 还有一次运行，把俱乐部统计换成完整的一周。

### 在本地运行

需要 Python 3.11 或更高版本。

```bash
pip install -r requirements.txt
python -m wta check hackernews    # 测试一个来源，打印条数、发布时间和样例
python -m wta check rss:量子位     # 只测试一个订阅
# 完整跑一遍，结果写到仓库外面的目录里看效果（不调用大模型）：
python -m wta --root ../wta-preview --config config.yaml run --no-llm
# 用已有的日报数据生成某一周的快讯（先把 data/ 复制到 ../wta-preview 里）：
python -m wta --root ../wta-preview --config config.yaml kuaixun --week 2026-W42 --no-llm
```

不要直接在仓库目录里运行 `python -m wta run`：它会改写 `data/`、`daily/`、`weekly/` 和 README 里的“最新一期”，这些文件由定时任务维护。不小心改了的话，提交前用 `git restore` 还原。

在中国大陆运行时，多数境外来源需要代理：设置环境变量 `HTTPS_PROXY` 即可。读取 GitHub 接口不带令牌每小时只有 60 次额度，本地调试建议设置 `GITHUB_TOKEN`。

### 配置

所有可调的东西都在 [config.yaml](config.yaml) 里：每个栏目放几条、关键词表、订阅列表、关注的仓库、论文的关注方向、快讯每个栏目登几条和政策关键词、用哪家大模型。改配置不需要改代码。

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
  kuaixun.py         每周快讯：挑选、分栏、改写
  club.py policy.py deadlines.py   快讯的俱乐部动态、政策动向、活动预告
  render.py          生成页面（Markdown，快讯另有公众号排版版 HTML）
  publish.py         写文件
  cli.py             命令行入口
data/                每天的数据（JSON），页面都从这里生成；data/weekly/ 是每期快讯
daily/  weekly/      日报和每周快讯
tests/               测试（全部使用假数据，不访问网络）
```

### AI 使用说明

- 中文标题和摘要由大模型根据抓到的文字生成，页面上有标注，可能有误，请以原文为准。每条内容都附原文链接。
- 来源没给简介的 AI 动态（主要是 Hacker News 的帖子），程序会到原文网页取网页自带的描述和正文开头几段，最多 800 字，只给大模型写摘要用，不显示在页面上，不保存全文。需要登录的网站（X、领英等）不去取。
- 条目的链接、热度数字和来源名由程序根据抓到的数据写出，不经过大模型。来源自带的简介里如果有网址，GitHub 会自动把它显示成链接。
- 快讯的标题和正文由大模型根据日报里的资料改写，经过同样的核对，不合格的退回日报里已经核对过的中文标题和摘要；日期、链接、俱乐部的统计数字和会议截稿时间都由程序写出，不经过大模型。
- 程序会核对大模型写的标题和摘要：出现了原文里没有的英文名称，或三位以上、带小数点或百分号的数字，就不采用；一个汉字都没有的“翻译”也不采用。中文标题只拿原标题核对，不能把简介里的名称搬进标题。核对规则改进以后，之后的定时任务会按新规则复查当天已经登出的内容：不合格的撤下、改为显示原文，再补写一次，只补撤下的部分。这只能降低出错的可能：“谁发布、谁使用”这类关系和中文写的论断核对不了。
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

设计上参考了 [Horizon](https://github.com/Thysrael/Horizon)、[agents-radar](https://github.com/duanyytop/agents-radar) 和 [AIHOT](https://github.com/KKKKhazix/AIHOT)。每周快讯的体例参照 CCF 开源发展技术委员会的《CCF开源快讯》，俱乐部数据来自俱乐部的 [Open-Source-Dashboard](https://github.com/hust-open-atom-club/Open-Source-Dashboard)，会议截稿数据来自 [ccf-deadlines](https://github.com/ccfddl/ccf-deadlines)。

### 许可证

[MIT](LICENSE)
