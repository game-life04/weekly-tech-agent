# 每周科技收集 Agent

[![Daily digest](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml)
[![CI](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

每天早上整理 AI 与开源动态，参照《CCF开源快讯》的体例出一期「每日快讯」，8:30 推送到俱乐部 QQ 群；每周一再出一期「每周快讯」。全部由程序自动生成，内容就放在这个仓库里，打开就能看。

- **订阅**：[RSS 订阅源](https://raw.githubusercontent.com/game-life04/weekly-tech-agent/main/feed.xml)；或者在本仓库点 **Watch → Custom → Releases**，每周快讯出刊时 GitHub 会发邮件通知你。
- **投稿**：欢迎推荐值得一看的文章、开源项目、活动和俱乐部动态，请[提交 issue](https://github.com/game-life04/weekly-tech-agent/issues/new?template=submission.md)。
- **往期**：[每周快讯](weekly/README.md) · [每日快讯和日报](daily/README.md)

<!-- wta:latest:start -->

## 每日快讯 · 11.26（周四）

> 今日 AI 与开源要闻 **13** 条，3 分钟速读。<br>
> [单独打开](daily/2026/2026-11-26-kuaixun.md) · [公众号排版版](daily/2026/2026-11-26-kuaixun.html) · [完整日报（含热度和原题）](daily/2026/2026-11-26.md) · [往期日报](daily/README.md)

<details>
<summary>群消息文字版（点开后，点代码框右上角的按钮整段复制）</summary>

```text
【每日科技快讯】11月26日 周四
今日 AI 与开源要闻 13 条，3 分钟速读

【俱乐部动态】
1. 开放原子开源俱乐部合并 12 个 PR、提交 11 次
2. homebrew-tap 合并 9 个 PR
3. OpenAtomClub 合并 2 个 PR

【国内动态】
4. 可灵4.0全量上线 支持最长30秒视频
→ 快手可灵4.0全量上线，支持单次原生生成最长30秒视频，重点补强大幅度动作和复杂运镜。

【开源项目】
5. PenGPT：基于文本生成手写和素描的生成式 Transformer
→ PenGPT 是一个小型 Transformer 模型，专注于从文本生成手写和素描，项目投入比例是 80% 数据、15% 速度和 5% 架构。
6. Hy4 flash模型开源
→ 腾讯混元开源Hy4 flash的GGUF量化权重，官方实测在48GB显存设备上生成速度最高到每秒89个token。
7. Mastra：现代 TypeScript AI 应用框架
→ Mastra 是一个现代的 TypeScript 框架，用于构建 AI 驱动的应用程序和智能体。
8. EdgeEver：AI 原生笔记应用
→ EdgeEver 是一个 AI 原生笔记应用，支持 Evernote/Obsidian 替代品，提供即时多平台同步和 MCP 支持。
9. KuroCat：3D桌面打字小黑猫与AI编程伴侣
→ KuroCat是一个开源的3D/2D桌面打字小黑猫与AI编程伴侣，支持多种AI模型和平台。

【学术前沿】
10. Lazy Agents：利用可验证信念强化学习
→ 论文提出了可验证信念强化学习方法，利用模拟器计算后验概率指导智能体行动，提升长任务性能。
11. AI能解决以前顶级物理学家一天的问题
→ 前沿AI已经能解决以前顶级物理学家需要一整天才能解决的问题。
12. Claude和ChatGPT挑战AlphaFold
→ Anthropic最新版Claude在鲜为人知细菌蛋白质序列预测上表现优于其它大模型，OpenAI宣布其大模型成功设计出新蛋白质。
13. NightWatch：计算机使用代理主动感知框架
→ 论文提出了NightWatch框架，通过轻量级系统模型实时监控界面状态，减少感知滞后并提高任务成功率。

【活动预告】
· 12月3日 EuroVis 2027 论文截稿

完整版（含原文链接）：https://github.com/game-life04/weekly-tech-agent/blob/main/daily/2026/2026-11-26-kuaixun.md
标题和要点由 AI 整理，可能有误，请以原文为准。
```

</details>

### 今日快讯

#### 俱乐部动态

**开放原子开源俱乐部合并 12 个 PR、提交 11 次**<br>11月25日，据俱乐部开源仪表盘统计，开放原子开源俱乐部跟踪的 122 个仓库中有 4 个有人参与开发，共新增 PR 4 个、合并 12 个，提交 11 次，新增代码 53 行、删除 62 行，4 位贡献者参与。<br><sub>（来源：[俱乐部开源仪表盘](https://osd.openatom.club/)）</sub>

**homebrew-tap 合并 9 个 PR**<br>11月25日，Agent SIG的 homebrew-tap 仓库新增 PR 2 个、合并 9 个、提交 3 次、新增代码 1 行，1 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/homebrew-tap)）</sub>

**OpenAtomClub 合并 2 个 PR**<br>11月25日，数字基础设施维护 SIG的 OpenAtomClub 仓库新增 PR 1 个、合并 2 个、提交 7 次、新增代码 52 行，2 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/OpenAtomClub)）</sub>

#### 国内动态

**可灵4.0全量上线 支持最长30秒视频**<br>11月26日，快手可灵4.0全量上线，支持单次原生生成最长30秒视频，重点补强大幅度动作和复杂运镜。<br><sub>（来源：[新智元](https://aiera.com.cn/2026/11/26/other/admin/120096/%e7%88%86%e8%82%9d%e5%ae%9e%e6%b5%8b%e5%9b%9b%e5%a4%a7%e5%9b%bd%e4%ba%a7ai%e7%a5%9e%e5%99%a8%ef%bc%817%e5%a4%a7%e5%8f%98%e6%80%81%e8%80%83%e9%a2%98%ef%bc%8c%e9%80%bc%e5%87%ba%e6%9c%80%e9%87%8e/)）</sub>

#### 开源项目

**PenGPT：基于文本生成手写和素描的生成式 Transformer**<br>11月25日，PenGPT 是一个小型 Transformer 模型，专注于从文本生成手写和素描，项目投入比例是 80% 数据、15% 速度和 5% 架构。<br><sub>（来源：[Hacker News](https://greydanus.github.io/2026/11/12/pengpt/)）</sub>

**Hy4 flash模型开源**<br>11月25日，腾讯混元开源Hy4 flash的GGUF量化权重，官方实测在48GB显存设备上生成速度最高到每秒89个token。<br><sub>（来源：[开源中国](https://www.oschina.net/news/503813)）</sub>

**Mastra：现代 TypeScript AI 应用框架**<br>11月26日消息，Mastra 是一个现代的 TypeScript 框架，用于构建 AI 驱动的应用程序和智能体。<br><sub>（来源：[GitHub Trending](https://github.com/mastra-ai/mastra)）</sub>

**EdgeEver：AI 原生笔记应用**<br>11月26日消息，EdgeEver 是一个 AI 原生笔记应用，支持 Evernote/Obsidian 替代品，提供即时多平台同步和 MCP 支持。<br><sub>（来源：[GitHub Trending](https://github.com/tianma-if/edgeever)）</sub>

**KuroCat：3D桌面打字小黑猫与AI编程伴侣**<br>11月26日消息，KuroCat是一个开源的3D/2D桌面打字小黑猫与AI编程伴侣，支持多种AI模型和平台。<br><sub>（来源：[GitHub 新项目](https://github.com/qianyiai/kurocat)）</sub>

#### 学术前沿

**Lazy Agents：利用可验证信念强化学习**<br>11月25日，论文提出了可验证信念强化学习方法，利用模拟器计算后验概率指导智能体行动，提升长任务性能。<br><sub>（来源：[arXiv · 智能体](https://arxiv.org/abs/2611.32884)）</sub>

**AI能解决以前顶级物理学家一天的问题**<br>11月25日，前沿AI已经能解决以前顶级物理学家需要一整天才能解决的问题。<br><sub>（来源：[Ars Technica](https://arstechnica.com/ai/2026/11/ai-can-do-the-calculations-physicists-are-figuring-out-what-comes-next/)）</sub>

**Claude和ChatGPT挑战AlphaFold**<br>11月25日，Anthropic最新版Claude在鲜为人知细菌蛋白质序列预测上表现优于其它大模型，OpenAI宣布其大模型成功设计出新蛋白质。<br><sub>（来源：[Solidot](https://www.solidot.org/story?sid=85992)）</sub>

**NightWatch：计算机使用代理主动感知框架**<br>11月26日消息，论文提出了NightWatch框架，通过轻量级系统模型实时监控界面状态，减少感知滞后并提高任务成功率。<br><sub>（来源：[arXiv · 智能体](https://arxiv.org/abs/2611.28947)）</sub>

### 活动预告

**EuroVis 2027 论文截稿**<br>12月3日，Eurographics Conference on Visualization（EuroVis 2027，CCF-B 类，图形学与多媒体）Full papers的论文提交截止时间为北京时间12月3日 19:59，摘要截止时间为11月24日 19:59。会议将于 May 31-June 4, 2027 在 Stuttgart, Germany 举行。<br><sub>（来源：[会议官网](https://eurovis27.github.io/web/)）</sub>

<sub>标题和正文由 AI 根据原文整理（glm-4.7-flash），可能有误，请以原文为准。 俱乐部动态的统计日期为11月25日，数据来自[俱乐部开源仪表盘](https://osd.openatom.club/)。 会议截稿时间来自[CCFDDL](https://ccfddl.com/)，已换算成北京时间，请以会议官网为准。 有新闻线索欢迎[提交 Issue](https://github.com/game-life04/weekly-tech-agent/issues)。 本期由[每周科技收集 Agent](https://github.com/game-life04/weekly-tech-agent)于 2026-11-26 10:12（北京时间）自动生成。</sub>

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
