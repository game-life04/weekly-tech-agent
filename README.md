# 每周科技收集 Agent

[![Daily digest](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml)
[![CI](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

每天早上整理 AI 与开源动态，参照《CCF开源快讯》的体例出一期「每日快讯」，8:30 推送到俱乐部 QQ 群；每周一再出一期「每周快讯」。全部由程序自动生成，内容就放在这个仓库里，打开就能看。

- **订阅**：[RSS 订阅源](https://raw.githubusercontent.com/game-life04/weekly-tech-agent/main/feed.xml)；或者在本仓库点 **Watch → Custom → Releases**，每周快讯出刊时 GitHub 会发邮件通知你。
- **投稿**：欢迎推荐值得一看的文章、开源项目、活动和俱乐部动态，请[提交 issue](https://github.com/game-life04/weekly-tech-agent/issues/new?template=submission.md)。
- **往期**：[每周快讯](weekly/README.md) · [每日快讯和日报](daily/README.md)

<!-- wta:latest:start -->

## 每日快讯 · 11.19（周四）

> 今日 AI 与开源要闻 **14** 条，3 分钟速读。<br>
> [单独打开](daily/2026/2026-11-19-kuaixun.md) · [公众号排版版](daily/2026/2026-11-19-kuaixun.html) · [完整日报（含热度和原题）](daily/2026/2026-11-19.md) · [往期日报](daily/README.md)

<details>
<summary>群消息文字版（点开后，点代码框右上角的按钮整段复制）</summary>

```text
【每日科技快讯】11月19日 周四
今日 AI 与开源要闻 14 条，3 分钟速读

【俱乐部动态】
1. 开放原子开源俱乐部合并 2 个 PR、提交 4 次
2. Open-Source-Dashboard 合并 2 个 PR
3. AtomGit-mobile4Harmony 新增 4 个 PR

【国内动态】
4. RadixArk 发布 DaisyRose-27B 模型
→ RadixArk 发布 DaisyRose-27B 模型，在 Terminal-Bench 4.1 上 pass@1 提升至 12.0%。

【海外动态】
5. Google 发布 Gemini 4 Neon 模型
→ Google 发布 Gemini 4 Neon 模型，支持文本、图像、视频、音频和 PDF，上下文窗口为一百万个 token。

【开源项目】
6. vLLM 使用 FlyDSL MonoKernels
→ vLLM 使用 FlyDSL MonoKernels 在 AMD Instinct GPU 上实现高交互性解码，提升智能体响应速度。
7. LocalAI 发布 5.0.0 版本
→ LocalAI 发布 5.0.0 版本，新增桌面应用、项目管理和 Python 沙箱，支持 Office 文档和团队共享。
8. openai/whisper：鲁棒语音识别
→ whisper 项目通过大规模弱监督实现鲁棒语音识别，支持多种语言和任务。
9. bojieli/ai-agent-book：AI Agent 开源书籍
→ 《深入理解 AI Agent：设计原理与工程实践》开源主仓库，包含正文、PDF 与配套代码。
10. colbymchenry/codegraph：代码知识图谱
→ codegraph 提供预索引代码知识图谱，自动同步代码变更，支持多个智能体，减少 Token 消耗。

【学术前沿】
11. Xing4：基于国产芯片与框架的前沿智能体模型
→ Xing4 系列大语言模型通过在昇腾芯片上的架构和训练基础设施改进，扩展了 TeleChat 谱系。
12. 权重空间编程无需 Transformer
→ 研究探讨了在无需梯度训练的情况下，大语言模型如何通过手动编写目标权重来设计模型结构。
13. OpenAI 分析编码智能体加速研究
→ OpenAI 分析了编码智能体如何加速 AI 研究，指出其性能参差不齐，并探讨了递归自我改进的信号。
14. Dharma-AI 分析微调耗时预测
→ Dharma-AI 分析了 272 个生产环境微调案例，预测端到端微调时间，解决共享 GPU 集群调度难题。

完整版（含原文链接）：https://github.com/game-life04/weekly-tech-agent/blob/main/daily/2026/2026-11-19-kuaixun.md
标题和要点由 AI 整理，可能有误，请以原文为准。
```

</details>

### 今日快讯

#### 俱乐部动态

**开放原子开源俱乐部合并 2 个 PR、提交 4 次**<br>11月18日，据俱乐部开源仪表盘统计，开放原子开源俱乐部跟踪的 122 个仓库中有 5 个有人参与开发，共新增 PR 9 个、合并 2 个，提交 4 次，新增代码 51 行、删除 16 行，5 位贡献者参与，其中 1 位是第一次贡献。<br><sub>（来源：[俱乐部开源仪表盘](https://osd.openatom.club/)）</sub>

**Open-Source-Dashboard 合并 2 个 PR**<br>11月18日，数字基础设施维护 SIG的 Open-Source-Dashboard 仓库新增 PR 3 个、合并 2 个、提交 4 次、新增代码 51 行，2 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/Open-Source-Dashboard)）</sub>

**AtomGit-mobile4Harmony 新增 4 个 PR**<br>11月18日，Agent SIG的 AtomGit-mobile4Harmony 仓库新增 PR 4 个，2 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/AtomGit-mobile4Harmony)）</sub>

#### 国内动态

**RadixArk 发布 DaisyRose-27B 模型**<br>11月19日，RadixArk 发布 DaisyRose-27B 模型，在 Terminal-Bench 4.1 上 pass\@1 提升至 12.0%。<br><sub>（来源：[Hugging Face 博客](https://huggingface.co/blog/RadixArk/daisyrose-27b-pushing-the-frontier-of-post-trainin)）</sub>

#### 海外动态

**Google 发布 Gemini 4 Neon 模型**<br>11月19日，Google 发布 Gemini 4 Neon 模型，支持文本、图像、视频、音频和 PDF，上下文窗口为一百万个 token。<br><sub>（来源：[The Decoder](https://the-decoder.com/google-ships-gemini-4-neon-its-fourth-new-gemini-model-in-a-month/)）</sub>

#### 开源项目

**vLLM 使用 FlyDSL MonoKernels**<br>11月18日，vLLM 使用 FlyDSL MonoKernels 在 AMD Instinct GPU 上实现高交互性解码，提升智能体响应速度。<br><sub>（来源：[vLLM 博客](https://vllm.ai/blog/2026-11-18-flydsl-monokernels)）</sub>

**LocalAI 发布 5.0.0 版本**<br>11月19日，LocalAI 发布 5.0.0 版本，新增桌面应用、项目管理和 Python 沙箱，支持 Office 文档和团队共享。<br><sub>（来源：[GitHub 版本发布](https://github.com/mudler/LocalAI/releases/tag/v5.0.0)）</sub>

**openai/whisper：鲁棒语音识别**<br>11月19日消息，whisper 项目通过大规模弱监督实现鲁棒语音识别，支持多种语言和任务。<br><sub>（来源：[GitHub Trending](https://github.com/openai/whisper)）</sub>

**bojieli/ai-agent-book：AI Agent 开源书籍**<br>11月19日消息，《深入理解 AI Agent：设计原理与工程实践》开源主仓库，包含正文、PDF 与配套代码。<br><sub>（来源：[GitHub Trending](https://github.com/bojieli/ai-agent-book)）</sub>

**colbymchenry/codegraph：代码知识图谱**<br>11月19日消息，codegraph 提供预索引代码知识图谱，自动同步代码变更，支持多个智能体，减少 Token 消耗。<br><sub>（来源：[GitHub Trending](https://github.com/colbymchenry/codegraph)）</sub>

#### 学术前沿

**Xing4：基于国产芯片与框架的前沿智能体模型**<br>11月17日，Xing4 系列大语言模型通过在昇腾芯片上的架构和训练基础设施改进，扩展了 TeleChat 谱系。<br><sub>（来源：[arXiv · 智能体](https://arxiv.org/abs/2611.22115)）</sub>

**权重空间编程无需 Transformer**<br>11月17日，研究探讨了在无需梯度训练的情况下，大语言模型如何通过手动编写目标权重来设计模型结构。<br><sub>（来源：[Hugging Face 热门论文](https://arxiv.org/abs/2611.22055)）</sub>

**OpenAI 分析编码智能体加速研究**<br>11月18日，OpenAI 分析了编码智能体如何加速 AI 研究，指出其性能参差不齐，并探讨了递归自我改进的信号。<br><sub>（来源：[OpenAI](https://openai.com/index/research-acceleration-jagged-frontier)）</sub>

**Dharma-AI 分析微调耗时预测**<br>11月19日，Dharma-AI 分析了 272 个生产环境微调案例，预测端到端微调时间，解决共享 GPU 集群调度难题。<br><sub>（来源：[Hugging Face 博客](https://huggingface.co/blog/Dharma-AI/predicting-fine-tuning-time)）</sub>

<sub>标题和正文由 AI 根据原文整理（glm-4.7-flash），可能有误，请以原文为准。 俱乐部动态的统计日期为11月18日，数据来自[俱乐部开源仪表盘](https://osd.openatom.club/)。 有新闻线索欢迎[提交 Issue](https://github.com/game-life04/weekly-tech-agent/issues)。 本期由[每周科技收集 Agent](https://github.com/game-life04/weekly-tech-agent)于 2026-11-19 09:12（北京时间）自动生成。</sub>

## 每周快讯 第 5 期 · 11.09–11.15

> 本期头条：DeepMind 推出 AlphaProof Code 验证复杂软件<br>
> 上周 AI 与开源要闻 **26** 条，5 分钟速读。<br>
> [阅读全文](weekly/2026-W46.md) · [公众号排版版](weekly/2026-W46.html) · [往期快讯](weekly/README.md)

**俱乐部动态**<br>
✨ [开放原子开源俱乐部一周合并 15 个 PR、提交 16 次](https://osd.openatom.club/)<br>
✨ [pwnhustcollege\_skill 一周合并 3 个 PR](https://github.com/hust-open-atom-club/pwnhustcollege_skill)<br>
✨ [pwn.hust.college 一周合并 3 个 PR](https://github.com/hust-open-atom-club/pwn.hust.college)<br>
✨ [homebrew-tap 一周合并 3 个 PR](https://github.com/hust-open-atom-club/homebrew-tap)

**国内动态**<br>
✨ [千问办公2.0上线Team Agent协作功能](https://zhidx.com/p/608469.html)<br>
✨ [DeepSeek开放全家桶应用API](https://zhidx.com/p/610514.html)

**海外动态**<br>
✨ [Claude Fable 5.2 和 Claude Mythos 5.2 发布](https://www.anthropic.com/claude-fable-and-mythos-5-2)<br>
✨ [Muse Ember：最小且高效的模型](https://research.meta.ai/blog/muse-ember)<br>
✨ [Gemini 4 Carbon 现已上线](https://deepmind.google/blog/gemini-4-carbon-is-now-available/)<br>
✨ [Gemini 4 Hydrogen：面向代理工作流的高效模型](https://deepmind.google/blog/introducing-gemini-4-hydrogen/)<br>
✨ [李飞飞World Labs开放Atlas世界模型](https://www.ifanr.com/1689379?utm_source=rss&utm_medium=rss&utm_campaign=)

**开源项目**<br>
✨ [Llama-modchip: 284B DeepSeek on 64GB RAM, no GPU](https://github.com/synchopate/llama-modchip)<br>
✨ [Show HN：将你的编码代理迁移到现代 Web 原语](https://github.com/GoogleChrome/modern-web-guidance)<br>
✨ [smolmaxxing：让旧设备运行大型语言模型](https://github.com/hyperionaidev/smolmaxxing/)<br>
✨ [GoogleChrome/modern-web-guidance-src](https://github.com/GoogleChrome/modern-web-guidance-src)

**学术前沿**<br>
✨ [DeepMind 推出 AlphaProof Code 验证复杂软件](https://deepmind.google/blog/introducing-alphaproof-code/)<br>
✨ [DeepMind 发布 AlphaGenome 2 解码 DNA](https://deepmind.google/blog/alphagenome-2-deciphering-how-cells-read-dna-to-better-understand-disease/)<br>
✨ [AI 解锁哥德尔手稿，据说包含数百个已证明的定理](https://www.theguardian.com/science/2026/nov/13/kurt-godel-notebooks-ai-helps-unlock-hidden-discoveries-man-who-transformed-maths)

**产业纵横**<br>
✨ [高通展示端侧MoE智能体](https://www.qbitai.com/2026/11/508478.html)<br>
✨ [Amazon 用 Strands Decider 替换 Sonnet 4.6，节省数百万美元](https://strandsagents.com/blog/amazon-saves-millions-replacing-sonnet-with-strands-decider/)<br>
✨ [Anthropic 递交 IPO 申请](https://ipo.anthropic.com/us/)

**活动预告**<br>
✨ [CVPR 2027 论文截稿](https://cvpr.thecvf.com/Conferences/2027)<br>
✨ [EuroVis 2027 论文截稿](https://eurovis27.github.io/web/)<br>
✨ [AAMAS 2027 论文截稿](https://warwick.ac.uk/fac/sci/dcs/aamas2027/)<br>
✨ [ICAPS 2027 论文截稿](https://icaps27.icaps-conference.org/)<br>
✨ [COLING 2027 论文截稿](https://2027.coling-iccl.org/)

<!-- wta:latest:end -->

---

## 关于这个项目

内容由程序自动抓取、去重、打分，再由大模型分栏和改写（页面上都有标注，可能有误，请以原文为准），GitHub Actions 每天定时运行，不需要服务器。收集哪些来源、怎么工作、怎么在本地运行和加一个信息来源，见 [docs/about.md](docs/about.md)；参与贡献见 [CONTRIBUTING.md](CONTRIBUTING.md)。

### 致谢

设计上参考了 [Horizon](https://github.com/Thysrael/Horizon)、[agents-radar](https://github.com/duanyytop/agents-radar) 和 [AIHOT](https://github.com/KKKKhazix/AIHOT)。每周快讯的体例参照 CCF 开源发展技术委员会的《CCF开源快讯》，俱乐部数据来自俱乐部的 [Open-Source-Dashboard](https://github.com/hust-open-atom-club/Open-Source-Dashboard)，会议截稿数据来自 [ccf-deadlines](https://github.com/ccfddl/ccf-deadlines)。

### 许可证

[MIT](LICENSE)
