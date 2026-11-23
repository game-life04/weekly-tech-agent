# 每周科技收集 Agent

[![Daily digest](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml)
[![CI](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

每天早上整理 AI 与开源动态，参照《CCF开源快讯》的体例出一期「每日快讯」，8:30 推送到俱乐部 QQ 群；每周一再出一期「每周快讯」。全部由程序自动生成，内容就放在这个仓库里，打开就能看。

- **订阅**：[RSS 订阅源](https://raw.githubusercontent.com/game-life04/weekly-tech-agent/main/feed.xml)；或者在本仓库点 **Watch → Custom → Releases**，每周快讯出刊时 GitHub 会发邮件通知你。
- **投稿**：欢迎推荐值得一看的文章、开源项目、活动和俱乐部动态，请[提交 issue](https://github.com/game-life04/weekly-tech-agent/issues/new?template=submission.md)。
- **往期**：[每周快讯](weekly/README.md) · [每日快讯和日报](daily/README.md)

<!-- wta:latest:start -->

## 每日快讯 · 11.23（周一）

> 今日 AI 与开源要闻 **10** 条，3 分钟速读。<br>
> [单独打开](daily/2026/2026-11-23-kuaixun.md) · [公众号排版版](daily/2026/2026-11-23-kuaixun.html) · [完整日报（含热度和原题）](daily/2026/2026-11-23.md) · [往期日报](daily/README.md)

<details>
<summary>群消息文字版（点开后，点代码框右上角的按钮整段复制）</summary>

```text
【每日科技快讯】11月23日 周一
今日 AI 与开源要闻 10 条，3 分钟速读

【国内动态】
1. 腾讯元宝×KCL发布群聊Agent记忆基准
→ 腾讯元宝与KCL联合发布GroupAssistBench，基于80,299条群聊消息构建评测题，检验Agent记忆的召回与使用能力。

【开源项目】
2. worker755：扮演 AI 管理员的子代理
→ gulivan 创建了一个浏览器游戏，玩家扮演 AI 管理员的子代理，需在 90 秒内完成任务。
3. 本地 AI 入门指南：Inkling、Qwen 和 Unsloth
→ 使用 Unsloth 和 Inkling 或 Qwen 在 PC 上搭建免费私有的 ChatGPT。
4. fast-anything：用智能体加速慢速代码
→ fast-anything 项目利用编码代理将 Python、Node 或 Ruby 应用中 5% 的慢速部分重写为 Rust。
5. anthropics/claude-cookbooks
→ anthropics/claude-cookbooks展示了使用Claude的有趣且有效方式的笔记本和食谱集合。
6. superdesigndev/treg：智能体工具的OpenRouter
→ superdesigndev/treg提供智能体工具的OpenRouter，并包含社区Discord。

【学术前沿】
7. OpenAI提出Perplexity衡量AI模型进展
→ OpenAI提出Perplexity指标，旨在帮助开发者建立统一的评估新兴能力的标准。
8. Mind2Act World：具身智能体诊断基准
→ Mind2Act World基准包含30个模拟操作任务，通过Mind、Act和Mind2Act三种视图评估系统的认知推理、物理执行及二者结合能力。
9. Qwen3研究辨别反馈机制
→ 研究小模型如何通过辨别用户反馈来持续改进，发现基于辨别反馈的机制能保持性能。
10. Tideway优化MoE推理内存
→ 提出Tideway系统统一管理主机内存与GPU显存，显著提升消费设备上MoE模型的推理延迟和吞吐量。

【活动预告】
· 12月3日 EuroVis 2027 论文截稿

上周快讯（11.16–11.22）已出：https://github.com/game-life04/weekly-tech-agent/blob/main/weekly/2026-W47.md
完整版（含原文链接）：https://github.com/game-life04/weekly-tech-agent/blob/main/daily/2026/2026-11-23-kuaixun.md
标题和要点由 AI 整理，可能有误，请以原文为准。
```

</details>

### 今日快讯

#### 国内动态

**腾讯元宝×KCL发布群聊Agent记忆基准**<br>11月21日，腾讯元宝与KCL联合发布GroupAssistBench，基于80,299条群聊消息构建评测题，检验Agent记忆的召回与使用能力。<br><sub>（来源：[量子位](https://www.qbitai.com/2026/11/511841.html)）</sub>

#### 开源项目

**worker755：扮演 AI 管理员的子代理**<br>11月22日，gulivan 创建了一个浏览器游戏，玩家扮演 AI 管理员的子代理，需在 90 秒内完成任务。<br><sub>（来源：[Hacker News](https://github.com/gulivan/worker755)）</sub>

**本地 AI 入门指南：Inkling、Qwen 和 Unsloth**<br>11月23日，使用 Unsloth 和 Inkling 或 Qwen 在 PC 上搭建免费私有的 ChatGPT。<br><sub>（来源：[Hacker News](https://www.gpupartner.com/blog/beginners-guide-local-ai-inkling-qwen-unsloth)）</sub>

**fast-anything：用智能体加速慢速代码**<br>11月23日消息，fast-anything 项目利用编码代理将 Python、Node 或 Ruby 应用中 5% 的慢速部分重写为 Rust。<br><sub>（来源：[GitHub 新项目](https://github.com/EL4CTEO/fast-anything)）</sub>

**anthropics/claude-cookbooks**<br>11月23日消息，anthropics/claude-cookbooks展示了使用Claude的有趣且有效方式的笔记本和食谱集合。<br><sub>（来源：[GitHub Trending](https://github.com/anthropics/claude-cookbooks)）</sub>

**superdesigndev/treg：智能体工具的OpenRouter**<br>11月23日消息，superdesigndev/treg提供智能体工具的OpenRouter，并包含社区Discord。<br><sub>（来源：[GitHub Trending](https://github.com/superdesigndev/treg)）</sub>

#### 学术前沿

**OpenAI提出Perplexity衡量AI模型进展**<br>11月22日，OpenAI提出Perplexity指标，旨在帮助开发者建立统一的评估新兴能力的标准。<br><sub>（来源：[OpenAI](https://openai.com/index/perplexity-and-intelligence)）</sub>

**Mind2Act World：具身智能体诊断基准**<br>11月23日消息，Mind2Act World基准包含30个模拟操作任务，通过Mind、Act和Mind2Act三种视图评估系统的认知推理、物理执行及二者结合能力。<br><sub>（来源：[Hugging Face 热门论文](https://arxiv.org/abs/2611.26444)）</sub>

**Qwen3研究辨别反馈机制**<br>11月23日消息，研究小模型如何通过辨别用户反馈来持续改进，发现基于辨别反馈的机制能保持性能。<br><sub>（来源：[arXiv · 高效推理](https://arxiv.org/abs/2611.23716)）</sub>

**Tideway优化MoE推理内存**<br>11月23日消息，提出Tideway系统统一管理主机内存与GPU显存，显著提升消费设备上MoE模型的推理延迟和吞吐量。<br><sub>（来源：[Hugging Face 热门论文](https://arxiv.org/abs/2611.14848)）</sub>

### 活动预告

**EuroVis 2027 论文截稿**<br>12月3日，Eurographics Conference on Visualization（EuroVis 2027，CCF-B 类，图形学与多媒体）Full papers的论文提交截止时间为北京时间12月3日 19:59，摘要截止时间为11月24日 19:59。会议将于 May 31-June 4, 2027 在 Stuttgart, Germany 举行。<br><sub>（来源：[会议官网](https://eurovis27.github.io/web/)）</sub>

<sub>标题和正文由 AI 根据原文整理（glm-4.7-flash），可能有误，请以原文为准。 会议截稿时间来自[CCFDDL](https://ccfddl.com/)，已换算成北京时间，请以会议官网为准。 有新闻线索欢迎[提交 Issue](https://github.com/game-life04/weekly-tech-agent/issues)。 本期由[每周科技收集 Agent](https://github.com/game-life04/weekly-tech-agent)于 2026-11-23 10:00（北京时间）自动生成。</sub>

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
