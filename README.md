# 每周科技收集 Agent

[![Daily digest](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml)
[![CI](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

每天自动收集 AI 和大模型领域值得看的动态、开源项目和论文，整理成一份日报，每周再汇总成周报。内容直接放在这个仓库里，打开就能看。

<!-- wta:latest:start -->

## 最新一期 · 2026-10-17（周六）

> 收录 **21** 条：🗞️ AI 动态 8 · 🛠️ 开源圈 8 · 📄 前沿论文 5<br>
> [本周周报](weekly/2026-W42.md) · [往期日报](daily/README.md) · [往期周报](weekly/README.md) · [单独打开这一期](daily/2026/2026-10-17.md)

### 🗞️ AI 动态

**1. [Muse Spark Open](https://research.meta.ai/blog/muse-spark-open)**<br>Muse Spark Open 是目前最强大的美国开源模型，支持 816B 参数和 1M 上下文窗口，专为编码和智能体工作设计。<br><sub>Hacker News · 899 分 · 465 评论 · #模型发布 #开源 #Apple · [讨论](https://news.ycombinator.com/item?id=50107379)</sub>

**2. [美国基准地图：AI 测试覆盖了 90% 的工作时间吗？](https://www.mercor.com/research/labor-index/benchmark-map/)**<br>新发布的基准地图评估了 AI 测试对美国经济各行业的覆盖情况，发现目前覆盖的经济价值工作仍然有限。<br><sub>Hacker News · 328 分 · 292 评论 · #评测 #行业动态 #基准测试 · 原题：90% of US working hours are spent on tasks not covered well by AI benchmarks · [讨论](https://news.ycombinator.com/item?id=50121179)</sub>

**3. [Beam：501B 参数开源模型](https://huggingface.co/blog/reflection-beam)**<br>Reflection 实验室发布首个开源模型 Beam，支持文本输入和百万级上下文窗口。<br><sub>Hugging Face 博客 · #模型发布 #开源 · 原题：Welcome Beam: a 501B open model you can own, customize, and scale</sub>

**4. [将 AI 智能体落地生物实验室](https://research.google/blog/grounding-ai-agents-in-biological-reality-building-blocks-for-autonomous-wet-labs/)**<br>Google 研究将 AI 智能体与物理实验室机器人结合，实现快速闭环分子设计。<br><sub>Google Research · #行业动态 #智能体 · 原题：Grounding AI agents in biological reality: Building blocks for autonomous wet labs</sub>

**5. [Anthropic 获得最高垃圾信用评级](https://www.ft.com/content/5a310aee-f555-4266-874c-b1b4db20186d)**<br><sub>Hacker News · 163 分 · 44 评论 · #行业动态 #Anthropic · 原题：Anthropic assigned highest junk credit rating in June · [讨论](https://news.ycombinator.com/item?id=50122112)</sub>

**6. [在 Mac Studio 上使用 MLX 和 RDMA 进行分布式推理](https://machinelearning.apple.com/research/mlx-distributed-inference)**<br>MLX 框架利用 Apple 统一内存架构，让研究人员在本地硬件上运行大模型。<br><sub>Apple 机器学习研究 · 238 分 · 107 评论 · 同时见于 Hacker News · #推理加速 #开源工具 · 原题：Local and Distributed Large LLM Inference with MLX and RDMA on Mac Studio · [讨论](https://news.ycombinator.com/item?id=50118320)</sub>

**7. [Show HN：Gemini 4 Argon 玩星际争霸](https://starskirmish.com/bench/v0-2/)**<br>StarSkirmish 基准测试评估了 LLM 编写星际争霸机器人的能力，Gemini 4 Argon 在测试中表现出色。<br><sub>Hacker News · 171 分 · 75 评论 · #游戏 #评测 #Gemini · 原题：Show HN: Gemini 4 Argon plays StarCraft · [讨论](https://news.ycombinator.com/item?id=50118688)</sub>

**8. [AI 不是黑箱，99% 神经元清晰可见](https://www.leiphone.com/category/yanxishe/Vr0JmbkUeZV5D9Qz.html)**<br>可解释性专家 Nick Cammarata 推翻十年前结论，称神经元检测的是几何形状而非物体。<br><sub>雷峰网 · #可解释性 #论文 · 原题：推翻一切！Nick Cammarata 万字长文宣告，AI 不是黑箱，99% 神经元清晰可见</sub>

### 🛠️ 开源圈

**1. [xerj-org/xerj](https://github.com/xerj-org/xerj)**<br>XERJ 通过自动索引功能，使用比 grep 少 40 倍的 token 来搜索代码、文档和日志，兼容 Elasticsearch。<br><sub>GitHub Trending · 今日 +1.6k ★ · 6.9k ★ · #开源工具 #搜索 #RAG</sub>

**2. [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)**<br>Anthropic 官方维护的高质量 Claude Code 插件目录。<br><sub>GitHub Trending · 今日 +1.6k ★ · 40.4k ★ · #开源工具 #插件 #Anthropic</sub>

**3. [feder-cr/git-ai](https://github.com/feder-cr/git-ai)**<br>Git designed for AI agents.<br><sub>GitHub 新项目 · 1.1k ★</sub>

**4. [obra/superpowers](https://github.com/obra/superpowers)**<br>superpowers 是一个智能体技能框架和软件开发方法论。<br><sub>GitHub Trending · 今日 +973 ★ · 300.6k ★ · #开源工具 #智能体 #开发框架</sub>

**5. [Scaling Kimi K3 on AMD Instinct MI355X: Matching NVIDIA HGX B300 Throughput per GPU on AgentX](https://vllm.ai/blog/2026-10-16-kimi-k3-mi355x)**<br>vLLM 团队分享了在 AMD Instinct MI355X 上优化 Kimi K3 推理速度的经验。<br><sub>vLLM 博客 · #推理加速 #开源工具</sub>

**6. [Reflection's Beam is freely available on Ollama for a limited time](https://ollama.com/blog/reflection-beam)**<br>Reflection 的 Beam 模型在 Ollama 上限时免费提供，支持软件工程和智能体任务。<br><sub>Ollama 博客 · #模型发布 #开源</sub>

**7. [huggingface/transformers v5.20.0](https://github.com/huggingface/transformers/releases/tag/v5.20.0)**<br>次版本更新<br><sub>GitHub 版本发布 · #模型发布 #开源工具</sub>

**8. [anomalyco/opencode](https://github.com/anomalyco/opencode)**<br>The open source coding agent.<br><sub>GitHub Trending · 今日 +485 ★ · 214.3k ★</sub>

### 📄 前沿论文

**1. [OpenGCUA：通用计算机使用全栈开源](https://arxiv.org/abs/2610.22200)**<br>OpenGCUA 旨在构建一个通用的计算机使用智能体全栈开源项目。它通过代码执行和决策转移机制，在 OSWorld-v2 评测中显著提升了多个模型的任务得分。<br><sub>Hugging Face 热门论文 · 266 赞 · #智能体 #计算机使用 #开源 · 原题：OpenGCUA: Toward a Fully Open Stack for Generalist Computer Use · [代码](https://github.com/Tongyi-MAI/OpenGCUA)</sub>

**2. [Waypoint-OPD：通过门控策略蒸馏转移RL诱导的策略变化](https://arxiv.org/abs/2610.21601)**<br>Waypoint-OPD 提出利用早期和晚期教师策略变化的相对一致性来指导选择性转移。该方法在数学和代码推理任务中，相比仅使用端点转移的方法表现更优。<br><sub>Hugging Face 热门论文 · 451 赞 · #强化学习 #策略蒸馏 #知识蒸馏 · 原题：Waypoint-OPD: Transferring RL-Induced Policy Shifts via Gated On-Policy Distillation · [代码](https://github.com/hhhbxloveai/WaypointOPD)</sub>

**3. [Any Time, Any Space：基于世界状态的智能体视频生成框架](https://arxiv.org/abs/2610.20571)**<br>ATAS 框架通过显式引用位置、相机和事件时间，将剧本转化为具有时空一致性的镜头请求。它在多个视频生成器和基准测试中，显著提高了跨镜头的一致性。<br><sub>Hugging Face 热门论文 · 340 赞 · #视频生成 #智能体 #一致性 · 原题：Any Time, Any Space: A World-State-Centric Framework for Agentic Video Generation · [代码](https://github.com/ziplab/ATAS)</sub>

**4. [KV4-RL：解锁 RLVR 的 INT4 KV 缓存量化加速](https://arxiv.org/abs/2610.14448)**<br>KV4-RL 结合无校准 INT4 量化和选择性 INT8 保护，解决了 INT4 推理可能降低学习效果的问题。在 Qwen3-8B-Base GRPO 训练中，它实现了显著的加速。<br><sub>arXiv · 高效推理 · 36 赞 · #高效推理 #强化学习 #量化 · 原题：KV4-RL: Unlocking Faster Asynchronous Rollouts for RLVR with INT4 KV Cache Quantization</sub>

**5. [分析 LLM 隐藏状态的信息与几何特性以实现推测解码](https://arxiv.org/abs/2610.12939)**<br>该研究提出基于信息量和多样性的多层隐藏状态选择框架，用于推测解码。通过熵和 CKA 算法，选出的层集在 EAGLE3 风格的推测解码中优于固定基线。<br><sub>arXiv · 高效推理 · 17 赞 · #高效推理 #推测解码 #LLM · 原题：Surfing the Activation Wave: Analyzing the Information and Geometry of LLM Hidden States for Speculative Decoding</sub>

<sub>中文标题和摘要由 AI 生成（glm-4.7-flash），可能有误，请以原文为准。 本期候选来自：Hacker News 58、RSS 订阅 54（40 个源）、量子位 5、GitHub Trending 48、GitHub 新项目 293、GitHub 版本发布 5、热门模型 16（2 个源）、论文 27。 由[每周科技收集 Agent](https://github.com/game-life04/weekly-tech-agent)于 2026-10-17 06:05（北京时间）自动生成。</sub>

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
  → 大模型打分并给入选内容写中文标题和摘要（可选；没有简介的 AI 动态先到原文网页取一小段当资料）
  → 生成 daily/、weekly/ 下的 Markdown 和本页顶部的“最新一期”
  → 提交回仓库
```

整个流程由 GitHub Actions 每天定时运行（[.github/workflows/daily.yml](.github/workflows/daily.yml)），不需要服务器。GitHub 的定时任务经常晚到两三个小时，有时干脆不触发，所以一天设了三次（北京时间 03:17、05:47、09:17）：先跑到的那次负责抓取和出刊，后面的不重新抓取，只补上大模型之前没写成的中文摘要。日报出现的时间因此不固定，一般在北京时间早上。

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
- 来源没给简介的 AI 动态（主要是 Hacker News 的帖子），程序会到原文网页取网页自带的描述和正文开头几段，最多 800 字，只给大模型写摘要用，不显示在页面上，不保存全文。需要登录的网站（X、领英等）不去取。
- 条目的链接、热度数字和来源名由程序根据抓到的数据写出，不经过大模型。来源自带的简介里如果有网址，GitHub 会自动把它显示成链接。
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

设计上参考了 [Horizon](https://github.com/Thysrael/Horizon)、[agents-radar](https://github.com/duanyytop/agents-radar) 和 [AIHOT](https://github.com/KKKKhazix/AIHOT)。

### 许可证

[MIT](LICENSE)
