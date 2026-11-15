# 每周科技收集 Agent

[![Daily digest](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml)
[![CI](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

每天早上整理 AI 与开源动态，参照《CCF开源快讯》的体例出一期「每日快讯」，8:30 推送到俱乐部 QQ 群；每周一再出一期「每周快讯」。全部由程序自动生成，内容就放在这个仓库里，打开就能看。

- **订阅**：[RSS 订阅源](https://raw.githubusercontent.com/game-life04/weekly-tech-agent/main/feed.xml)；或者在本仓库点 **Watch → Custom → Releases**，每周快讯出刊时 GitHub 会发邮件通知你。
- **投稿**：欢迎推荐值得一看的文章、开源项目、活动和俱乐部动态，请[提交 issue](https://github.com/game-life04/weekly-tech-agent/issues/new?template=submission.md)。
- **往期**：[每周快讯](weekly/README.md) · [每日快讯和日报](daily/README.md)

<!-- wta:latest:start -->

## 每日快讯 · 11.16（周一）

> 今日 AI 与开源要闻 **17** 条，3 分钟速读。<br>
> [单独打开](daily/2026/2026-11-16-kuaixun.md) · [公众号排版版](daily/2026/2026-11-16-kuaixun.html) · [完整日报（含热度和原题）](daily/2026/2026-11-16.md) · [往期日报](daily/README.md)

<details>
<summary>群消息文字版（点开后，点代码框右上角的按钮整段复制）</summary>

```text
【每日科技快讯】11月16日 周一
今日 AI 与开源要闻 17 条，3 分钟速读

【俱乐部动态】
1. 开放原子开源俱乐部合并 1 个 PR、提交 0 次
2. pwnhustcollege_skill 合并 1 个 PR
3. AtomGit-Mobile4Android 新增 1 个 PR

【国内动态】
4. 百度词元所发布首日数据亮眼
→ 百度词元所发布首日新增供应商超100家，客户超1000家，日均调用次数突破5000万次。
5. DeepSeek 开放全家桶应用 API
→ DeepSeek 正式开放全家桶应用 API，方便开发者调用。
6. 华为云上线 openPangu-2.1-Pro 模型
→ 华为云 MaaS 平台上线开源盘古模型 openPangu-2.1-Pro，围绕 Agent 开发、AI 编码和推理优化方向能力升级。

【海外动态】
7. OpenAI 科学博客上线
→ OpenAI 上线科学博客，分享新发现、实用方法和研究人员的一手经验。

【开源项目】
8. Unsloth 发布 Qwen3.8-27B 动态量化 v3.1
→ Unsloth 发布 Qwen3.8-27B 的动态量化 v3.1，在 Terminal Bench 等基准测试中平均准确率提升 5-10%。
9. plannotator：管理智能体工作流和代码审查
→ plannotator 是一个用于管理智能体工作流、代码审查和团队协作的桌面工具。
10. 腾讯 LoopForge：代码智能体工作流编排工具
→ 腾讯开源的代码智能体工作流编排工具，支持本地化部署，可编排 Codex 和 Claude Code。
11. ag-ui：Agent-User 交互协议
→ ag-ui-protocol/ag-ui 是 Agent-User 交互协议，旨在将智能体集成到前端应用中。
12. stitch-skills：Agent Skills 库
→ google-labs-code/stitch-skills 是与 Stitch MCP 服务器配合使用的 Agent Skills 库，兼容多种编码智能体。

【学术前沿】
13. DeepSeek V3 在 190 行纯 JAX 代码中实现
→ 开发者用 190 行纯 JAX 代码在 MacBook Air 上从头预训练了 DeepSeek V3，展示了其架构细节。
14. 现代大模型中的位置编码解析
→ 文章深入解析 RoPE 等方法如何编码和处理 Token 位置信息，并探讨现代架构的适配。
15. OpenAI 探索标准模型在格点上的非微扰定义
→ OpenAI 探索标准模型在格点上的非微扰定义，借助 GPT-6 Astra 将想法转化为详细证明。
16. CoMem：基于对比记忆学习的选择性上下文压缩
→ 针对长上下文推理中任务相关证据分布差异大的问题，提出 CoMem 框架，通过查询引导的对比压缩学习实现高效推理。

【产业纵横】
17. 英伟达被指通过投资初创公司制造 GPU 短缺
→ 华尔街日报报道，英伟达通过投资 AI 初创公司来购买其 GPU，人为推高了 GPU 和内存短缺。

【活动预告】
· 11月17日 CVPR 2027 论文截稿

上周快讯（11.09–11.15）已出：https://github.com/game-life04/weekly-tech-agent/blob/main/weekly/2026-W46.md
完整版（含原文链接）：https://github.com/game-life04/weekly-tech-agent/blob/main/daily/2026/2026-11-16-kuaixun.md
标题和要点由 AI 整理，可能有误，请以原文为准。
```

</details>

### 今日快讯

#### 俱乐部动态

**开放原子开源俱乐部合并 1 个 PR、提交 0 次**<br>11月15日，据俱乐部开源仪表盘统计，开放原子开源俱乐部跟踪的 122 个仓库中有 2 个有人参与开发，共新增 PR 1 个、合并 1 个，提交 0 次，新增代码 0 行、删除 0 行，3 位贡献者参与。<br><sub>（来源：[俱乐部开源仪表盘](https://osd.openatom.club/)）</sub>

**pwnhustcollege\_skill 合并 1 个 PR**<br>11月15日，pwn.hust.college SIG的 pwnhustcollege\_skill 仓库合并 1 个，2 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/pwnhustcollege_skill)）</sub>

**AtomGit-Mobile4Android 新增 1 个 PR**<br>11月15日，Agent SIG的 AtomGit-Mobile4Android 仓库新增 PR 1 个，1 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/AtomGit-Mobile4Android)）</sub>

#### 国内动态

**百度词元所发布首日数据亮眼**<br>11月14日，百度词元所发布首日新增供应商超100家，客户超1000家，日均调用次数突破5000万次。<br><sub>（来源：[雷峰网](https://www.leiphone.com/category/industrynews/cqPXhF38rM4VcVa7.html)）</sub>

**DeepSeek 开放全家桶应用 API**<br>11月15日，DeepSeek 正式开放全家桶应用 API，方便开发者调用。<br><sub>（来源：[新智元](https://aiera.com.cn/2026/11/15/other/admin/123914/%e5%88%9a%e5%88%9a%ef%bc%8cdeepseek%e5%85%a8%e5%ae%b6%e6%a1%b6api%e6%ad%a3%e5%bc%8f%e5%bc%80%e6%94%be%ef%bc%81%e4%bd%a0%e4%b9%9f%e8%83%bd%e9%80%a0%e4%b8%80%e4%b8%aadeepseek%e4%ba%86/)）</sub>

**华为云上线 openPangu-2.1-Pro 模型**<br>11月15日，华为云 MaaS 平台上线开源盘古模型 openPangu-2.1-Pro，围绕 Agent 开发、AI 编码和推理优化方向能力升级。<br><sub>（来源：[IT之家](https://www.ithome.com/1/027/450.htm)）</sub>

#### 海外动态

**OpenAI 科学博客上线**<br>11月16日，OpenAI 上线科学博客，分享新发现、实用方法和研究人员的一手经验。<br><sub>（来源：[OpenAI](https://openai.com/index/our-new-blog-for-science)）</sub>

#### 开源项目

**Unsloth 发布 Qwen3.8-27B 动态量化 v3.1**<br>11月14日，Unsloth 发布 Qwen3.8-27B 的动态量化 v3.1，在 Terminal Bench 等基准测试中平均准确率提升 5-10%。<br><sub>（来源：[Hacker News](https://unsloth.ai/docs/models/qwen3.8)）</sub>

**plannotator：管理智能体工作流和代码审查**<br>11月16日消息，plannotator 是一个用于管理智能体工作流、代码审查和团队协作的桌面工具。<br><sub>（来源：[GitHub Trending](https://github.com/backnotprop/plannotator)）</sub>

**腾讯 LoopForge：代码智能体工作流编排工具**<br>11月16日消息，腾讯开源的代码智能体工作流编排工具，支持本地化部署，可编排 Codex 和 Claude Code。<br><sub>（来源：[GitHub Trending](https://github.com/Tencent/LoopForge)）</sub>

**ag-ui：Agent-User 交互协议**<br>11月16日消息，ag-ui-protocol/ag-ui 是 Agent-User 交互协议，旨在将智能体集成到前端应用中。<br><sub>（来源：[GitHub Trending](https://github.com/ag-ui-protocol/ag-ui)）</sub>

**stitch-skills：Agent Skills 库**<br>11月16日消息，google-labs-code/stitch-skills 是与 Stitch MCP 服务器配合使用的 Agent Skills 库，兼容多种编码智能体。<br><sub>（来源：[GitHub Trending](https://github.com/google-labs-code/stitch-skills)）</sub>

#### 学术前沿

**DeepSeek V3 在 190 行纯 JAX 代码中实现**<br>11月14日，开发者用 190 行纯 JAX 代码在 MacBook Air 上从头预训练了 DeepSeek V3，展示了其架构细节。<br><sub>（来源：[Hacker News](https://github.com/Vaibhaav-Tiwari/deepseek-v3-jax)）</sub>

**现代大模型中的位置编码解析**<br>11月15日，文章深入解析 RoPE 等方法如何编码和处理 Token 位置信息，并探讨现代架构的适配。<br><sub>（来源：[Ahead of AI](https://magazine.sebastianraschka.com/p/understanding-positional-embeddings)）</sub>

**OpenAI 探索标准模型在格点上的非微扰定义**<br>11月16日，OpenAI 探索标准模型在格点上的非微扰定义，借助 GPT-6 Astra 将想法转化为详细证明。<br><sub>（来源：[OpenAI](https://openai.com/index/step-toward-defining-the-standard-model)）</sub>

**CoMem：基于对比记忆学习的选择性上下文压缩**<br>11月16日消息，针对长上下文推理中任务相关证据分布差异大的问题，提出 CoMem 框架，通过查询引导的对比压缩学习实现高效推理。<br><sub>（来源：[arXiv · 长上下文与检索](https://arxiv.org/abs/2611.16384)）</sub>

#### 产业纵横

**英伟达被指通过投资初创公司制造 GPU 短缺**<br>11月14日，华尔街日报报道，英伟达通过投资 AI 初创公司来购买其 GPU，人为推高了 GPU 和内存短缺。<br><sub>（来源：[Hacker News](https://www.techpowerup.com/354814/nvidia-allegedly-engineered-scarcity-by-funding-ai-startups-to-buy-its-gpus)）</sub>

### 活动预告

**CVPR 2027 论文截稿**<br>11月17日，IEEE/CVF Conference on Computer Vision and Pattern Recognition（CVPR 2027，CCF-A 类，人工智能）论文提交截止时间为北京时间11月17日 19:59，摘要截止时间为11月11日 19:59。会议将于 June 22-25, 2027 在 Seattle, WA, United States 举行。<br><sub>（来源：[会议官网](https://cvpr.thecvf.com/Conferences/2027)）</sub>

<sub>标题和正文由 AI 根据原文整理（glm-4.7-flash），可能有误，请以原文为准。 俱乐部动态的统计日期为11月15日，数据来自[俱乐部开源仪表盘](https://osd.openatom.club/)。 会议截稿时间来自[CCFDDL](https://ccfddl.com/)，已换算成北京时间，请以会议官网为准。 有新闻线索欢迎[提交 Issue](https://github.com/game-life04/weekly-tech-agent/issues)。 本期由[每周科技收集 Agent](https://github.com/game-life04/weekly-tech-agent)于 2026-11-16 07:22（北京时间）自动生成。</sub>

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
✨ [梁圣再放大招：人人都能手搓 DeepSeek App 了](https://zhidx.com/p/610514.html)

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
