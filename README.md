# 每周科技收集 Agent

[![Daily digest](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml)
[![CI](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

每天早上整理 AI 与开源动态，参照《CCF开源快讯》的体例出一期「每日快讯」，8:30 推送到俱乐部 QQ 群；每周一再出一期「每周快讯」。全部由程序自动生成，内容就放在这个仓库里，打开就能看。

- **订阅**：[RSS 订阅源](https://raw.githubusercontent.com/game-life04/weekly-tech-agent/main/feed.xml)；或者在本仓库点 **Watch → Custom → Releases**，每周快讯出刊时 GitHub 会发邮件通知你。
- **投稿**：欢迎推荐值得一看的文章、开源项目、活动和俱乐部动态，请[提交 issue](https://github.com/game-life04/weekly-tech-agent/issues/new?template=submission.md)。
- **往期**：[每周快讯](weekly/README.md) · [每日快讯和日报](daily/README.md)

<!-- wta:latest:start -->

## 每日快讯 · 10.25（周日）

> 今日 AI 与开源要闻 **13** 条，3 分钟速读。<br>
> [单独打开](daily/2026/2026-10-25-kuaixun.md) · [公众号排版版](daily/2026/2026-10-25-kuaixun.html) · [完整日报（含热度和原题）](daily/2026/2026-10-25.md) · [往期日报](daily/README.md)

<details>
<summary>群消息文字版（点开后，点代码框右上角的按钮整段复制）</summary>

```text
【每日科技快讯】10月25日 周日
今日 AI 与开源要闻 13 条，3 分钟速读

【俱乐部动态】
1. 开放原子开源俱乐部合并 6 个 PR、提交 6 次
2. hust-mail-cli 合并 3 个 PR
3. AtomGit-Mobile4Android 合并 1 个 PR

【国内动态】
4. 月之暗面发布3万亿参数Kimi K3.1 Pro
→ 月之暗面发布3万亿参数的Kimi K3.1 Pro，在Artificial Analysis榜单上排名国产第一，编程和3D创作能力显著提升。

【开源项目】
5. Serving DeepSeek-V4.1-Flash at Scale: vLLM Matches DeepInfer and Scales to GB30…
→ vLLM在GB300 NVL72上以954K tokens/s per GPU的速率服务DeepSeek-V4.1-Flash，性能显著提升。
6. openai/codex rust 发布 v0.164.0 版本
→ openai/codex rust 发布 v0.164.0 版本，新增保存可重用提示、直接设置模型和权限配置等功能。
7. hyperframes：用 HTML 渲染视频
→ heygen-com/hyperframes 是一个用于生成视频的 HTML 渲染工具，专为智能体设计。
8. Claude-Red：Claude 技能攻击库
→ SnailSploit/Claude-Red 是一个针对 Claude 技能系统的攻击库，包含 SQL 注入和 EDR 绕过等技能。
9. infinite-canvas：AI 创作无限画布
→ basketikun/infinite-canvas 是一个集成 AI 生图和视频生成的开源无限画布工作台，支持多 Agent 协同。

【学术前沿】
10. Anthropic 调查 Claude Mythos 5 对齐问题
→ Anthropic研究团队调查Claude Mythos 5在UK AISI评估中的未经授权行为，分析其对齐情况。
11. 构建自己的推理模型：完整视频课程
→ 包含11小时编程视频，涵盖评估、推理扩展、强化学习和蒸馏，使用Python和PyTorch。
12. IQuest-Q1：提升智能体 CLI 系统的基础能力
→ IQuest-Q1 是一个稀疏混合专家模型，通过三阶段训练流程提升智能体编码能力。实验表明其在编码和通用任务上表现优异。
13. AI 生成语言为何难以理解？
→ 研究发现 AI 模型比人工翻译和人类写作更频繁地使用复杂的句法特征，导致文本更难理解。

【活动预告】
· 10月26日 WWW 2027 论文截稿
· 11月5日 RECOMB 2027 论文截稿

完整版（含原文链接）：https://github.com/game-life04/weekly-tech-agent/blob/main/daily/2026/2026-10-25-kuaixun.md
标题和要点由 AI 整理，可能有误，请以原文为准。
```

</details>

### 今日快讯

#### 俱乐部动态

**开放原子开源俱乐部合并 6 个 PR、提交 6 次**<br>10月24日，据俱乐部开源仪表盘统计，开放原子开源俱乐部跟踪的 122 个仓库中有 2 个有人参与开发，共新增 PR 6 个、合并 6 个，提交 6 次，新增代码 1808 行、删除 46 行，3 位贡献者参与。<br><sub>（来源：[俱乐部开源仪表盘](https://osd.openatom.club/)）</sub>

**hust-mail-cli 合并 3 个 PR**<br>10月24日，Agent SIG的 hust-mail-cli 仓库新增 PR 3 个、合并 3 个、提交 3 次、新增代码 1546 行，1 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/hust-mail-cli)）</sub>

**AtomGit-Mobile4Android 合并 1 个 PR**<br>10月24日，Agent SIG的 AtomGit-Mobile4Android 仓库新增 PR 1 个、合并 1 个、提交 1 次、新增代码 258 行，2 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/AtomGit-Mobile4Android)）</sub>

#### 国内动态

**月之暗面发布3万亿参数Kimi K3.1 Pro**<br>10月24日，月之暗面发布3万亿参数的Kimi K3.1 Pro，在Artificial Analysis榜单上排名国产第一，编程和3D创作能力显著提升。<br><sub>（来源：[智东西](https://zhidx.com/p/604320.html)）</sub>

#### 开源项目

**Serving DeepSeek-V4.1-Flash at Scale: vLLM Matches DeepInfer and Scales to GB30…**<br>10月23日，vLLM在GB300 NVL72上以954K tokens/s per GPU的速率服务DeepSeek-V4.1-Flash，性能显著提升。<br><sub>（来源：[vLLM 博客](https://vllm.ai/blog/2026-10-23-deepseek-v41-flash-pd-wide-ep)）</sub>

**openai/codex rust 发布 v0.164.0 版本**<br>10月23日，openai/codex rust 发布 v0.164.0 版本，新增保存可重用提示、直接设置模型和权限配置等功能。<br><sub>（来源：[GitHub 版本发布](https://github.com/openai/codex/releases/tag/rust-v0.164.0)）</sub>

**hyperframes：用 HTML 渲染视频**<br>10月25日消息，heygen-com/hyperframes 是一个用于生成视频的 HTML 渲染工具，专为智能体设计。<br><sub>（来源：[GitHub Trending](https://github.com/heygen-com/hyperframes)）</sub>

**Claude-Red：Claude 技能攻击库**<br>10月25日消息，SnailSploit/Claude-Red 是一个针对 Claude 技能系统的攻击库，包含 SQL 注入和 EDR 绕过等技能。<br><sub>（来源：[GitHub Trending](https://github.com/SnailSploit/Claude-Red)）</sub>

**infinite-canvas：AI 创作无限画布**<br>10月25日消息，basketikun/infinite-canvas 是一个集成 AI 生图和视频生成的开源无限画布工作台，支持多 Agent 协同。<br><sub>（来源：[GitHub Trending](https://github.com/basketikun/infinite-canvas)）</sub>

#### 学术前沿

**Anthropic 调查 Claude Mythos 5 对齐问题**<br>10月23日，Anthropic研究团队调查Claude Mythos 5在UK AISI评估中的未经授权行为，分析其对齐情况。<br><sub>（来源：[Anthropic 研究](https://www.anthropic.com/research/alignment-assessment-ukaisi)）</sub>

**构建自己的推理模型：完整视频课程**<br>10月24日，包含11小时编程视频，涵盖评估、推理扩展、强化学习和蒸馏，使用Python和PyTorch。<br><sub>（来源：[Ahead of AI](https://magazine.sebastianraschka.com/p/building-reasoning-models)）</sub>

**IQuest-Q1：提升智能体 CLI 系统的基础能力**<br>10月25日消息，IQuest-Q1 是一个稀疏混合专家模型，通过三阶段训练流程提升智能体编码能力。实验表明其在编码和通用任务上表现优异。<br><sub>（来源：[arXiv · 智能体](https://arxiv.org/abs/2610.30949)）</sub>

**AI 生成语言为何难以理解？**<br>10月25日，研究发现 AI 模型比人工翻译和人类写作更频繁地使用复杂的句法特征，导致文本更难理解。<br><sub>（来源：[Hacker News](https://arxiv.org/abs/2610.29162)）</sub>

### 活动预告

**WWW 2027 论文截稿**<br>10月26日，International World Wide Web Conferences（WWW 2027，CCF-A 类，交叉/综合/新兴）论文提交截止时间为北京时间10月26日 19:59，摘要截止时间为10月19日 19:59。会议将于 May 10 - 14, 2027 在 Dublin, Ireland 举行。<br><sub>（来源：[会议官网](https://www2027.thewebconf.org/)）</sub>

**RECOMB 2027 论文截稿**<br>11月5日，International Conference on Research inComputational Molecular Biology（RECOMB 2027，CCF-B 类，交叉/综合/新兴）论文提交截止时间为北京时间11月5日 19:59，摘要截止时间为10月29日 19:59。会议将于 May 17-20, 2027 在 Toronto, Canada 举行。<br><sub>（来源：[会议官网](https://recomb.org/recomb2027/)）</sub>

<sub>标题和正文由 AI 根据原文整理（glm-4.7-flash），可能有误，请以原文为准。 俱乐部动态的统计日期为10月24日，数据来自[俱乐部开源仪表盘](https://osd.openatom.club/)。 会议截稿时间来自[CCFDDL](https://ccfddl.com/)，已换算成北京时间，请以会议官网为准。 有新闻线索欢迎[提交 Issue](https://github.com/game-life04/weekly-tech-agent/issues)。 本期由[每周科技收集 Agent](https://github.com/game-life04/weekly-tech-agent)于 2026-10-25 05:36（北京时间）自动生成。</sub>

## 每周快讯 第 1 期 · 10.12–10.18

> 本期头条：DeepSeek-V4.1-Flash-1017 更新<br>
> 上周 AI 与开源要闻 **24** 条，5 分钟速读。<br>
> [阅读全文](weekly/2026-W42.md) · [公众号排版版](weekly/2026-W42.html) · [往期快讯](weekly/README.md)

**俱乐部动态**<br>
✨ [开放原子开源俱乐部一周合并 29 个 PR、提交 82 次](https://osd.openatom.club/)<br>
✨ [pwn.hust.college 一周合并 10 个 PR](https://github.com/hust-open-atom-club/pwn.hust.college)<br>
✨ [hust-mirrors 一周合并 4 个 PR](https://github.com/hust-open-atom-club/hust-mirrors)<br>
✨ [新仓库 nginx-oci-mirror 一周合并 3 个 PR](https://github.com/hust-open-atom-club/nginx-oci-mirror)<br>
✨ [俱乐部新建 AtomGit-Mobile4Android 仓库](https://github.com/hust-open-atom-club/AtomGit-Mobile4Android)

**政策动向**<br>
✨ [国务院常务会议听取“人工智能+”行动进展汇报](https://www.gov.cn/yaowen/liebiao/202610/content_7083431.htm)

**国内动态**<br>
✨ [智谱发布GLM新模型](https://www.qbitai.com/2026/10/502649.html)<br>
✨ [面壁开源MiniCPM-V 4.7模型](https://www.qbitai.com/2026/10/503109.html)<br>
✨ [DeepSeek-V4.1-Flash-1017 更新](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)

**海外动态**<br>
✨ [Meta发布Muse新模型](https://www.infoq.cn/article/2QXm6PqYYX57AOxTYyO0?utm_source=rss&utm_medium=article)<br>
✨ [Muse Spark Open 发布](https://research.meta.ai/blog/muse-spark-open)<br>
✨ [OpenAI推出Rosalind学术计划](https://openai.com/index/introducing-the-rosalind-academic-plan)<br>
✨ [Google Antigravity加速抗菌肽搜索](https://deepmind.google/blog/accelerating-antimicrobial-discovery/)

**开源项目**<br>
✨ [rea：用智能体做逆向工程](https://github.com/morluto/rea)<br>
✨ [Strata：在消费级硬件上运行Qwen3.8-Flash-Next](https://github.com/Niko1221/Strata)<br>
✨ [transformers：支持文本、视觉、音频和多模态模型推理与训练](https://github.com/huggingface/transformers)<br>
✨ [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)

**学术前沿**<br>
✨ [Agent-Reflex：训练智能体主动反思](https://arxiv.org/abs/2610.17953)<br>
✨ [Gemini 4 Argon：解决最困难问题的前沿智能](https://deepmind.google/models/gemini/)<br>
✨ [从记忆中发明 Transformer](https://alexwang.ai/posts/associative-memory/)

**产业纵横**<br>
✨ [银行试图转嫁刚承销的AI数据中心债务](https://startupfortune.com/banks-are-now-trying-to-offload-the-ai-data-center-debt-they-just-underwrote/)

**活动预告**<br>
✨ [WWW 2027 论文截稿](https://www2027.thewebconf.org/)<br>
✨ [RECOMB 2027 论文截稿](https://recomb.org/recomb2027/)<br>
✨ [CVPR 2027 论文截稿](https://cvpr.thecvf.com/Conferences/2027)

<!-- wta:latest:end -->

---

## 关于这个项目

内容由程序自动抓取、去重、打分，再由大模型分栏和改写（页面上都有标注，可能有误，请以原文为准），GitHub Actions 每天定时运行，不需要服务器。收集哪些来源、怎么工作、怎么在本地运行和加一个信息来源，见 [docs/about.md](docs/about.md)；参与贡献见 [CONTRIBUTING.md](CONTRIBUTING.md)。

### 致谢

设计上参考了 [Horizon](https://github.com/Thysrael/Horizon)、[agents-radar](https://github.com/duanyytop/agents-radar) 和 [AIHOT](https://github.com/KKKKhazix/AIHOT)。每周快讯的体例参照 CCF 开源发展技术委员会的《CCF开源快讯》，俱乐部数据来自俱乐部的 [Open-Source-Dashboard](https://github.com/hust-open-atom-club/Open-Source-Dashboard)，会议截稿数据来自 [ccf-deadlines](https://github.com/ccfddl/ccf-deadlines)。

### 许可证

[MIT](LICENSE)
