# 每周科技收集 Agent

[![Daily digest](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml)
[![CI](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

每天早上整理 AI 与开源动态，参照《CCF开源快讯》的体例出一期「每日快讯」，8:30 推送到俱乐部 QQ 群；每周一再出一期「每周快讯」。全部由程序自动生成，内容就放在这个仓库里，打开就能看。

- **订阅**：[RSS 订阅源](https://raw.githubusercontent.com/game-life04/weekly-tech-agent/main/feed.xml)；或者在本仓库点 **Watch → Custom → Releases**，每周快讯出刊时 GitHub 会发邮件通知你。
- **投稿**：欢迎推荐值得一看的文章、开源项目、活动和俱乐部动态，请[提交 issue](https://github.com/game-life04/weekly-tech-agent/issues/new?template=submission.md)。
- **往期**：[每周快讯](weekly/README.md) · [每日快讯和日报](daily/README.md)

<!-- wta:latest:start -->

## 每日快讯 · 11.05（周四）

> 今日 AI 与开源要闻 **13** 条，3 分钟速读。<br>
> [单独打开](daily/2026/2026-11-05-kuaixun.md) · [公众号排版版](daily/2026/2026-11-05-kuaixun.html) · [完整日报（含热度和原题）](daily/2026/2026-11-05.md) · [往期日报](daily/README.md)

<details>
<summary>群消息文字版（点开后，点代码框右上角的按钮整段复制）</summary>

```text
【每日科技快讯】11月5日 周四
今日 AI 与开源要闻 13 条，3 分钟速读

【俱乐部动态】
1. 开放原子开源俱乐部合并 2 个 PR、提交 9 次
2. AtomGit-mobile4Harmony 合并 1 个 PR
3. AtomGit-Mobile4Android 合并 1 个 PR

【国内动态】
4. 月之暗面发布Kimi K3.1 Pro模型权重
→ 月之暗面开放Kimi K3.1 Pro模型权重，包含2.8T参数和百万级上下文窗口。

【开源项目】
5. NVIDIA/auto-ontology：语义图推理框架
→ NVIDIA/auto-ontology是一个用于构建语义图推理层的Python框架。
6. llama.cpp 发布 v0.9.0 版本
→ llama.cpp v0.9.0 发布，新增 OCP FP8 E4M3 量化支持。
7. microsoft/ai-agents-for-beginners
→ microsoft/ai-agents-for-beginners提供18个课程帮助开发者入门构建AI智能体。
8. speridlabs/idol：图像生成3D模型
→ speridlabs/idol是一个基于Apache-2.0许可证的图像到3D模型。
9. FareedKhan-dev/kimi-k3-in-c
→ FareedKhan-dev/kimi-k3-in-c提供了Kimi K3的C语言实现，可在8.24GB内存中运行。

【学术前沿】
10. Agile Deliberation：AI 辅助人类定义模糊类别
→ Google Research 提出通过交互式审议工作流和 LLM 优化循环，帮助用户构建准确且对齐的图像分类器。
11. 系统1与系统2协同设计：AGI的关键
→ 研究提出通过轻量级预测器系统1与系统2协同设计，显著降低执行计算量。
12. Axion 1.0：开源智能体基础模型
→ Axion 1.0是一个开源智能体基础模型，具备强大的自主推理和工具使用能力。
13. CoworkOS框架实现智能体协作自动化
→ CoworkOS是一个通用框架，用于管理长期工作流，将任务策略与执行管理分离，支持智能体间协作。

【活动预告】
· 11月5日 RECOMB 2027 论文截稿
· 11月17日 CVPR 2027 论文截稿

完整版（含原文链接）：https://github.com/game-life04/weekly-tech-agent/blob/main/daily/2026/2026-11-05-kuaixun.md
标题和要点由 AI 整理，可能有误，请以原文为准。
```

</details>

### 今日快讯

#### 俱乐部动态

**开放原子开源俱乐部合并 2 个 PR、提交 9 次**<br>11月4日，据俱乐部开源仪表盘统计，开放原子开源俱乐部跟踪的 122 个仓库中有 3 个有人参与开发，共新增 PR 22 个、合并 2 个，提交 9 次，新增代码 1735 行、删除 360 行，3 位贡献者参与。<br><sub>（来源：[俱乐部开源仪表盘](https://osd.openatom.club/)）</sub>

**AtomGit-mobile4Harmony 合并 1 个 PR**<br>11月4日，Agent SIG的 AtomGit-mobile4Harmony 仓库合并 1 个、提交 7 次、新增代码 1252 行，1 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/AtomGit-mobile4Harmony)）</sub>

**AtomGit-Mobile4Android 合并 1 个 PR**<br>11月4日，Agent SIG的 AtomGit-Mobile4Android 仓库合并 1 个、提交 1 次、新增代码 481 行，1 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/AtomGit-Mobile4Android)）</sub>

#### 国内动态

**月之暗面发布Kimi K3.1 Pro模型权重**<br>11月4日，月之暗面开放Kimi K3.1 Pro模型权重，包含2.8T参数和百万级上下文窗口。<br><sub>（来源：[Hacker News](https://huggingface.co/moonshotai/Kimi-K3.1-Pro)）</sub>

#### 开源项目

**NVIDIA/auto-ontology：语义图推理框架**<br>11月3日，NVIDIA/auto-ontology是一个用于构建语义图推理层的Python框架。<br><sub>（来源：[GitHub Trending](https://github.com/NVIDIA/auto-ontology)）</sub>

**llama.cpp 发布 v0.9.0 版本**<br>11月4日，llama.cpp v0.9.0 发布，新增 OCP FP8 E4M3 量化支持。<br><sub>（来源：[GitHub 版本发布](https://github.com/ggml-org/llama.cpp/releases/tag/v0.9.0)）</sub>

**microsoft/ai-agents-for-beginners**<br>11月5日消息，microsoft/ai-agents-for-beginners提供18个课程帮助开发者入门构建AI智能体。<br><sub>（来源：[GitHub Trending](https://github.com/microsoft/ai-agents-for-beginners)）</sub>

**speridlabs/idol：图像生成3D模型**<br>11月5日消息，speridlabs/idol是一个基于Apache-2.0许可证的图像到3D模型。<br><sub>（来源：[Hugging Face 热门模型](https://huggingface.co/speridlabs/idol)）</sub>

**FareedKhan-dev/kimi-k3-in-c**<br>11月5日消息，FareedKhan-dev/kimi-k3-in-c提供了Kimi K3的C语言实现，可在8.24GB内存中运行。<br><sub>（来源：[GitHub Trending](https://github.com/FareedKhan-dev/kimi-k3-in-c)）</sub>

#### 学术前沿

**Agile Deliberation：AI 辅助人类定义模糊类别**<br>11月5日，Google Research 提出通过交互式审议工作流和 LLM 优化循环，帮助用户构建准确且对齐的图像分类器。<br><sub>（来源：[Google Research](https://research.google/blog/agile-deliberation-how-ai-helps-humans-define-the-gray-areas/)）</sub>

**系统1与系统2协同设计：AGI的关键**<br>11月5日消息，研究提出通过轻量级预测器系统1与系统2协同设计，显著降低执行计算量。<br><sub>（来源：[Hugging Face 热门论文](https://arxiv.org/abs/2610.39497)）</sub>

**Axion 1.0：开源智能体基础模型**<br>11月5日消息，Axion 1.0是一个开源智能体基础模型，具备强大的自主推理和工具使用能力。<br><sub>（来源：[arXiv · 智能体](https://arxiv.org/abs/2611.03233)）</sub>

**CoworkOS框架实现智能体协作自动化**<br>11月5日消息，CoworkOS是一个通用框架，用于管理长期工作流，将任务策略与执行管理分离，支持智能体间协作。<br><sub>（来源：[arXiv · 智能体](https://arxiv.org/abs/2611.03178)）</sub>

### 活动预告

**RECOMB 2027 论文截稿**<br>11月5日，International Conference on Research inComputational Molecular Biology（RECOMB 2027，CCF-B 类，交叉/综合/新兴）论文提交截止时间为北京时间11月5日 19:59，摘要截止时间为10月29日 19:59。会议将于 May 17-20, 2027 在 Toronto, Canada 举行。<br><sub>（来源：[会议官网](https://recomb.org/recomb2027/)）</sub>

**CVPR 2027 论文截稿**<br>11月17日，IEEE/CVF Conference on Computer Vision and Pattern Recognition（CVPR 2027，CCF-A 类，人工智能）论文提交截止时间为北京时间11月17日 19:59，摘要截止时间为11月11日 19:59。会议将于 June 20-25, 2027 在 Seattle, WA, United States 举行。<br><sub>（来源：[会议官网](https://cvpr.thecvf.com/Conferences/2027)）</sub>

<sub>标题和正文由 AI 根据原文整理（glm-4.7-flash），可能有误，请以原文为准。 俱乐部动态的统计日期为11月4日，数据来自[俱乐部开源仪表盘](https://osd.openatom.club/)。 会议截稿时间来自[CCFDDL](https://ccfddl.com/)，已换算成北京时间，请以会议官网为准。 有新闻线索欢迎[提交 Issue](https://github.com/game-life04/weekly-tech-agent/issues)。 本期由[每周科技收集 Agent](https://github.com/game-life04/weekly-tech-agent)于 2026-11-05 08:22（北京时间）自动生成。</sub>

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
