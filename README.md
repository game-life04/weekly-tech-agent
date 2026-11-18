# 每周科技收集 Agent

[![Daily digest](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml)
[![CI](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

每天早上整理 AI 与开源动态，参照《CCF开源快讯》的体例出一期「每日快讯」，8:30 推送到俱乐部 QQ 群；每周一再出一期「每周快讯」。全部由程序自动生成，内容就放在这个仓库里，打开就能看。

- **订阅**：[RSS 订阅源](https://raw.githubusercontent.com/game-life04/weekly-tech-agent/main/feed.xml)；或者在本仓库点 **Watch → Custom → Releases**，每周快讯出刊时 GitHub 会发邮件通知你。
- **投稿**：欢迎推荐值得一看的文章、开源项目、活动和俱乐部动态，请[提交 issue](https://github.com/game-life04/weekly-tech-agent/issues/new?template=submission.md)。
- **往期**：[每周快讯](weekly/README.md) · [每日快讯和日报](daily/README.md)

<!-- wta:latest:start -->

## 每日快讯 · 11.18（周三）

> 今日 AI 与开源要闻 **14** 条，3 分钟速读。<br>
> [单独打开](daily/2026/2026-11-18-kuaixun.md) · [公众号排版版](daily/2026/2026-11-18-kuaixun.html) · [完整日报（含热度和原题）](daily/2026/2026-11-18.md) · [往期日报](daily/README.md)

<details>
<summary>群消息文字版（点开后，点代码框右上角的按钮整段复制）</summary>

```text
【每日科技快讯】11月18日 周三
今日 AI 与开源要闻 14 条，3 分钟速读

【俱乐部动态】
1. 开放原子开源俱乐部合并 1 个 PR、提交 3 次
2. pwn.hust.college 合并 1 个 PR

【国内动态】
3. 阿里通义千问发布Qwen4-Max模型
→ 阿里通义千问发布Qwen4-Max模型，支持聊天、多模态理解、图像生成、文档处理和工具调用等功能。

【海外动态】
4. OpenAI发布GPT-6.2 Astra和Sol模型
→ OpenAI发布GPT-6.2 Astra和Sol，在专业输出、编程和效率上有所提升，成本更低。
5. Google Gemini Tasks功能免费
→ Google在六个国家免费提供Gemini Tasks功能，并新增美国功能和更深的Google Workspace集成。

【开源项目】
6. Claude-BugHunter 技能包包含 82 个技能
→ Claude-BugHunter 技能包包含 82 个技能和 681 个已披露漏洞模式，用于漏洞挖掘和外部红队工作。
7. Datasette Lite在浏览器运行
→ Datasette Lite使用WebAssembly和Pyodide，在浏览器中运行完整的Python应用。
8. inference-optimisation-skill 技能包
→ inference-optimisation-skill 技能包用于在任意硬件上优化本地 LLM 推理速度。
9. LangChain指南：如何为AI智能体选择安全沙箱
→ LangChain提供为AI智能体选择安全沙箱的指南，包括文件系统隔离、网络访问和资源限制。
10. usestrix/strix
→ 开源 AI 渗透测试工具，用于发现和修复应用漏洞。

【学术前沿】
11. SWE-CoWork：评测组织中的数字员工
→ 本文提出SWE-CoWork基准，模拟软件组织环境评测编码智能体。实验发现模型在部分实现与任务交付间存在巨大差距，即使提供完整需求也难以显著提升成功率。
12. K2-Horizon：开源语言模型前沿舰队
→ K2-Horizon包含从0.9B到375B-A23B的六款开源模型，用于通用推理和智能体工作。引入Mixture-of-Value Attention和softplus注意力门控，36B-A4B模型在相同数据下接近32B密集模型性能。
13. Sage S2.1 Flash 技术报告
→ We introduce Sage S1.5 Flash, a 320-billion-parameter general-purpose mixture-of-experts model designed to reason over…
14. VibePrevisBench：评测Blender中的4D场景生成
→ 本文提出VibePrevisBench基准，评估智能体在Blender中重建4D场景的能力。通过规则和视觉语言模型双重检查，发现多模态理解是关键，且智能体在错误修正上存在不足。

完整版（含原文链接）：https://github.com/game-life04/weekly-tech-agent/blob/main/daily/2026/2026-11-18-kuaixun.md
标题和要点由 AI 整理，可能有误，请以原文为准。
```

</details>

### 今日快讯

#### 俱乐部动态

**开放原子开源俱乐部合并 1 个 PR、提交 3 次**<br>11月17日，据俱乐部开源仪表盘统计，开放原子开源俱乐部跟踪的 122 个仓库中有 1 个有人参与开发，共新增 PR 2 个、合并 1 个，提交 3 次，新增代码 19 行、删除 28 行，1 位贡献者参与。<br><sub>（来源：[俱乐部开源仪表盘](https://osd.openatom.club/)）</sub>

**pwn.hust.college 合并 1 个 PR**<br>11月17日，pwn.hust.college SIG的 pwn.hust.college 仓库新增 PR 1 个、合并 1 个、提交 3 次、新增代码 19 行，1 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/pwn.hust.college)）</sub>

#### 国内动态

**阿里通义千问发布Qwen4-Max模型**<br>11月16日，阿里通义千问发布Qwen4-Max模型，支持聊天、多模态理解、图像生成、文档处理和工具调用等功能。<br><sub>（来源：[Hacker News](https://qwen.ai/blog?id=qwen4-max)）</sub>

#### 海外动态

**OpenAI发布GPT-6.2 Astra和Sol模型**<br>11月18日，OpenAI发布GPT-6.2 Astra和Sol，在专业输出、编程和效率上有所提升，成本更低。<br><sub>（来源：[OpenAI](https://openai.com/index/introducing-gpt-6-2-astra-sol)）</sub>

**Google Gemini Tasks功能免费**<br>11月18日，Google在六个国家免费提供Gemini Tasks功能，并新增美国功能和更深的Google Workspace集成。<br><sub>（来源：[Google AI](https://blog.google/innovation-and-ai/products/gemini-app/tasks-in-gemini-free-new-features/)）</sub>

#### 开源项目

**Claude-BugHunter 技能包包含 82 个技能**<br>11月18日消息，Claude-BugHunter 技能包包含 82 个技能和 681 个已披露漏洞模式，用于漏洞挖掘和外部红队工作。<br><sub>（来源：[GitHub Trending](https://github.com/elementalsouls/Claude-BugHunter)）</sub>

**Datasette Lite在浏览器运行**<br>11月18日，Datasette Lite使用WebAssembly和Pyodide，在浏览器中运行完整的Python应用。<br><sub>（来源：[Simon Willison](https://simonwillison.net/2026/Nov/17/datasette-lite/)）</sub>

**inference-optimisation-skill 技能包**<br>11月18日消息，inference-optimisation-skill 技能包用于在任意硬件上优化本地 LLM 推理速度。<br><sub>（来源：[GitHub 新项目](https://github.com/sybil-solutions/inference-optimisation-skill)）</sub>

**LangChain指南：如何为AI智能体选择安全沙箱**<br>11月18日，LangChain提供为AI智能体选择安全沙箱的指南，包括文件系统隔离、网络访问和资源限制。<br><sub>（来源：[LangChain 博客](https://www.langchain.com/blog/how-to-choose-the-right-sandbox-for-your-agent)）</sub>

**usestrix/strix**<br>11月18日消息，开源 AI 渗透测试工具，用于发现和修复应用漏洞。<br><sub>（来源：[GitHub Trending](https://github.com/usestrix/strix)）</sub>

#### 学术前沿

**SWE-CoWork：评测组织中的数字员工**<br>11月16日，本文提出SWE-CoWork基准，模拟软件组织环境评测编码智能体。实验发现模型在部分实现与任务交付间存在巨大差距，即使提供完整需求也难以显著提升成功率。<br><sub>（来源：[arXiv · 智能体](https://arxiv.org/abs/2611.20218)）</sub>

**K2-Horizon：开源语言模型前沿舰队**<br>11月16日，K2-Horizon包含从0.9B到375B-A23B的六款开源模型，用于通用推理和智能体工作。引入Mixture-of-Value Attention和softplus注意力门控，36B-A4B模型在相同数据下接近32B密集模型性能。<br><sub>（来源：[Hugging Face 热门论文](https://arxiv.org/abs/2611.21003)）</sub>

**Sage S2.1 Flash 技术报告**<br>11月16日，We introduce Sage S1.5 Flash, a 320-billion-parameter general-purpose mixture-of-experts model designed to reason over…<br><sub>（来源：[Hugging Face 热门论文](https://arxiv.org/abs/2611.21072)）</sub>

**VibePrevisBench：评测Blender中的4D场景生成**<br>11月18日消息，本文提出VibePrevisBench基准，评估智能体在Blender中重建4D场景的能力。通过规则和视觉语言模型双重检查，发现多模态理解是关键，且智能体在错误修正上存在不足。<br><sub>（来源：[arXiv · 智能体](https://arxiv.org/abs/2611.15789)）</sub>

<sub>标题和正文由 AI 根据原文整理（glm-4.7-flash），可能有误，请以原文为准。 俱乐部动态的统计日期为11月17日，数据来自[俱乐部开源仪表盘](https://osd.openatom.club/)。 有新闻线索欢迎[提交 Issue](https://github.com/game-life04/weekly-tech-agent/issues)。 本期由[每周科技收集 Agent](https://github.com/game-life04/weekly-tech-agent)于 2026-11-18 09:36（北京时间）自动生成。</sub>

## 每周快讯 第 5 期 · 11.09–11.15

> 本期头条：DeepMind 推出 AlphaProof Code 验证复杂软件<br>
> 上周 AI 与开源要闻 **26** 条，5 分钟速读。<br>
> [阅读全文](weekly/2026-W46.md) · [公众号排版版](weekly/2026-W46.html) · [往期快讯](weekly/README.md)

**俱乐部动态**<br>
✨ [开放原子开源俱乐部一周合并 15 个 PR、提交 16 次](https://osd.openatom.club/)<br>
✨ [pwnhustcollege\_skill 一周合并 3 个 PR](https://github.com/hust-open-atom-club/pwnhustcollege_skill)<br>
✨ [pwn.hust.college 一周合并 3 个 PR](https://github.com/hust-open-atom-club/pwn.hust.college)<br>
✨ [homebrew-tap 一周合并 3 个 PR](https://github.com/hust-open-atom-club/homebrew-tap)

**国内动态**<br>
✨ [千问办公2.0上线Team Agent协作功能](https://zhidx.com/p/608469.html)<br>
✨ [DeepSeek开放全家桶应用API](https://zhidx.com/p/610514.html)

**海外动态**<br>
✨ [Claude Fable 5.2 和 Claude Mythos 5.2 发布](https://www.anthropic.com/claude-fable-and-mythos-5-2)<br>
✨ [Muse Ember：最小且高效的模型](https://research.meta.ai/blog/muse-ember)<br>
✨ [Gemini 4 Carbon 现已上线](https://deepmind.google/blog/gemini-4-carbon-is-now-available/)<br>
✨ [Gemini 4 Hydrogen：面向代理工作流的高效模型](https://deepmind.google/blog/introducing-gemini-4-hydrogen/)<br>
✨ [李飞飞World Labs开放Atlas世界模型](https://www.ifanr.com/1689379?utm_source=rss&utm_medium=rss&utm_campaign=)

**开源项目**<br>
✨ [Llama-modchip: 284B DeepSeek on 64GB RAM, no GPU](https://github.com/synchopate/llama-modchip)<br>
✨ [Show HN：将你的编码代理迁移到现代 Web 原语](https://github.com/GoogleChrome/modern-web-guidance)<br>
✨ [smolmaxxing：让旧设备运行大型语言模型](https://github.com/hyperionaidev/smolmaxxing/)<br>
✨ [GoogleChrome/modern-web-guidance-src](https://github.com/GoogleChrome/modern-web-guidance-src)

**学术前沿**<br>
✨ [DeepMind 推出 AlphaProof Code 验证复杂软件](https://deepmind.google/blog/introducing-alphaproof-code/)<br>
✨ [DeepMind 发布 AlphaGenome 2 解码 DNA](https://deepmind.google/blog/alphagenome-2-deciphering-how-cells-read-dna-to-better-understand-disease/)<br>
✨ [AI 解锁哥德尔手稿，据说包含数百个已证明的定理](https://www.theguardian.com/science/2026/nov/13/kurt-godel-notebooks-ai-helps-unlock-hidden-discoveries-man-who-transformed-maths)

**产业纵横**<br>
✨ [高通展示端侧MoE智能体](https://www.qbitai.com/2026/11/508478.html)<br>
✨ [Amazon 用 Strands Decider 替换 Sonnet 4.6，节省数百万美元](https://strandsagents.com/blog/amazon-saves-millions-replacing-sonnet-with-strands-decider/)<br>
✨ [Anthropic 递交 IPO 申请](https://ipo.anthropic.com/us/)

**活动预告**<br>
✨ [CVPR 2027 论文截稿](https://cvpr.thecvf.com/Conferences/2027)<br>
✨ [EuroVis 2027 论文截稿](https://eurovis27.github.io/web/)<br>
✨ [AAMAS 2027 论文截稿](https://warwick.ac.uk/fac/sci/dcs/aamas2027/)<br>
✨ [ICAPS 2027 论文截稿](https://icaps27.icaps-conference.org/)<br>
✨ [COLING 2027 论文截稿](https://2027.coling-iccl.org/)

<!-- wta:latest:end -->

---

## 关于这个项目

内容由程序自动抓取、去重、打分，再由大模型分栏和改写（页面上都有标注，可能有误，请以原文为准），GitHub Actions 每天定时运行，不需要服务器。收集哪些来源、怎么工作、怎么在本地运行和加一个信息来源，见 [docs/about.md](docs/about.md)；参与贡献见 [CONTRIBUTING.md](CONTRIBUTING.md)。

### 致谢

设计上参考了 [Horizon](https://github.com/Thysrael/Horizon)、[agents-radar](https://github.com/duanyytop/agents-radar) 和 [AIHOT](https://github.com/KKKKhazix/AIHOT)。每周快讯的体例参照 CCF 开源发展技术委员会的《CCF开源快讯》，俱乐部数据来自俱乐部的 [Open-Source-Dashboard](https://github.com/hust-open-atom-club/Open-Source-Dashboard)，会议截稿数据来自 [ccf-deadlines](https://github.com/ccfddl/ccf-deadlines)。

### 许可证

[MIT](LICENSE)
