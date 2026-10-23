# 每周科技收集 Agent

[![Daily digest](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml)
[![CI](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

每天早上整理 AI 与开源动态，参照《CCF开源快讯》的体例出一期「每日快讯」，8:30 推送到俱乐部 QQ 群；每周一再出一期「每周快讯」。全部由程序自动生成，内容就放在这个仓库里，打开就能看。

- **订阅**：[RSS 订阅源](https://raw.githubusercontent.com/game-life04/weekly-tech-agent/main/feed.xml)；或者在本仓库点 **Watch → Custom → Releases**，每周快讯出刊时 GitHub 会发邮件通知你。
- **投稿**：欢迎推荐值得一看的文章、开源项目、活动和俱乐部动态，请[提交 issue](https://github.com/game-life04/weekly-tech-agent/issues/new?template=submission.md)。
- **往期**：[每周快讯](weekly/README.md) · [每日快讯和日报](daily/README.md)

<!-- wta:latest:start -->

## 每日快讯 · 10.24（周六）

> 今日 AI 与开源要闻 **16** 条，3 分钟速读。<br>
> [单独打开](daily/2026/2026-10-24-kuaixun.md) · [公众号排版版](daily/2026/2026-10-24-kuaixun.html) · [完整日报（含热度和原题）](daily/2026/2026-10-24.md) · [往期日报](daily/README.md)

<details>
<summary>群消息文字版（点开后，点代码框右上角的按钮整段复制）</summary>

```text
【每日科技快讯】10月24日 周六
今日 AI 与开源要闻 16 条，3 分钟速读

【俱乐部动态】
1. 开放原子开源俱乐部合并 2 个 PR、提交 2 次
2. hust-mail-cli 合并 2 个 PR
3. AtomGit-Mobile4Android 新增 1 个 PR

【国内动态】
4. 月之暗面发布Kimi K3.1 Pro模型
→ 月之暗面发布了首个拥有100万token上下文窗口的3T级开源模型Kimi K3.1 Pro，并推出了速度提升2-3倍的K3.1 Pro Highspeed版本。

【开源项目】
5. WorldTUI：360M模型模拟终端
→ 作者微调了一个360M参数的语言模型来模拟终端，它能记住之前的操作并运行vim和tmux等命令。
6. vLLM 在 16 个 H200 上部署 GLM-5.3
→ vLLM 在 16 个 H200 上部署 GLM-5.3，支持 100 万 token 上下文，速度提升 1.7–3.2 倍。
7. claude-howto：Claude Code可视化指南
→ 提供Claude Code的可视化、示例驱动指南，包含从基础概念到高级智能体的模板。
8. anthropics/knowledge-work-plugins开源
→ Anthropic开源了知识工作插件仓库，旨在供知识工作者在Claude Cowork中使用。
9. book-to-skill：PDF转Claude Code技能
→ 开源项目可将任何技术书PDF转换为Claude Code技能，方便学习和参考。

【学术前沿】
10. Anthropic：LLMs 让大规模形式化软件验证成为可能
→ Anthropic 的 Claude 在 123 个开源库的编译代码中形式化证明了安全属性，并发现了多年未发现的漏洞。
11. AI 在数学上越来越擅长，原因如下
→ AI 模型正在解决更多数学问题，其成功模式可能有助于预测它们接下来能解决的问题。
12. WildAWM：计算机使用智能体环境合成
→ 提出WildAWM管道，利用开源模型构建支持多种交互界面的环境，用于训练通用计算机使用智能体。
13. 虚拟世界具身智能体持续预训练研究
→ 研究数据量、多样性和模型容量对虚拟世界中具身智能体学习的影响，发现多样性改善向相关世界的迁移。

【产业纵横】
14. OpenAI 联合机构部署数千个 AI 智能体分析小鼠脑细胞
→ OpenAI 联合 PerturbAI 和斯克里普斯研究所，利用数千个 AI 智能体在 32 分钟内分析数百万个小鼠脑细胞数据。
15. OpenAI 加强前沿模型训练环境的安全性
→ OpenAI 介绍了如何通过离线环境和高算力红队测试来加强前沿模型训练和评估的隔离措施。
16. OpenAI 为 10 亿 ChatGPT 用户快速扩展在线存储
→ OpenAI 通过可靠的多租户和全球缓存，将 ChatGPT 的读取速度提高了 12 倍。

【活动预告】
· 10月26日 WWW 2027 论文截稿
· 11月5日 RECOMB 2027 论文截稿

完整版（含原文链接）：https://github.com/game-life04/weekly-tech-agent/blob/main/daily/2026/2026-10-24-kuaixun.md
标题和要点由 AI 整理，可能有误，请以原文为准。
```

</details>

### 今日快讯

#### 俱乐部动态

**开放原子开源俱乐部合并 2 个 PR、提交 2 次**<br>10月23日，据俱乐部开源仪表盘统计，开放原子开源俱乐部跟踪的 122 个仓库中有 4 个有人参与开发，共新增 PR 5 个、合并 2 个，提交 2 次，新增代码 1151 行、删除 128 行，4 位贡献者参与，其中 2 位是第一次贡献。<br><sub>（来源：[俱乐部开源仪表盘](https://osd.openatom.club/)）</sub>

**hust-mail-cli 合并 2 个 PR**<br>10月23日，Agent SIG的 hust-mail-cli 仓库新增 PR 2 个、合并 2 个、提交 2 次、新增代码 1151 行，1 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/hust-mail-cli)）</sub>

**AtomGit-Mobile4Android 新增 1 个 PR**<br>10月23日，Agent SIG的 AtomGit-Mobile4Android 仓库新增 PR 1 个，1 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/AtomGit-Mobile4Android)）</sub>

#### 国内动态

**月之暗面发布Kimi K3.1 Pro模型**<br>10月24日，月之暗面发布了首个拥有100万token上下文窗口的3T级开源模型Kimi K3.1 Pro，并推出了速度提升2-3倍的K3.1 Pro Highspeed版本。<br><sub>（来源：[Hacker News](https://www.kimi.ai/blog/kimi-k3-1-pro)）</sub>

#### 开源项目

**WorldTUI：360M模型模拟终端**<br>10月22日，作者微调了一个360M参数的语言模型来模拟终端，它能记住之前的操作并运行vim和tmux等命令。<br><sub>（来源：[Hacker News](https://simedw.com/2026/10/21/world-model-terminal/)）</sub>

**vLLM 在 16 个 H200 上部署 GLM-5.3**<br>10月23日，vLLM 在 16 个 H200 上部署 GLM-5.3，支持 100 万 token 上下文，速度提升 1.7–3.2 倍。<br><sub>（来源：[vLLM 博客](https://vllm.ai/blog/2026-10-23-glm53-part2-pcp-dcp-hisparse)）</sub>

**claude-howto：Claude Code可视化指南**<br>10月24日消息，提供Claude Code的可视化、示例驱动指南，包含从基础概念到高级智能体的模板。<br><sub>（来源：[GitHub Trending](https://github.com/luongnv89/claude-howto)）</sub>

**anthropics/knowledge-work-plugins开源**<br>10月24日消息，Anthropic开源了知识工作插件仓库，旨在供知识工作者在Claude Cowork中使用。<br><sub>（来源：[GitHub Trending](https://github.com/anthropics/knowledge-work-plugins)）</sub>

**book-to-skill：PDF转Claude Code技能**<br>10月24日消息，开源项目可将任何技术书PDF转换为Claude Code技能，方便学习和参考。<br><sub>（来源：[GitHub Trending](https://github.com/virgiliojr94/book-to-skill)）</sub>

#### 学术前沿

**Anthropic：LLMs 让大规模形式化软件验证成为可能**<br>10月22日，Anthropic 的 Claude 在 123 个开源库的编译代码中形式化证明了安全属性，并发现了多年未发现的漏洞。<br><sub>（来源：[Anthropic 研究](https://www.anthropic.com/research/formal-verification)）</sub>

**AI 在数学上越来越擅长，原因如下**<br>10月23日，AI 模型正在解决更多数学问题，其成功模式可能有助于预测它们接下来能解决的问题。<br><sub>（来源：[Latent Space](https://latent.space/p/ai-is-getting-good-at-math/)）</sub>

**WildAWM：计算机使用智能体环境合成**<br>10月24日消息，提出WildAWM管道，利用开源模型构建支持多种交互界面的环境，用于训练通用计算机使用智能体。<br><sub>（来源：[arXiv · 智能体](https://arxiv.org/abs/2610.26828)）</sub>

**虚拟世界具身智能体持续预训练研究**<br>10月24日消息，研究数据量、多样性和模型容量对虚拟世界中具身智能体学习的影响，发现多样性改善向相关世界的迁移。<br><sub>（来源：[arXiv · 智能体](https://arxiv.org/abs/2610.28698)）</sub>

#### 产业纵横

**OpenAI 联合机构部署数千个 AI 智能体分析小鼠脑细胞**<br>10月23日，OpenAI 联合 PerturbAI 和斯克里普斯研究所，利用数千个 AI 智能体在 32 分钟内分析数百万个小鼠脑细胞数据。<br><sub>（来源：[IT之家](https://www.ithome.com/1/017/274.htm)）</sub>

**OpenAI 加强前沿模型训练环境的安全性**<br>10月23日，OpenAI 介绍了如何通过离线环境和高算力红队测试来加强前沿模型训练和评估的隔离措施。<br><sub>（来源：[OpenAI](https://openai.com/index/securing-our-frontier-model-training-environment)）</sub>

**OpenAI 为 10 亿 ChatGPT 用户快速扩展在线存储**<br>10月24日，OpenAI 通过可靠的多租户和全球缓存，将 ChatGPT 的读取速度提高了 12 倍。<br><sub>（来源：[OpenAI](https://openai.com/index/scaling-storage-one-billion-users-part-two)）</sub>

### 活动预告

**WWW 2027 论文截稿**<br>10月26日，International World Wide Web Conferences（WWW 2027，CCF-A 类，交叉/综合/新兴）论文提交截止时间为北京时间10月26日 19:59，摘要截止时间为10月19日 19:59。会议将于 May 10 - 14, 2027 在 Dublin, Ireland 举行。<br><sub>（来源：[会议官网](https://www2027.thewebconf.org/)）</sub>

**RECOMB 2027 论文截稿**<br>11月5日，International Conference on Research inComputational Molecular Biology（RECOMB 2027，CCF-B 类，交叉/综合/新兴）论文提交截止时间为北京时间11月5日 19:59，摘要截止时间为10月29日 19:59。会议将于 May 17-20, 2027 在 Toronto, Canada 举行。<br><sub>（来源：[会议官网](https://recomb.org/recomb2027/)）</sub>

<sub>标题和正文由 AI 根据原文整理（glm-4.7-flash），可能有误，请以原文为准。 俱乐部动态的统计日期为10月23日，数据来自[俱乐部开源仪表盘](https://osd.openatom.club/)。 会议截稿时间来自[CCFDDL](https://ccfddl.com/)，已换算成北京时间，请以会议官网为准。 有新闻线索欢迎[提交 Issue](https://github.com/game-life04/weekly-tech-agent/issues)。 本期由[每周科技收集 Agent](https://github.com/game-life04/weekly-tech-agent)于 2026-10-24 06:10（北京时间）自动生成。</sub>

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
