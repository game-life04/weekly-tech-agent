# 每周科技收集 Agent

[![Daily digest](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml)
[![CI](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

每天早上整理 AI 与开源动态，参照《CCF开源快讯》的体例出一期「每日快讯」，8:30 推送到俱乐部 QQ 群；每周一再出一期「每周快讯」。全部由程序自动生成，内容就放在这个仓库里，打开就能看。

- **订阅**：[RSS 订阅源](https://raw.githubusercontent.com/game-life04/weekly-tech-agent/main/feed.xml)；或者在本仓库点 **Watch → Custom → Releases**，每周快讯出刊时 GitHub 会发邮件通知你。
- **投稿**：欢迎推荐值得一看的文章、开源项目、活动和俱乐部动态，请[提交 issue](https://github.com/game-life04/weekly-tech-agent/issues/new?template=submission.md)。
- **往期**：[每周快讯](weekly/README.md) · [每日快讯和日报](daily/README.md)

<!-- wta:latest:start -->

## 每日快讯 · 10.28（周三）

> 今日 AI 与开源要闻 **15** 条，3 分钟速读。<br>
> [单独打开](daily/2026/2026-10-28-kuaixun.md) · [公众号排版版](daily/2026/2026-10-28-kuaixun.html) · [完整日报（含热度和原题）](daily/2026/2026-10-28.md) · [往期日报](daily/README.md)

<details>
<summary>群消息文字版（点开后，点代码框右上角的按钮整段复制）</summary>

```text
【每日科技快讯】10月28日 周三
今日 AI 与开源要闻 15 条，3 分钟速读

【俱乐部动态】
1. 开放原子开源俱乐部合并 2 个 PR、提交 2 次
2. AtomGit-Mobile4Android 合并 1 个 PR
3. kernel_translation_review_skill 合并 1 个 PR

【开源项目】
4. Survival LLM：离线 AI 助手
→ Survival LLM 是一款在本地运行的免费 AI 助手和生存库，包含 150 万篇离线文章。
5. Agent-Reach：多平台搜索工具
→ Agent-Reach 让 AI 智能体能够通过命令行读取和搜索 Twitter、Reddit、YouTube 等多个平台。
6. LangChain 分享设计智能体构建经验
→ LangChain 分享了在 Slack 中构建开源设计智能体 Content Studio 的经验。
7. i-have-adhd：ADHD 友好输出技能
→ i-have-adhd 是一个用于防止代码智能体隐藏答案的技能，输出对 ADHD 友好。
8. TradingAgents：多智能体交易框架
→ TradingAgents 是一个多智能体 LLM 金融交易框架。

【学术前沿】
9. Work Agents：工作代理系统框架
→ Work Agents 提出以工作为中心的系统级框架，将工作代理定义为结合基础模型与运行时工具的系统。
10. Google DeepMind 发布 Genie 4 世界模型
→ Google DeepMind 发布 Genie 4，解锁实时模拟中的前所未有的真实感。
11. Trajectory2Gym：工具使用交互合成
→ Trajectory2Gym 提出构建可执行交互并仅从 grounded 决策中提取监督信号，显著提升了 Qwen3 的性能。
12. Google Research 提出睡眠框架
→ Google Research 提出睡眠框架，让大语言模型在持续学习中保留知识。

【产业纵横】
13. IBM CEO 称开源模型性价比高
→ IBM CEO Arvind Krishna 表示，开源模型现在在本地部署方面具备极高的性价比。
14. Retell 使用 OpenAI 模型支撑 1 亿月调用量
→ Retell 的语音代理基准测试中 GPT-6 Astra 表现优异，Codex 助其实现 160 万美元年营收。
15. Anthropic 与六家药企合作加速药物研发
→ Anthropic 与六家药企合作，并启动罕见肌肉营养不良药物研发项目。

【活动预告】
· 11月5日 RECOMB 2027 论文截稿

完整版（含原文链接）：https://github.com/game-life04/weekly-tech-agent/blob/main/daily/2026/2026-10-28-kuaixun.md
标题和要点由 AI 整理，可能有误，请以原文为准。
```

</details>

### 今日快讯

#### 俱乐部动态

**开放原子开源俱乐部合并 2 个 PR、提交 2 次**<br>10月27日，据俱乐部开源仪表盘统计，开放原子开源俱乐部跟踪的 122 个仓库中有 3 个有人参与开发，共新增 PR 0 个、合并 2 个，提交 2 次，新增代码 1503 行、删除 2 行，3 位贡献者参与。<br><sub>（来源：[俱乐部开源仪表盘](https://osd.openatom.club/)）</sub>

**AtomGit-Mobile4Android 合并 1 个 PR**<br>10月27日，Agent SIG的 AtomGit-Mobile4Android 仓库合并 1 个、提交 1 次、新增代码 1503 行，1 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/AtomGit-Mobile4Android)）</sub>

**kernel\_translation\_review\_skill 合并 1 个 PR**<br>10月27日，Linux内核SIG的 kernel\_translation\_review\_skill 仓库合并 1 个、提交 1 次，1 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/kernel_translation_review_skill)）</sub>

#### 开源项目

**Survival LLM：离线 AI 助手**<br>10月28日，Survival LLM 是一款在本地运行的免费 AI 助手和生存库，包含 150 万篇离线文章。<br><sub>（来源：[Hacker News](https://www.brangus.io/survival-llm)）</sub>

**Agent-Reach：多平台搜索工具**<br>10月28日消息，Agent-Reach 让 AI 智能体能够通过命令行读取和搜索 Twitter、Reddit、YouTube 等多个平台。<br><sub>（来源：[GitHub Trending](https://github.com/Panniantong/Agent-Reach)）</sub>

**LangChain 分享设计智能体构建经验**<br>10月28日，LangChain 分享了在 Slack 中构建开源设计智能体 Content Studio 的经验。<br><sub>（来源：[LangChain 博客](https://www.langchain.com/blog/design-agent)）</sub>

**i-have-adhd：ADHD 友好输出技能**<br>10月28日消息，i-have-adhd 是一个用于防止代码智能体隐藏答案的技能，输出对 ADHD 友好。<br><sub>（来源：[GitHub Trending](https://github.com/ayghri/i-have-adhd)）</sub>

**TradingAgents：多智能体交易框架**<br>10月28日消息，TradingAgents 是一个多智能体 LLM 金融交易框架。<br><sub>（来源：[GitHub Trending](https://github.com/TauricResearch/TradingAgents)）</sub>

#### 学术前沿

**Work Agents：工作代理系统框架**<br>10月27日，Work Agents 提出以工作为中心的系统级框架，将工作代理定义为结合基础模型与运行时工具的系统。<br><sub>（来源：[arXiv · 智能体](https://arxiv.org/abs/2610.35845)）</sub>

**Google DeepMind 发布 Genie 4 世界模型**<br>10月28日，Google DeepMind 发布 Genie 4，解锁实时模拟中的前所未有的真实感。<br><sub>（来源：[Google DeepMind](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/)）</sub>

**Trajectory2Gym：工具使用交互合成**<br>10月28日消息，Trajectory2Gym 提出构建可执行交互并仅从 grounded 决策中提取监督信号，显著提升了 Qwen3 的性能。<br><sub>（来源：[arXiv · 智能体](https://arxiv.org/abs/2610.33568)）</sub>

**Google Research 提出睡眠框架**<br>10月28日，Google Research 提出睡眠框架，让大语言模型在持续学习中保留知识。<br><sub>（来源：[Google Research](https://research.google/blog/the-sleep-framework-a-new-way-for-llms-to-retain-knowledge-in-continual-learning/)）</sub>

#### 产业纵横

**IBM CEO 称开源模型性价比高**<br>10月26日，IBM CEO Arvind Krishna 表示，开源模型现在在本地部署方面具备极高的性价比。<br><sub>（来源：[Hacker News](https://www.theregister.com/systems/2026/10/22/ibm-ceo-says-open-weight-models-are-now-irresistibly-good-and-cheap-on-prem/5304640)）</sub>

**Retell 使用 OpenAI 模型支撑 1 亿月调用量**<br>10月27日，Retell 的语音代理基准测试中 GPT-6 Astra 表现优异，Codex 助其实现 160 万美元年营收。<br><sub>（来源：[OpenAI](https://openai.com/index/retell-ai)）</sub>

**Anthropic 与六家药企合作加速药物研发**<br>10月27日，Anthropic 与六家药企合作，并启动罕见肌肉营养不良药物研发项目。<br><sub>（来源：[Anthropic](https://www.anthropic.com/research/early-progress-drug-development)）</sub>

### 活动预告

**RECOMB 2027 论文截稿**<br>11月5日，International Conference on Research inComputational Molecular Biology（RECOMB 2027，CCF-B 类，交叉/综合/新兴）论文提交截止时间为北京时间11月5日 19:59，摘要截止时间为10月29日 19:59。会议将于 May 17-20, 2027 在 Toronto, Canada 举行。<br><sub>（来源：[会议官网](https://recomb.org/recomb2027/)）</sub>

<sub>标题和正文由 AI 根据原文整理（glm-4.7-flash），可能有误，请以原文为准。 俱乐部动态的统计日期为10月27日，数据来自[俱乐部开源仪表盘](https://osd.openatom.club/)。 会议截稿时间来自[CCFDDL](https://ccfddl.com/)，已换算成北京时间，请以会议官网为准。 有新闻线索欢迎[提交 Issue](https://github.com/game-life04/weekly-tech-agent/issues)。 本期由[每周科技收集 Agent](https://github.com/game-life04/weekly-tech-agent)于 2026-10-28 08:46（北京时间）自动生成。</sub>

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
