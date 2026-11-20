# 每周科技收集 Agent

[![Daily digest](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml)
[![CI](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

每天早上整理 AI 与开源动态，参照《CCF开源快讯》的体例出一期「每日快讯」，8:30 推送到俱乐部 QQ 群；每周一再出一期「每周快讯」。全部由程序自动生成，内容就放在这个仓库里，打开就能看。

- **订阅**：[RSS 订阅源](https://raw.githubusercontent.com/game-life04/weekly-tech-agent/main/feed.xml)；或者在本仓库点 **Watch → Custom → Releases**，每周快讯出刊时 GitHub 会发邮件通知你。
- **投稿**：欢迎推荐值得一看的文章、开源项目、活动和俱乐部动态，请[提交 issue](https://github.com/game-life04/weekly-tech-agent/issues/new?template=submission.md)。
- **往期**：[每周快讯](weekly/README.md) · [每日快讯和日报](daily/README.md)

<!-- wta:latest:start -->

## 每日快讯 · 11.20（周五）

> 今日 AI 与开源要闻 **16** 条，3 分钟速读。<br>
> [单独打开](daily/2026/2026-11-20-kuaixun.md) · [公众号排版版](daily/2026/2026-11-20-kuaixun.html) · [完整日报（含热度和原题）](daily/2026/2026-11-20.md) · [往期日报](daily/README.md)

<details>
<summary>群消息文字版（点开后，点代码框右上角的按钮整段复制）</summary>

```text
【每日科技快讯】11月20日 周五
今日 AI 与开源要闻 16 条，3 分钟速读

【俱乐部动态】
1. 开放原子开源俱乐部合并 7 个 PR、提交 11 次
2. AtomGit-mobile4Harmony 合并 6 个 PR
3. hust-mirrors 合并 1 个 PR

【海外动态】
4. Google DeepMind 推出 Genie 4
→ Google DeepMind 为 Google AI Ultra 订阅用户提供 Genie 4，可生成具有实时音频和编辑功能的交互式世界。
5. Google DeepMind 发布 Gemini 4 Neon
→ Google DeepMind 推出 Gemini 4 Neon，在复杂软件工程、知识工作和科学工作流中提供前沿级智能。

【开源项目】
6. huggingface/peft 发布 0.22.0 版本
→ huggingface/peft 新增 PaCA 方法，通过微调预训练权重的随机输入列来加速训练。
7. blender-ai-mcp-addon：Blender AI 助手
→ blender-ai-mcp-addon 是 Blender AI 助手和 MCP 服务器，支持视觉聊天、场景工具和多智能体工作流。
8. SoduWork：原生 AI 引擎
→ SoduWork 是面向团队和智能体的原生 AI 引擎，支持多框架、多智能体和自托管。
9. pi：AI 智能体工具包
→ pi 是 AI 智能体工具包，提供统一 LLM API、智能体循环、TUI 和编码智能体 CLI。
10. openai/codex rust 发布 0.171.0 版本
→ openai/codex rust 新增 GPT-6.2 Sol 和 Astra 模型，默认启用 TUI 工作区。

【学术前沿】
11. QDA：基于智能体的闭环 LLM 量化设计
→ QDA 系统利用智能体通过多轮评估优化量化配方，在多个推理模型上提升了量化精度。
12. Claude Fable 5.2 解决黑洞物理问题
→ Claude Fable 5.2 解决了理论物理中关于黑洞和量子引力理论搜索的两个开放问题。
13. Multi-Branch Transformer：并行化架构
→ Multi-Branch Transformer 通过并行执行独立参数分支来扩展模型，在参数和训练计算量匹配的情况下表现优于传统模型。
14. SPILLWAY：防御工具使用智能体
→ SPILLWAY 方法通过分离目标准入与清洗过程来防御工具使用智能体的提示注入攻击。

【产业纵横】
15. KPMG 使用 AI 代理进行审计试验
→ KPMG 使用超过 100 个 AI 代理进行审计试验，AI 代理在提问方面表现优于会计师。
16. Anthropic 上市市值 1.27 万亿美元
→ Anthropic 上市首日大涨 17%，市值达 1.27 万亿美元，成为最受关注的 AI 公司之一。

【活动预告】
· 12月3日 EuroVis 2027 论文截稿

完整版（含原文链接）：https://github.com/game-life04/weekly-tech-agent/blob/main/daily/2026/2026-11-20-kuaixun.md
标题和要点由 AI 整理，可能有误，请以原文为准。
```

</details>

### 今日快讯

#### 俱乐部动态

**开放原子开源俱乐部合并 7 个 PR、提交 11 次**<br>11月19日，据俱乐部开源仪表盘统计，开放原子开源俱乐部跟踪的 122 个仓库中有 2 个有人参与开发，共新增 PR 2 个、合并 7 个，提交 11 次，新增代码 8845 行、删除 139 行，4 位贡献者参与。<br><sub>（来源：[俱乐部开源仪表盘](https://osd.openatom.club/)）</sub>

**AtomGit-mobile4Harmony 合并 6 个 PR**<br>11月19日，Agent SIG的 AtomGit-mobile4Harmony 仓库合并 6 个、提交 10 次、新增代码 8725 行，2 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/AtomGit-mobile4Harmony)）</sub>

**hust-mirrors 合并 1 个 PR**<br>11月19日，镜像站运维 SIG的 hust-mirrors 仓库合并 1 个、提交 1 次、新增代码 120 行，2 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/hust-mirrors)）</sub>

#### 海外动态

**Google DeepMind 推出 Genie 4**<br>11月19日，Google DeepMind 为 Google AI Ultra 订阅用户提供 Genie 4，可生成具有实时音频和编辑功能的交互式世界。<br><sub>（来源：[Google DeepMind](https://deepmind.google/blog/genie-4-is-now-available/)）</sub>

**Google DeepMind 发布 Gemini 4 Neon**<br>11月19日，Google DeepMind 推出 Gemini 4 Neon，在复杂软件工程、知识工作和科学工作流中提供前沿级智能。<br><sub>（来源：[Google DeepMind](https://deepmind.google/blog/introducing-gemini-4-neon/)）</sub>

#### 开源项目

**huggingface/peft 发布 0.22.0 版本**<br>11月19日，huggingface/peft 新增 PaCA 方法，通过微调预训练权重的随机输入列来加速训练。<br><sub>（来源：[GitHub 版本发布](https://github.com/huggingface/peft/releases/tag/v0.22.0)）</sub>

**blender-ai-mcp-addon：Blender AI 助手**<br>11月20日消息，blender-ai-mcp-addon 是 Blender AI 助手和 MCP 服务器，支持视觉聊天、场景工具和多智能体工作流。<br><sub>（来源：[GitHub 新项目](https://github.com/bookwjitchieni1986/blender-ai-mcp-addon)）</sub>

**SoduWork：原生 AI 引擎**<br>11月20日消息，SoduWork 是面向团队和智能体的原生 AI 引擎，支持多框架、多智能体和自托管。<br><sub>（来源：[GitHub 新项目](https://github.com/mdiri-ai/SoduWork)）</sub>

**pi：AI 智能体工具包**<br>11月20日消息，pi 是 AI 智能体工具包，提供统一 LLM API、智能体循环、TUI 和编码智能体 CLI。<br><sub>（来源：[GitHub Trending](https://github.com/earendil-works/pi)）</sub>

**openai/codex rust 发布 0.171.0 版本**<br>11月20日，openai/codex rust 新增 GPT-6.2 Sol 和 Astra 模型，默认启用 TUI 工作区。<br><sub>（来源：[GitHub 版本发布](https://github.com/openai/codex/releases/tag/rust-v0.171.0)）</sub>

#### 学术前沿

**QDA：基于智能体的闭环 LLM 量化设计**<br>11月18日，QDA 系统利用智能体通过多轮评估优化量化配方，在多个推理模型上提升了量化精度。<br><sub>（来源：[arXiv · 高效推理](https://arxiv.org/abs/2611.23388)）</sub>

**Claude Fable 5.2 解决黑洞物理问题**<br>11月20日，Claude Fable 5.2 解决了理论物理中关于黑洞和量子引力理论搜索的两个开放问题。<br><sub>（来源：[Hacker News](https://www.anthropic.com/research/claude-black-hole-physics)）</sub>

**Multi-Branch Transformer：并行化架构**<br>11月20日消息，Multi-Branch Transformer 通过并行执行独立参数分支来扩展模型，在参数和训练计算量匹配的情况下表现优于传统模型。<br><sub>（来源：[Hugging Face 热门论文](https://arxiv.org/abs/2611.19800)）</sub>

**SPILLWAY：防御工具使用智能体**<br>11月20日消息，SPILLWAY 方法通过分离目标准入与清洗过程来防御工具使用智能体的提示注入攻击。<br><sub>（来源：[Hugging Face 热门论文](https://arxiv.org/abs/2611.07222)）</sub>

#### 产业纵横

**KPMG 使用 AI 代理进行审计试验**<br>11月18日，KPMG 使用超过 100 个 AI 代理进行审计试验，AI 代理在提问方面表现优于会计师。<br><sub>（来源：[Hacker News](https://europeanbusinessmagazine.com/ai-agents-better-questions-kpmg/)）</sub>

**Anthropic 上市市值 1.27 万亿美元**<br>11月20日，Anthropic 上市首日大涨 17%，市值达 1.27 万亿美元，成为最受关注的 AI 公司之一。<br><sub>（来源：[极客公园](http://www.geekpark.net/news/374235)）</sub>

### 活动预告

**EuroVis 2027 论文截稿**<br>12月3日，Eurographics Conference on Visualization（EuroVis 2027，CCF-B 类，图形学与多媒体）Full papers的论文提交截止时间为北京时间12月3日 19:59，摘要截止时间为11月24日 19:59。会议将于 May 31-June 4, 2027 在 Stuttgart, Germany 举行。<br><sub>（来源：[会议官网](https://eurovis27.github.io/web/)）</sub>

<sub>标题和正文由 AI 根据原文整理（glm-4.7-flash），可能有误，请以原文为准。 俱乐部动态的统计日期为11月19日，数据来自[俱乐部开源仪表盘](https://osd.openatom.club/)。 会议截稿时间来自[CCFDDL](https://ccfddl.com/)，已换算成北京时间，请以会议官网为准。 有新闻线索欢迎[提交 Issue](https://github.com/game-life04/weekly-tech-agent/issues)。 本期由[每周科技收集 Agent](https://github.com/game-life04/weekly-tech-agent)于 2026-11-20 09:15（北京时间）自动生成。</sub>

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
