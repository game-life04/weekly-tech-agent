# 每周科技收集 Agent

[![Daily digest](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml)
[![CI](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

每天早上整理 AI 与开源动态，参照《CCF开源快讯》的体例出一期「每日快讯」，8:30 推送到俱乐部 QQ 群；每周一再出一期「每周快讯」。全部由程序自动生成，内容就放在这个仓库里，打开就能看。

- **订阅**：[RSS 订阅源](https://raw.githubusercontent.com/game-life04/weekly-tech-agent/main/feed.xml)；或者在本仓库点 **Watch → Custom → Releases**，每周快讯出刊时 GitHub 会发邮件通知你。
- **投稿**：欢迎推荐值得一看的文章、开源项目、活动和俱乐部动态，请[提交 issue](https://github.com/game-life04/weekly-tech-agent/issues/new?template=submission.md)。
- **往期**：[每周快讯](weekly/README.md) · [每日快讯和日报](daily/README.md)

<!-- wta:latest:start -->

## 每日快讯 · 11.25（周三）

> 今日 AI 与开源要闻 **14** 条，3 分钟速读。<br>
> [单独打开](daily/2026/2026-11-25-kuaixun.md) · [公众号排版版](daily/2026/2026-11-25-kuaixun.html) · [完整日报（含热度和原题）](daily/2026/2026-11-25.md) · [往期日报](daily/README.md)

<details>
<summary>群消息文字版（点开后，点代码框右上角的按钮整段复制）</summary>

```text
【每日科技快讯】11月25日 周三
今日 AI 与开源要闻 14 条，3 分钟速读

【俱乐部动态】
1. 开放原子开源俱乐部合并 1 个 PR、提交 4 次
2. AtomGit-Mobile4Android 合并 1 个 PR
3. .github 提交 3 次

【国内动态】
4. 智谱发布全新架构GLM-5.4
→ 智谱采用Loop Transformer架构发布GLM-5.4，非高峰时段最高可达200 Token/s。

【开源项目】
5. vLLM Day-0 Support for ERNIE 5.5 Flash Preview: Plugin Deployment and E2E Infer…
→ vLLM发布0.32.0版本，支持百度ERNIE 5.5 Flash Preview，提供插件部署和端到端推理加速。
6. LangChain推出Agent Lake
→ LangChain推出Agent Lake，用于存储和筛选智能体产生的轨迹，将其转化为修复方案和微调模型。
7. agy-fast：Google Antigravity MCP 加速插件
→ Google Antigravity 的非侵入式 MCP 加速插件可减少 LLM 轮次、代币配额和上传流量。
8. pierridotite/mobile-agent-testers
→ 在 GitHub 免费运行器上，20 个 Claude Code 智能体并行在 iOS 模拟器和 Android 模拟器中测试手机应用。
9. Anthropic发布Python SDK v2.14.0
→ Anthropic发布Python SDK v2.14.0，新增Google数据控制、合规审查支持，修复代理配置问题。

【学术前沿】
10. WeMM-Ecom：微信电商多模态内容理解
→ WeMM-Ecom 是一套多模态大语言模型，通过两阶段预训练和混合思维后训练提升电商能力。
11. OpenAI提出GPT-6蛋白质设计新方法
→ OpenAI利用推理和代码设计蛋白质结构和序列，实验室测试显示在五个目标上具有结合证据。
12. Google提出DeepCrossAttention架构
→ Google提出DeepCrossAttention架构，通过可学习权重和深度交叉注意力动态结合层输出，防止信息稀释。
13. Nemotron-Labs-VisualCreation：像素即代码的智能体视觉创作
→ Nemotron-Labs-VisualCreation 框架通过像素即代码连接视觉创作能力，使用离散视觉标记和显式程序表示图像。

【产业纵横】
14. Tidal 将禁止完全 AI 生成的音乐
→ Tidal 将于 12 月 9 日起移除完全 AI 生成的曲目，成为首个全面禁止 AI 音乐的流媒体平台。

【活动预告】
· 12月3日 EuroVis 2027 论文截稿

完整版（含原文链接）：https://github.com/game-life04/weekly-tech-agent/blob/main/daily/2026/2026-11-25-kuaixun.md
标题和要点由 AI 整理，可能有误，请以原文为准。
```

</details>

### 今日快讯

#### 俱乐部动态

**开放原子开源俱乐部合并 1 个 PR、提交 4 次**<br>11月24日，据俱乐部开源仪表盘统计，开放原子开源俱乐部跟踪的 122 个仓库中有 3 个有人参与开发，共新增 PR 4 个、合并 1 个，提交 4 次，新增代码 1515 行、删除 131 行，3 位贡献者参与，其中 1 位是第一次贡献。<br><sub>（来源：[俱乐部开源仪表盘](https://osd.openatom.club/)）</sub>

**AtomGit-Mobile4Android 合并 1 个 PR**<br>11月24日，Agent SIG的 AtomGit-Mobile4Android 仓库新增 PR 1 个、合并 1 个、提交 1 次、新增代码 1500 行，1 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/AtomGit-Mobile4Android)）</sub>

**.github 提交 3 次**<br>11月24日，数字基础设施维护 SIG的 .github 仓库新增 PR 1 个、提交 3 次、新增代码 15 行，1 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/.github)）</sub>

#### 国内动态

**智谱发布全新架构GLM-5.4**<br>11月24日，智谱采用Loop Transformer架构发布GLM-5.4，非高峰时段最高可达200 Token/s。<br><sub>（来源：[量子位](https://www.qbitai.com/2026/11/512423.html)）</sub>

#### 开源项目

**vLLM Day-0 Support for ERNIE 5.5 Flash Preview: Plugin Deployment and E2E Infer…**<br>11月24日，vLLM发布0.32.0版本，支持百度ERNIE 5.5 Flash Preview，提供插件部署和端到端推理加速。<br><sub>（来源：[vLLM 博客](https://vllm.ai/blog/2026-11-24-ernie-5-5-flash-preview)）</sub>

**LangChain推出Agent Lake**<br>11月25日，LangChain推出Agent Lake，用于存储和筛选智能体产生的轨迹，将其转化为修复方案和微调模型。<br><sub>（来源：[LangChain 博客](https://www.langchain.com/blog/the-agent-lake)）</sub>

**agy-fast：Google Antigravity MCP 加速插件**<br>11月25日消息，Google Antigravity 的非侵入式 MCP 加速插件可减少 LLM 轮次、代币配额和上传流量。<br><sub>（来源：[GitHub 新项目](https://github.com/INK-Q/agy-fast)）</sub>

**pierridotite/mobile-agent-testers**<br>11月25日消息，在 GitHub 免费运行器上，20 个 Claude Code 智能体并行在 iOS 模拟器和 Android 模拟器中测试手机应用。<br><sub>（来源：[GitHub 新项目](https://github.com/pierridotite/mobile-agent-testers)）</sub>

**Anthropic发布Python SDK v2.14.0**<br>11月25日，Anthropic发布Python SDK v2.14.0，新增Google数据控制、合规审查支持，修复代理配置问题。<br><sub>（来源：[GitHub 版本发布](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v2.14.0)）</sub>

#### 学术前沿

**WeMM-Ecom：微信电商多模态内容理解**<br>11月23日，WeMM-Ecom 是一套多模态大语言模型，通过两阶段预训练和混合思维后训练提升电商能力。<br><sub>（来源：[Hugging Face 热门论文](https://arxiv.org/abs/2611.30662)）</sub>

**OpenAI提出GPT-6蛋白质设计新方法**<br>11月24日，OpenAI利用推理和代码设计蛋白质结构和序列，实验室测试显示在五个目标上具有结合证据。<br><sub>（来源：[OpenAI](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities)）</sub>

**Google提出DeepCrossAttention架构**<br>11月24日，Google提出DeepCrossAttention架构，通过可学习权重和深度交叉注意力动态结合层输出，防止信息稀释。<br><sub>（来源：[Google Research](https://research.google/blog/supercharging-transformer-residual-connections/)）</sub>

**Nemotron-Labs-VisualCreation：像素即代码的智能体视觉创作**<br>11月24日，Nemotron-Labs-VisualCreation 框架通过像素即代码连接视觉创作能力，使用离散视觉标记和显式程序表示图像。<br><sub>（来源：[arXiv · 智能体](https://arxiv.org/abs/2611.31358)）</sub>

#### 产业纵横

**Tidal 将禁止完全 AI 生成的音乐**<br>11月25日，Tidal 将于 12 月 9 日起移除完全 AI 生成的曲目，成为首个全面禁止 AI 音乐的流媒体平台。<br><sub>（来源：[Hacker News](https://variety.com/2026/music/news/tidal-bans-ai-generated-music-1236956924/)）</sub>

### 活动预告

**EuroVis 2027 论文截稿**<br>12月3日，Eurographics Conference on Visualization（EuroVis 2027，CCF-B 类，图形学与多媒体）Full papers的论文提交截止时间为北京时间12月3日 19:59，摘要截止时间为11月24日 19:59。会议将于 May 31-June 4, 2027 在 Stuttgart, Germany 举行。<br><sub>（来源：[会议官网](https://eurovis27.github.io/web/)）</sub>

<sub>标题和正文由 AI 根据原文整理（glm-4.7-flash），可能有误，请以原文为准。 俱乐部动态的统计日期为11月24日，数据来自[俱乐部开源仪表盘](https://osd.openatom.club/)。 会议截稿时间来自[CCFDDL](https://ccfddl.com/)，已换算成北京时间，请以会议官网为准。 有新闻线索欢迎[提交 Issue](https://github.com/game-life04/weekly-tech-agent/issues)。 本期由[每周科技收集 Agent](https://github.com/game-life04/weekly-tech-agent)于 2026-11-25 17:51（北京时间）自动生成。</sub>

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
