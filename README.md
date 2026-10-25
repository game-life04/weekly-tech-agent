# 每周科技收集 Agent

[![Daily digest](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml)
[![CI](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

每天早上整理 AI 与开源动态，参照《CCF开源快讯》的体例出一期「每日快讯」，8:30 推送到俱乐部 QQ 群；每周一再出一期「每周快讯」。全部由程序自动生成，内容就放在这个仓库里，打开就能看。

- **订阅**：[RSS 订阅源](https://raw.githubusercontent.com/game-life04/weekly-tech-agent/main/feed.xml)；或者在本仓库点 **Watch → Custom → Releases**，每周快讯出刊时 GitHub 会发邮件通知你。
- **投稿**：欢迎推荐值得一看的文章、开源项目、活动和俱乐部动态，请[提交 issue](https://github.com/game-life04/weekly-tech-agent/issues/new?template=submission.md)。
- **往期**：[每周快讯](weekly/README.md) · [每日快讯和日报](daily/README.md)

<!-- wta:latest:start -->

## 每日快讯 · 10.26（周一）

> 今日 AI 与开源要闻 **13** 条，3 分钟速读。<br>
> [单独打开](daily/2026/2026-10-26-kuaixun.md) · [公众号排版版](daily/2026/2026-10-26-kuaixun.html) · [完整日报（含热度和原题）](daily/2026/2026-10-26.md) · [往期日报](daily/README.md)

<details>
<summary>群消息文字版（点开后，点代码框右上角的按钮整段复制）</summary>

```text
【每日科技快讯】10月26日 周一
今日 AI 与开源要闻 13 条，3 分钟速读

【俱乐部动态】
1. 开放原子开源俱乐部合并 2 个 PR、提交 2 次
2. AtomGit-Mobile4Android 提交 1 次
3. hustsync.rs 新增 18 个 PR

【国内动态】
4. 千里科技发布AI毫米波雷达
→ Nvidia's new data engine Flora labels one hour of robot video for 72 cents instead of $88 with GPT-6 Astra, while scori…

【开源项目】
5. Ollama 支持语音模型 Phonon
→ Ollama支持语音模型，从Gradium的Phonon开始，支持多语言、多声音流式朗读，在Apple Silicon上比实时快100倍。
6. Shubhamsaboo/awesome-llm-apps
→ awesome-llm-apps仓库收录了100+个AI Agents、Agent Skills和RAG Apps，均为免费开源项目。
7. hallmark：Anti-AI-slop 设计技能
→ hallmark项目为Claude Code、Cursor和Codex提供Anti-AI-slop设计技能，旨在生成更符合人类审美的代码。
8. gemini-cli：终端版AI代理
→ gemini-cli是一个开源AI代理，将Gemini的强大功能直接集成到终端中。
9. LangChain 分享公司驯兽师构建组件
→ LangChain分享了构建内部公司驯兽师的五个组件，展示了其在营销、销售和工程团队中的应用。

【学术前沿】
10. Cerebras部署万亿参数AI模型
→ Cerebras展示了如何将万亿参数的前沿模型映射到WSE-3T晶圆上，实现每秒1000-2000+ token的推理。
11. 10岁CNN在皮肤癌诊断上超越前沿大模型
→ 皮肤科医生测试发现，GPT-6 Astra和Claude Fable 5.1的皮肤癌诊断准确率不如一个10岁的CNN。
12. AI使用让伯克利教授不再批改作业
→ 伯克利教授Richard Borcherds因学生过度使用AI获得高分，决定不再批改作业。
13. MAPS框架调节检索增强生成搜索动量
→ MAPS框架将顺序推理扩展为并行推理范式，通过识别互补检索方向来调节搜索动量。

【活动预告】
· 10月26日 WWW 2027 论文截稿
· 11月5日 RECOMB 2027 论文截稿

上周快讯（10.19–10.25）已出：https://github.com/game-life04/weekly-tech-agent/blob/main/weekly/2026-W43.md
完整版（含原文链接）：https://github.com/game-life04/weekly-tech-agent/blob/main/daily/2026/2026-10-26-kuaixun.md
标题和要点由 AI 整理，可能有误，请以原文为准。
```

</details>

### 今日快讯

#### 俱乐部动态

**开放原子开源俱乐部合并 2 个 PR、提交 2 次**<br>10月25日，据俱乐部开源仪表盘统计，开放原子开源俱乐部跟踪的 122 个仓库中有 2 个有人参与开发，共新增 PR 20 个、合并 2 个，提交 2 次，新增代码 19 行、删除 2 行，2 位贡献者参与。<br><sub>（来源：[俱乐部开源仪表盘](https://osd.openatom.club/)）</sub>

**AtomGit-Mobile4Android 提交 1 次**<br>10月25日，Agent SIG的 AtomGit-Mobile4Android 仓库提交 1 次、新增代码 17 行，1 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/AtomGit-Mobile4Android)）</sub>

**hustsync.rs 新增 18 个 PR**<br>10月25日，镜像站运维 SIG的 hustsync.rs 仓库新增 PR 18 个，1 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/hustsync.rs)）</sub>

#### 国内动态

**千里科技发布AI毫米波雷达**<br>10月25日，Nvidia's new data engine Flora labels one hour of robot video for 72 cents instead of <span>$</span>88 with GPT-6 Astra, while scori…<br><sub>（来源：[The Decoder](https://the-decoder.com/nvidia-open-sources-flora-to-make-robot-video-labeling-125x-cheaper-than-gpt-6-astra/)）</sub>

#### 开源项目

**Ollama 支持语音模型 Phonon**<br>10月24日，Ollama支持语音模型，从Gradium的Phonon开始，支持多语言、多声音流式朗读，在Apple Silicon上比实时快100倍。<br><sub>（来源：[Ollama 博客](https://ollama.com/blog/speech-models)）</sub>

**Shubhamsaboo/awesome-llm-apps**<br>10月26日消息，awesome-llm-apps仓库收录了100+个AI Agents、Agent Skills和RAG Apps，均为免费开源项目。<br><sub>（来源：[GitHub Trending](https://github.com/Shubhamsaboo/awesome-llm-apps)）</sub>

**hallmark：Anti-AI-slop 设计技能**<br>10月26日消息，hallmark项目为Claude Code、Cursor和Codex提供Anti-AI-slop设计技能，旨在生成更符合人类审美的代码。<br><sub>（来源：[GitHub Trending](https://github.com/Nutlope/hallmark)）</sub>

**gemini-cli：终端版AI代理**<br>10月26日消息，gemini-cli是一个开源AI代理，将Gemini的强大功能直接集成到终端中。<br><sub>（来源：[GitHub Trending](https://github.com/google-gemini/gemini-cli)）</sub>

**LangChain 分享公司驯兽师构建组件**<br>10月26日，LangChain分享了构建内部公司驯兽师的五个组件，展示了其在营销、销售和工程团队中的应用。<br><sub>（来源：[LangChain 博客](https://www.langchain.com/blog/components-building-company-harness)）</sub>

#### 学术前沿

**Cerebras部署万亿参数AI模型**<br>10月25日，Cerebras展示了如何将万亿参数的前沿模型映射到WSE-3T晶圆上，实现每秒1000-2000+ token的推理。<br><sub>（来源：[Hacker News](https://www.cerebras.ai/blog/how-we-deploy-trillion-parameter-frontier-models-on-cerebras)）</sub>

**10岁CNN在皮肤癌诊断上超越前沿大模型**<br>10月26日，皮肤科医生测试发现，GPT-6 Astra和Claude Fable 5.1的皮肤癌诊断准确率不如一个10岁的CNN。<br><sub>（来源：[Hacker News](https://lynchlab.net/llm-skin-cancer)）</sub>

**AI使用让伯克利教授不再批改作业**<br>10月26日，伯克利教授Richard Borcherds因学生过度使用AI获得高分，决定不再批改作业。<br><sub>（来源：[Hacker News](https://www.dailycal.org/news/campus/academics/ai-use-leads-uc-berkeley-math-professor-to-see-no-point-in-grading-homework/article_bdf1eae2-c08b-491f-b9f1-81a7cea177de.html)）</sub>

**MAPS框架调节检索增强生成搜索动量**<br>10月26日消息，MAPS框架将顺序推理扩展为并行推理范式，通过识别互补检索方向来调节搜索动量。<br><sub>（来源：[arXiv · 长上下文与检索](https://arxiv.org/abs/2610.29792)）</sub>

### 活动预告

**WWW 2027 论文截稿**<br>10月26日，International World Wide Web Conferences（WWW 2027，CCF-A 类，交叉/综合/新兴）论文提交截止时间为北京时间10月26日 19:59，摘要截止时间为10月19日 19:59。会议将于 May 10 - 14, 2027 在 Dublin, Ireland 举行。<br><sub>（来源：[会议官网](https://www2027.thewebconf.org/)）</sub>

**RECOMB 2027 论文截稿**<br>11月5日，International Conference on Research inComputational Molecular Biology（RECOMB 2027，CCF-B 类，交叉/综合/新兴）论文提交截止时间为北京时间11月5日 19:59，摘要截止时间为10月29日 19:59。会议将于 May 17-20, 2027 在 Toronto, Canada 举行。<br><sub>（来源：[会议官网](https://recomb.org/recomb2027/)）</sub>

<sub>标题和正文由 AI 根据原文整理（glm-4.7-flash），可能有误，请以原文为准。 俱乐部动态的统计日期为10月25日，数据来自[俱乐部开源仪表盘](https://osd.openatom.club/)。 会议截稿时间来自[CCFDDL](https://ccfddl.com/)，已换算成北京时间，请以会议官网为准。 有新闻线索欢迎[提交 Issue](https://github.com/game-life04/weekly-tech-agent/issues)。 本期由[每周科技收集 Agent](https://github.com/game-life04/weekly-tech-agent)于 2026-10-26 07:36（北京时间）自动生成。</sub>

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
