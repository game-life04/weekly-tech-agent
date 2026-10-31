# 每周科技收集 Agent

[![Daily digest](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml)
[![CI](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

每天早上整理 AI 与开源动态，参照《CCF开源快讯》的体例出一期「每日快讯」，8:30 推送到俱乐部 QQ 群；每周一再出一期「每周快讯」。全部由程序自动生成，内容就放在这个仓库里，打开就能看。

- **订阅**：[RSS 订阅源](https://raw.githubusercontent.com/game-life04/weekly-tech-agent/main/feed.xml)；或者在本仓库点 **Watch → Custom → Releases**，每周快讯出刊时 GitHub 会发邮件通知你。
- **投稿**：欢迎推荐值得一看的文章、开源项目、活动和俱乐部动态，请[提交 issue](https://github.com/game-life04/weekly-tech-agent/issues/new?template=submission.md)。
- **往期**：[每周快讯](weekly/README.md) · [每日快讯和日报](daily/README.md)

<!-- wta:latest:start -->

## 每日快讯 · 11.01（周日）

> 今日 AI 与开源要闻 **17** 条，3 分钟速读。<br>
> [单独打开](daily/2026/2026-11-01-kuaixun.md) · [公众号排版版](daily/2026/2026-11-01-kuaixun.html) · [完整日报（含热度和原题）](daily/2026/2026-11-01.md) · [往期日报](daily/README.md)

<details>
<summary>群消息文字版（点开后，点代码框右上角的按钮整段复制）</summary>

```text
【每日科技快讯】11月1日 周日
今日 AI 与开源要闻 17 条，3 分钟速读

【俱乐部动态】
1. 开放原子开源俱乐部合并 1 个 PR、提交 1 次
2. AtomGit-Mobile4Android 合并 1 个 PR
3. intro2oss 新增 1 个 PR

【国内动态】
4. DeepSeek开源Super-agent架构
→ DeepSeek开源Super-agent架构，引入调度、缓存等思想，提升多任务协作效率。
5. 阿里千问接入Apple智能
→ 阿里巴巴与Apple达成合作，将千问集成至Apple智能，中国用户可在Siri、写作工具及视觉智能中调用千问。
6. Momenta发布X7 Ultra芯片
→ Momenta发布X7 Ultra芯片，超大核NPU达700TOPS，NPU计算利用率达98.7%。
7. 阿里千问接入Apple智能
→ 阿里巴巴与Apple达成合作，将千问集成至Apple智能，中国用户可在Siri、写作工具及视觉智能中调用千问。

【开源项目】
8. DeepSeek完成1055亿元融资
→ DeepSeek 第二轮融资拿下了 1055 亿元人民币，约 158 亿美元。The Information 拿到了出资名单，近 30 家投资者——比金额更有意思的是名单的构成变化。 腾讯和宁德时代仍是两大主力。腾讯两轮各出 100 亿；…
9. Orkas：本地优先的桌面 AI 团队
→ Orkas 是一个本地优先的桌面 AI 团队，包含 16 个内置专家代理。
10. MinerU 发布 4.1.0 版本
→ MinerU发布4.1.0版本，支持主流平台与GPU自动加速，统一Tasks异步接口。
11. sapper-v2：自主渗透测试军团
→ sapper-v2 是一个自主渗透测试军团，包含 AI 指挥官和意图图。
12. diy-llm：LLM 全栈知识
→ diy-llm 涵盖预训练、分词、Transformer、MoE 等全栈知识。

【学术前沿】
13. Qwen3.5 权重中运行任天堂
→ 将 NES CPU 编译进 Qwen3.5 模型权重，实现游戏运行。
14. LOWN：扩散视觉语言模型视觉路由
→ LOWN 方法通过比较有无图像的预测结果来决定是否处理图像，将解码计算量降低至 35.3%。
15. CLE：大模型智能体持续学习评测
→ CLE 基准包含 120 个人工任务和 600 个等级，用于评测大模型智能体的经验积累能力。
16. OmniShowcase：多视角图像生成全景一致视频
→ OmniShowcase提出自动化数据合成管道和几何条件方法，生成覆盖12种相机运动的视频，在多视角视频生成中达到最先进水平。

【产业纵横】
17. 思科给工程师无限 AI 代币重写遗留代码
→ 思科总裁给工程师无限 AI 代币，要求其重写遗留代码。

【活动预告】
· 11月5日 RECOMB 2027 论文截稿

完整版（含原文链接）：https://github.com/game-life04/weekly-tech-agent/blob/main/daily/2026/2026-11-01-kuaixun.md
标题和要点由 AI 整理，可能有误，请以原文为准。
```

</details>

### 今日快讯

#### 俱乐部动态

**开放原子开源俱乐部合并 1 个 PR、提交 1 次**<br>10月31日，据俱乐部开源仪表盘统计，开放原子开源俱乐部跟踪的 122 个仓库中有 3 个有人参与开发，共新增 PR 3 个、合并 1 个，提交 1 次，新增代码 1497 行、删除 50 行，4 位贡献者参与，其中 1 位是第一次贡献。<br><sub>（来源：[俱乐部开源仪表盘](https://osd.openatom.club/)）</sub>

**AtomGit-Mobile4Android 合并 1 个 PR**<br>10月31日，Agent SIG的 AtomGit-Mobile4Android 仓库新增 PR 2 个、合并 1 个、提交 1 次、新增代码 1497 行，2 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/AtomGit-Mobile4Android)）</sub>

**intro2oss 新增 1 个 PR**<br>10月31日，数字基础设施维护 SIG的 intro2oss 仓库新增 PR 1 个，1 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/intro2oss)）</sub>

#### 国内动态

**DeepSeek开源Super-agent架构**<br>10月31日，DeepSeek开源Super-agent架构，引入调度、缓存等思想，提升多任务协作效率。<br><sub>（来源：[量子位](https://www.qbitai.com/2026/10/506904.html)）</sub>

**阿里千问接入Apple智能**<br>10月31日，阿里巴巴与Apple达成合作，将千问集成至Apple智能，中国用户可在Siri、写作工具及视觉智能中调用千问。<br><sub>（来源：[极客公园](http://www.geekpark.net/news/373220)）</sub>

**Momenta发布X7 Ultra芯片**<br>10月31日，Momenta发布X7 Ultra芯片，超大核NPU达700TOPS，NPU计算利用率达98.7%。<br><sub>（来源：[量子位](https://www.qbitai.com/2026/10/506866.html)）</sub>

**阿里千问接入Apple智能**<br>10月31日，阿里巴巴与Apple达成合作，将千问集成至Apple智能，中国用户可在Siri、写作工具及视觉智能中调用千问。<br><sub>（来源：[雷峰网](https://www.leiphone.com/category/industrynews/es0ZV9LsDEsG7QLE.html)）</sub>

#### 开源项目

**DeepSeek完成1055亿元融资**<br>10月30日，DeepSeek 第二轮融资拿下了 1055 亿元人民币，约 158 亿美元。The Information 拿到了出资名单，近 30 家投资者——比金额更有意思的是名单的构成变化。 腾讯和宁德时代仍是两大主力。腾讯两轮各出 100 亿；…<br><sub>（来源：[开源中国](https://www.oschina.net/news/503318)）</sub>

**Orkas：本地优先的桌面 AI 团队**<br>11月1日消息，Orkas 是一个本地优先的桌面 AI 团队，包含 16 个内置专家代理。<br><sub>（来源：[GitHub Trending](https://github.com/Orkas-AI/Orkas)）</sub>

**MinerU 发布 4.1.0 版本**<br>11月1日消息，MinerU发布4.1.0版本，支持主流平台与GPU自动加速，统一Tasks异步接口。<br><sub>（来源：[GitHub 版本发布](https://github.com/opendatalab/MinerU/releases/tag/mineru-4.1.0-released)）</sub>

**sapper-v2：自主渗透测试军团**<br>11月1日消息，sapper-v2 是一个自主渗透测试军团，包含 AI 指挥官和意图图。<br><sub>（来源：[GitHub 新项目](https://github.com/N1nEmAn/sapper-v2)）</sub>

**diy-llm：LLM 全栈知识**<br>11月1日消息，diy-llm 涵盖预训练、分词、Transformer、MoE 等全栈知识。<br><sub>（来源：[GitHub Trending](https://github.com/datawhalechina/diy-llm)）</sub>

#### 学术前沿

**Qwen3.5 权重中运行任天堂**<br>10月31日，将 NES CPU 编译进 Qwen3.5 模型权重，实现游戏运行。<br><sub>（来源：[Hacker News](https://github.com/dbreunig/nesformer)）</sub>

**LOWN：扩散视觉语言模型视觉路由**<br>11月1日消息，LOWN 方法通过比较有无图像的预测结果来决定是否处理图像，将解码计算量降低至 35.3%。<br><sub>（来源：[Hugging Face 热门论文](https://arxiv.org/abs/2610.36671)）</sub>

**CLE：大模型智能体持续学习评测**<br>11月1日消息，CLE 基准包含 120 个人工任务和 600 个等级，用于评测大模型智能体的经验积累能力。<br><sub>（来源：[arXiv · 智能体](https://arxiv.org/abs/2610.33956)）</sub>

**OmniShowcase：多视角图像生成全景一致视频**<br>11月1日消息，OmniShowcase提出自动化数据合成管道和几何条件方法，生成覆盖12种相机运动的视频，在多视角视频生成中达到最先进水平。<br><sub>（来源：[Hugging Face 热门论文](https://arxiv.org/abs/2610.35684)）</sub>

#### 产业纵横

**思科给工程师无限 AI 代币重写遗留代码**<br>10月30日，思科总裁给工程师无限 AI 代币，要求其重写遗留代码。<br><sub>（来源：[Hacker News](https://fortune.com/2026/10/30/cisco-president-jeetu-patel-gen-z-27-year-old-unlimited-ai-tokens-rewrite-legacy-code-entry-level-jobs/)）</sub>

### 活动预告

**RECOMB 2027 论文截稿**<br>11月5日，International Conference on Research inComputational Molecular Biology（RECOMB 2027，CCF-B 类，交叉/综合/新兴）论文提交截止时间为北京时间11月5日 19:59，摘要截止时间为10月29日 19:59。会议将于 May 17-20, 2027 在 Toronto, Canada 举行。<br><sub>（来源：[会议官网](https://recomb.org/recomb2027/)）</sub>

<sub>标题和正文由 AI 根据原文整理（glm-4.7-flash），可能有误，请以原文为准。 俱乐部动态的统计日期为10月31日，数据来自[俱乐部开源仪表盘](https://osd.openatom.club/)。 会议截稿时间来自[CCFDDL](https://ccfddl.com/)，已换算成北京时间，请以会议官网为准。 有新闻线索欢迎[提交 Issue](https://github.com/game-life04/weekly-tech-agent/issues)。 本期由[每周科技收集 Agent](https://github.com/game-life04/weekly-tech-agent)于 2026-11-01 06:28（北京时间）自动生成。</sub>

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
