# 每周科技收集 Agent

[![Daily digest](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml)
[![CI](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

每天早上整理 AI 与开源动态，参照《CCF开源快讯》的体例出一期「每日快讯」，8:30 推送到俱乐部 QQ 群；每周一再出一期「每周快讯」。全部由程序自动生成，内容就放在这个仓库里，打开就能看。

- **订阅**：[RSS 订阅源](https://raw.githubusercontent.com/game-life04/weekly-tech-agent/main/feed.xml)；或者在本仓库点 **Watch → Custom → Releases**，每周快讯出刊时 GitHub 会发邮件通知你。
- **投稿**：欢迎推荐值得一看的文章、开源项目、活动和俱乐部动态，请[提交 issue](https://github.com/game-life04/weekly-tech-agent/issues/new?template=submission.md)。
- **往期**：[每周快讯](weekly/README.md) · [每日快讯和日报](daily/README.md)

<!-- wta:latest:start -->

## 每日快讯 · 11.09（周一）

> 今日 AI 与开源要闻 **12** 条，3 分钟速读。<br>
> [单独打开](daily/2026/2026-11-09-kuaixun.md) · [公众号排版版](daily/2026/2026-11-09-kuaixun.html) · [完整日报（含热度和原题）](daily/2026/2026-11-09.md) · [往期日报](daily/README.md)

<details>
<summary>群消息文字版（点开后，点代码框右上角的按钮整段复制）</summary>

```text
【每日科技快讯】11月9日 周一
今日 AI 与开源要闻 12 条，3 分钟速读

【俱乐部动态】
1. 开放原子开源俱乐部合并 2 个 PR、提交 0 次
2. Open-Source-Dashboard 合并 2 个 PR
3. AtomGit-mobile4Harmony 新增 2 个 PR

【开源项目】
4. Llama-modchip：在64GB内存上运行DeepSeek模型
→ Llama-modchip项目允许在纯64GB CPU上运行284B DeepSeek-V4-Flash和30B MoEs模型，无需GPU。
5. QwenLM/qwen-code 发布 v0.27.0 版本
→ QwenLM/qwen-code v0.27.0发布，支持托管代理会话管理、Web Shell任务热力图等功能。
6. Qwen/Qwen3.8-27B：图文理解模型
→ Qwen/Qwen3.8-27B 是一个图文理解模型，许可证为 apache-2.0。
7. Concat：开源视频编辑器
→ Concat 是一个真正免费、开源、本地优先、跨平台的视频编辑器，支持 JSON-RPC API 和 MCP。
8. billion-context：上下文压缩插件
→ billion-context 是一个上下文压缩插件，支持月级长会话和省 token，100k 上下文即可。

【学术前沿】
9. 斯坦福CS146S课程引发AI时代工程教育思考
→ 斯坦福CS146S课程让学生能一键完成往年作业，引发对AI时代工程教育的思考。
10. D3D：异步推测解码的解耦扩散草稿
→ D3D 提出了一种独立的扩散草稿模型，通过结合分块去噪和辅助自回归监督，实现长前缀接受。
11. LoopVQ：循环Transformer的亚1比特KV缓存量化
→ LoopVQ 针对循环 Transformer 的 KV 缓存提出了一种向量量化方法，在 0.5 比特每元素时优于现有方法。
12. Confucius4-R2T2：实时转录的稳定前缀流式ASR模型
→ Confucius4-R2T2通过引入最长稳定前缀概念，将全上下文ASR模型转化为稳定前缀流式模型，确保输出稳定且延迟低。

【活动预告】
· 11月17日 CVPR 2027 论文截稿

上周快讯（11.02–11.08）已出：https://github.com/game-life04/weekly-tech-agent/blob/main/weekly/2026-W45.md
完整版（含原文链接）：https://github.com/game-life04/weekly-tech-agent/blob/main/daily/2026/2026-11-09-kuaixun.md
标题和要点由 AI 整理，可能有误，请以原文为准。
```

</details>

### 今日快讯

#### 俱乐部动态

**开放原子开源俱乐部合并 2 个 PR、提交 0 次**<br>11月8日，据俱乐部开源仪表盘统计，开放原子开源俱乐部跟踪的 122 个仓库中有 5 个有人参与开发，共新增 PR 6 个、合并 2 个，提交 0 次，新增代码 0 行、删除 0 行，5 位贡献者参与。<br><sub>（来源：[俱乐部开源仪表盘](https://osd.openatom.club/)）</sub>

**Open-Source-Dashboard 合并 2 个 PR**<br>11月8日，数字基础设施维护 SIG的 Open-Source-Dashboard 仓库合并 2 个，2 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/Open-Source-Dashboard)）</sub>

**AtomGit-mobile4Harmony 新增 2 个 PR**<br>11月8日，Agent SIG的 AtomGit-mobile4Harmony 仓库新增 PR 2 个，1 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/AtomGit-mobile4Harmony)）</sub>

#### 开源项目

**Llama-modchip：在64GB内存上运行DeepSeek模型**<br>11月8日，Llama-modchip项目允许在纯64GB CPU上运行284B DeepSeek-V4-Flash和30B MoEs模型，无需GPU。<br><sub>（来源：[Hacker News](https://github.com/synchopate/llama-modchip)）</sub>

**QwenLM/qwen-code 发布 v0.27.0 版本**<br>11月8日，QwenLM/qwen-code v0.27.0发布，支持托管代理会话管理、Web Shell任务热力图等功能。<br><sub>（来源：[GitHub 版本发布](https://github.com/QwenLM/qwen-code/releases/tag/v0.27.0)）</sub>

**Qwen/Qwen3.8-27B：图文理解模型**<br>11月9日消息，Qwen/Qwen3.8-27B 是一个图文理解模型，许可证为 apache-2.0。<br><sub>（来源：[Hugging Face 热门模型](https://huggingface.co/Qwen/Qwen3.8-27B)）</sub>

**Concat：开源视频编辑器**<br>11月9日消息，Concat 是一个真正免费、开源、本地优先、跨平台的视频编辑器，支持 JSON-RPC API 和 MCP。<br><sub>（来源：[GitHub Trending](https://github.com/jub0t/Concat)）</sub>

**billion-context：上下文压缩插件**<br>11月9日消息，billion-context 是一个上下文压缩插件，支持月级长会话和省 token，100k 上下文即可。<br><sub>（来源：[GitHub Trending](https://github.com/ranxianglei/billion-context)）</sub>

#### 学术前沿

**斯坦福CS146S课程引发AI时代工程教育思考**<br>11月9日，斯坦福CS146S课程让学生能一键完成往年作业，引发对AI时代工程教育的思考。<br><sub>（来源：[Latent Space](https://latent.space/p/cs146s/)）</sub>

**D3D：异步推测解码的解耦扩散草稿**<br>11月9日消息，D3D 提出了一种独立的扩散草稿模型，通过结合分块去噪和辅助自回归监督，实现长前缀接受。<br><sub>（来源：[arXiv · 高效推理](https://arxiv.org/abs/2611.06425)）</sub>

**LoopVQ：循环Transformer的亚1比特KV缓存量化**<br>11月9日消息，LoopVQ 针对循环 Transformer 的 KV 缓存提出了一种向量量化方法，在 0.5 比特每元素时优于现有方法。<br><sub>（来源：[arXiv · 高效推理](https://arxiv.org/abs/2611.05304)）</sub>

**Confucius4-R2T2：实时转录的稳定前缀流式ASR模型**<br>11月9日消息，Confucius4-R2T2通过引入最长稳定前缀概念，将全上下文ASR模型转化为稳定前缀流式模型，确保输出稳定且延迟低。<br><sub>（来源：[arXiv · 语音](https://arxiv.org/abs/2611.06043)）</sub>

### 活动预告

**CVPR 2027 论文截稿**<br>11月17日，IEEE/CVF Conference on Computer Vision and Pattern Recognition（CVPR 2027，CCF-A 类，人工智能）论文提交截止时间为北京时间11月17日 19:59，摘要截止时间为11月11日 19:59。会议将于 June 20-25, 2027 在 Seattle, WA, United States 举行。<br><sub>（来源：[会议官网](https://cvpr.thecvf.com/Conferences/2027)）</sub>

<sub>标题和正文由 AI 根据原文整理（glm-4.7-flash），可能有误，请以原文为准。 俱乐部动态的统计日期为11月8日，数据来自[俱乐部开源仪表盘](https://osd.openatom.club/)。 会议截稿时间来自[CCFDDL](https://ccfddl.com/)，已换算成北京时间，请以会议官网为准。 有新闻线索欢迎[提交 Issue](https://github.com/game-life04/weekly-tech-agent/issues)。 本期由[每周科技收集 Agent](https://github.com/game-life04/weekly-tech-agent)于 2026-11-09 06:52（北京时间）自动生成。</sub>

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
