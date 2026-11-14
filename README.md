# 每周科技收集 Agent

[![Daily digest](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml)
[![CI](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

每天早上整理 AI 与开源动态，参照《CCF开源快讯》的体例出一期「每日快讯」，8:30 推送到俱乐部 QQ 群；每周一再出一期「每周快讯」。全部由程序自动生成，内容就放在这个仓库里，打开就能看。

- **订阅**：[RSS 订阅源](https://raw.githubusercontent.com/game-life04/weekly-tech-agent/main/feed.xml)；或者在本仓库点 **Watch → Custom → Releases**，每周快讯出刊时 GitHub 会发邮件通知你。
- **投稿**：欢迎推荐值得一看的文章、开源项目、活动和俱乐部动态，请[提交 issue](https://github.com/game-life04/weekly-tech-agent/issues/new?template=submission.md)。
- **往期**：[每周快讯](weekly/README.md) · [每日快讯和日报](daily/README.md)

<!-- wta:latest:start -->

## 每日快讯 · 11.14（周六）

> 今日 AI 与开源要闻 **17** 条，3 分钟速读。<br>
> [单独打开](daily/2026/2026-11-14-kuaixun.md) · [公众号排版版](daily/2026/2026-11-14-kuaixun.html) · [完整日报（含热度和原题）](daily/2026/2026-11-14.md) · [往期日报](daily/README.md)

<details>
<summary>群消息文字版（点开后，点代码框右上角的按钮整段复制）</summary>

```text
【每日科技快讯】11月14日 周六
今日 AI 与开源要闻 17 条，3 分钟速读

【俱乐部动态】
1. 开放原子开源俱乐部合并 5 个 PR、提交 5 次
2. pwntools-dojo 合并 2 个 PR
3. hust-mirrors 合并 2 个 PR

【国内动态】
4. DeepSeek 开放全家桶应用 API
→ DeepSeek 正式开放全家桶应用 API，将联网搜索、深度思考、文件输入等能力整合进原有 API，开发者可调用相关功能。

【海外动态】
5. Google 推出 Gemini 4 Hydrogen 模型
→ Google 推出 Gemini 4 Hydrogen 模型，专为可靠智能体工作流和日常任务设计，提供速度和效率。
6. OpenAI 推出 ChatGPT Wallet
→ OpenAI 发布了 ChatGPT Wallet，允许 ChatGPT Work、Codex 和 Dots 中的代理在用户批准下完成购买。
7. 利用 Antigravity 的 /teamwork 推进科学与工程
→ Google Research 展示了 Antigravity 的 /teamwork 多智能体系统，与人类专家合作解决数学、化学等领域的开放问题。

【开源项目】
8. llama.cpp 发布 v1.0.0 版本
→ llama.cpp v1.0.0 移除了废弃的公共 API，并添加了 OCP FP8 KV caches、host-memory MoE expert cache 等新功能。
9. transformers 发布 v5.23.0 版本
→ transformers v5.23.0 新增了 Inkling 2 Small 多模态模型，该模型接受文本和图像输入并生成文本输出。
10. GoogleChrome/modern-web-guidance-src
→ modern-web-guidance-src 保持编码代理与最新 Web 最佳实践同步。
11. alibaba/open-code-review
→ alibaba/open-code-review 开源混合架构代码审查工具，支持多语言规则集和 LLM 代理。
12. alexeyw/lot-map Claude Code 实时地图
→ alexeyw/lot-map 是 Claude Code 实时地图，可视化展示工具调用和模型步骤。

【学术前沿】
13. Anthropic 分享安全评估建议
→ Anthropic分享了设计、运行和报告安全评估的建议，强调评估对模型部署和训练的重要性。
14. Actor, Judge, or Teacher？理解长时智能体中的决策模型
→ Actor, Judge, or Teacher 研究决策模型在长时智能体中的三种角色：Actor、Judge和Teacher。
15. MACaQ 提出模型无关的快速校准量化方法
→ MACaQ 是一种 MXFP4 W4A4 训练后量化方法，通过在线应用通道缩放和块哈达玛变换来减少内存和计算成本。
16. SO-Arena评测系统一模型能力谱系与可靠性
→ SO-Arena是一个评测系统一模型能力谱系和决策可靠性的基准，涵盖11个领域和五个能力家族。

【产业纵横】
17. Anthropic 递交 IPO 申请
→ Anthropic 申请成为上市公司，致力于确保 AI 的益处并缓解其风险。

【活动预告】
· 11月17日 CVPR 2027 论文截稿

完整版（含原文链接）：https://github.com/game-life04/weekly-tech-agent/blob/main/daily/2026/2026-11-14-kuaixun.md
标题和要点由 AI 整理，可能有误，请以原文为准。
```

</details>

### 今日快讯

#### 俱乐部动态

**开放原子开源俱乐部合并 5 个 PR、提交 5 次**<br>11月13日，据俱乐部开源仪表盘统计，开放原子开源俱乐部跟踪的 122 个仓库中有 5 个有人参与开发，共新增 PR 6 个、合并 5 个，提交 5 次，新增代码 1463 行、删除 1462 行，9 位贡献者参与。<br><sub>（来源：[俱乐部开源仪表盘](https://osd.openatom.club/)）</sub>

**pwntools-dojo 合并 2 个 PR**<br>11月13日，pwn.hust.college SIG的 pwntools-dojo 仓库新增 PR 1 个、合并 2 个、提交 3 次、新增代码 168 行，2 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/pwntools-dojo)）</sub>

**hust-mirrors 合并 2 个 PR**<br>11月13日，镜像站运维 SIG的 hust-mirrors 仓库新增 PR 1 个、合并 2 个、提交 2 次、新增代码 1295 行，4 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/hust-mirrors)）</sub>

#### 国内动态

**DeepSeek 开放全家桶应用 API**<br>11月13日，DeepSeek 正式开放全家桶应用 API，将联网搜索、深度思考、文件输入等能力整合进原有 API，开发者可调用相关功能。<br><sub>（来源：[智东西](https://zhidx.com/p/610514.html)）</sub>

#### 海外动态

**Google 推出 Gemini 4 Hydrogen 模型**<br>11月13日，Google 推出 Gemini 4 Hydrogen 模型，专为可靠智能体工作流和日常任务设计，提供速度和效率。<br><sub>（来源：[Hacker News](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/)）</sub>

**OpenAI 推出 ChatGPT Wallet**<br>11月13日，OpenAI 发布了 ChatGPT Wallet，允许 ChatGPT Work、Codex 和 Dots 中的代理在用户批准下完成购买。<br><sub>（来源：[OpenAI](https://openai.com/index/introducing-chatgpt-wallet)）</sub>

**利用 Antigravity 的 /teamwork 推进科学与工程**<br>11月14日，Google Research 展示了 Antigravity 的 /teamwork 多智能体系统，与人类专家合作解决数学、化学等领域的开放问题。<br><sub>（来源：[Google Research](https://research.google/blog/advancing-science-engineering-with-antigravitys-teamwork-feature/)）</sub>

#### 开源项目

**llama.cpp 发布 v1.0.0 版本**<br>11月13日，llama.cpp v1.0.0 移除了废弃的公共 API，并添加了 OCP FP8 KV caches、host-memory MoE expert cache 等新功能。<br><sub>（来源：[GitHub 版本发布](https://github.com/ggml-org/llama.cpp/releases/tag/v1.0.0)）</sub>

**transformers 发布 v5.23.0 版本**<br>11月13日，transformers v5.23.0 新增了 Inkling 2 Small 多模态模型，该模型接受文本和图像输入并生成文本输出。<br><sub>（来源：[GitHub 版本发布](https://github.com/huggingface/transformers/releases/tag/v5.23.0)）</sub>

**GoogleChrome/modern-web-guidance-src**<br>11月14日消息，modern-web-guidance-src 保持编码代理与最新 Web 最佳实践同步。<br><sub>（来源：[GitHub Trending](https://github.com/GoogleChrome/modern-web-guidance-src)）</sub>

**alibaba/open-code-review**<br>11月14日消息，alibaba/open-code-review 开源混合架构代码审查工具，支持多语言规则集和 LLM 代理。<br><sub>（来源：[GitHub Trending](https://github.com/alibaba/open-code-review)）</sub>

**alexeyw/lot-map Claude Code 实时地图**<br>11月14日消息，alexeyw/lot-map 是 Claude Code 实时地图，可视化展示工具调用和模型步骤。<br><sub>（来源：[GitHub 新项目](https://github.com/alexeyw/lot-map)）</sub>

#### 学术前沿

**Anthropic 分享安全评估建议**<br>11月13日，Anthropic分享了设计、运行和报告安全评估的建议，强调评估对模型部署和训练的重要性。<br><sub>（来源：[Anthropic 研究](https://www.anthropic.com/research/building-strong-safety-evaluations)）</sub>

**Actor, Judge, or Teacher？理解长时智能体中的决策模型**<br>11月13日，Actor, Judge, or Teacher 研究决策模型在长时智能体中的三种角色：Actor、Judge和Teacher。<br><sub>（来源：[arXiv · 智能体](https://arxiv.org/abs/2611.17167)）</sub>

**MACaQ 提出模型无关的快速校准量化方法**<br>11月14日消息，MACaQ 是一种 MXFP4 W4A4 训练后量化方法，通过在线应用通道缩放和块哈达玛变换来减少内存和计算成本。<br><sub>（来源：[arXiv · 高效推理](https://arxiv.org/abs/2611.10649)）</sub>

**SO-Arena评测系统一模型能力谱系与可靠性**<br>11月14日消息，SO-Arena是一个评测系统一模型能力谱系和决策可靠性的基准，涵盖11个领域和五个能力家族。<br><sub>（来源：[Hugging Face 热门论文](https://arxiv.org/abs/2611.15777)）</sub>

#### 产业纵横

**Anthropic 递交 IPO 申请**<br>11月12日，Anthropic 申请成为上市公司，致力于确保 AI 的益处并缓解其风险。<br><sub>（来源：[Hacker News](https://ipo.anthropic.com/us/)）</sub>

### 活动预告

**CVPR 2027 论文截稿**<br>11月17日，IEEE/CVF Conference on Computer Vision and Pattern Recognition（CVPR 2027，CCF-A 类，人工智能）论文提交截止时间为北京时间11月17日 19:59，摘要截止时间为11月11日 19:59。会议将于 June 22-25, 2027 在 Seattle, WA, United States 举行。<br><sub>（来源：[会议官网](https://cvpr.thecvf.com/Conferences/2027)）</sub>

<sub>标题和正文由 AI 根据原文整理（glm-4.7-flash），可能有误，请以原文为准。 俱乐部动态的统计日期为11月13日，数据来自[俱乐部开源仪表盘](https://osd.openatom.club/)。 会议截稿时间来自[CCFDDL](https://ccfddl.com/)，已换算成北京时间，请以会议官网为准。 有新闻线索欢迎[提交 Issue](https://github.com/game-life04/weekly-tech-agent/issues)。 本期由[每周科技收集 Agent](https://github.com/game-life04/weekly-tech-agent)于 2026-11-14 08:19（北京时间）自动生成。</sub>

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
