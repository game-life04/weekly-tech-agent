# 每周科技收集 Agent

[![Daily digest](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml)
[![CI](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

每天早上整理 AI 与开源动态，参照《CCF开源快讯》的体例出一期「每日快讯」，8:30 推送到俱乐部 QQ 群；每周一再出一期「每周快讯」。全部由程序自动生成，内容就放在这个仓库里，打开就能看。

- **订阅**：[RSS 订阅源](https://raw.githubusercontent.com/game-life04/weekly-tech-agent/main/feed.xml)；或者在本仓库点 **Watch → Custom → Releases**，每周快讯出刊时 GitHub 会发邮件通知你。
- **投稿**：欢迎推荐值得一看的文章、开源项目、活动和俱乐部动态，请[提交 issue](https://github.com/game-life04/weekly-tech-agent/issues/new?template=submission.md)。
- **往期**：[每周快讯](weekly/README.md) · [每日快讯和日报](daily/README.md)

<!-- wta:latest:start -->

## 每日快讯 · 11.10（周二）

> 今日 AI 与开源要闻 **18** 条，3 分钟速读。<br>
> [单独打开](daily/2026/2026-11-10-kuaixun.md) · [公众号排版版](daily/2026/2026-11-10-kuaixun.html) · [完整日报（含热度和原题）](daily/2026/2026-11-10.md) · [往期日报](daily/README.md)

<details>
<summary>群消息文字版（点开后，点代码框右上角的按钮整段复制）</summary>

```text
【每日科技快讯】11月10日 周二
今日 AI 与开源要闻 18 条，3 分钟速读

【俱乐部动态】
1. 开放原子开源俱乐部合并 2 个 PR、提交 3 次
2. pwnhustcollege_skill 合并 1 个 PR
3. pwn.hust.college 合并 1 个 PR

【国内动态】
4. 千问办公 2.0 上线团队协作功能
→ 千问办公 2.0 推出 Team Agent 协作功能，支持多人与 Agent 协同工作。
5. 赶在IPO前，Claude最强模型空降！宾大教授感慨“几乎达到AGI”
→ Anthropic 发布两款新模型，在基准测试中表现优异，已上线云服务。

【海外动态】
6. Claude Fable 5.2 和 Claude Mythos 5.2 发布
→ Anthropic 推出两款新模型，在编程、金融和科学领域表现优异。
7. OpenAI 推出 Control Room 管理系统
→ OpenAI 发布了用于追踪和停止研究基础设施中模型工作负载的中央系统。
8. CodeRabbit 使用 OpenAI 模型提升开发效率
→ CodeRabbit 利用 OpenAI 模型治理 AI 生成代码，使团队交付量提升 20 倍。
9. Claude Code 意外泄露 GitHub 上的机密
→ Claude Code 的“不再询问”提示导致密码和 API 密钥等敏感信息被公开。

【开源项目】
10. google-deepmind/mujoco
→ Multi-Joint dynamics with Contact. A general purpose physics simulator.
11. ZhuLinsen/daily_stock_analysis
→ LLM 驱动的多市场股票智能分析系统：多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。 LLM-powered multi-market stock analysis system with multi-source mark…
12. meta/astryx
→ An open source design system that's fully customizable and agent ready。
13. anthropics/claude-quickstarts
→ A collection of projects designed to help developers quickly get started with building deployable applications using th…
14. DIYgod/pinky
→ Let AI agents use your phone, with you in the loop.

【学术前沿】
15. What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents?
→ While multi-turn agentic reinforcement learning (RL) excels on long-horizon tasks, its performance gains remain highly…
16. PCBRouteAgent: How Close Are LLM Agents to Becoming PCB Routing Engineers?
→ Automating printed circuit board (PCB) routing requires coordinating board-level connectivity decisions with geometric…
17. Random Is Almost Enough? Stable and Low-Cost Benchmark Compression via BestRand
→ Benchmark compression reduces the often prohibitive time and cost of model evaluation by evaluating models on a small b…
18. LowRAM: Low-Rank Keys and Amortised Values for Composable KV Cache Compression…
→ Autoregressive decoding relies on the KV cache, whose memory footprint grows linearly with context length and caps batc…

【活动预告】
· 11月17日 CVPR 2027 论文截稿

完整版（含原文链接）：https://github.com/game-life04/weekly-tech-agent/blob/main/daily/2026/2026-11-10-kuaixun.md
标题和要点由 AI 整理，可能有误，请以原文为准。
```

</details>

### 今日快讯

#### 俱乐部动态

**开放原子开源俱乐部合并 2 个 PR、提交 3 次**<br>11月9日，据俱乐部开源仪表盘统计，开放原子开源俱乐部跟踪的 122 个仓库中有 6 个有人参与开发，共新增 PR 6 个、合并 2 个，提交 3 次，新增代码 31 行、删除 0 行，3 位贡献者参与。<br><sub>（来源：[俱乐部开源仪表盘](https://osd.openatom.club/)）</sub>

**pwnhustcollege\_skill 合并 1 个 PR**<br>11月9日，pwn.hust.college SIG的 pwnhustcollege\_skill 仓库新增 PR 1 个、合并 1 个、提交 2 次、新增代码 31 行，1 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/pwnhustcollege_skill)）</sub>

**pwn.hust.college 合并 1 个 PR**<br>11月9日，pwn.hust.college SIG的 pwn.hust.college 仓库合并 1 个、提交 1 次，2 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/pwn.hust.college)）</sub>

#### 国内动态

**千问办公 2.0 上线团队协作功能**<br>11月9日，千问办公 2.0 推出 Team Agent 协作功能，支持多人与 Agent 协同工作。<br><sub>（来源：[智东西](https://zhidx.com/p/608469.html)）</sub>

**赶在IPO前，Claude最强模型空降！宾大教授感慨“几乎达到AGI”**<br>11月10日，Anthropic 发布两款新模型，在基准测试中表现优异，已上线云服务。<br><sub>（来源：[智东西](https://zhidx.com/p/608593.html)）</sub>

#### 海外动态

**Claude Fable 5.2 和 Claude Mythos 5.2 发布**<br>11月9日，Anthropic 推出两款新模型，在编程、金融和科学领域表现优异。<br><sub>（来源：[Anthropic](https://www.anthropic.com/claude-fable-and-mythos-5-2)）</sub>

**OpenAI 推出 Control Room 管理系统**<br>11月9日，OpenAI 发布了用于追踪和停止研究基础设施中模型工作负载的中央系统。<br><sub>（来源：[OpenAI](https://openai.com/index/control-room)）</sub>

**CodeRabbit 使用 OpenAI 模型提升开发效率**<br>11月9日，CodeRabbit 利用 OpenAI 模型治理 AI 生成代码，使团队交付量提升 20 倍。<br><sub>（来源：[OpenAI](https://openai.com/index/coderabbit-codex-daybreak)）</sub>

**Claude Code 意外泄露 GitHub 上的机密**<br>11月10日，Claude Code 的“不再询问”提示导致密码和 API 密钥等敏感信息被公开。<br><sub>（来源：[Ars Technica](https://arstechnica.com/ai/2026/11/claude-code-settings-files-expose-thousands-of-secrets-on-github/)）</sub>

#### 开源项目

**google-deepmind/mujoco**<br>11月10日消息，Multi-Joint dynamics with Contact. A general purpose physics simulator.<br><sub>（来源：[GitHub Trending](https://github.com/google-deepmind/mujoco)）</sub>

**ZhuLinsen/daily\_stock\_analysis**<br>11月10日消息，LLM 驱动的多市场股票智能分析系统：多源行情、实时新闻、决策看板与自动推送，支持零成本定时运行。 LLM-powered multi-market stock analysis system with multi-source mark…<br><sub>（来源：[GitHub Trending](https://github.com/ZhuLinsen/daily_stock_analysis)）</sub>

**meta/astryx**<br>11月10日消息，An open source design system that's fully customizable and agent ready。<br><sub>（来源：[GitHub Trending](https://github.com/meta/astryx)）</sub>

**anthropics/claude-quickstarts**<br>11月10日消息，A collection of projects designed to help developers quickly get started with building deployable applications using th…<br><sub>（来源：[GitHub Trending](https://github.com/anthropics/claude-quickstarts)）</sub>

**DIYgod/pinky**<br>11月10日消息，Let AI agents use your phone, with you in the loop.<br><sub>（来源：[GitHub 新项目](https://github.com/DIYgod/pinky)）</sub>

#### 学术前沿

**What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents?**<br>11月10日消息，While multi-turn agentic reinforcement learning (RL) excels on long-horizon tasks, its performance gains remain highly…<br><sub>（来源：[arXiv · 智能体](https://arxiv.org/abs/2611.06483)）</sub>

**PCBRouteAgent: How Close Are LLM Agents to Becoming PCB Routing Engineers?**<br>11月10日消息，Automating printed circuit board (PCB) routing requires coordinating board-level connectivity decisions with geometric…<br><sub>（来源：[arXiv · 智能体](https://arxiv.org/abs/2611.08175)）</sub>

**Random Is Almost Enough? Stable and Low-Cost Benchmark Compression via BestRand**<br>11月10日消息，Benchmark compression reduces the often prohibitive time and cost of model evaluation by evaluating models on a small b…<br><sub>（来源：[Hugging Face 热门论文](https://arxiv.org/abs/2611.00883)）</sub>

**LowRAM: Low-Rank Keys and Amortised Values for Composable KV Cache Compression…**<br>11月10日消息，Autoregressive decoding relies on the KV cache, whose memory footprint grows linearly with context length and caps batc…<br><sub>（来源：[arXiv · 高效推理](https://arxiv.org/abs/2611.07025)）</sub>

### 活动预告

**CVPR 2027 论文截稿**<br>11月17日，IEEE/CVF Conference on Computer Vision and Pattern Recognition（CVPR 2027，CCF-A 类，人工智能）论文提交截止时间为北京时间11月17日 19:59，摘要截止时间为11月11日 19:59。会议将于 June 20-25, 2027 在 Seattle, WA, United States 举行。<br><sub>（来源：[会议官网](https://cvpr.thecvf.com/Conferences/2027)）</sub>

<sub>标题和正文由 AI 根据原文整理（glm-4.7-flash），可能有误，请以原文为准。 俱乐部动态的统计日期为11月9日，数据来自[俱乐部开源仪表盘](https://osd.openatom.club/)。 会议截稿时间来自[CCFDDL](https://ccfddl.com/)，已换算成北京时间，请以会议官网为准。 有新闻线索欢迎[提交 Issue](https://github.com/game-life04/weekly-tech-agent/issues)。 本期由[每周科技收集 Agent](https://github.com/game-life04/weekly-tech-agent)于 2026-11-10 10:07（北京时间）自动生成。</sub>

## 每周快讯 第 4 期 · 11.02–11.08

> 本期头条：OpenAI 构建可扩展的 Git 后端<br>
> 上周 AI 与开源要闻 **26** 条，5 分钟速读。<br>
> [阅读全文](weekly/2026-W45.md) · [公众号排版版](weekly/2026-W45.html) · [往期快讯](weekly/README.md)

**俱乐部动态**<br>
✨ [开放原子开源俱乐部一周合并 12 个 PR、提交 20 次](https://osd.openatom.club/)<br>
✨ [AtomGit-Mobile4Android 一周合并 3 个 PR](https://github.com/hust-open-atom-club/AtomGit-Mobile4Android)<br>
✨ [Open-Source-Dashboard 一周合并 2 个 PR](https://github.com/hust-open-atom-club/Open-Source-Dashboard)<br>
✨ [AtomGit-mobile4Harmony 一周合并 1 个 PR](https://github.com/hust-open-atom-club/AtomGit-mobile4Harmony)

**国内动态**<br>
✨ [美团发布 LongCat-2.5 多模态模型](https://zhidx.com/p/606379.html)<br>
✨ [赛迪研究院：我国AI推理数据量首超训练数据量](https://www.ithome.com/1/020/809.htm)<br>
✨ [月之暗面发布Kimi K3.1 Pro模型](https://huggingface.co/moonshotai/Kimi-K3.1-Pro)<br>
✨ [百度开源文心5.5 Flash Base](https://www.qbitai.com/2026/11/507787.html)

**海外动态**<br>
✨ [OpenAI 构建可扩展的 Git 后端](https://openai.com/index/scaling-git-at-openai)<br>
✨ [OpenAI 推出 Grid Protectors 计划](https://openai.com/index/grid-protectors-program)<br>
✨ [OpenAI 自动修复 Linux 内核漏洞](https://openai.com/index/a-thousand-fewer-paths-to-root)<br>
✨ [OpenAI 推出 GPT‑6 Cyber 模型](https://openai.com/index/introducing-gpt-6-cyber)<br>
✨ [OpenAI 发布 BioBasicsBench 基准](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science)<br>
✨ [Gemini Omni 1.2 Flash：原生15秒视频生成与编辑](https://deepmind.google/blog/gemini-omni-12-flash-fast-and-cost-effective-with-longer-clips/)

**开源项目**<br>
✨ [agent-desktop：AI 智能体的计算机使用 CLI](https://github.com/vercel-labs/agent-desktop)<br>
✨ [auto-ontology：语义图推理层 Python 框架](https://github.com/NVIDIA/auto-ontology)<br>
✨ [colibri：前沿 MoE 模型的分层推理引擎](https://github.com/JustVugg/colibri)<br>
✨ [agent-autoloop：命令行 Agent 自动接活工具](https://github.com/KKKKhazix/agent-autoloop)

**学术前沿**<br>
✨ [Astra：直接读写权重优化 Qwen](https://rikiyat.github.io/blog/weight-space-programming/)<br>
✨ [LLM 可读写神经网络权重](https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/)<br>
✨ [Hy-Nomas：自由形式交互式世界生成](https://arxiv.org/abs/2610.36729)

**产业纵横**<br>
✨ [四大 AI 公司推行 AI 数据抓取退出标准](https://www.ithome.com/1/020/837.htm)<br>
✨ [Images 2.6](https://openai.com/index/introducing-images-2-6/)

**活动预告**<br>
✨ [CVPR 2027 论文截稿](https://cvpr.thecvf.com/Conferences/2027)<br>
✨ [EuroVis 2027 论文截稿](https://eurovis27.github.io/web/)<br>
✨ [ICAPS 2027 论文截稿](https://icaps27.icaps-conference.org/)

<!-- wta:latest:end -->

---

## 关于这个项目

内容由程序自动抓取、去重、打分，再由大模型分栏和改写（页面上都有标注，可能有误，请以原文为准），GitHub Actions 每天定时运行，不需要服务器。收集哪些来源、怎么工作、怎么在本地运行和加一个信息来源，见 [docs/about.md](docs/about.md)；参与贡献见 [CONTRIBUTING.md](CONTRIBUTING.md)。

### 致谢

设计上参考了 [Horizon](https://github.com/Thysrael/Horizon)、[agents-radar](https://github.com/duanyytop/agents-radar) 和 [AIHOT](https://github.com/KKKKhazix/AIHOT)。每周快讯的体例参照 CCF 开源发展技术委员会的《CCF开源快讯》，俱乐部数据来自俱乐部的 [Open-Source-Dashboard](https://github.com/hust-open-atom-club/Open-Source-Dashboard)，会议截稿数据来自 [ccf-deadlines](https://github.com/ccfddl/ccf-deadlines)。

### 许可证

[MIT](LICENSE)
