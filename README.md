# 每周科技收集 Agent

[![Daily digest](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml)
[![CI](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

每天早上整理 AI 与开源动态，参照《CCF开源快讯》的体例出一期「每日快讯」，8:30 推送到俱乐部 QQ 群；每周一再出一期「每周快讯」。全部由程序自动生成，内容就放在这个仓库里，打开就能看。

- **订阅**：[RSS 订阅源](https://raw.githubusercontent.com/game-life04/weekly-tech-agent/main/feed.xml)；或者在本仓库点 **Watch → Custom → Releases**，每周快讯出刊时 GitHub 会发邮件通知你。
- **投稿**：欢迎推荐值得一看的文章、开源项目、活动和俱乐部动态，请[提交 issue](https://github.com/game-life04/weekly-tech-agent/issues/new?template=submission.md)。
- **往期**：[每周快讯](weekly/README.md) · [每日快讯和日报](daily/README.md)

<!-- wta:latest:start -->

## 每日快讯 · 11.27（周五）

> 今日 AI 与开源要闻 **19** 条，3 分钟速读。<br>
> [单独打开](daily/2026/2026-11-27-kuaixun.md) · [公众号排版版](daily/2026/2026-11-27-kuaixun.html) · [完整日报（含热度和原题）](daily/2026/2026-11-27.md) · [往期日报](daily/README.md)

<details>
<summary>群消息文字版（点开后，点代码框右上角的按钮整段复制）</summary>

```text
【每日科技快讯】11月27日 周五
今日 AI 与开源要闻 19 条，3 分钟速读

【俱乐部动态】
1. 开放原子开源俱乐部合并 9 个 PR、提交 6 次
2. TranslateProject 合并 6 个 PR
3. AtomGit-Mobile4Android 合并 1 个 PR

【国内动态】
4. 国产模型扎进 AI4S 深水区，几毫秒破译尘封18年密码学悬案
→ 作者丨 高允毅 编辑丨岑 峰 11月20日， AI for Science 迎来了一个载入史册的日子：Anthropic 数学家联合 Claude 拿下黎曼猜想的关键突破，同一天，以复杂的数学计算著称的密码学领域，也被AI撼动。 据 Mi…
5. AI 3D界的“X光”来了！一图直出巴洛克雕塑，3D打印开箱即用
→ 还得是科班尖子生。
6. 20个AI Agents组队，4天狂跑350次实验，超越ClickBench最佳公开成绩
→ Quickwit查询总耗时降31%，最高降87%。
7. 前Codex负责人：在OpenAI，dots正成为干活的主要方式
→ 11月24日凌晨，OpenAI的Tibo Sottiaux（原Codex负责人）在X上扔了颗雷。

【海外动态】
8. Anthropic CEO长文刷屏！超级智能时代的桌面APP来了
→ 今天凌晨2点22分，Anthropic CEO Dario Amodei在X上发了一篇长帖。
9. Former OpenAI researcher says the Riemann proof matters less than the fact that…
→ Complexity theorist and former OpenAI researcher Scott Aaronson argues that AI's recent math breakthroughs matter far b…

【开源项目】
10. ggml-org/llama.cpp v1.1.0
→ 次版本更新。
11. xorbitsai/inference v4.3.0
→ 次版本更新。
12. alesha-pro/llm.asm
→ 该项目用纯 x86-64 NASM 汇编编写了 Qwen3-0.6B 推理、裸机启动 OS 和 Mini-GPT 训练器。
13. nexu-io/opengame
→ 该项目提供游戏素材，支持将编码代理转化为全栈 AI 游戏工作室。
14. bendlang/bend：通过证明阻止 AI 错误的快速语言
→ Bend 2 是一种通过证明来阻止 AI 错误的快速语言。

【学术前沿】
15. Google 发布 Cogentic 研究论文
→ Google Research 发布了包含整数分解、离散对数等内容的研究论文，内容发布在 GitHub 上。
16. Sage-Med：医疗多模态智能的扩展
→ 本文提出 Sage-Med-Preview 模型，通过结合特定阶段的数据筛选和渐进式训练课程，在视觉理解和医疗语言能力上均有显著提升。
17. Any-Rate：基于编码位平面的半比特多精度量化
→ 本文提出 Any-Rate 方法，从单个检查点提供 2-8 比特的量化，在 2-4 比特范围内以半比特步进。
18. Anthropic 发布 GRH Lean 验证精简版
→ Anthropic 与 Claude 合作发布了黎曼猜想和广义黎曼猜想的 Lean 4 证明精简版。

【产业纵横】
19. Google 要求 AI 代理使用其 MCP 服务器
→ Google 规定从 2027 年起，AI 代理必须通过其 MCP 服务器访问 Workspace 服务。

【活动预告】
· 12月3日 EuroVis 2027 论文截稿

完整版（含原文链接）：https://github.com/game-life04/weekly-tech-agent/blob/main/daily/2026/2026-11-27-kuaixun.md
标题和要点由 AI 整理，可能有误，请以原文为准。
```

</details>

### 今日快讯

#### 俱乐部动态

**开放原子开源俱乐部合并 9 个 PR、提交 6 次**<br>11月26日，据俱乐部开源仪表盘统计，开放原子开源俱乐部跟踪的 122 个仓库中有 3 个有人参与开发，共新增 PR 3 个、合并 9 个，提交 6 次，新增代码 4839 行、删除 246 行，5 位贡献者参与，其中 1 位是第一次贡献。<br><sub>（来源：[俱乐部开源仪表盘](https://osd.openatom.club/)）</sub>

**TranslateProject 合并 6 个 PR**<br>11月26日，HCTT SIG的 TranslateProject 仓库新增 PR 2 个、合并 6 个、提交 2 次、新增代码 135 行，3 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/TranslateProject)）</sub>

**AtomGit-Mobile4Android 合并 1 个 PR**<br>11月26日，Agent SIG的 AtomGit-Mobile4Android 仓库合并 1 个、提交 1 次、新增代码 4613 行，1 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/AtomGit-Mobile4Android)）</sub>

#### 国内动态

**国产模型扎进 AI4S 深水区，几毫秒破译尘封18年密码学悬案**<br>11月26日，作者丨 高允毅 编辑丨岑 峰 11月20日， AI for Science 迎来了一个载入史册的日子：Anthropic 数学家联合 Claude 拿下黎曼猜想的关键突破，同一天，以复杂的数学计算著称的密码学领域，也被AI撼动。 据 Mi…<br><sub>（来源：[雷峰网](https://www.leiphone.com/category/yanxishe/T2xmmiMAC6WbuuCM.html)）</sub>

**AI 3D界的“X光”来了！一图直出巴洛克雕塑，3D打印开箱即用**<br>11月26日，还得是科班尖子生。<br><sub>（来源：[量子位](https://www.qbitai.com/2026/11/512981.html)）</sub>

**20个AI Agents组队，4天狂跑350次实验，超越ClickBench最佳公开成绩**<br>11月27日，Quickwit查询总耗时降31%，最高降87%。<br><sub>（来源：[量子位](https://www.qbitai.com/2026/11/513053.html)）</sub>

**前Codex负责人：在OpenAI，dots正成为干活的主要方式**<br>11月27日，11月24日凌晨，OpenAI的Tibo Sottiaux（原Codex负责人）在X上扔了颗雷。<br><sub>（来源：[新智元](https://aiera.com.cn/2026/11/27/other/admin/125509/%e5%89%8dcodex%e8%b4%9f%e8%b4%a3%e4%ba%ba%ef%bc%9a%e5%9c%a8openai%ef%bc%8cdots%e6%ad%a3%e6%88%90%e4%b8%ba%e5%b9%b2%e6%b4%bb%e7%9a%84%e4%b8%bb%e8%a6%81%e6%96%b9%e5%bc%8f/)）</sub>

#### 海外动态

**Anthropic CEO长文刷屏！超级智能时代的桌面APP来了**<br>11月27日，今天凌晨2点22分，Anthropic CEO Dario Amodei在X上发了一篇长帖。<br><sub>（来源：[新智元](https://aiera.com.cn/2026/11/27/other/admin/125526/anthropic-ceo%e9%95%bf%e6%96%87%e5%88%b7%e5%b1%8f%ef%bc%81%e8%b6%85%e7%ba%a7%e6%99%ba%e8%83%bd%e6%97%b6%e4%bb%a3%e7%9a%84%e6%a1%8c%e9%9d%a2app%e6%9d%a5%e4%ba%86/)）</sub>

**Former OpenAI researcher says the Riemann proof matters less than the fact that…**<br>11月27日，Complexity theorist and former OpenAI researcher Scott Aaronson argues that AI's recent math breakthroughs matter far b…<br><sub>（来源：[The Decoder](https://the-decoder.com/former-openai-researcher-says-the-riemann-proof-matters-less-than-the-fact-that-an-ai-system-can-produce-it/)）</sub>

#### 开源项目

**ggml-org/llama.cpp v1.1.0**<br>11月26日，次版本更新。<br><sub>（来源：[GitHub 版本发布](https://github.com/ggml-org/llama.cpp/releases/tag/v1.1.0)）</sub>

**xorbitsai/inference v4.3.0**<br>11月26日，次版本更新。<br><sub>（来源：[GitHub 版本发布](https://github.com/xorbitsai/inference/releases/tag/v4.3.0)）</sub>

**alesha-pro/llm.asm**<br>11月27日消息，该项目用纯 x86-64 NASM 汇编编写了 Qwen3-0.6B 推理、裸机启动 OS 和 Mini-GPT 训练器。<br><sub>（来源：[GitHub 新项目](https://github.com/alesha-pro/llm.asm)）</sub>

**nexu-io/opengame**<br>11月27日消息，该项目提供游戏素材，支持将编码代理转化为全栈 AI 游戏工作室。<br><sub>（来源：[GitHub 新项目](https://github.com/nexu-io/opengame)）</sub>

**bendlang/bend：通过证明阻止 AI 错误的快速语言**<br>11月27日消息，Bend 2 是一种通过证明来阻止 AI 错误的快速语言。<br><sub>（来源：[GitHub Trending](https://github.com/bendlang/bend)）</sub>

#### 学术前沿

**Google 发布 Cogentic 研究论文**<br>11月25日，Google Research 发布了包含整数分解、离散对数等内容的研究论文，内容发布在 GitHub 上。<br><sub>（来源：[Hacker News](https://github.com/google-research/google-research/tree/master/cogentic_research_papers)）</sub>

**Sage-Med：医疗多模态智能的扩展**<br>11月25日，本文提出 Sage-Med-Preview 模型，通过结合特定阶段的数据筛选和渐进式训练课程，在视觉理解和医疗语言能力上均有显著提升。<br><sub>（来源：[Hugging Face 热门论文](https://arxiv.org/abs/2611.34575)）</sub>

**Any-Rate：基于编码位平面的半比特多精度量化**<br>11月25日，本文提出 Any-Rate 方法，从单个检查点提供 2-8 比特的量化，在 2-4 比特范围内以半比特步进。<br><sub>（来源：[arXiv · 高效推理](https://arxiv.org/abs/2611.34402)）</sub>

**Anthropic 发布 GRH Lean 验证精简版**<br>11月26日，Anthropic 与 Claude 合作发布了黎曼猜想和广义黎曼猜想的 Lean 4 证明精简版。<br><sub>（来源：[Hacker News](https://github.com/lsernau/grh-lean)）</sub>

#### 产业纵横

**Google 要求 AI 代理使用其 MCP 服务器**<br>11月26日，Google 规定从 2027 年起，AI 代理必须通过其 MCP 服务器访问 Workspace 服务。<br><sub>（来源：[Hacker News](https://techstackups.com/articles/google-workspace-ai-agents-mcp/)）</sub>

### 活动预告

**EuroVis 2027 论文截稿**<br>12月3日，Eurographics Conference on Visualization（EuroVis 2027，CCF-B 类，图形学与多媒体）Full papers的论文提交截止时间为北京时间12月3日 19:59，摘要截止时间为11月24日 19:59。会议将于 May 31-June 4, 2027 在 Stuttgart, Germany 举行。<br><sub>（来源：[会议官网](https://eurovis27.github.io/web/)）</sub>

<sub>标题和正文由 AI 根据原文整理（glm-4.7-flash），可能有误，请以原文为准。 俱乐部动态的统计日期为11月26日，数据来自[俱乐部开源仪表盘](https://osd.openatom.club/)。 会议截稿时间来自[CCFDDL](https://ccfddl.com/)，已换算成北京时间，请以会议官网为准。 有新闻线索欢迎[提交 Issue](https://github.com/game-life04/weekly-tech-agent/issues)。 本期由[每周科技收集 Agent](https://github.com/game-life04/weekly-tech-agent)于 2026-11-27 10:10（北京时间）自动生成。</sub>

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
