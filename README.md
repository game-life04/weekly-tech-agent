# 每周科技收集 Agent

[![Daily digest](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml)
[![CI](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

每天早上整理 AI 与开源动态，参照《CCF开源快讯》的体例出一期「每日快讯」，8:30 推送到俱乐部 QQ 群；每周一再出一期「每周快讯」。全部由程序自动生成，内容就放在这个仓库里，打开就能看。

- **订阅**：[RSS 订阅源](https://raw.githubusercontent.com/game-life04/weekly-tech-agent/main/feed.xml)；或者在本仓库点 **Watch → Custom → Releases**，每周快讯出刊时 GitHub 会发邮件通知你。
- **投稿**：欢迎推荐值得一看的文章、开源项目、活动和俱乐部动态，请[提交 issue](https://github.com/game-life04/weekly-tech-agent/issues/new?template=submission.md)。
- **往期**：[每周快讯](weekly/README.md) · [每日快讯和日报](daily/README.md)

<!-- wta:latest:start -->

## 每日快讯 · 11.15（周日）

> 今日 AI 与开源要闻 **13** 条，3 分钟速读。<br>
> [单独打开](daily/2026/2026-11-15-kuaixun.md) · [公众号排版版](daily/2026/2026-11-15-kuaixun.html) · [完整日报（含热度和原题）](daily/2026/2026-11-15.md) · [往期日报](daily/README.md)

<details>
<summary>群消息文字版（点开后，点代码框右上角的按钮整段复制）</summary>

```text
【每日科技快讯】11月15日 周日
今日 AI 与开源要闻 13 条，3 分钟速读

【俱乐部动态】
1. 开放原子开源俱乐部合并 3 个 PR、提交 4 次
2. pwnhustcollege_skill 合并 1 个 PR
3. AtomGit-Mobile4Android 合并 1 个 PR

【国内动态】
4. 李飞飞世界模型Atlas正式开放
→ 李飞飞创办的World Labs正式开放世界模型Atlas，用户可通过提示词生成3D场景。

【开源项目】
5. ai--manus2.0：通用 AI Agent 系统
→ AI Manus 是一个通用 AI Agent 系统，支持在沙盒环境中运行各种工具和操作。
6. GitHub Copilot app：agent 原生桌面体验
→ GitHub Copilot app 是一个面向 GitHub 仓库的 agent 原生桌面体验，用于查找、运行、引导和落地软件工作。
7. ChromeDevTools/chrome-devtools-mcp
→ Chrome DevTools for coding agents。
8. LangChain博客讨论Goal Engineering
→ LangChain博客指出智能体承担开放性目标并驱动其完成是未来发展方向。
9. LLMs-from-scratch：从零实现 LLM
→ 使用 PyTorch 从零开始逐步实现一个类似 ChatGPT 的 LLM。

【学术前沿】
10. AI 解锁哥德尔手稿
→ AI 帮助解读库尔特·哥德尔留下的 1,009 页手稿，其中包含数百个已证明的定理。
11. 斯坦福等团队发布SPU湿实验预测基准
→ 斯坦福等团队推出Science Prediction Universe基准，测试AI在化学、生物等领域的湿实验预测能力。
12. Claude完成费马大定理形式化证明
→ Claude Fable 5.2在30小时内完成费马大定理的形式化证明，并发现13年前证明中的错误。
13. 600 次实验发现 JEPA 世界模型
→ JEPA 是一种联合嵌入预测架构，用于解决长时域任务，包含编码器、预测器和规划器。

【活动预告】
· 11月17日 CVPR 2027 论文截稿

完整版（含原文链接）：https://github.com/game-life04/weekly-tech-agent/blob/main/daily/2026/2026-11-15-kuaixun.md
标题和要点由 AI 整理，可能有误，请以原文为准。
```

</details>

### 今日快讯

#### 俱乐部动态

**开放原子开源俱乐部合并 3 个 PR、提交 4 次**<br>11月14日，据俱乐部开源仪表盘统计，开放原子开源俱乐部跟踪的 122 个仓库中有 3 个有人参与开发，共新增 PR 2 个、合并 3 个，提交 4 次，新增代码 1690 行、删除 82 行，5 位贡献者参与。<br><sub>（来源：[俱乐部开源仪表盘](https://osd.openatom.club/)）</sub>

**pwnhustcollege\_skill 合并 1 个 PR**<br>11月14日，pwn.hust.college SIG的 pwnhustcollege\_skill 仓库新增 PR 2 个、合并 1 个、提交 2 次、新增代码 16 行，2 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/pwnhustcollege_skill)）</sub>

**AtomGit-Mobile4Android 合并 1 个 PR**<br>11月14日，Agent SIG的 AtomGit-Mobile4Android 仓库合并 1 个、提交 1 次、新增代码 1674 行，2 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/AtomGit-Mobile4Android)）</sub>

#### 国内动态

**李飞飞世界模型Atlas正式开放**<br>11月13日，李飞飞创办的World Labs正式开放世界模型Atlas，用户可通过提示词生成3D场景。<br><sub>（来源：[爱范儿](https://www.ifanr.com/1689379?utm_source=rss&utm_medium=rss&utm_campaign=)）</sub>

#### 开源项目

**ai--manus2.0：通用 AI Agent 系统**<br>11月15日消息，AI Manus 是一个通用 AI Agent 系统，支持在沙盒环境中运行各种工具和操作。<br><sub>（来源：[GitHub 新项目](https://github.com/Topkiflare74/ai--manus2.0)）</sub>

**GitHub Copilot app：agent 原生桌面体验**<br>11月15日消息，GitHub Copilot app 是一个面向 GitHub 仓库的 agent 原生桌面体验，用于查找、运行、引导和落地软件工作。<br><sub>（来源：[GitHub 新项目](https://github.com/trackboatwrightplan/GitHub-Copilot-app)）</sub>

**ChromeDevTools/chrome-devtools-mcp**<br>11月15日消息，Chrome DevTools for coding agents。<br><sub>（来源：[GitHub Trending](https://github.com/ChromeDevTools/chrome-devtools-mcp)）</sub>

**LangChain博客讨论Goal Engineering**<br>11月15日，LangChain博客指出智能体承担开放性目标并驱动其完成是未来发展方向。<br><sub>（来源：[LangChain 博客](https://www.langchain.com/blog/goal-engineering)）</sub>

**LLMs-from-scratch：从零实现 LLM**<br>11月15日消息，使用 PyTorch 从零开始逐步实现一个类似 ChatGPT 的 LLM。<br><sub>（来源：[GitHub Trending](https://github.com/rasbt/LLMs-from-scratch)）</sub>

#### 学术前沿

**AI 解锁哥德尔手稿**<br>11月14日，AI 帮助解读库尔特·哥德尔留下的 1,009 页手稿，其中包含数百个已证明的定理。<br><sub>（来源：[Hacker News](https://www.theguardian.com/science/2026/nov/13/kurt-godel-notebooks-ai-helps-unlock-hidden-discoveries-man-who-transformed-maths)）</sub>

**斯坦福等团队发布SPU湿实验预测基准**<br>11月14日，斯坦福等团队推出Science Prediction Universe基准，测试AI在化学、生物等领域的湿实验预测能力。<br><sub>（来源：[量子位](https://www.qbitai.com/2026/11/510232.html)）</sub>

**Claude完成费马大定理形式化证明**<br>11月14日，Claude Fable 5.2在30小时内完成费马大定理的形式化证明，并发现13年前证明中的错误。<br><sub>（来源：[新智元](https://aiera.com.cn/2026/11/14/other/admin/123766/%e6%95%b0%e5%ad%a6%e7%95%8c%e9%9c%87%e5%8a%a8%ef%bc%81claude%e4%b8%80%e5%8f%a3%e6%b0%94%e5%86%99%e4%b8%8b19%e4%b8%87%e8%a1%8c%e6%ba%90%e7%a0%81%ef%bc%8c%e6%8f%aa%e5%87%ba13%e5%b9%b4%e5%89%8d%e8%af%81/)）</sub>

**600 次实验发现 JEPA 世界模型**<br>11月14日，JEPA 是一种联合嵌入预测架构，用于解决长时域任务，包含编码器、预测器和规划器。<br><sub>（来源：[Hacker News](https://haddyalchaer.com/jepa)）</sub>

### 活动预告

**CVPR 2027 论文截稿**<br>11月17日，IEEE/CVF Conference on Computer Vision and Pattern Recognition（CVPR 2027，CCF-A 类，人工智能）论文提交截止时间为北京时间11月17日 19:59，摘要截止时间为11月11日 19:59。会议将于 June 22-25, 2027 在 Seattle, WA, United States 举行。<br><sub>（来源：[会议官网](https://cvpr.thecvf.com/Conferences/2027)）</sub>

<sub>标题和正文由 AI 根据原文整理（glm-4.7-flash），可能有误，请以原文为准。 俱乐部动态的统计日期为11月14日，数据来自[俱乐部开源仪表盘](https://osd.openatom.club/)。 会议截稿时间来自[CCFDDL](https://ccfddl.com/)，已换算成北京时间，请以会议官网为准。 有新闻线索欢迎[提交 Issue](https://github.com/game-life04/weekly-tech-agent/issues)。 本期由[每周科技收集 Agent](https://github.com/game-life04/weekly-tech-agent)于 2026-11-15 06:58（北京时间）自动生成。</sub>

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
