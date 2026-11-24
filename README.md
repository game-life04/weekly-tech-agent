# 每周科技收集 Agent

[![Daily digest](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml)
[![CI](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

每天早上整理 AI 与开源动态，参照《CCF开源快讯》的体例出一期「每日快讯」，8:30 推送到俱乐部 QQ 群；每周一再出一期「每周快讯」。全部由程序自动生成，内容就放在这个仓库里，打开就能看。

- **订阅**：[RSS 订阅源](https://raw.githubusercontent.com/game-life04/weekly-tech-agent/main/feed.xml)；或者在本仓库点 **Watch → Custom → Releases**，每周快讯出刊时 GitHub 会发邮件通知你。
- **投稿**：欢迎推荐值得一看的文章、开源项目、活动和俱乐部动态，请[提交 issue](https://github.com/game-life04/weekly-tech-agent/issues/new?template=submission.md)。
- **往期**：[每周快讯](weekly/README.md) · [每日快讯和日报](daily/README.md)

<!-- wta:latest:start -->

## 每日快讯 · 11.24（周二）

> 今日 AI 与开源要闻 **19** 条，3 分钟速读。<br>
> [单独打开](daily/2026/2026-11-24-kuaixun.md) · [公众号排版版](daily/2026/2026-11-24-kuaixun.html) · [完整日报（含热度和原题）](daily/2026/2026-11-24.md) · [往期日报](daily/README.md)

<details>
<summary>群消息文字版（点开后，点代码框右上角的按钮整段复制）</summary>

```text
【每日科技快讯】11月24日 周二
今日 AI 与开源要闻 19 条，3 分钟速读

【俱乐部动态】
1. 开放原子开源俱乐部合并 1 个 PR、提交 1 次
2. AtomGit-Mobile4Android 合并 1 个 PR

【国内动态】
3. 智能体复杂记忆甚至跑不过原始RAG？UIUC等首提「记忆税」
→ 新智元报道，UIUC 等机构提出「记忆税」概念，指出智能体在建立记忆时，原始交互记录会被重新编织，导致性能下降。
4. 蚂蚁 Ling-3.2-air 模型发布并开源
→ 蚂蚁科技发布并开源 Ling-3.2-air 模型，拥有 1240 亿总参数，在代码仓库问题解决和多步骤工作流任务上表现提升。

【海外动态】
5. Anthropic 2028 年电力来源分析
→ 分析 Anthropic 的总电力使用和排放，预计 2028 年将排放 3200 万公吨二氧化碳。
6. NariQ：10GB 文件中的 Qwen3.8-27B
→ NariQ 提供 Qwen3.8-27B 的 GGUF 版本，支持 3、2.5 和 2 位量化。
7. AI 智能体群攻克 P vs NP
→ AI 智能体群正在协同攻击计算机科学中最著名的开放问题 P vs NP。
8. 利用智能体和形式验证寻找更快的量子算法
→ Google DeepMind 使用智能体团队和形式验证来改进用于聚变和化学的量子算法。
9. OpenAI 和 Cisco 推出 Shirudo
→ OpenAI 和 Cisco 推出了用于 Linux 的开源运行时 Shirudo，帮助团队在部署补丁时保护运行中的系统。
10. Anthropic 发布 Claude Ship
→ Anthropic 推出 Claude Ship，允许 AI 智能体审查、修复和批准代码更改，旨在消除 AI 生成代码堆积带来的瓶颈。

【开源项目】
11. Skip the DRAM Tier: MoRI UMBP Runs the Agentic KV Cache on NVMe
→ vLLM 博客介绍 MoRI UMBP，在 AMD Instinct MI355X GPU 上，NVMe 上的 MoRI UMBP KV 池性能与 DRAM 池相差不到 1%。
12. XinaTian/MROffice
→ MR Office 是浏览器中的开源办公套件，支持文档、表格、演示文稿、PDF 和代码编辑。
13. erkamyaman/safe-anything
→ safe-anything 是一个快速、100% Rust 编写的漏洞扫描器，支持多种漏洞检测。
14. Ladybird 发布 alpha 版本，从零开发的开源浏览器引擎
→ Ladybird 浏览器引擎进入 alpha 测试阶段，这是一个从零开始开发的开源浏览器引擎。
15. phone-harness/phone-harness
→ let your agent control your phone。

【学术前沿】
16. cmHC: Balancing Stream Mixing in Hyper-Connections via Geometric Contraction
→ Manifold-constrained Hyper-Connections (mHC) extends residual connections to multiple streams and stabilizes residual p…
17. WeMM-Video: Pushing the Frontiers of Open-Source Omni-Modal Video Understanding
→ Video understanding, particularly with accompanying audio, remains a central challenge in multimodal intelligence. In t…
18. Non-penetrating World Models
→ We study a new problem of preventing object penetration in interactive video world models. To understand how existing m…
19. AutoPILOT: A Visual Agent Harness for Real-Time Gameplay
→ Multimodal foundation models can play video games well when the game waits for them, but often fail when it keeps runni…

【活动预告】
· 12月3日 EuroVis 2027 论文截稿

完整版（含原文链接）：https://github.com/game-life04/weekly-tech-agent/blob/main/daily/2026/2026-11-24-kuaixun.md
标题和要点由 AI 整理，可能有误，请以原文为准。
```

</details>

### 今日快讯

#### 俱乐部动态

**开放原子开源俱乐部合并 1 个 PR、提交 1 次**<br>11月23日，据俱乐部开源仪表盘统计，开放原子开源俱乐部跟踪的 122 个仓库中有 1 个有人参与开发，共新增 PR 0 个、合并 1 个，提交 1 次，新增代码 1807 行、删除 47 行，1 位贡献者参与。<br><sub>（来源：[俱乐部开源仪表盘](https://osd.openatom.club/)）</sub>

**AtomGit-Mobile4Android 合并 1 个 PR**<br>11月23日，Agent SIG的 AtomGit-Mobile4Android 仓库合并 1 个、提交 1 次、新增代码 1807 行，1 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/AtomGit-Mobile4Android)）</sub>

#### 国内动态

**智能体复杂记忆甚至跑不过原始RAG？UIUC等首提「记忆税」**<br>11月24日，新智元报道，UIUC 等机构提出「记忆税」概念，指出智能体在建立记忆时，原始交互记录会被重新编织，导致性能下降。<br><sub>（来源：[新智元](https://aiera.com.cn/2026/11/24/other/admin/125031/%e6%99%ba%e8%83%bd%e4%bd%93%e5%a4%8d%e6%9d%82%e8%ae%b0%e5%bf%86%e7%94%9a%e8%87%b3%e8%b7%91%e4%b8%8d%e8%bf%87%e5%8e%9f%e5%a7%8brag%ef%bc%9fuiuc%e7%ad%89%e9%a6%96%e6%8f%90%e3%80%8c%e8%ae%b0%e5%bf%86/)）</sub>

**蚂蚁 Ling-3.2-air 模型发布并开源**<br>11月24日，蚂蚁科技发布并开源 Ling-3.2-air 模型，拥有 1240 亿总参数，在代码仓库问题解决和多步骤工作流任务上表现提升。<br><sub>（来源：[IT之家](https://www.ithome.com/1/031/426.htm)）</sub>

#### 海外动态

**Anthropic 2028 年电力来源分析**<br>11月22日，分析 Anthropic 的总电力使用和排放，预计 2028 年将排放 3200 万公吨二氧化碳。<br><sub>（来源：[Hacker News](https://betterdatacenterproject.com/2026/11/16/how-ai-is-powered-a-breakdown-of-byop-and-grid-power/)）</sub>

**NariQ：10GB 文件中的 Qwen3.8-27B**<br>11月23日，NariQ 提供 Qwen3.8-27B 的 GGUF 版本，支持 3、2.5 和 2 位量化。<br><sub>（来源：[Hacker News](https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF)）</sub>

**AI 智能体群攻克 P vs NP**<br>11月23日，AI 智能体群正在协同攻击计算机科学中最著名的开放问题 P vs NP。<br><sub>（来源：[Hacker News](https://pequalnp.com/)）</sub>

**利用智能体和形式验证寻找更快的量子算法**<br>11月24日，Google DeepMind 使用智能体团队和形式验证来改进用于聚变和化学的量子算法。<br><sub>（来源：[Google DeepMind](https://deepmind.google/blog/finding-faster-quantum-algorithms-with-agents-and-formal-verification/)）</sub>

**OpenAI 和 Cisco 推出 Shirudo**<br>11月24日，OpenAI 和 Cisco 推出了用于 Linux 的开源运行时 Shirudo，帮助团队在部署补丁时保护运行中的系统。<br><sub>（来源：[OpenAI](https://openai.com/index/introducing-shirudo)）</sub>

**Anthropic 发布 Claude Ship**<br>11月24日，Anthropic 推出 Claude Ship，允许 AI 智能体审查、修复和批准代码更改，旨在消除 AI 生成代码堆积带来的瓶颈。<br><sub>（来源：[TechCrunch](https://techcrunch.com/2026/11/23/anthropic-launches-claude-ship-letting-ai-agents-review-fix-and-approve-code-changes/)）</sub>

#### 开源项目

**Skip the DRAM Tier: MoRI UMBP Runs the Agentic KV Cache on NVMe**<br>11月23日，vLLM 博客介绍 MoRI UMBP，在 AMD Instinct MI355X GPU 上，NVMe 上的 MoRI UMBP KV 池性能与 DRAM 池相差不到 1%。<br><sub>（来源：[vLLM 博客](https://vllm.ai/blog/2026-11-23-skip-the-dram-tier)）</sub>

**XinaTian/MROffice**<br>11月24日消息，MR Office 是浏览器中的开源办公套件，支持文档、表格、演示文稿、PDF 和代码编辑。<br><sub>（来源：[GitHub 新项目](https://github.com/XinaTian/MROffice)）</sub>

**erkamyaman/safe-anything**<br>11月24日消息，safe-anything 是一个快速、100% Rust 编写的漏洞扫描器，支持多种漏洞检测。<br><sub>（来源：[GitHub 新项目](https://github.com/erkamyaman/safe-anything)）</sub>

**Ladybird 发布 alpha 版本，从零开发的开源浏览器引擎**<br>11月24日，Ladybird 浏览器引擎进入 alpha 测试阶段，这是一个从零开始开发的开源浏览器引擎。<br><sub>（来源：[开源中国](https://www.oschina.net/news/503767/ladybird-alpha)）</sub>

**phone-harness/phone-harness**<br>11月24日消息，let your agent control your phone。<br><sub>（来源：[GitHub Trending](https://github.com/phone-harness/phone-harness)）</sub>

#### 学术前沿

**cmHC: Balancing Stream Mixing in Hyper-Connections via Geometric Contraction**<br>11月24日消息，Manifold-constrained Hyper-Connections (mHC) extends residual connections to multiple streams and stabilizes residual p…<br><sub>（来源：[Hugging Face 热门论文](https://arxiv.org/abs/2611.27193)）</sub>

**WeMM-Video: Pushing the Frontiers of Open-Source Omni-Modal Video Understanding**<br>11月24日消息，Video understanding, particularly with accompanying audio, remains a central challenge in multimodal intelligence. In t…<br><sub>（来源：[Hugging Face 热门论文](https://arxiv.org/abs/2611.26409)）</sub>

**Non-penetrating World Models**<br>11月24日消息，We study a new problem of preventing object penetration in interactive video world models. To understand how existing m…<br><sub>（来源：[Hugging Face 热门论文](https://arxiv.org/abs/2611.27963)）</sub>

**AutoPILOT: A Visual Agent Harness for Real-Time Gameplay**<br>11月24日消息，Multimodal foundation models can play video games well when the game waits for them, but often fail when it keeps runni…<br><sub>（来源：[arXiv · 智能体](https://arxiv.org/abs/2611.28202)）</sub>

### 活动预告

**EuroVis 2027 论文截稿**<br>12月3日，Eurographics Conference on Visualization（EuroVis 2027，CCF-B 类，图形学与多媒体）Full papers的论文提交截止时间为北京时间12月3日 19:59，摘要截止时间为11月24日 19:59。会议将于 May 31-June 4, 2027 在 Stuttgart, Germany 举行。<br><sub>（来源：[会议官网](https://eurovis27.github.io/web/)）</sub>

<sub>标题和正文由 AI 根据原文整理（glm-4.7-flash），可能有误，请以原文为准。 俱乐部动态的统计日期为11月23日，数据来自[俱乐部开源仪表盘](https://osd.openatom.club/)。 会议截稿时间来自[CCFDDL](https://ccfddl.com/)，已换算成北京时间，请以会议官网为准。 有新闻线索欢迎[提交 Issue](https://github.com/game-life04/weekly-tech-agent/issues)。 本期由[每周科技收集 Agent](https://github.com/game-life04/weekly-tech-agent)于 2026-11-24 12:17（北京时间）自动生成。</sub>

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
