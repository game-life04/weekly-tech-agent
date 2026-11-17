# 每周科技收集 Agent

[![Daily digest](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml)
[![CI](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

每天早上整理 AI 与开源动态，参照《CCF开源快讯》的体例出一期「每日快讯」，8:30 推送到俱乐部 QQ 群；每周一再出一期「每周快讯」。全部由程序自动生成，内容就放在这个仓库里，打开就能看。

- **订阅**：[RSS 订阅源](https://raw.githubusercontent.com/game-life04/weekly-tech-agent/main/feed.xml)；或者在本仓库点 **Watch → Custom → Releases**，每周快讯出刊时 GitHub 会发邮件通知你。
- **投稿**：欢迎推荐值得一看的文章、开源项目、活动和俱乐部动态，请[提交 issue](https://github.com/game-life04/weekly-tech-agent/issues/new?template=submission.md)。
- **往期**：[每周快讯](weekly/README.md) · [每日快讯和日报](daily/README.md)

<!-- wta:latest:start -->

## 每日快讯 · 11.17（周二）

> 今日 AI 与开源要闻 **14** 条，3 分钟速读。<br>
> [单独打开](daily/2026/2026-11-17-kuaixun.md) · [公众号排版版](daily/2026/2026-11-17-kuaixun.html) · [完整日报（含热度和原题）](daily/2026/2026-11-17.md) · [往期日报](daily/README.md)

<details>
<summary>群消息文字版（点开后，点代码框右上角的按钮整段复制）</summary>

```text
【每日科技快讯】11月17日 周二
今日 AI 与开源要闻 14 条，3 分钟速读

【俱乐部动态】
1. 开放原子开源俱乐部合并 1 个 PR、提交 5 次
2. AtomGit-Mobile4Android 合并 1 个 PR
3. hustmirrors-waf-backend 提交 4 次

【国内动态】
4. 华为云发布CloudRobo-WM1.2具身世界模型
→ 华为云推出首款昇腾原生具身世界模型CloudRobo-WM1.2，在RoboTwin 2.0、LiberoPro 2.0评测中均位列第一。

【海外动态】
5. TokenEconomizer开源插件发布
→ 微软开源插件TokenEconomizer通过利用历史会话减少重复学习，降低AI编程代理的成本并保持任务成功。

【开源项目】
6. vLLM发布v0.34.0版本
→ vLLM v0.34.0发布，新增10个模型，默认开启可扩展KV缓存，提供Blackwell和MI355X加速。
7. blender-ai-mcp-addon：Blender AI 助手
→ hitkeeen 发布 Blender AI 助手和 MCP 服务器，支持视觉聊天、场景工具和多智能体工作流。
8. Gemini-Config-Checker-：Chain 区域扫描器
→ YellowLaborerMarket 发布 Chain 区域扫描器，用于查找能进入 Google AI Studio 和 Gemini 的代理配置。
9. paper-orchestra：自动撰写 AI 论文框架
→ google-research 发布 PaperOrchestra，这是一个用于自动撰写 AI 研究论文的多智能体框架。
10. rakazo：开源 Grok Bot 替代品
→ elie222 发布开源 Grok Bot 替代品，支持自定义模型和沙箱。

【学术前沿】
11. OpenAI发布科学家使用ChatGPT研究报告
→ OpenAI发布报告，分析了1800多名科学家利用ChatGPT进行研究的工作流程、生产力及发现预期。
12. OpenAI GPT-6 Astra攻克标准模型难题
→ OpenAI物理学家利用GPT-6 Astra将粒子物理学25年未解的数学问题转化为可工作的证明。
13. Envisioning Agentic Robotics：智能体机器人新纪元
→ 论文提出 embodied System 2 作为智能体机器人的决策核心，旨在解决通用推理在物理约束下转化为有效可验证动作的挑战。
14. Gamer：通用视觉-语言-动作基础模型
→ Gamer 是一个专为复杂交互环境中的长时任务设计的通用智能体框架，结合了感知、记忆管理和多步推理。

【活动预告】
· 11月17日 CVPR 2027 论文截稿

完整版（含原文链接）：https://github.com/game-life04/weekly-tech-agent/blob/main/daily/2026/2026-11-17-kuaixun.md
标题和要点由 AI 整理，可能有误，请以原文为准。
```

</details>

### 今日快讯

#### 俱乐部动态

**开放原子开源俱乐部合并 1 个 PR、提交 5 次**<br>11月16日，据俱乐部开源仪表盘统计，开放原子开源俱乐部跟踪的 122 个仓库中有 3 个有人参与开发，共新增 PR 2 个、合并 1 个，提交 5 次，新增代码 1843 行、删除 215 行，3 位贡献者参与。<br><sub>（来源：[俱乐部开源仪表盘](https://osd.openatom.club/)）</sub>

**AtomGit-Mobile4Android 合并 1 个 PR**<br>11月16日，Agent SIG的 AtomGit-Mobile4Android 仓库新增 PR 1 个、合并 1 个、提交 1 次、新增代码 616 行，1 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/AtomGit-Mobile4Android)）</sub>

**hustmirrors-waf-backend 提交 4 次**<br>11月16日，镜像站运维 SIG的 hustmirrors-waf-backend 仓库提交 4 次、新增代码 1227 行，1 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/hustmirrors-waf-backend)）</sub>

#### 国内动态

**华为云发布CloudRobo-WM1.2具身世界模型**<br>11月17日，华为云推出首款昇腾原生具身世界模型CloudRobo-WM1.2，在RoboTwin 2.0、LiberoPro 2.0评测中均位列第一。<br><sub>（来源：[智东西](https://zhidx.com/p/610813.html)）</sub>

#### 海外动态

**TokenEconomizer开源插件发布**<br>11月17日，微软开源插件TokenEconomizer通过利用历史会话减少重复学习，降低AI编程代理的成本并保持任务成功。<br><sub>（来源：[Microsoft Research](https://www.microsoft.com/en-us/research/blog/tokeneconomizer-learning-from-experience-to-make-ai-coding-agents-more-efficient/)）</sub>

#### 开源项目

**vLLM发布v0.34.0版本**<br>11月17日，vLLM v0.34.0发布，新增10个模型，默认开启可扩展KV缓存，提供Blackwell和MI355X加速。<br><sub>（来源：[GitHub 版本发布](https://github.com/vllm-project/vllm/releases/tag/v0.34.0)）</sub>

**blender-ai-mcp-addon：Blender AI 助手**<br>11月17日消息，hitkeeen 发布 Blender AI 助手和 MCP 服务器，支持视觉聊天、场景工具和多智能体工作流。<br><sub>（来源：[GitHub 新项目](https://github.com/hitkeeen/blender-ai-mcp-addon)）</sub>

**Gemini-Config-Checker-：Chain 区域扫描器**<br>11月17日消息，YellowLaborerMarket 发布 Chain 区域扫描器，用于查找能进入 Google AI Studio 和 Gemini 的代理配置。<br><sub>（来源：[GitHub 新项目](https://github.com/YellowLaborerMarket/Gemini-Config-Checker-)）</sub>

**paper-orchestra：自动撰写 AI 论文框架**<br>11月17日消息，google-research 发布 PaperOrchestra，这是一个用于自动撰写 AI 研究论文的多智能体框架。<br><sub>（来源：[GitHub Trending](https://github.com/google-research/paper-orchestra)）</sub>

**rakazo：开源 Grok Bot 替代品**<br>11月17日消息，elie222 发布开源 Grok Bot 替代品，支持自定义模型和沙箱。<br><sub>（来源：[GitHub Trending](https://github.com/elie222/rakazo)）</sub>

#### 学术前沿

**OpenAI发布科学家使用ChatGPT研究报告**<br>11月16日，OpenAI发布报告，分析了1800多名科学家利用ChatGPT进行研究的工作流程、生产力及发现预期。<br><sub>（来源：[OpenAI](https://openai.com/index/science-at-the-frontier)）</sub>

**OpenAI GPT-6 Astra攻克标准模型难题**<br>11月17日，OpenAI物理学家利用GPT-6 Astra将粒子物理学25年未解的数学问题转化为可工作的证明。<br><sub>（来源：[The Decoder](https://the-decoder.com/openais-gpt-6-astra-tackles-the-standard-models-toughest-math-problem-on-a-lattice/)）</sub>

**Envisioning Agentic Robotics：智能体机器人新纪元**<br>11月17日消息，论文提出 embodied System 2 作为智能体机器人的决策核心，旨在解决通用推理在物理约束下转化为有效可验证动作的挑战。<br><sub>（来源：[arXiv · 智能体](https://arxiv.org/abs/2611.18359)）</sub>

**Gamer：通用视觉-语言-动作基础模型**<br>11月17日消息，Gamer 是一个专为复杂交互环境中的长时任务设计的通用智能体框架，结合了感知、记忆管理和多步推理。<br><sub>（来源：[arXiv · 智能体](https://arxiv.org/abs/2611.18397)）</sub>

### 活动预告

**CVPR 2027 论文截稿**<br>11月17日，IEEE/CVF Conference on Computer Vision and Pattern Recognition（CVPR 2027，CCF-A 类，人工智能）论文提交截止时间为北京时间11月17日 19:59，摘要截止时间为11月11日 19:59。会议将于 June 22-25, 2027 在 Seattle, WA, United States 举行。<br><sub>（来源：[会议官网](https://cvpr.thecvf.com/Conferences/2027)）</sub>

<sub>标题和正文由 AI 根据原文整理（glm-4.7-flash），可能有误，请以原文为准。 俱乐部动态的统计日期为11月16日，数据来自[俱乐部开源仪表盘](https://osd.openatom.club/)。 会议截稿时间来自[CCFDDL](https://ccfddl.com/)，已换算成北京时间，请以会议官网为准。 有新闻线索欢迎[提交 Issue](https://github.com/game-life04/weekly-tech-agent/issues)。 本期由[每周科技收集 Agent](https://github.com/game-life04/weekly-tech-agent)于 2026-11-17 12:12（北京时间）自动生成。</sub>

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
