# 每周科技收集 Agent

[![Daily digest](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml)
[![CI](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

每天早上整理 AI 与开源动态，参照《CCF开源快讯》的体例出一期「每日快讯」，8:30 推送到俱乐部 QQ 群；每周一再出一期「每周快讯」。全部由程序自动生成，内容就放在这个仓库里，打开就能看。

- **订阅**：[RSS 订阅源](https://raw.githubusercontent.com/game-life04/weekly-tech-agent/main/feed.xml)；或者在本仓库点 **Watch → Custom → Releases**，每周快讯出刊时 GitHub 会发邮件通知你。
- **投稿**：欢迎推荐值得一看的文章、开源项目、活动和俱乐部动态，请[提交 issue](https://github.com/game-life04/weekly-tech-agent/issues/new?template=submission.md)。
- **往期**：[每周快讯](weekly/README.md) · [每日快讯和日报](daily/README.md)

<!-- wta:latest:start -->

## 每日快讯 · 11.08（周日）

> 今日 AI 与开源要闻 **16** 条，3 分钟速读。<br>
> [单独打开](daily/2026/2026-11-08-kuaixun.md) · [公众号排版版](daily/2026/2026-11-08-kuaixun.html) · [完整日报（含热度和原题）](daily/2026/2026-11-08.md) · [往期日报](daily/README.md)

<details>
<summary>群消息文字版（点开后，点代码框右上角的按钮整段复制）</summary>

```text
【每日科技快讯】11月8日 周日
今日 AI 与开源要闻 16 条，3 分钟速读

【俱乐部动态】
1. 开放原子开源俱乐部合并 1 个 PR、提交 5 次
2. kernel_translation_review_skill 合并 1 个 PR
3. hustsync.rs 提交 3 次

【国内动态】
4. 前OpenAI CTO推新模型，让用户自己训AI！创企估值被曝冲刺2600亿
→ Thinking Machines Lab 发布通用多模态模型 Inkling 2 Small，参数量达 5940 亿，支持用户自定义训练。

【开源项目】
5. vLLM 迁移至 LibTorch Stable ABI
→ vLLM 迁移至 LibTorch Stable ABI，无需重新编译即可兼容 PyTorch 升级。
6. Xorbits inference 发布 v4.2.0 版本
→ Xorbits inference 发布 v4.2.0 版本，新增 Xavier 前缀缓存共享功能，支持 Mooncake Store 存储。
7. rea-video：逆向分析视频制作方式
→ rea-video项目逐镜拆解视频，分析拍摄、AI生成或编码方式，并给出复刻方案。
8. voicebox：开源AI语音工作室
→ voicebox是一个开源的AI语音工作室，支持克隆、语音转文字和语音创作。
9. openai-cookbook：OpenAI API使用指南
→ openai-cookbook提供了使用OpenAI API的示例和指南。

【学术前沿】
10. ProQuant：边缘多模态大模型量化训练
→ ProQuant提出渐进式量化感知训练框架，通过自标签重采样提升边缘多模态大模型在低比特量化下的表现。
11. 认知共生体：迈向AI增强人类智能
→ 论文提出认知共生体概念，旨在构建终身、嵌入式且主动的AI伴侣，以增强人类智能。
12. Anthropic 研究发现 AI 审计员误报率随搜索深度增加
→ AI models can often spot problematic behavior by other AI agents in logs, according to a study by Anthropic researcher…
13. FlashOffloading：长上下文LLM低延迟KV缓存卸载
→ FlashOffloading架构通过完全卸载KV缓存并优化管理，显著提升了长上下文LLM服务的推理吞吐量。

【产业纵横】
14. OpenAI 与 Hacktron 合作寻找系统漏洞
→ OpenAI 与 Hacktron 合作测试与第三方服务的连接，旨在加强前沿 AI 的防御能力。
15. GitHub 推出代号 Rubicon 的新 Git 存储架构
→ GitHub 推出代号 Rubicon 的新架构，支持单个仓库容纳 5000 个智能体并发协作，每秒处理 7200 次推送。
16. AICon 北京探讨工业 OT 场景下大模型落地
→ AICon 北京大会强调工程能力是 Agent 规模化落地的关键，指出通用大模型在工业现场存在幻觉与失控问题。

【活动预告】
· 11月17日 CVPR 2027 论文截稿

完整版（含原文链接）：https://github.com/game-life04/weekly-tech-agent/blob/main/daily/2026/2026-11-08-kuaixun.md
标题和要点由 AI 整理，可能有误，请以原文为准。
```

</details>

### 今日快讯

#### 俱乐部动态

**开放原子开源俱乐部合并 1 个 PR、提交 5 次**<br>11月7日，据俱乐部开源仪表盘统计，开放原子开源俱乐部跟踪的 122 个仓库中有 3 个有人参与开发，共新增 PR 3 个、合并 1 个，提交 5 次，新增代码 662 行、删除 44 行，3 位贡献者参与。<br><sub>（来源：[俱乐部开源仪表盘](https://osd.openatom.club/)）</sub>

**kernel\_translation\_review\_skill 合并 1 个 PR**<br>11月7日，Linux内核SIG的 kernel\_translation\_review\_skill 仓库新增 PR 1 个、合并 1 个、提交 2 次、新增代码 5 行，1 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/kernel_translation_review_skill)）</sub>

**hustsync.rs 提交 3 次**<br>11月7日，镜像站运维 SIG的 hustsync.rs 仓库提交 3 次、新增代码 657 行，1 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/hustsync.rs)）</sub>

#### 国内动态

**前OpenAI CTO推新模型，让用户自己训AI！创企估值被曝冲刺2600亿**<br>11月6日，Thinking Machines Lab 发布通用多模态模型 Inkling 2 Small，参数量达 5940 亿，支持用户自定义训练。<br><sub>（来源：[智东西](https://zhidx.com/p/608120.html)）</sub>

#### 开源项目

**vLLM 迁移至 LibTorch Stable ABI**<br>11月6日，vLLM 迁移至 LibTorch Stable ABI，无需重新编译即可兼容 PyTorch 升级。<br><sub>（来源：[vLLM 博客](https://vllm.ai/blog/2026-11-06-stable-abi-cuda)）</sub>

**Xorbits inference 发布 v4.2.0 版本**<br>11月7日，Xorbits inference 发布 v4.2.0 版本，新增 Xavier 前缀缓存共享功能，支持 Mooncake Store 存储。<br><sub>（来源：[GitHub 版本发布](https://github.com/xorbitsai/inference/releases/tag/v4.2.0)）</sub>

**rea-video：逆向分析视频制作方式**<br>11月8日消息，rea-video项目逐镜拆解视频，分析拍摄、AI生成或编码方式，并给出复刻方案。<br><sub>（来源：[GitHub 新项目](https://github.com/JuneYaooo/rea-video)）</sub>

**voicebox：开源AI语音工作室**<br>11月8日消息，voicebox是一个开源的AI语音工作室，支持克隆、语音转文字和语音创作。<br><sub>（来源：[GitHub Trending](https://github.com/jamiepine/voicebox)）</sub>

**openai-cookbook：OpenAI API使用指南**<br>11月8日消息，openai-cookbook提供了使用OpenAI API的示例和指南。<br><sub>（来源：[GitHub Trending](https://github.com/openai/openai-cookbook)）</sub>

#### 学术前沿

**ProQuant：边缘多模态大模型量化训练**<br>11月6日，ProQuant提出渐进式量化感知训练框架，通过自标签重采样提升边缘多模态大模型在低比特量化下的表现。<br><sub>（来源：[arXiv · 高效推理](https://arxiv.org/abs/2611.08216)）</sub>

**认知共生体：迈向AI增强人类智能**<br>11月8日消息，论文提出认知共生体概念，旨在构建终身、嵌入式且主动的AI伴侣，以增强人类智能。<br><sub>（来源：[arXiv · 智能体](https://arxiv.org/abs/2611.05376)）</sub>

**Anthropic 研究发现 AI 审计员误报率随搜索深度增加**<br>11月8日，AI models can often spot problematic behavior by other AI agents in logs, according to a study by Anthropic researcher…<br><sub>（来源：[The Decoder](https://the-decoder.com/ai-auditors-catch-most-agent-misbehavior-but-flood-reviewers-with-false-alarms-new-study-finds/)）</sub>

**FlashOffloading：长上下文LLM低延迟KV缓存卸载**<br>11月8日消息，FlashOffloading架构通过完全卸载KV缓存并优化管理，显著提升了长上下文LLM服务的推理吞吐量。<br><sub>（来源：[arXiv · 长上下文与检索](https://arxiv.org/abs/2611.07542)）</sub>

#### 产业纵横

**OpenAI 与 Hacktron 合作寻找系统漏洞**<br>11月6日，OpenAI 与 Hacktron 合作测试与第三方服务的连接，旨在加强前沿 AI 的防御能力。<br><sub>（来源：[OpenAI](https://openai.com/index/partnering-with-hacktron)）</sub>

**GitHub 推出代号 Rubicon 的新 Git 存储架构**<br>11月7日，GitHub 推出代号 Rubicon 的新架构，支持单个仓库容纳 5000 个智能体并发协作，每秒处理 7200 次推送。<br><sub>（来源：[IT之家](https://www.ithome.com/1/023/823.htm)）</sub>

**AICon 北京探讨工业 OT 场景下大模型落地**<br>11月7日，AICon 北京大会强调工程能力是 Agent 规模化落地的关键，指出通用大模型在工业现场存在幻觉与失控问题。<br><sub>（来源：[InfoQ 中文](https://www.infoq.cn/article/K1bCIbHxeu3wLIjdusgr?utm_source=rss&utm_medium=article)）</sub>

### 活动预告

**CVPR 2027 论文截稿**<br>11月17日，IEEE/CVF Conference on Computer Vision and Pattern Recognition（CVPR 2027，CCF-A 类，人工智能）论文提交截止时间为北京时间11月17日 19:59，摘要截止时间为11月11日 19:59。会议将于 June 20-25, 2027 在 Seattle, WA, United States 举行。<br><sub>（来源：[会议官网](https://cvpr.thecvf.com/Conferences/2027)）</sub>

<sub>标题和正文由 AI 根据原文整理（glm-4.7-flash），可能有误，请以原文为准。 俱乐部动态的统计日期为11月7日，数据来自[俱乐部开源仪表盘](https://osd.openatom.club/)。 会议截稿时间来自[CCFDDL](https://ccfddl.com/)，已换算成北京时间，请以会议官网为准。 有新闻线索欢迎[提交 Issue](https://github.com/game-life04/weekly-tech-agent/issues)。 本期由[每周科技收集 Agent](https://github.com/game-life04/weekly-tech-agent)于 2026-11-08 06:45（北京时间）自动生成。</sub>

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
