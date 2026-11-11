# 每周科技收集 Agent

[![Daily digest](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml)
[![CI](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

每天早上整理 AI 与开源动态，参照《CCF开源快讯》的体例出一期「每日快讯」，8:30 推送到俱乐部 QQ 群；每周一再出一期「每周快讯」。全部由程序自动生成，内容就放在这个仓库里，打开就能看。

- **订阅**：[RSS 订阅源](https://raw.githubusercontent.com/game-life04/weekly-tech-agent/main/feed.xml)；或者在本仓库点 **Watch → Custom → Releases**，每周快讯出刊时 GitHub 会发邮件通知你。
- **投稿**：欢迎推荐值得一看的文章、开源项目、活动和俱乐部动态，请[提交 issue](https://github.com/game-life04/weekly-tech-agent/issues/new?template=submission.md)。
- **往期**：[每周快讯](weekly/README.md) · [每日快讯和日报](daily/README.md)

<!-- wta:latest:start -->

## 每日快讯 · 11.11（周三）

> 今日 AI 与开源要闻 **15** 条，3 分钟速读。<br>
> [单独打开](daily/2026/2026-11-11-kuaixun.md) · [公众号排版版](daily/2026/2026-11-11-kuaixun.html) · [完整日报（含热度和原题）](daily/2026/2026-11-11.md) · [往期日报](daily/README.md)

<details>
<summary>群消息文字版（点开后，点代码框右上角的按钮整段复制）</summary>

```text
【每日科技快讯】11月11日 周三
今日 AI 与开源要闻 15 条，3 分钟速读

【俱乐部动态】
1. 开放原子开源俱乐部合并 4 个 PR、提交 2 次
2. homebrew-tap 合并 3 个 PR
3. AtomGit-Mobile4Android 合并 1 个 PR

【国内动态】
4. MiniMax 开源 H3 Image 模型
→ MiniMax 开源 H3 Image 模型，被称作最强开源模型。

【海外动态】
5. Muse Ember：最小且高效的模型
→ Muse Ember 是专为复杂推理设计的最小模型，性价比优于 Claude Haiku 5.5 或 GPT-6 Luna。
6. Claude Whiteboards、Claude Sheets 和 Claude Data
→ Claude 推出白板、电子表格和数据仪表盘功能，支持团队协作。

【开源项目】
7. MinerU 发布 4.2.0 版本
→ MinerU 4.2.0 升级了 WebUI 交互与结果溯源，改善了复杂 PDF、公式和表格的解析质量。
8. Modern Web Guidance：现代 Web 最佳实践
→ Modern Web Guidance 帮助编码代理遵循最新的 Web 最佳实践，引导其远离遗留模式。
9. ha-mcp：配置 Home Assistant
→ ha-mcp 使用 Claude、ChatGPT 等助手配置和自动化 Home Assistant。
10. agent-skills：AI 编码代理技能
→ agent-skills 提供生产级的工程技能，帮助 AI 编码代理提升代码质量。
11. OpenSandbox：AI 代理沙箱运行时
→ OpenSandbox 是一个安全、快速且可扩展的沙箱运行时，用于 AI 代理。

【学术前沿】
12. Sage-Taiyi：元认知科学发现架构
→ Sage-Taiyi 是一种受元认知启发的架构，利用积累的科学理解来指导研究。
13. DeepMind 验证 Signal 核心加密
→ DeepMind 的 AlphaProof Code 代理在 Lean 中编写了三百万行证明来验证 Signal 的核心加密。
14. WorldFoundry：世界智能统一基础设施
→ WorldFoundry 定义了一个生成式世界模型，它维护环境的持久状态表示，并生成连贯轨迹。
15. P^2-MOPD 加速多教师策略蒸馏
→ P^2-MOPD 将学生和专家参数的线性组合视为可微模型，通过联合优化混合系数和学生权重来加速多教师策略蒸馏，使专家充当参数先验。

【活动预告】
· 11月17日 CVPR 2027 论文截稿

完整版（含原文链接）：https://github.com/game-life04/weekly-tech-agent/blob/main/daily/2026/2026-11-11-kuaixun.md
标题和要点由 AI 整理，可能有误，请以原文为准。
```

</details>

### 今日快讯

#### 俱乐部动态

**开放原子开源俱乐部合并 4 个 PR、提交 2 次**<br>11月10日，据俱乐部开源仪表盘统计，开放原子开源俱乐部跟踪的 122 个仓库中有 2 个有人参与开发，共新增 PR 1 个、合并 4 个，提交 2 次，新增代码 594 行、删除 264 行，2 位贡献者参与。<br><sub>（来源：[俱乐部开源仪表盘](https://osd.openatom.club/)）</sub>

**homebrew-tap 合并 3 个 PR**<br>11月10日，Agent SIG的 homebrew-tap 仓库新增 PR 1 个、合并 3 个、提交 1 次，1 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/homebrew-tap)）</sub>

**AtomGit-Mobile4Android 合并 1 个 PR**<br>11月10日，Agent SIG的 AtomGit-Mobile4Android 仓库合并 1 个、提交 1 次、新增代码 594 行，1 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/AtomGit-Mobile4Android)）</sub>

#### 国内动态

**MiniMax 开源 H3 Image 模型**<br>11月11日，MiniMax 开源 H3 Image 模型，被称作最强开源模型。<br><sub>（来源：[新智元](https://aiera.com.cn/2026/11/11/other/admin/123309/%e7%aa%81%e5%8f%91%ef%bc%81%e3%80%8c%e6%ba%90%e7%a5%9e%e3%80%8d-minimax-%e5%bc%80%e6%ba%90h3-image%ef%bc%8c%e6%9c%80%e5%bc%ba%e5%bc%80%e6%ba%90%e6%a8%a1%e5%9e%8b%e4%b8%ad%e5%9b%bd%e9%80%a0/)）</sub>

#### 海外动态

**Muse Ember：最小且高效的模型**<br>11月10日，Muse Ember 是专为复杂推理设计的最小模型，性价比优于 Claude Haiku 5.5 或 GPT-6 Luna。<br><sub>（来源：[Hacker News](https://research.meta.ai/blog/muse-ember)）</sub>

**Claude Whiteboards、Claude Sheets 和 Claude Data**<br>11月11日，Claude 推出白板、电子表格和数据仪表盘功能，支持团队协作。<br><sub>（来源：[Hacker News](https://claude.com/resources/articles/sheets-whiteboards-data)）</sub>

#### 开源项目

**MinerU 发布 4.2.0 版本**<br>11月10日，MinerU 4.2.0 升级了 WebUI 交互与结果溯源，改善了复杂 PDF、公式和表格的解析质量。<br><sub>（来源：[GitHub 版本发布](https://github.com/opendatalab/MinerU/releases/tag/mineru-4.2.0-released)）</sub>

**Modern Web Guidance：现代 Web 最佳实践**<br>11月11日，Modern Web Guidance 帮助编码代理遵循最新的 Web 最佳实践，引导其远离遗留模式。<br><sub>（来源：[Hacker News](https://github.com/GoogleChrome/modern-web-guidance)）</sub>

**ha-mcp：配置 Home Assistant**<br>11月11日消息，ha-mcp 使用 Claude、ChatGPT 等助手配置和自动化 Home Assistant。<br><sub>（来源：[GitHub Trending](https://github.com/homeassistant-ai/ha-mcp)）</sub>

**agent-skills：AI 编码代理技能**<br>11月11日消息，agent-skills 提供生产级的工程技能，帮助 AI 编码代理提升代码质量。<br><sub>（来源：[GitHub Trending](https://github.com/addyosmani/agent-skills)）</sub>

**OpenSandbox：AI 代理沙箱运行时**<br>11月11日消息，OpenSandbox 是一个安全、快速且可扩展的沙箱运行时，用于 AI 代理。<br><sub>（来源：[GitHub Trending](https://github.com/opensandbox-group/OpenSandbox)）</sub>

#### 学术前沿

**Sage-Taiyi：元认知科学发现架构**<br>11月9日，Sage-Taiyi 是一种受元认知启发的架构，利用积累的科学理解来指导研究。<br><sub>（来源：[Hugging Face 热门论文](https://arxiv.org/abs/2611.12762)）</sub>

**DeepMind 验证 Signal 核心加密**<br>11月10日，DeepMind 的 AlphaProof Code 代理在 Lean 中编写了三百万行证明来验证 Signal 的核心加密。<br><sub>（来源：[Google DeepMind](https://deepmind.google/blog/introducing-alphaproof-code/)）</sub>

**WorldFoundry：世界智能统一基础设施**<br>11月11日消息，WorldFoundry 定义了一个生成式世界模型，它维护环境的持久状态表示，并生成连贯轨迹。<br><sub>（来源：[Hugging Face 热门论文](https://arxiv.org/abs/2611.10771)）</sub>

**P^2-MOPD 加速多教师策略蒸馏**<br>11月11日消息，P^2-MOPD 将学生和专家参数的线性组合视为可微模型，通过联合优化混合系数和学生权重来加速多教师策略蒸馏，使专家充当参数先验。<br><sub>（来源：[Hugging Face 热门论文](https://arxiv.org/abs/2611.03953)）</sub>

### 活动预告

**CVPR 2027 论文截稿**<br>11月17日，IEEE/CVF Conference on Computer Vision and Pattern Recognition（CVPR 2027，CCF-A 类，人工智能）论文提交截止时间为北京时间11月17日 19:59，摘要截止时间为11月11日 19:59。会议将于 June 22-25, 2027 在 Seattle, WA, United States 举行。<br><sub>（来源：[会议官网](https://cvpr.thecvf.com/Conferences/2027)）</sub>

<sub>标题和正文由 AI 根据原文整理（glm-4.7-flash），可能有误，请以原文为准。 俱乐部动态的统计日期为11月10日，数据来自[俱乐部开源仪表盘](https://osd.openatom.club/)。 会议截稿时间来自[CCFDDL](https://ccfddl.com/)，已换算成北京时间，请以会议官网为准。 有新闻线索欢迎[提交 Issue](https://github.com/game-life04/weekly-tech-agent/issues)。 本期由[每周科技收集 Agent](https://github.com/game-life04/weekly-tech-agent)于 2026-11-11 09:31（北京时间）自动生成。</sub>

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
