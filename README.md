# 每周科技收集 Agent

[![Daily digest](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml)
[![CI](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

每天早上整理 AI 与开源动态，参照《CCF开源快讯》的体例出一期「每日快讯」，8:30 推送到俱乐部 QQ 群；每周一再出一期「每周快讯」。全部由程序自动生成，内容就放在这个仓库里，打开就能看。

- **订阅**：[RSS 订阅源](https://raw.githubusercontent.com/game-life04/weekly-tech-agent/main/feed.xml)；或者在本仓库点 **Watch → Custom → Releases**，每周快讯出刊时 GitHub 会发邮件通知你。
- **投稿**：欢迎推荐值得一看的文章、开源项目、活动和俱乐部动态，请[提交 issue](https://github.com/game-life04/weekly-tech-agent/issues/new?template=submission.md)。
- **往期**：[每周快讯](weekly/README.md) · [每日快讯和日报](daily/README.md)

<!-- wta:latest:start -->

## 每日快讯 · 11.13（周五）

> 今日 AI 与开源要闻 **15** 条，3 分钟速读。<br>
> [单独打开](daily/2026/2026-11-13-kuaixun.md) · [公众号排版版](daily/2026/2026-11-13-kuaixun.html) · [完整日报（含热度和原题）](daily/2026/2026-11-13.md) · [往期日报](daily/README.md)

<details>
<summary>群消息文字版（点开后，点代码框右上角的按钮整段复制）</summary>

```text
【每日科技快讯】11月13日 周五
今日 AI 与开源要闻 15 条，3 分钟速读

【俱乐部动态】
1. 开放原子开源俱乐部合并 0 个 PR、提交 0 次
2. pwntools-dojo 新增 1 个 PR

【国内动态】
3. MiniMax开源H3-Image生图模型
→ MiniMax开源H3-Image，原生支持4K分辨率，细节还原度高。

【海外动态】
4. 谷歌推出Gemini 4 Hydrogen模型
→ 谷歌推出Gemini 4 Hydrogen，专为可靠代理工作流和日常任务设计，提供高效智能。
5. 谷歌发布多模态决策模型Gemini Decision 1
→ 谷歌发布多模态决策模型Gemini Decision 1，输出全免费。

【开源项目】
6. smolmaxxing：让旧设备运行大型语言模型
→ smolmaxxing 项目通过自定义内核和内存管理，让旧设备运行大型语言模型。
7. vLLM部署DeepSeek-V4.1-Flash
→ vLLM在Vera Rubin NVL72上部署DeepSeek-V4.1-Flash，吞吐量达GB300的58倍。
8. OpenAI 发布 Codex Security CLI 和 SDK
→ OpenAI 发布 Codex Security CLI 和 TypeScript SDK，用于查找、验证和修复安全漏洞。
9. LangChain介绍评估驱动开发
→ LangChain介绍评估驱动开发，通过定义指标和编写评估脚本，帮助构建更稳定的AI智能体。
10. agentes-chat：自托管的开源 Slack 替代品
→ agentes-chat 是自托管的开源 Slack 替代品，支持团队和 AI 代理在频道和私信中协作。

【学术前沿】
11. REAL Loss 优化推测解码的期望接受长度
→ REAL Loss 通过路径权重和无偏估计直接优化推测解码中的期望接受长度，在 Qwen3.6-35B-A3B 目标模型上优于其他基线方法。
12. 姚期智与杨植麟刷新图论纪录
→ 姚期智与杨植麟联合研究，Kimi构造出630条边的图，刷新人类纪录。
13. TOME-Math 数据集提升数学证明监督效果
→ TOME-Math 数据集将大学数学教材转化为约 38 万条结构化证明监督记录，微调后的模型在基准测试中平均得分提升了 16.7 个百分点。
14. BioXArena-Pro：生物医学智能体评测基准
→ 论文构建了包含64个研究级建模任务的BioXArena-Pro基准，用于评测生物医学智能体。研究发现智能体在适应新数据时表现优于直接复现方法。

【产业纵横】
15. Amplitude用OpenAI实现快速产品改进
→ Amplitude利用OpenAI模型和编码代理，快速识别需求并交付产品变更。

【活动预告】
· 11月17日 CVPR 2027 论文截稿

完整版（含原文链接）：https://github.com/game-life04/weekly-tech-agent/blob/main/daily/2026/2026-11-13-kuaixun.md
标题和要点由 AI 整理，可能有误，请以原文为准。
```

</details>

### 今日快讯

#### 俱乐部动态

**开放原子开源俱乐部合并 0 个 PR、提交 0 次**<br>11月12日，据俱乐部开源仪表盘统计，开放原子开源俱乐部跟踪的 122 个仓库中有 1 个有人参与开发，共新增 PR 1 个、合并 0 个，提交 0 次，新增代码 0 行、删除 0 行，2 位贡献者参与。<br><sub>（来源：[俱乐部开源仪表盘](https://osd.openatom.club/)）</sub>

**pwntools-dojo 新增 1 个 PR**<br>11月12日，pwn.hust.college SIG的 pwntools-dojo 仓库新增 PR 1 个，2 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/pwntools-dojo)）</sub>

#### 国内动态

**MiniMax开源H3-Image生图模型**<br>11月12日，MiniMax开源H3-Image，原生支持4K分辨率，细节还原度高。<br><sub>（来源：[量子位](https://www.qbitai.com/2026/11/509440.html)）</sub>

#### 海外动态

**谷歌推出Gemini 4 Hydrogen模型**<br>11月13日，谷歌推出Gemini 4 Hydrogen，专为可靠代理工作流和日常任务设计，提供高效智能。<br><sub>（来源：[Google DeepMind](https://deepmind.google/blog/introducing-gemini-4-hydrogen/)）</sub>

**谷歌发布多模态决策模型Gemini Decision 1**<br>11月13日，谷歌发布多模态决策模型Gemini Decision 1，输出全免费。<br><sub>（来源：[新智元](https://aiera.com.cn/2026/11/13/other/admin/123638/%e8%b0%b7%e6%ad%8c%e5%8f%91%e5%b8%83%e9%a6%96%e4%b8%aa%e5%86%b3%e7%ad%96%e6%a8%a1%e5%9e%8b%ef%bc%81%e8%be%93%e5%87%ba%e5%85%a8%e5%85%8d%e8%b4%b9%ef%bc%8c%e7%99%be%e4%b8%87token%e4%bd%8e%e8%87%b30-1/)）</sub>

#### 开源项目

**smolmaxxing：让旧设备运行大型语言模型**<br>11月12日，smolmaxxing 项目通过自定义内核和内存管理，让旧设备运行大型语言模型。<br><sub>（来源：[Hacker News](https://github.com/hyperionaidev/smolmaxxing/)）</sub>

**vLLM部署DeepSeek-V4.1-Flash**<br>11月12日，vLLM在Vera Rubin NVL72上部署DeepSeek-V4.1-Flash，吞吐量达GB300的58倍。<br><sub>（来源：[vLLM 博客](https://vllm.ai/blog/2026-11-12-deepseek-v41-flash-vera-rubin)）</sub>

**OpenAI 发布 Codex Security CLI 和 SDK**<br>11月13日消息，OpenAI 发布 Codex Security CLI 和 TypeScript SDK，用于查找、验证和修复安全漏洞。<br><sub>（来源：[GitHub Trending](https://github.com/openai/codex-security)）</sub>

**LangChain介绍评估驱动开发**<br>11月13日，LangChain介绍评估驱动开发，通过定义指标和编写评估脚本，帮助构建更稳定的AI智能体。<br><sub>（来源：[LangChain 博客](https://www.langchain.com/blog/what-is-eval-driven-development)）</sub>

**agentes-chat：自托管的开源 Slack 替代品**<br>11月13日消息，agentes-chat 是自托管的开源 Slack 替代品，支持团队和 AI 代理在频道和私信中协作。<br><sub>（来源：[GitHub 新项目](https://github.com/agentes-chat/agentes-chat)）</sub>

#### 学术前沿

**REAL Loss 优化推测解码的期望接受长度**<br>11月11日，REAL Loss 通过路径权重和无偏估计直接优化推测解码中的期望接受长度，在 Qwen3.6-35B-A3B 目标模型上优于其他基线方法。<br><sub>（来源：[arXiv · 高效推理](https://arxiv.org/abs/2611.14399)）</sub>

**姚期智与杨植麟刷新图论纪录**<br>11月12日，姚期智与杨植麟联合研究，Kimi构造出630条边的图，刷新人类纪录。<br><sub>（来源：[雷峰网](https://www.leiphone.com/category/ai/3vRqaeAILJdgRlhL.html)）</sub>

**TOME-Math 数据集提升数学证明监督效果**<br>11月13日消息，TOME-Math 数据集将大学数学教材转化为约 38 万条结构化证明监督记录，微调后的模型在基准测试中平均得分提升了 16.7 个百分点。<br><sub>（来源：[Hugging Face 热门论文](https://arxiv.org/abs/2610.40394)）</sub>

**BioXArena-Pro：生物医学智能体评测基准**<br>11月13日消息，论文构建了包含64个研究级建模任务的BioXArena-Pro基准，用于评测生物医学智能体。研究发现智能体在适应新数据时表现优于直接复现方法。<br><sub>（来源：[arXiv · 智能体](https://arxiv.org/abs/2611.13994)）</sub>

#### 产业纵横

**Amplitude用OpenAI实现快速产品改进**<br>11月13日，Amplitude利用OpenAI模型和编码代理，快速识别需求并交付产品变更。<br><sub>（来源：[OpenAI](https://openai.com/business/customer-stories/amplitude)）</sub>

### 活动预告

**CVPR 2027 论文截稿**<br>11月17日，IEEE/CVF Conference on Computer Vision and Pattern Recognition（CVPR 2027，CCF-A 类，人工智能）论文提交截止时间为北京时间11月17日 19:59，摘要截止时间为11月11日 19:59。会议将于 June 22-25, 2027 在 Seattle, WA, United States 举行。<br><sub>（来源：[会议官网](https://cvpr.thecvf.com/Conferences/2027)）</sub>

<sub>标题和正文由 AI 根据原文整理（glm-4.7-flash），可能有误，请以原文为准。 俱乐部动态的统计日期为11月12日，数据来自[俱乐部开源仪表盘](https://osd.openatom.club/)。 会议截稿时间来自[CCFDDL](https://ccfddl.com/)，已换算成北京时间，请以会议官网为准。 有新闻线索欢迎[提交 Issue](https://github.com/game-life04/weekly-tech-agent/issues)。 本期由[每周科技收集 Agent](https://github.com/game-life04/weekly-tech-agent)于 2026-11-13 08:21（北京时间）自动生成。</sub>

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
