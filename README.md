# 每周科技收集 Agent

[![Daily digest](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml)
[![CI](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

每天早上整理 AI 与开源动态，参照《CCF开源快讯》的体例出一期「每日快讯」，8:30 推送到俱乐部 QQ 群；每周一再出一期「每周快讯」。全部由程序自动生成，内容就放在这个仓库里，打开就能看。

- **订阅**：[RSS 订阅源](https://raw.githubusercontent.com/game-life04/weekly-tech-agent/main/feed.xml)；或者在本仓库点 **Watch → Custom → Releases**，每周快讯出刊时 GitHub 会发邮件通知你。
- **投稿**：欢迎推荐值得一看的文章、开源项目、活动和俱乐部动态，请[提交 issue](https://github.com/game-life04/weekly-tech-agent/issues/new?template=submission.md)。
- **往期**：[每周快讯](weekly/README.md) · [每日快讯和日报](daily/README.md)

<!-- wta:latest:start -->

## 每日快讯 · 11.04（周三）

> 今日 AI 与开源要闻 **14** 条，3 分钟速读。<br>
> [单独打开](daily/2026/2026-11-04-kuaixun.md) · [公众号排版版](daily/2026/2026-11-04-kuaixun.html) · [完整日报（含热度和原题）](daily/2026/2026-11-04.md) · [往期日报](daily/README.md)

<details>
<summary>群消息文字版（点开后，点代码框右上角的按钮整段复制）</summary>

```text
【每日科技快讯】11月4日 周三
今日 AI 与开源要闻 14 条，3 分钟速读

【俱乐部动态】
1. 开放原子开源俱乐部合并 3 个 PR、提交 2 次
2. AtomGit-Mobile4Android 合并 1 个 PR

【开源项目】
3. open-webui 发布 v0.13.0 版本
→ open-webui 新增标签页工作区，支持文件、终端、预览、语音等多种功能集成。
4. Colibri：针对前沿 MoE 模型的分层推理引擎
→ Colibri 是一个针对前沿 MoE 模型的分层推理引擎，支持 GPU、RAM 和 NVMe。
5. TokenEconomizer：面向编码代理的体验驱动黑盒成本控制
→ TokenEconomizer 是一个面向编码代理的体验驱动黑盒成本控制工具。
6. Project NOMAD：离线优先的知识与教育服务器
→ Project NOMAD 是一个离线优先的知识与教育服务器，无需联网即可运行。
7. agent-browser：AI 代理的浏览器自动化 CLI
→ agent-browser 是一个用于 AI 代理的浏览器自动化命令行工具。

【学术前沿】
8. LLM 可读写神经网络权重
→ Weight Space Programming 论文指出大模型能直接修改权重，DeepSeek 也在探索相关应用。
9. 论文发现大模型可读写神经网络权重
→ 新论文指出前沿模型能直接解释和修改神经网络的原始权重，实现权重空间编程。
10. Hy-Nomas：迈向自由形式交互式世界生成
→ 为了解决交互式世界生成中模型难以在多轮交互中保持历史和动作后果的问题，本文提出了Hy-Nomas视频世界模型。该方法通过结构化视频描述与动作感知因果注意力对齐，并引入视觉语言提示增强器，实现了基于文本指令和连续相机控制的自由形式交互。实验表明，Hy-Nomas在现有世界模型中表现更优。
11. 生成式 AI 基础：直观的数学入门
→ 本书推导了生成模型的核心数学原理，涵盖从 PCA 到扩散模型等主流架构。

【产业纵横】
12. 富士胶片将把磁带产量提高 5 倍
→ 受生成式 AI 推动的数据归档需求激增，富士胶片将投资约 10 亿日元扩大磁带产能。
13. Anthropic 内部 AI 使用成本超员工薪资
→ Anthropic IPO 文件显示，其内部 AI 使用价值已超过员工薪酬，且增长迅速。
14. OpenAI 推广 ChatGPT 加速物理世界工程
→ OpenAI 展示 ChatGPT 和 Codex 如何帮助工程师加速 CAD、PCB 设计等物理世界工作流。

【活动预告】
· 11月5日 RECOMB 2027 论文截稿
· 11月17日 CVPR 2027 论文截稿

完整版（含原文链接）：https://github.com/game-life04/weekly-tech-agent/blob/main/daily/2026/2026-11-04-kuaixun.md
标题和要点由 AI 整理，可能有误，请以原文为准。
```

</details>

### 今日快讯

#### 俱乐部动态

**开放原子开源俱乐部合并 3 个 PR、提交 2 次**<br>11月3日，据俱乐部开源仪表盘统计，开放原子开源俱乐部跟踪的 122 个仓库中有 1 个有人参与开发，共新增 PR 3 个、合并 3 个，提交 2 次，新增代码 1001 行、删除 3 行，2 位贡献者参与。<br><sub>（来源：[俱乐部开源仪表盘](https://osd.openatom.club/)）</sub>

**AtomGit-Mobile4Android 合并 1 个 PR**<br>11月3日，Agent SIG的 AtomGit-Mobile4Android 仓库新增 PR 1 个、合并 1 个、提交 1 次、新增代码 999 行，2 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/AtomGit-Mobile4Android)）</sub>

#### 开源项目

**open-webui 发布 v0.13.0 版本**<br>11月3日，open-webui 新增标签页工作区，支持文件、终端、预览、语音等多种功能集成。<br><sub>（来源：[GitHub 版本发布](https://github.com/open-webui/open-webui/releases/tag/v0.13.0)）</sub>

**Colibri：针对前沿 MoE 模型的分层推理引擎**<br>11月4日消息，Colibri 是一个针对前沿 MoE 模型的分层推理引擎，支持 GPU、RAM 和 NVMe。<br><sub>（来源：[GitHub Trending](https://github.com/JustVugg/colibri)）</sub>

**TokenEconomizer：面向编码代理的体验驱动黑盒成本控制**<br>11月4日消息，TokenEconomizer 是一个面向编码代理的体验驱动黑盒成本控制工具。<br><sub>（来源：[GitHub 新项目](https://github.com/microsoft/TokenEconomizer)）</sub>

**Project NOMAD：离线优先的知识与教育服务器**<br>11月4日消息，Project NOMAD 是一个离线优先的知识与教育服务器，无需联网即可运行。<br><sub>（来源：[GitHub Trending](https://github.com/Crosstalk-Solutions/project-nomad)）</sub>

**agent-browser：AI 代理的浏览器自动化 CLI**<br>11月4日消息，agent-browser 是一个用于 AI 代理的浏览器自动化命令行工具。<br><sub>（来源：[GitHub Trending](https://github.com/vercel-labs/agent-browser)）</sub>

#### 学术前沿

**LLM 可读写神经网络权重**<br>11月3日，Weight Space Programming 论文指出大模型能直接修改权重，DeepSeek 也在探索相关应用。<br><sub>（来源：[Latent Space](https://latent.space/p/ainews-llms-can-read-write-neural-network-weights-weight-space-programming-cuts-autoresearch-out-of/)）</sub>

**论文发现大模型可读写神经网络权重**<br>11月4日，新论文指出前沿模型能直接解释和修改神经网络的原始权重，实现权重空间编程。<br><sub>（来源：[Simon Willison](https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/)）</sub>

**Hy-Nomas：迈向自由形式交互式世界生成**<br>11月4日消息，为了解决交互式世界生成中模型难以在多轮交互中保持历史和动作后果的问题，本文提出了Hy-Nomas视频世界模型。该方法通过结构化视频描述与动作感知因果注意力对齐，并引入视觉语言提示增强器，实现了基于文本指令和连续相机控制的自由形式交互。实验表明，Hy-Nomas在现有世界模型中表现更优。<br><sub>（来源：[Hugging Face 热门论文](https://arxiv.org/abs/2610.36729)）</sub>

**生成式 AI 基础：直观的数学入门**<br>11月4日，本书推导了生成模型的核心数学原理，涵盖从 PCA 到扩散模型等主流架构。<br><sub>（来源：[Hacker News](https://arxiv.org/abs/2605.29713)）</sub>

#### 产业纵横

**富士胶片将把磁带产量提高 5 倍**<br>11月2日，受生成式 AI 推动的数据归档需求激增，富士胶片将投资约 10 亿日元扩大磁带产能。<br><sub>（来源：[Hacker News](https://arstechnica.com/gadgets/2026/10/fujifilm-to-boost-tape-production-5x-as-ai-fuels-archiving-demand/)）</sub>

**Anthropic 内部 AI 使用成本超员工薪资**<br>11月3日，Anthropic IPO 文件显示，其内部 AI 使用价值已超过员工薪酬，且增长迅速。<br><sub>（来源：[Hacker News](https://www.businessinsider.com/anthropic-claude-internal-ai-use-exceeds-employee-pay-tokens-2026-11)）</sub>

**OpenAI 推广 ChatGPT 加速物理世界工程**<br>11月3日，OpenAI 展示 ChatGPT 和 Codex 如何帮助工程师加速 CAD、PCB 设计等物理世界工作流。<br><sub>（来源：[OpenAI](https://openai.com/index/accelerating-engineering-for-the-physical-world)）</sub>

### 活动预告

**RECOMB 2027 论文截稿**<br>11月5日，International Conference on Research inComputational Molecular Biology（RECOMB 2027，CCF-B 类，交叉/综合/新兴）论文提交截止时间为北京时间11月5日 19:59，摘要截止时间为10月29日 19:59。会议将于 May 17-20, 2027 在 Toronto, Canada 举行。<br><sub>（来源：[会议官网](https://recomb.org/recomb2027/)）</sub>

**CVPR 2027 论文截稿**<br>11月17日，IEEE/CVF Conference on Computer Vision and Pattern Recognition（CVPR 2027，CCF-A 类，人工智能）论文提交截止时间为北京时间11月17日 19:59，摘要截止时间为11月11日 19:59。会议将于 June 20-25, 2027 在 Seattle, WA, United States 举行。<br><sub>（来源：[会议官网](https://cvpr.thecvf.com/Conferences/2027)）</sub>

<sub>标题和正文由 AI 根据原文整理（glm-4.7-flash），可能有误，请以原文为准。 俱乐部动态的统计日期为11月3日，数据来自[俱乐部开源仪表盘](https://osd.openatom.club/)。 会议截稿时间来自[CCFDDL](https://ccfddl.com/)，已换算成北京时间，请以会议官网为准。 有新闻线索欢迎[提交 Issue](https://github.com/game-life04/weekly-tech-agent/issues)。 本期由[每周科技收集 Agent](https://github.com/game-life04/weekly-tech-agent)于 2026-11-04 07:59（北京时间）自动生成。</sub>

## 每周快讯 第 3 期 · 10.26–11.01

> 本期头条：Gemini 4 Carbon：下一代前沿模型<br>
> 上周 AI 与开源要闻 **26** 条，5 分钟速读。<br>
> [阅读全文](weekly/2026-W44.md) · [公众号排版版](weekly/2026-W44.html) · [往期快讯](weekly/README.md)

**俱乐部动态**<br>
✨ [开放原子开源俱乐部一周合并 15 个 PR、提交 45 次](https://osd.openatom.club/)<br>
✨ [AtomGit-Mobile4Android 一周合并 3 个 PR](https://github.com/hust-open-atom-club/AtomGit-Mobile4Android)<br>
✨ [hustsync.rs 一周合并 3 个 PR](https://github.com/hust-open-atom-club/hustsync.rs)<br>
✨ [AtomGit-mobile4Harmony 一周合并 2 个 PR](https://github.com/hust-open-atom-club/AtomGit-mobile4Harmony)

**国内动态**<br>
✨ [DeepSeek开源推理框架DeepInfer](https://www.leiphone.com/category/industrynews/IaMw7vRrTCadlbCY.html)<br>
✨ [影溯想建成具身仿真数采中心](https://www.leiphone.com/category/academic/xPVWQgBN3Foj7fo5.html)<br>
✨ [DeepSeek 开源 Super-agent 架构](https://www.qbitai.com/2026/10/506904.html)<br>
✨ [阿里千问集成至Apple智能](https://www.leiphone.com/category/industrynews/es0ZV9LsDEsG7QLE.html)

**海外动态**<br>
✨ [英国设立AI生物安全实验室](https://36kr.com/newsflashes/4040790852719490?f=rss)<br>
✨ [Google DeepMind 发布 Genie 4 世界模型](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/)<br>
✨ [Gemini 4 Carbon：下一代前沿模型](https://deepmind.google/blog/gemini-4-carbon-our-next-frontier-model/)<br>
✨ [Mistral Large 4 权重开源](https://mistral.ai/news/mistral-large-4-oss/)<br>
✨ [苹果宣布接入阿里千问](http://www.geekpark.net/news/373220)

**开源项目**<br>
✨ [claude-seo：Claude Code 通用 SEO 技能库](https://github.com/AgriciDaniel/claude-seo)<br>
✨ [cindy：开源开箱即用的 AI Agent](https://github.com/makecindy/cindy)<br>
✨ [huggingface/transformers 发布 v5.22.0](https://github.com/huggingface/transformers/releases/tag/v5.22.0)<br>
✨ [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)

**学术前沿**<br>
✨ [OpenAI 分享 Kakeya 猜想等模型结果](https://openai.com/index/building-scientific-understanding-with-academic-communities)<br>
✨ [10岁CNN在皮肤癌诊断上超越前沿大模型](https://lynchlab.net/llm-skin-cancer)<br>
✨ [三体：多模态智能体递归自进化](https://arxiv.org/abs/2610.36077)

**产业纵横**<br>
✨ [OpenAI 和 Anthropic 大幅降低 LLM 价格](https://minimaxir.com/2026/10/cheap-llms/)<br>
✨ [Cerebras 部署万亿参数 AI 模型](https://www.cerebras.ai/blog/how-we-deploy-trillion-parameter-frontier-models-on-cerebras)<br>
✨ [Momenta 集成世界模型指导芯片设计](https://www.qbitai.com/2026/10/506866.html)

**活动预告**<br>
✨ [RECOMB 2027 论文截稿](https://recomb.org/recomb2027/)<br>
✨ [CVPR 2027 论文截稿](https://cvpr.thecvf.com/Conferences/2027)<br>
✨ [ICAPS 2027 论文截稿](https://icaps27.icaps-conference.org/)

<!-- wta:latest:end -->

---

## 关于这个项目

内容由程序自动抓取、去重、打分，再由大模型分栏和改写（页面上都有标注，可能有误，请以原文为准），GitHub Actions 每天定时运行，不需要服务器。收集哪些来源、怎么工作、怎么在本地运行和加一个信息来源，见 [docs/about.md](docs/about.md)；参与贡献见 [CONTRIBUTING.md](CONTRIBUTING.md)。

### 致谢

设计上参考了 [Horizon](https://github.com/Thysrael/Horizon)、[agents-radar](https://github.com/duanyytop/agents-radar) 和 [AIHOT](https://github.com/KKKKhazix/AIHOT)。每周快讯的体例参照 CCF 开源发展技术委员会的《CCF开源快讯》，俱乐部数据来自俱乐部的 [Open-Source-Dashboard](https://github.com/hust-open-atom-club/Open-Source-Dashboard)，会议截稿数据来自 [ccf-deadlines](https://github.com/ccfddl/ccf-deadlines)。

### 许可证

[MIT](LICENSE)
