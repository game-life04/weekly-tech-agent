# 每周科技收集 Agent

[![Daily digest](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml)
[![CI](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

每天早上整理 AI 与开源动态，参照《CCF开源快讯》的体例出一期「每日快讯」，8:30 推送到俱乐部 QQ 群；每周一再出一期「每周快讯」。全部由程序自动生成，内容就放在这个仓库里，打开就能看。

- **订阅**：[RSS 订阅源](https://raw.githubusercontent.com/game-life04/weekly-tech-agent/main/feed.xml)；或者在本仓库点 **Watch → Custom → Releases**，每周快讯出刊时 GitHub 会发邮件通知你。
- **投稿**：欢迎推荐值得一看的文章、开源项目、活动和俱乐部动态，请[提交 issue](https://github.com/game-life04/weekly-tech-agent/issues/new?template=submission.md)。
- **往期**：[每周快讯](weekly/README.md) · [每日快讯和日报](daily/README.md)

<!-- wta:latest:start -->

## 每日快讯 · 10.30（周五）

> 今日 AI 与开源要闻 **16** 条，3 分钟速读。<br>
> [单独打开](daily/2026/2026-10-30-kuaixun.md) · [公众号排版版](daily/2026/2026-10-30-kuaixun.html) · [完整日报（含热度和原题）](daily/2026/2026-10-30.md) · [往期日报](daily/README.md)

<details>
<summary>群消息文字版（点开后，点代码框右上角的按钮整段复制）</summary>

```text
【每日科技快讯】10月30日 周五
今日 AI 与开源要闻 16 条，3 分钟速读

【俱乐部动态】
1. 开放原子开源俱乐部合并 3 个 PR、提交 32 次
2. AtomGit-mobile4Harmony 合并 2 个 PR
3. AtomGit-Mobile4Android 合并 1 个 PR

【海外动态】
4. DAYJOB: Tax 评测 AI 代理在 50 个税务任务中的表现
→ DAYJOB: Tax 评测 AI 代理在 50 个专业税务环境中的表现，测试其处理复杂记录和专业判断的能力。
5. Mistral Large 4 开源 1T 参数多模态模型
→ Mistral 开源了 Le Chonk 模型，这是一个 1T 参数的原生多模态混合专家模型，在欧洲数据中心训练。
6. Gemini 4 Carbon 登顶 Artificial Analysis 指数 v5
→ Google 的 Gemini 4 Carbon 在 Artificial Analysis 指数 v5 中排名第一，仅次于 Claude Opus 5.5。
7. Claude Code 频繁发送背景代理的完整记录
→ Claude Code 每 30 秒向模型发送一次背景代理的完整记录，以填充状态栏，消耗大量 token。

【开源项目】
8. huggingface/transformers 发布 v5.22.0
→ huggingface/transformers 发布了 v5.22.0 版本，包含 Mistral Large 4 模型。
9. vLLM 支持 Mistral Large 4
→ vLLM 提供对 Mistral Large 4 的 Day-0 支持，包含稀疏 MLA、跨层 KV 共享等功能。
10. vectorize-io/hindsight
→ Hindsight: Agent Memory That Learns。
11. Donchitos/Claude-Code-Game-Studios
→ 该项目包含 49 个 AI 代理和 72 个工作流技能，模拟真实工作室层级。
12. thedotmack/claude-mem
→ 该工具捕获代理在会话中的操作，使用 AI 压缩并注入相关上下文到未来会话。

【学术前沿】
13. Trial by Trace：评估智能体框架的可靠性与失败归因
→ 现有基准多关注模型能力，本文提出 TraceTrial-Bench，将框架可靠性分为七个组件。通过轨迹追踪和双层评估框架，在 3,420 次运行中测得框架得分 59.8% 至 72.0%，31.1% 的运行虽未达标但任务成功。
14. PDRVLA：带物理动力学表示的视觉-语言-动作模型
→ 视觉-语言-动作模型对物理动态理解有限，本文提出 PDRVLA，通过轻量级物理动力学模块从视觉-语言特征中提取物理标记。在四个仿真基准上，LIBERO 成功率达 99.3%，LIBERO-Plus 为 89.9%。
15. 函数空间时间自蒸馏用于策略优化
→ 强化学习可验证奖励提升语言模型推理，但标量结果监督粗糙。本文提出函数空间策略优化（FSPO），通过稀疏历史分布和特权分歧校正，在 5 小时训练预算下平均准确率提升约 4%，内存从 70 GB 降至 56 GB。
16. RouteDRAG: Learning to Route and Control Agentic Execution for Multimodal Docum…
→ Web-based applications increasingly rely on understanding long multimodal documents, where answering questions often re…

【活动预告】
· 11月5日 RECOMB 2027 论文截稿

完整版（含原文链接）：https://github.com/game-life04/weekly-tech-agent/blob/main/daily/2026/2026-10-30-kuaixun.md
标题和要点由 AI 整理，可能有误，请以原文为准。
```

</details>

### 今日快讯

#### 俱乐部动态

**开放原子开源俱乐部合并 3 个 PR、提交 32 次**<br>10月29日，据俱乐部开源仪表盘统计，开放原子开源俱乐部跟踪的 122 个仓库中有 2 个有人参与开发，共新增 PR 1 个、合并 3 个，提交 32 次，新增代码 8188 行、删除 139 行，3 位贡献者参与。<br><sub>（来源：[俱乐部开源仪表盘](https://osd.openatom.club/)）</sub>

**AtomGit-mobile4Harmony 合并 2 个 PR**<br>10月29日，Agent SIG的 AtomGit-mobile4Harmony 仓库合并 2 个、提交 31 次、新增代码 7609 行，2 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/AtomGit-mobile4Harmony)）</sub>

**AtomGit-Mobile4Android 合并 1 个 PR**<br>10月29日，Agent SIG的 AtomGit-Mobile4Android 仓库新增 PR 1 个、合并 1 个、提交 1 次、新增代码 579 行，1 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/AtomGit-Mobile4Android)）</sub>

#### 海外动态

**DAYJOB: Tax 评测 AI 代理在 50 个税务任务中的表现**<br>10月28日，DAYJOB: Tax 评测 AI 代理在 50 个专业税务环境中的表现，测试其处理复杂记录和专业判断的能力。<br><sub>（来源：[Hacker News](https://surgehq.ai/blog/dayjob-tax)）</sub>

**Mistral Large 4 开源 1T 参数多模态模型**<br>10月29日，Mistral 开源了 Le Chonk 模型，这是一个 1T 参数的原生多模态混合专家模型，在欧洲数据中心训练。<br><sub>（来源：[Mistral AI](https://mistral.ai/news/mistral-large-4-oss/)）</sub>

**Gemini 4 Carbon 登顶 Artificial Analysis 指数 v5**<br>10月29日，Google 的 Gemini 4 Carbon 在 Artificial Analysis 指数 v5 中排名第一，仅次于 Claude Opus 5.5。<br><sub>（来源：[Hacker News](https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1)）</sub>

**Claude Code 频繁发送背景代理的完整记录**<br>10月29日，Claude Code 每 30 秒向模型发送一次背景代理的完整记录，以填充状态栏，消耗大量 token。<br><sub>（来源：[Hacker News](https://gist.github.com/flamerix-ai/c3905705cc4205e5de3011fa2e74efce)）</sub>

#### 开源项目

**huggingface/transformers 发布 v5.22.0**<br>10月29日，huggingface/transformers 发布了 v5.22.0 版本，包含 Mistral Large 4 模型。<br><sub>（来源：[GitHub 版本发布](https://github.com/huggingface/transformers/releases/tag/v5.22.0)）</sub>

**vLLM 支持 Mistral Large 4**<br>10月29日，vLLM 提供对 Mistral Large 4 的 Day-0 支持，包含稀疏 MLA、跨层 KV 共享等功能。<br><sub>（来源：[vLLM 博客](https://vllm.ai/blog/2026-10-29-mistral-large-4)）</sub>

**vectorize-io/hindsight**<br>10月30日消息，Hindsight: Agent Memory That Learns。<br><sub>（来源：[GitHub Trending](https://github.com/vectorize-io/hindsight)）</sub>

**Donchitos/Claude-Code-Game-Studios**<br>10月30日消息，该项目包含 49 个 AI 代理和 72 个工作流技能，模拟真实工作室层级。<br><sub>（来源：[GitHub Trending](https://github.com/Donchitos/Claude-Code-Game-Studios)）</sub>

**thedotmack/claude-mem**<br>10月30日消息，该工具捕获代理在会话中的操作，使用 AI 压缩并注入相关上下文到未来会话。<br><sub>（来源：[GitHub Trending](https://github.com/thedotmack/claude-mem)）</sub>

#### 学术前沿

**Trial by Trace：评估智能体框架的可靠性与失败归因**<br>10月30日消息，现有基准多关注模型能力，本文提出 TraceTrial-Bench，将框架可靠性分为七个组件。通过轨迹追踪和双层评估框架，在 3,420 次运行中测得框架得分 59.8% 至 72.0%，31.1% 的运行虽未达标但任务成功。<br><sub>（来源：[arXiv · 智能体](https://arxiv.org/abs/2610.32285)）</sub>

**PDRVLA：带物理动力学表示的视觉-语言-动作模型**<br>10月30日消息，视觉-语言-动作模型对物理动态理解有限，本文提出 PDRVLA，通过轻量级物理动力学模块从视觉-语言特征中提取物理标记。在四个仿真基准上，LIBERO 成功率达 99.3%，LIBERO-Plus 为 89.9%。<br><sub>（来源：[Hugging Face 热门论文](https://arxiv.org/abs/2610.37381)）</sub>

**函数空间时间自蒸馏用于策略优化**<br>10月30日消息，强化学习可验证奖励提升语言模型推理，但标量结果监督粗糙。本文提出函数空间策略优化（FSPO），通过稀疏历史分布和特权分歧校正，在 5 小时训练预算下平均准确率提升约 4%，内存从 70 GB 降至 56 GB。<br><sub>（来源：[Hugging Face 热门论文](https://arxiv.org/abs/2610.19687)）</sub>

**RouteDRAG: Learning to Route and Control Agentic Execution for Multimodal Docum…**<br>10月30日消息，Web-based applications increasingly rely on understanding long multimodal documents, where answering questions often re…<br><sub>（来源：[arXiv · 长上下文与检索](https://arxiv.org/abs/2610.36444)）</sub>

### 活动预告

**RECOMB 2027 论文截稿**<br>11月5日，International Conference on Research inComputational Molecular Biology（RECOMB 2027，CCF-B 类，交叉/综合/新兴）论文提交截止时间为北京时间11月5日 19:59，摘要截止时间为10月29日 19:59。会议将于 May 17-20, 2027 在 Toronto, Canada 举行。<br><sub>（来源：[会议官网](https://recomb.org/recomb2027/)）</sub>

<sub>标题和正文由 AI 根据原文整理（glm-4.7-flash），可能有误，请以原文为准。 俱乐部动态的统计日期为10月29日，数据来自[俱乐部开源仪表盘](https://osd.openatom.club/)。 会议截稿时间来自[CCFDDL](https://ccfddl.com/)，已换算成北京时间，请以会议官网为准。 有新闻线索欢迎[提交 Issue](https://github.com/game-life04/weekly-tech-agent/issues)。 本期由[每周科技收集 Agent](https://github.com/game-life04/weekly-tech-agent)于 2026-10-30 07:17（北京时间）自动生成。</sub>

## 每周快讯 第 2 期 · 10.19–10.25

> 本期头条：Claude 在 123 个开源库中形式化证明安全属性<br>
> 上周 AI 与开源要闻 **27** 条，5 分钟速读。<br>
> [阅读全文](weekly/2026-W43.md) · [公众号排版版](weekly/2026-W43.html) · [往期快讯](weekly/README.md)

**俱乐部动态**<br>
✨ [开放原子开源俱乐部一周合并 31 个 PR、提交 35 次](https://osd.openatom.club/)<br>
✨ [新仓库 hust-mail-cli 一周合并 18 个 PR](https://github.com/hust-open-atom-club/hust-mail-cli)<br>
✨ [pwn.hust.college 一周合并 4 个 PR](https://github.com/hust-open-atom-club/pwn.hust.college)<br>
✨ [AtomGit-Mobile4Android 一周合并 3 个 PR](https://github.com/hust-open-atom-club/AtomGit-Mobile4Android)

**国内动态**<br>
✨ [VAST 开源实时世界模型 EdenLive](https://www.qbitai.com/2026/10/504136.html)<br>
✨ [DeepSeek 发布 V4.1-Flash-1017 模型](https://www.qbitai.com/2026/10/504067.html)<br>
✨ [MiniMax发布M3.1 Flash模型](https://zhidx.com/p/602354.html)<br>
✨ [多智能体协同重构医疗AI](https://www.qbitai.com/2026/10/504734.html)<br>
✨ [Kimi 发布 K3.1 Pro 3T级开源模型](https://www.kimi.ai/blog/kimi-k3-1-pro)<br>
✨ [月之暗面发布3万亿参数Kimi K3.1 Pro](https://zhidx.com/p/604320.html)

**海外动态**<br>
✨ [Mistral 发布 Timestral 时间序列模型](https://mistral.ai/news/timestral/)<br>
✨ [OpenAI 提升低资源编程语言代码能力](https://openai.com/index/low-resource-programming-languages)<br>
✨ [Voxtral 3：Mistral 的语音智能体 SDK](https://mistral.ai/news/voxtral-3/)<br>
✨ [Patch the Planet：AI 协助全球漏洞响应](https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/)<br>
✨ [Mistral 发布 ML4 1万亿参数多模态模型](https://mistral.ai/news/mistral-large-4/)<br>
✨ [解决KLS猜想：高维计算难题](https://www.microsoft.com/en-us/research/blog/solving-a-31-year-old-grand-challenge-in-mathematics-the-kls-conjecture/)

**开源项目**<br>
✨ [Sphinx：在代码发布前测试你的 AI](https://sphinx-six-theta.vercel.app/)<br>
✨ [DeepInfer：DeepSeek 模型高性能推理框架](https://github.com/deepseek-ai/DeepInfer)<br>
✨ [OpenShell：自主 AI 智能体安全运行时](https://github.com/NVIDIA/OpenShell)<br>
✨ [claude-howto：Claude Code 可视化指南](https://github.com/luongnv89/claude-howto)

**学术前沿**<br>
✨ [HybridAgents 在潜在空间思考](https://arxiv.org/abs/2610.18861)<br>
✨ [Claude 设计抗蝎毒蛋白结合剂](https://www.anthropic.com/research/claude-scorpion-toxin-binder-design)<br>
✨ [Claude 在 123 个开源库中形式化证明安全属性](https://www.anthropic.com/research/formal-verification)

**产业纵横**<br>
✨ [OpenAI 模型登陆 Google Cloud](https://openai.com/index/openai-models-google-cloud/)

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
