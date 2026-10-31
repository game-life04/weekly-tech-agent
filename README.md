# 每周科技收集 Agent

[![Daily digest](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml)
[![CI](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

每天早上整理 AI 与开源动态，参照《CCF开源快讯》的体例出一期「每日快讯」，8:30 推送到俱乐部 QQ 群；每周一再出一期「每周快讯」。全部由程序自动生成，内容就放在这个仓库里，打开就能看。

- **订阅**：[RSS 订阅源](https://raw.githubusercontent.com/game-life04/weekly-tech-agent/main/feed.xml)；或者在本仓库点 **Watch → Custom → Releases**，每周快讯出刊时 GitHub 会发邮件通知你。
- **投稿**：欢迎推荐值得一看的文章、开源项目、活动和俱乐部动态，请[提交 issue](https://github.com/game-life04/weekly-tech-agent/issues/new?template=submission.md)。
- **往期**：[每周快讯](weekly/README.md) · [每日快讯和日报](daily/README.md)

<!-- wta:latest:start -->

## 每日快讯 · 10.31（周六）

> 今日 AI 与开源要闻 **11** 条，3 分钟速读。<br>
> [单独打开](daily/2026/2026-10-31-kuaixun.md) · [公众号排版版](daily/2026/2026-10-31-kuaixun.html) · [完整日报（含热度和原题）](daily/2026/2026-10-31.md) · [往期日报](daily/README.md)

<details>
<summary>群消息文字版（点开后，点代码框右上角的按钮整段复制）</summary>

```text
【每日科技快讯】10月31日 周六
今日 AI 与开源要闻 11 条，3 分钟速读

【俱乐部动态】
1. 开放原子开源俱乐部合并 0 个 PR、提交 0 次
2. AtomGit-mobile4Harmony 新增 1 个 PR

【开源项目】
3. OpenBot：拥有独立环境的AI同事
→ OpenBot是开源的AI同事，每个AI都拥有自己的浏览器、文件和工具，所有操作在发生前决定，发生后被记录。
4. harvey：自主AI销售代理
→ harvey是自主AI销售代理，支持Claude Code或Codex，能寻找潜在客户、撰写冷邮件并安排会议。
5. Mika：手机上的私人AI助理
→ Mika是运行在Android上的本地AI代理，能操作App和上网，帮助用户完成各种任务。
6. dsh-Go：DeepSeek Harness 装进口袋
→ dsh-go是DeepSeek Harness的移动端版本，可在手机本机运行，也能遥控电脑。
7. Unlimited-OCR-2：图文理解模型
→ Unlimited-OCR-2是图文理解模型，许可证为MIT。

【学术前沿】
8. 内在分布匹配：一步生成图像
→ Intrinsic Distribution Matching针对一步和少步文本生成图像细节不足的问题，通过匹配特征均值和标准差来提升生成质量。
9. 微控制器上的流式语音识别
→ Kroko在ESP32-P4上运行，将65.7M参数的Zipformer2流式语音识别模型压缩为26.65MB的int8权重文件。
10. Claude 模型自主完成小鼠脑部手术
→ Claude 模型自主选择基因疗法并给小鼠做手术，是首个自主选择治疗并施用于哺乳动物的 AI 代理。
11. A-RSI：零数据多模态自改进
→ A-RSI通过监控训练日志中的奖励变化和准确率来动态刷新任务池，在11个基准测试中将平均性能从57.77提升至61.05。

【活动预告】
· 11月5日 RECOMB 2027 论文截稿

完整版（含原文链接）：https://github.com/game-life04/weekly-tech-agent/blob/main/daily/2026/2026-10-31-kuaixun.md
标题和要点由 AI 整理，可能有误，请以原文为准。
```

</details>

### 今日快讯

#### 俱乐部动态

**开放原子开源俱乐部合并 0 个 PR、提交 0 次**<br>10月30日，据俱乐部开源仪表盘统计，开放原子开源俱乐部跟踪的 122 个仓库中有 1 个有人参与开发，共新增 PR 1 个、合并 0 个，提交 0 次，新增代码 0 行、删除 0 行，1 位贡献者参与。<br><sub>（来源：[俱乐部开源仪表盘](https://osd.openatom.club/)）</sub>

**AtomGit-mobile4Harmony 新增 1 个 PR**<br>10月30日，Agent SIG的 AtomGit-mobile4Harmony 仓库新增 PR 1 个，1 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/AtomGit-mobile4Harmony)）</sub>

#### 开源项目

**OpenBot：拥有独立环境的AI同事**<br>10月31日消息，OpenBot是开源的AI同事，每个AI都拥有自己的浏览器、文件和工具，所有操作在发生前决定，发生后被记录。<br><sub>（来源：[GitHub Trending](https://github.com/CopilotKit/OpenBot)）</sub>

**harvey：自主AI销售代理**<br>10月31日消息，harvey是自主AI销售代理，支持Claude Code或Codex，能寻找潜在客户、撰写冷邮件并安排会议。<br><sub>（来源：[GitHub Trending](https://github.com/ethanplusai/harvey)）</sub>

**Mika：手机上的私人AI助理**<br>10月31日消息，Mika是运行在Android上的本地AI代理，能操作App和上网，帮助用户完成各种任务。<br><sub>（来源：[GitHub 新项目](https://github.com/wangzan101/Mika)）</sub>

**dsh-Go：DeepSeek Harness 装进口袋**<br>10月31日消息，dsh-go是DeepSeek Harness的移动端版本，可在手机本机运行，也能遥控电脑。<br><sub>（来源：[GitHub 新项目](https://github.com/ccch1mneyyy/dsh-Go)）</sub>

**Unlimited-OCR-2：图文理解模型**<br>10月31日消息，Unlimited-OCR-2是图文理解模型，许可证为MIT。<br><sub>（来源：[Hugging Face 热门模型](https://huggingface.co/baidu/Unlimited-OCR-2)）</sub>

#### 学术前沿

**内在分布匹配：一步生成图像**<br>10月29日，Intrinsic Distribution Matching针对一步和少步文本生成图像细节不足的问题，通过匹配特征均值和标准差来提升生成质量。<br><sub>（来源：[Hugging Face 热门论文](https://arxiv.org/abs/2610.39633)）</sub>

**微控制器上的流式语音识别**<br>10月29日，Kroko在ESP32-P4上运行，将65.7M参数的Zipformer2流式语音识别模型压缩为26.65MB的int8权重文件。<br><sub>（来源：[arXiv · 语音](https://arxiv.org/abs/2610.38739)）</sub>

**Claude 模型自主完成小鼠脑部手术**<br>10月31日，Claude 模型自主选择基因疗法并给小鼠做手术，是首个自主选择治疗并施用于哺乳动物的 AI 代理。<br><sub>（来源：[The Decoder](https://the-decoder.com/a-claude-model-autonomously-chose-a-gene-therapy-and-operated-on-a-mouse-brain-with-no-human-decision-making/)）</sub>

**A-RSI：零数据多模态自改进**<br>10月31日消息，A-RSI通过监控训练日志中的奖励变化和准确率来动态刷新任务池，在11个基准测试中将平均性能从57.77提升至61.05。<br><sub>（来源：[Hugging Face 热门论文](https://arxiv.org/abs/2610.38568)）</sub>

### 活动预告

**RECOMB 2027 论文截稿**<br>11月5日，International Conference on Research inComputational Molecular Biology（RECOMB 2027，CCF-B 类，交叉/综合/新兴）论文提交截止时间为北京时间11月5日 19:59，摘要截止时间为10月29日 19:59。会议将于 May 17-20, 2027 在 Toronto, Canada 举行。<br><sub>（来源：[会议官网](https://recomb.org/recomb2027/)）</sub>

<sub>标题和正文由 AI 根据原文整理（glm-4.7-flash），可能有误，请以原文为准。 俱乐部动态的统计日期为10月30日，数据来自[俱乐部开源仪表盘](https://osd.openatom.club/)。 会议截稿时间来自[CCFDDL](https://ccfddl.com/)，已换算成北京时间，请以会议官网为准。 有新闻线索欢迎[提交 Issue](https://github.com/game-life04/weekly-tech-agent/issues)。 本期由[每周科技收集 Agent](https://github.com/game-life04/weekly-tech-agent)于 2026-10-31 09:09（北京时间）自动生成。</sub>

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
