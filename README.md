# 每周科技收集 Agent

[![Daily digest](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml)
[![CI](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

每天早上整理 AI 与开源动态，参照《CCF开源快讯》的体例出一期「每日快讯」，8:30 推送到俱乐部 QQ 群；每周一再出一期「每周快讯」。全部由程序自动生成，内容就放在这个仓库里，打开就能看。

- **订阅**：[RSS 订阅源](https://raw.githubusercontent.com/game-life04/weekly-tech-agent/main/feed.xml)；或者在本仓库点 **Watch → Custom → Releases**，每周快讯出刊时 GitHub 会发邮件通知你。
- **投稿**：欢迎推荐值得一看的文章、开源项目、活动和俱乐部动态，请[提交 issue](https://github.com/game-life04/weekly-tech-agent/issues/new?template=submission.md)。
- **往期**：[每周快讯](weekly/README.md) · [每日快讯和日报](daily/README.md)

<!-- wta:latest:start -->

## 每日快讯 · 11.28（周六）

> 今日 AI 与开源要闻 **18** 条，3 分钟速读。<br>
> [单独打开](daily/2026/2026-11-28-kuaixun.md) · [公众号排版版](daily/2026/2026-11-28-kuaixun.html) · [完整日报（含热度和原题）](daily/2026/2026-11-28.md) · [往期日报](daily/README.md)

<details>
<summary>群消息文字版（点开后，点代码框右上角的按钮整段复制）</summary>

```text
【每日科技快讯】11月28日 周六
今日 AI 与开源要闻 18 条，3 分钟速读

【俱乐部动态】
1. 开放原子开源俱乐部合并 3 个 PR、提交 17 次
2. atomgit-cli 提交 12 次
3. atomgit-cli 发布 v0.7.5

【国内动态】
4. 首个带跨任务空间记忆的原生基模开源
→ 首个带跨任务空间记忆的原生基模开源，机器人端侧就能跑。
5. 豆包工作宣布接入剪映官方插件
→ 豆包工作宣布接入剪映官方插件，支持通过自然语言完成视频剪辑。
6. Kimi 向科学家提供最高 2 万美元 API 免费额度
→ 月之暗面向自然科学等领域研究人员提供最高 2 万美元 Kimi API 额度。

【海外动态】
7. Introducing the llama.cpp benchmark dashboard for AMD Ryzen and Radeon
→ llama.cpp × AMD Benchmark 仪表盘上线，可追踪本地推理性能。
8. Taking Trainium3 to the Track: Generating Videos with LTX-2.5
→ 在 AWS Trainium3 机器上测试 LTX-2.5 视频生成模型。
9. Anthropic拆穿AI假遗忘！46万神经元动几十个，黑客知识就复活
→ Anthropic 研究发现 AI 的“假遗忘”现象，只需微调几十个神经元即可恢复知识。

【开源项目】
10. 微信开源 WeMM-Ecom：多模态基础模型家族、基于真实电商需求驱动
→ 腾讯微信视觉团队开源 WeMM-Ecom 多模态基础模型，提升电商场景识别能力。
11. opensetlabs/openset-llm
→ Fast local LLM inference on plain CPUs. No GPU, 8 GB of RAM. OpenAI-compatible server.
12. awslabs/cli-agent-orchestrator
→ Multi-agent orchestration for AI coding CLIs — Claude Code, Kiro, Codex, and more, coordinated in isolated tmux sessions。
13. DeadInternetStudios/100x-engineer-skill
→ 100x is a skill by a former Cursor engineer that turns prompts into formally verified, production-ready code。
14. DataTalksClub/llm-zoomcamp
→ LLM Zoomcamp - a free online course about real-life applications of LLMs. In 10 weeks you will learn how to build an AI…

【学术前沿】
15. Solve Vision with Code: Coding Agents Are Stronger Visual Reasoners Than Video…
→ Video generation models are increasingly evaluated as visual reasoners: given a first frame and a natural-language prom…
16. Stable Gated DeltaNet-2: Understanding and Mitigating Recurrent State Instabili…
→ Linear attention offers an efficient solution for long-sequence modeling via linear complexity and fixed-size recurrent…
17. DyLoMo-DiT: Dynamic Looped Mixture-of-Experts Diffusion Transformers
→ Diffusion Transformers (DiTs) scale model capacity by increasing both parameter count and computation. Mixture-of-Exper…
18. Revisiting LLMs as Context Engineers
→ As large language models (LLMs) are used in more and more new tasks, context engineering becomes a fundamental method t…

【活动预告】
· 12月3日 EuroVis 2027 论文截稿

完整版（含原文链接）：https://github.com/game-life04/weekly-tech-agent/blob/main/daily/2026/2026-11-28-kuaixun.md
标题和要点由 AI 整理，可能有误，请以原文为准。
```

</details>

### 今日快讯

#### 俱乐部动态

**开放原子开源俱乐部合并 3 个 PR、提交 17 次**<br>11月27日，据俱乐部开源仪表盘统计，开放原子开源俱乐部跟踪的 122 个仓库中有 1 个有人参与开发，共新增 PR 3 个、合并 3 个，提交 17 次，新增代码 227 行、删除 69 行，3 位贡献者参与。<br><sub>（来源：[俱乐部开源仪表盘](https://osd.openatom.club/)）</sub>

**atomgit-cli 提交 12 次**<br>11月27日，Agent SIG的 atomgit-cli 仓库提交 12 次、新增代码 215 行，3 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/atomgit-cli)）</sub>

**atomgit-cli 发布 v0.7.5**<br>11月27日，atomgit-cli 发布新版本 v0.7.5。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/atomgit-cli/releases/tag/v0.7.5)）</sub>

#### 国内动态

**首个带跨任务空间记忆的原生基模开源**<br>11月27日，首个带跨任务空间记忆的原生基模开源，机器人端侧就能跑。<br><sub>（来源：[量子位](https://www.qbitai.com/2026/11/513227.html)）</sub>

**豆包工作宣布接入剪映官方插件**<br>11月27日，豆包工作宣布接入剪映官方插件，支持通过自然语言完成视频剪辑。<br><sub>（来源：[智东西](https://zhidx.com/p/615139.html)）</sub>

**Kimi 向科学家提供最高 2 万美元 API 免费额度**<br>11月28日，月之暗面向自然科学等领域研究人员提供最高 2 万美元 Kimi API 额度。<br><sub>（来源：[Solidot](https://www.solidot.org/story?sid=86015)）</sub>

#### 海外动态

**Introducing the llama.cpp benchmark dashboard for AMD Ryzen and Radeon**<br>11月26日，llama.cpp × AMD Benchmark 仪表盘上线，可追踪本地推理性能。<br><sub>（来源：[Hugging Face 博客](https://huggingface.co/blog/ggml-org/llamacpp-amd-bench)）</sub>

**Taking Trainium3 to the Track: Generating Videos with LTX-2.5**<br>11月27日，在 AWS Trainium3 机器上测试 LTX-2.5 视频生成模型。<br><sub>（来源：[Hugging Face 博客](https://huggingface.co/blog/video-trainium3)）</sub>

**Anthropic拆穿AI假遗忘！46万神经元动几十个，黑客知识就复活**<br>11月28日，Anthropic 研究发现 AI 的“假遗忘”现象，只需微调几十个神经元即可恢复知识。<br><sub>（来源：[新智元](https://aiera.com.cn/2026/11/28/other/admin/125660/anthropic%e6%8b%86%e7%a9%bfai%e5%81%87%e9%81%97%e5%bf%98%ef%bc%8146%e4%b8%87%e7%a5%9e%e7%bb%8f%e5%85%83%e5%8a%a8%e5%87%a0%e5%8d%81%e4%b8%aa%ef%bc%8c%e9%bb%91%e5%ae%a2%e7%9f%a5%e8%af%86%e5%b0%b1/)）</sub>

#### 开源项目

**微信开源 WeMM-Ecom：多模态基础模型家族、基于真实电商需求驱动**<br>11月27日，腾讯微信视觉团队开源 WeMM-Ecom 多模态基础模型，提升电商场景识别能力。<br><sub>（来源：[开源中国](https://www.oschina.net/news/503871)）</sub>

**opensetlabs/openset-llm**<br>11月28日消息，Fast local LLM inference on plain CPUs. No GPU, 8 GB of RAM. OpenAI-compatible server.<br><sub>（来源：[GitHub 新项目](https://github.com/opensetlabs/openset-llm)）</sub>

**awslabs/cli-agent-orchestrator**<br>11月28日消息，Multi-agent orchestration for AI coding CLIs — Claude Code, Kiro, Codex, and more, coordinated in isolated tmux sessions。<br><sub>（来源：[GitHub Trending](https://github.com/awslabs/cli-agent-orchestrator)）</sub>

**DeadInternetStudios/100x-engineer-skill**<br>11月28日消息，100x is a skill by a former Cursor engineer that turns prompts into formally verified, production-ready code。<br><sub>（来源：[GitHub 新项目](https://github.com/DeadInternetStudios/100x-engineer-skill)）</sub>

**DataTalksClub/llm-zoomcamp**<br>11月28日消息，LLM Zoomcamp - a free online course about real-life applications of LLMs. In 10 weeks you will learn how to build an AI…<br><sub>（来源：[GitHub Trending](https://github.com/DataTalksClub/llm-zoomcamp)）</sub>

#### 学术前沿

**Solve Vision with Code: Coding Agents Are Stronger Visual Reasoners Than Video…**<br>11月26日，Video generation models are increasingly evaluated as visual reasoners: given a first frame and a natural-language prom…<br><sub>（来源：[arXiv · 智能体](https://arxiv.org/abs/2611.34813)）</sub>

**Stable Gated DeltaNet-2: Understanding and Mitigating Recurrent State Instabili…**<br>11月28日消息，Linear attention offers an efficient solution for long-sequence modeling via linear complexity and fixed-size recurrent…<br><sub>（来源：[Hugging Face 热门论文](https://arxiv.org/abs/2611.34051)）</sub>

**DyLoMo-DiT: Dynamic Looped Mixture-of-Experts Diffusion Transformers**<br>11月28日消息，Diffusion Transformers (DiTs) scale model capacity by increasing both parameter count and computation. Mixture-of-Exper…<br><sub>（来源：[Hugging Face 热门论文](https://arxiv.org/abs/2611.30844)）</sub>

**Revisiting LLMs as Context Engineers**<br>11月28日消息，As large language models (LLMs) are used in more and more new tasks, context engineering becomes a fundamental method t…<br><sub>（来源：[arXiv · 长上下文与检索](https://arxiv.org/abs/2611.30494)）</sub>

### 活动预告

**EuroVis 2027 论文截稿**<br>12月3日，Eurographics Conference on Visualization（EuroVis 2027，CCF-B 类，图形学与多媒体）Full papers的论文提交截止时间为北京时间12月3日 19:59，摘要截止时间为11月24日 19:59。会议将于 May 31-June 4, 2027 在 Stuttgart, Germany 举行。<br><sub>（来源：[会议官网](https://eurovis27.github.io/web/)）</sub>

<sub>标题和正文由 AI 根据原文整理（glm-4.7-flash），可能有误，请以原文为准。 俱乐部动态的统计日期为11月27日，数据来自[俱乐部开源仪表盘](https://osd.openatom.club/)。 会议截稿时间来自[CCFDDL](https://ccfddl.com/)，已换算成北京时间，请以会议官网为准。 有新闻线索欢迎[提交 Issue](https://github.com/game-life04/weekly-tech-agent/issues)。 本期由[每周科技收集 Agent](https://github.com/game-life04/weekly-tech-agent)于 2026-11-28 09:58（北京时间）自动生成。</sub>

## 每周快讯 第 6 期 · 11.16–11.22

> 本期头条：OpenAI发布GPT-6.2 Astra和Sol模型<br>
> 上周 AI 与开源要闻 **27** 条，5 分钟速读。<br>
> [阅读全文](weekly/2026-W47.md) · [公众号排版版](weekly/2026-W47.html) · [往期快讯](weekly/README.md)

**俱乐部动态**<br>
✨ [开放原子开源俱乐部一周合并 16 个 PR、提交 28 次](https://osd.openatom.club/)<br>
✨ [AtomGit-mobile4Harmony 一周合并 8 个 PR](https://github.com/hust-open-atom-club/AtomGit-mobile4Harmony)<br>
✨ [AtomGit-Mobile4Android 一周合并 4 个 PR](https://github.com/hust-open-atom-club/AtomGit-Mobile4Android)<br>
✨ [Open-Source-Dashboard 一周合并 2 个 PR](https://github.com/hust-open-atom-club/Open-Source-Dashboard)

**国内动态**<br>
✨ [阿里通义千问发布 Qwen4-Max 模型](https://qwen.ai/blog?id=qwen4-max)<br>
✨ [DeepSeek 开放全家桶应用 API](https://aiera.com.cn/2026/11/15/other/admin/123914/%e5%88%9a%e5%88%9a%ef%bc%8cdeepseek%e5%85%a8%e5%ae%b6%e6%a1%b6api%e6%ad%a3%e5%bc%8f%e5%bc%80%e6%94%be%ef%bc%81%e4%bd%a0%e4%b9%9f%e8%83%bd%e9%80%a0%e4%b8%80%e4%b8%aadeepseek%e4%ba%86/)<br>
✨ [华为云上线 openPangu-2.1-Pro 开源模型](https://www.ithome.com/1/027/450.htm)<br>
✨ [华为云发布 CloudRobo-WM1.2 具身世界模型](https://zhidx.com/p/610813.html)

**海外动态**<br>
✨ [OpenAI扩大对科学家的AI访问权限](https://openai.com/index/expanding-chatgpt-for-academic-researchers)<br>
✨ [OpenAI发布GPT-6.2 Astra和Sol模型](https://openai.com/index/introducing-gpt-6-2-astra-sol)<br>
✨ [Google DeepMind上线Genie 4](https://deepmind.google/blog/genie-4-is-now-available/)<br>
✨ [Google DeepMind发布Gemini 4 Neon](https://deepmind.google/blog/introducing-gemini-4-neon/)

**开源项目**<br>
✨ [vLLM 发布 v0.34.0 版本](https://github.com/vllm-project/vllm/releases/tag/v0.34.0)<br>
✨ [Claude-BugHunter 技能包](https://github.com/elementalsouls/Claude-BugHunter)<br>
✨ [Inkling 2 Mini：可在笔记本运行的模型](https://thinkingmachines.ai/news/inkling-2-mini/)<br>
✨ [autoclip 开源视频剪辑工具](https://github.com/zhouxiaoka/autoclip)

**学术前沿**<br>
✨ [科学家如何使用ChatGPT进行研究](https://openai.com/index/science-at-the-frontier)<br>
✨ [OpenAI分析编码智能体如何加速AI研究](https://openai.com/index/research-acceleration-jagged-frontier)<br>
✨ [语言模型可自行重写权重](https://arxiv.org/abs/2611.21885)

**产业纵横**<br>
✨ [KPMG 使用 AI 代理进行审计](https://europeanbusinessmagazine.com/ai-agents-better-questions-kpmg/)<br>
✨ [Anthropic 定价首次公开募股](https://www.anthropic.com/news/anthropic-prices-initial-public-offering)<br>
✨ [Anthropic 上市次日股价下跌](https://www.theguardian.com/business/2026/nov/20/global-stock-markets-slump-anthropic-ipo-ai-sell-off)

**活动预告**<br>
✨ [EuroVis 2027 论文截稿](https://eurovis27.github.io/web/)<br>
✨ [AAMAS 2027 论文截稿](https://warwick.ac.uk/fac/sci/dcs/aamas2027/)<br>
✨ [ICAPS 2027 论文截稿](https://icaps27.icaps-conference.org/)<br>
✨ [COLING 2027 论文截稿](https://2027.coling-iccl.org/)<br>
✨ [NAACL 2027 论文截稿](https://2027.naacl.org/)

<!-- wta:latest:end -->

---

## 关于这个项目

内容由程序自动抓取、去重、打分，再由大模型分栏和改写（页面上都有标注，可能有误，请以原文为准），GitHub Actions 每天定时运行，不需要服务器。收集哪些来源、怎么工作、怎么在本地运行和加一个信息来源，见 [docs/about.md](docs/about.md)；参与贡献见 [CONTRIBUTING.md](CONTRIBUTING.md)。

### 致谢

设计上参考了 [Horizon](https://github.com/Thysrael/Horizon)、[agents-radar](https://github.com/duanyytop/agents-radar) 和 [AIHOT](https://github.com/KKKKhazix/AIHOT)。每周快讯的体例参照 CCF 开源发展技术委员会的《CCF开源快讯》，俱乐部数据来自俱乐部的 [Open-Source-Dashboard](https://github.com/hust-open-atom-club/Open-Source-Dashboard)，会议截稿数据来自 [ccf-deadlines](https://github.com/ccfddl/ccf-deadlines)。

### 许可证

[MIT](LICENSE)
