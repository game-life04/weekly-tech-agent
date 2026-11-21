# 每周科技收集 Agent

[![Daily digest](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml)
[![CI](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

每天早上整理 AI 与开源动态，参照《CCF开源快讯》的体例出一期「每日快讯」，8:30 推送到俱乐部 QQ 群；每周一再出一期「每周快讯」。全部由程序自动生成，内容就放在这个仓库里，打开就能看。

- **订阅**：[RSS 订阅源](https://raw.githubusercontent.com/game-life04/weekly-tech-agent/main/feed.xml)；或者在本仓库点 **Watch → Custom → Releases**，每周快讯出刊时 GitHub 会发邮件通知你。
- **投稿**：欢迎推荐值得一看的文章、开源项目、活动和俱乐部动态，请[提交 issue](https://github.com/game-life04/weekly-tech-agent/issues/new?template=submission.md)。
- **往期**：[每周快讯](weekly/README.md) · [每日快讯和日报](daily/README.md)

<!-- wta:latest:start -->

## 每日快讯 · 11.21（周六）

> 今日 AI 与开源要闻 **12** 条，3 分钟速读。<br>
> [单独打开](daily/2026/2026-11-21-kuaixun.md) · [公众号排版版](daily/2026/2026-11-21-kuaixun.html) · [完整日报（含热度和原题）](daily/2026/2026-11-21.md) · [往期日报](daily/README.md)

<details>
<summary>群消息文字版（点开后，点代码框右上角的按钮整段复制）</summary>

```text
【每日科技快讯】11月21日 周六
今日 AI 与开源要闻 12 条，3 分钟速读

【俱乐部动态】
1. 开放原子开源俱乐部合并 2 个 PR、提交 4 次
2. AtomGit-Mobile4Android 合并 2 个 PR
3. AtomGit-mobile4Harmony 提交 2 次

【开源项目】
4. vLLM 原生支持 Inkling 2 Mini
→ vLLM 原生支持 Thinking Machines 的 Inkling 2 Mini，这是一种循环 MoE 模型。
5. autoclip：开源 AI 视频剪辑工具
→ 开源 AI 视频剪辑工具，一键将长视频剪成短视频并生成字幕。
6. neonclipping：本地开源剪辑引擎
→ 本地开源剪辑引擎，粘贴链接即可在约 2 分钟内生成带字幕的 9:16 短视频。
7. agentscope：构建可理解可信任的智能体
→ agentscope 是一个用于构建和运行智能体的框架。
8. linger：完全在本地运行的个人 AI 代理
→ 完全在本地运行的个人 AI 代理，旨在打破科技巨头对 AI 的控制。

【学术前沿】
9. OpenAI 提出对抗蒸馏分层防护方法
→ OpenAI 采用分层方法结合训练、防护、检测和执行，以防止能力提取。
10. Frostbite：AI 发现并验证的新型 CPU 架构
→ AI 系统发现并验证了 Frostbite CPU，能效比现代超标量 CPU 高 4.59 倍。
11. 语言模型可自行重写权重
→ 语言模型通过自身推理重写权重，无需梯度和训练即可变强。
12. METR 更新 AI 能力时间跨度图
→ METR 报告更新了时间跨度图，指出部分 AI 能力呈指数级提升，但模型在需要判断的任务上不如编程任务表现好。

【活动预告】
· 12月3日 EuroVis 2027 论文截稿

完整版（含原文链接）：https://github.com/game-life04/weekly-tech-agent/blob/main/daily/2026/2026-11-21-kuaixun.md
标题和要点由 AI 整理，可能有误，请以原文为准。
```

</details>

### 今日快讯

#### 俱乐部动态

**开放原子开源俱乐部合并 2 个 PR、提交 4 次**<br>11月20日，据俱乐部开源仪表盘统计，开放原子开源俱乐部跟踪的 122 个仓库中有 2 个有人参与开发，共新增 PR 2 个、合并 2 个，提交 4 次，新增代码 3403 行、删除 593 行，3 位贡献者参与。<br><sub>（来源：[俱乐部开源仪表盘](https://osd.openatom.club/)）</sub>

**AtomGit-Mobile4Android 合并 2 个 PR**<br>11月20日，Agent SIG的 AtomGit-Mobile4Android 仓库新增 PR 1 个、合并 2 个、提交 2 次、新增代码 2851 行，2 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/AtomGit-Mobile4Android)）</sub>

**AtomGit-mobile4Harmony 提交 2 次**<br>11月20日，Agent SIG的 AtomGit-mobile4Harmony 仓库提交 2 次、新增代码 552 行，1 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/AtomGit-mobile4Harmony)）</sub>

#### 开源项目

**vLLM 原生支持 Inkling 2 Mini**<br>11月20日，vLLM 原生支持 Thinking Machines 的 Inkling 2 Mini，这是一种循环 MoE 模型。<br><sub>（来源：[vLLM 博客](https://vllm.ai/blog/2026-11-20-inkling2-mini)）</sub>

**autoclip：开源 AI 视频剪辑工具**<br>11月21日消息，开源 AI 视频剪辑工具，一键将长视频剪成短视频并生成字幕。<br><sub>（来源：[GitHub Trending](https://github.com/zhouxiaoka/autoclip)）</sub>

**neonclipping：本地开源剪辑引擎**<br>11月21日消息，本地开源剪辑引擎，粘贴链接即可在约 2 分钟内生成带字幕的 9:16 短视频。<br><sub>（来源：[GitHub 新项目](https://github.com/iamajmeena/neonclipping)）</sub>

**agentscope：构建可理解可信任的智能体**<br>11月21日消息，agentscope 是一个用于构建和运行智能体的框架。<br><sub>（来源：[GitHub Trending](https://github.com/agentscope-ai/agentscope)）</sub>

**linger：完全在本地运行的个人 AI 代理**<br>11月21日消息，完全在本地运行的个人 AI 代理，旨在打破科技巨头对 AI 的控制。<br><sub>（来源：[GitHub 新项目](https://github.com/simplexai-labs/linger)）</sub>

#### 学术前沿

**OpenAI 提出对抗蒸馏分层防护方法**<br>11月20日，OpenAI 采用分层方法结合训练、防护、检测和执行，以防止能力提取。<br><sub>（来源：[OpenAI](https://openai.com/index/combatting-adversarial-distillation)）</sub>

**Frostbite：AI 发现并验证的新型 CPU 架构**<br>11月20日，AI 系统发现并验证了 Frostbite CPU，能效比现代超标量 CPU 高 4.59 倍。<br><sub>（来源：[Hacker News](https://architectlabs.com/blog/frostbite)）</sub>

**语言模型可自行重写权重**<br>11月21日，语言模型通过自身推理重写权重，无需梯度和训练即可变强。<br><sub>（来源：[Hacker News](https://arxiv.org/abs/2611.21885)）</sub>

**METR 更新 AI 能力时间跨度图**<br>11月21日，METR 报告更新了时间跨度图，指出部分 AI 能力呈指数级提升，但模型在需要判断的任务上不如编程任务表现好。<br><sub>（来源：[MIT 科技评论](https://www.technologyreview.com/2026/11/20/1149399/the-most-misunderstood-graph-in-ai-just-got-a-major-update/)）</sub>

### 活动预告

**EuroVis 2027 论文截稿**<br>12月3日，Eurographics Conference on Visualization（EuroVis 2027，CCF-B 类，图形学与多媒体）Full papers的论文提交截止时间为北京时间12月3日 19:59，摘要截止时间为11月24日 19:59。会议将于 May 31-June 4, 2027 在 Stuttgart, Germany 举行。<br><sub>（来源：[会议官网](https://eurovis27.github.io/web/)）</sub>

<sub>标题和正文由 AI 根据原文整理（glm-4.7-flash），可能有误，请以原文为准。 俱乐部动态的统计日期为11月20日，数据来自[俱乐部开源仪表盘](https://osd.openatom.club/)。 会议截稿时间来自[CCFDDL](https://ccfddl.com/)，已换算成北京时间，请以会议官网为准。 有新闻线索欢迎[提交 Issue](https://github.com/game-life04/weekly-tech-agent/issues)。 本期由[每周科技收集 Agent](https://github.com/game-life04/weekly-tech-agent)于 2026-11-21 08:47（北京时间）自动生成。</sub>

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
