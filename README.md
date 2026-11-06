# 每周科技收集 Agent

[![Daily digest](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml)
[![CI](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

每天早上整理 AI 与开源动态，参照《CCF开源快讯》的体例出一期「每日快讯」，8:30 推送到俱乐部 QQ 群；每周一再出一期「每周快讯」。全部由程序自动生成，内容就放在这个仓库里，打开就能看。

- **订阅**：[RSS 订阅源](https://raw.githubusercontent.com/game-life04/weekly-tech-agent/main/feed.xml)；或者在本仓库点 **Watch → Custom → Releases**，每周快讯出刊时 GitHub 会发邮件通知你。
- **投稿**：欢迎推荐值得一看的文章、开源项目、活动和俱乐部动态，请[提交 issue](https://github.com/game-life04/weekly-tech-agent/issues/new?template=submission.md)。
- **往期**：[每周快讯](weekly/README.md) · [每日快讯和日报](daily/README.md)

<!-- wta:latest:start -->

## 每日快讯 · 11.06（周五）

> 今日 AI 与开源要闻 **20** 条，3 分钟速读。<br>
> [单独打开](daily/2026/2026-11-06-kuaixun.md) · [公众号排版版](daily/2026/2026-11-06-kuaixun.html) · [完整日报（含热度和原题）](daily/2026/2026-11-06.md) · [往期日报](daily/README.md)

<details>
<summary>群消息文字版（点开后，点代码框右上角的按钮整段复制）</summary>

```text
【每日科技快讯】11月6日 周五
今日 AI 与开源要闻 20 条，3 分钟速读

【俱乐部动态】
1. 开放原子开源俱乐部合并 3 个 PR、提交 2 次
2. system-security-dojo-x64-2026 合并 1 个 PR
3. AtomGit-Mobile4Android 新增 2 个 PR

【政策动向】
4. 何立峰在北京调研时指出 强化科技创新与产业创新深度融合 推动经济持续向新向优向好发展
→ 据中国政府网消息：何立峰在北京调研时指出 强化科技创新与产业创新深度融合 推动经济持续向新向优向好发展。

【国内动态】
5. 百度开源文心5.5 Flash Base，多基准测试刷新同尺寸模型 SOTA
→ 百度开源文心5.5 Flash Base，在知识、推理等多个基准测试中刷新同尺寸模型 SOTA 表现。

【海外动态】
6. AI 正在迫使我们偿还 40 年的技术债务
→ AI 加速了网络攻击和防御，暴露了脆弱遗留系统中的技术债务。
7. GPT‑6 Cyber：推进对齐网络安全代理的前沿
→ OpenAI 推出 GPT‑6 Cyber 模型，用于发现可利用漏洞并开发修复方案，训练时保持在授权范围内。
8. Images 2.6
→ 在 ChatGPT、Codex 和 API 中提供更快的图像生成、GIF 创建和更精确的编辑控制。
9. Merge 结合 OpenAI 技术构建产品与商业工具
→ Merge 使用 GPT‑6 Astra、ChatGPT 和 Codex 审查产品代码并支持营销，还利用 AI 规划高管晚宴。
10. Gemini Omni 1.2 Flash：原生15秒视频生成与编辑
→ Gemini Omni 1.2 Flash 带来原生15秒视频生成与编辑功能，一致性更强且价格降低30%。
11. 使用 PDD Kit 正式验证智能体编写的全栈 Web 应用
→ PDD Kit 将开发者意图转化为 Verus 规范，证明 AI 生成的代码符合规范，并使用测试辅助验证。

【开源项目】
12. 百度发布最新基座模型 ERNIE 5.5 Flash Base：效率、开源、高性价比
→ 百度开源 ERNIE 5.5 Flash Base，采用 MoE 架构，总参数量 2800 亿，支持最长 100 万 Token 上下文。
13. KKKKhazix/agent-autoloop
→ 让你的命令行 Agent 在后台自己接活、自己跟进到底；平时不烦你，遇到拿不准的事才发卡片找你拍板。
14. scenario-labs/skills
→ AI 智能体通过 Scenario MCP 获取生产就绪的图像、视频、音频和 3D 资产。
15. garrytan/gstack
→ 提供 Claude Code 的精确配置，包含 23 个用于 CEO、设计师、工程经理等角色的工具。
16. microsoft/VibeVoice
→ Open-Source Frontier Voice AI。

【学术前沿】
17. Turns Matter：通过回合级信用推进流媒体视频强化学习
→ 现有方法在流媒体视频理解中存在奖励设计单一和轨迹级反馈不匹配的问题。TurnWise提出回合级GRPO框架，通过沉默完成前缀评分分离学习信号，并平均回合内损失。实验表明该方法优于先前RL方法。
18. FrontierPhysics：端到端物理研究智能体评测
→ 现有评测仅关注固定问题或子任务。FrontierPhysics引入56个由物理学家设计的任务，要求智能体完成文献综述、实验和论文撰写。评测发现智能体主要在推理严谨性和专家直觉上存在不足。
19. DreamX：视频扩散模型作为通用潜在动作学习器
→ 现有模型难以从视觉变化中分离出动作本质。DreamX利用预训练视频扩散模型提取紧凑的潜在动作，压缩视频帧并捕捉动作相关动态。该模型在LARY-Bench上表现优异，支持跨具身和环境的动作迁移。
20. SWE-Trail：编码智能体训练的历史引导轨迹收集
→ 现有轨迹收集方法导致数据冗余且存在训练测试不匹配。SWE-Trail利用历史轨迹指导后续收集，同时保持历史在智能体上下文之外。该方法通过执行候选动作选择有效路径，提升了学生模型的训练效果。

【活动预告】
· 11月17日 CVPR 2027 论文截稿

完整版（含原文链接）：https://github.com/game-life04/weekly-tech-agent/blob/main/daily/2026/2026-11-06-kuaixun.md
标题和要点由 AI 整理，可能有误，请以原文为准。
```

</details>

### 今日快讯

#### 俱乐部动态

**开放原子开源俱乐部合并 3 个 PR、提交 2 次**<br>11月5日，据俱乐部开源仪表盘统计，开放原子开源俱乐部跟踪的 122 个仓库中有 3 个有人参与开发，共新增 PR 4 个、合并 3 个，提交 2 次，新增代码 2 行、删除 2 行，4 位贡献者参与。<br><sub>（来源：[俱乐部开源仪表盘](https://osd.openatom.club/)）</sub>

**system-security-dojo-x64-2026 合并 1 个 PR**<br>11月5日，pwn.hust.college SIG的 system-security-dojo-x64-2026 仓库合并 1 个、提交 1 次，2 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/system-security-dojo-x64-2026)）</sub>

**AtomGit-Mobile4Android 新增 2 个 PR**<br>11月5日，Agent SIG的 AtomGit-Mobile4Android 仓库新增 PR 2 个，1 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/AtomGit-Mobile4Android)）</sub>

#### 政策动向

**何立峰在北京调研时指出 强化科技创新与产业创新深度融合 推动经济持续向新向优向好发展**<br>11月5日，据中国政府网消息：何立峰在北京调研时指出 强化科技创新与产业创新深度融合 推动经济持续向新向优向好发展。<br><sub>（来源：[中国政府网](https://www.gov.cn/yaowen/liebiao/202611/content_7085139.htm)）</sub>

#### 国内动态

**百度开源文心5.5 Flash Base，多基准测试刷新同尺寸模型 SOTA**<br>11月5日，百度开源文心5.5 Flash Base，在知识、推理等多个基准测试中刷新同尺寸模型 SOTA 表现。<br><sub>（来源：[量子位](https://www.qbitai.com/2026/11/507787.html)）</sub>

#### 海外动态

**AI 正在迫使我们偿还 40 年的技术债务**<br>11月4日，AI 加速了网络攻击和防御，暴露了脆弱遗留系统中的技术债务。<br><sub>（来源：[Hacker News](https://spectrum.ieee.org/ai-in-cybersecurity-php2shell-vulnerability)）</sub>

**GPT‑6 Cyber：推进对齐网络安全代理的前沿**<br>11月5日，OpenAI 推出 GPT‑6 Cyber 模型，用于发现可利用漏洞并开发修复方案，训练时保持在授权范围内。<br><sub>（来源：[OpenAI](https://openai.com/index/introducing-gpt-6-cyber)）</sub>

**Images 2.6**<br>11月5日，在 ChatGPT、Codex 和 API 中提供更快的图像生成、GIF 创建和更精确的编辑控制。<br><sub>（来源：[Hacker News](https://openai.com/index/introducing-images-2-6/)）</sub>

**Merge 结合 OpenAI 技术构建产品与商业工具**<br>11月5日，Merge 使用 GPT‑6 Astra、ChatGPT 和 Codex 审查产品代码并支持营销，还利用 AI 规划高管晚宴。<br><sub>（来源：[OpenAI](https://openai.com/index/merge-builds-with-openai)）</sub>

**Gemini Omni 1.2 Flash：原生15秒视频生成与编辑**<br>11月6日，Gemini Omni 1.2 Flash 带来原生15秒视频生成与编辑功能，一致性更强且价格降低30%。<br><sub>（来源：[Google DeepMind](https://deepmind.google/blog/gemini-omni-12-flash-fast-and-cost-effective-with-longer-clips/)）</sub>

**使用 PDD Kit 正式验证智能体编写的全栈 Web 应用**<br>11月6日，PDD Kit 将开发者意图转化为 Verus 规范，证明 AI 生成的代码符合规范，并使用测试辅助验证。<br><sub>（来源：[Microsoft Research](https://www.microsoft.com/en-us/research/blog/formally-verifying-agent-written-full-stack-web-apps-with-pdd-kit/)）</sub>

#### 开源项目

**百度发布最新基座模型 ERNIE 5.5 Flash Base：效率、开源、高性价比**<br>11月5日，百度开源 ERNIE 5.5 Flash Base，采用 MoE 架构，总参数量 2800 亿，支持最长 100 万 Token 上下文。<br><sub>（来源：[开源中国](https://www.oschina.net/news/503429/ernie-5-5-flash-base)）</sub>

**KKKKhazix/agent-autoloop**<br>11月6日消息，让你的命令行 Agent 在后台自己接活、自己跟进到底；平时不烦你，遇到拿不准的事才发卡片找你拍板。<br><sub>（来源：[GitHub 新项目](https://github.com/KKKKhazix/agent-autoloop)）</sub>

**scenario-labs/skills**<br>11月6日消息，AI 智能体通过 Scenario MCP 获取生产就绪的图像、视频、音频和 3D 资产。<br><sub>（来源：[GitHub Trending](https://github.com/scenario-labs/skills)）</sub>

**garrytan/gstack**<br>11月6日消息，提供 Claude Code 的精确配置，包含 23 个用于 CEO、设计师、工程经理等角色的工具。<br><sub>（来源：[GitHub Trending](https://github.com/garrytan/gstack)）</sub>

**microsoft/VibeVoice**<br>11月6日消息，Open-Source Frontier Voice AI。<br><sub>（来源：[GitHub Trending](https://github.com/microsoft/VibeVoice)）</sub>

#### 学术前沿

**Turns Matter：通过回合级信用推进流媒体视频强化学习**<br>11月4日，现有方法在流媒体视频理解中存在奖励设计单一和轨迹级反馈不匹配的问题。TurnWise提出回合级GRPO框架，通过沉默完成前缀评分分离学习信号，并平均回合内损失。实验表明该方法优于先前RL方法。<br><sub>（来源：[Hugging Face 热门论文](https://arxiv.org/abs/2611.06728)）</sub>

**FrontierPhysics：端到端物理研究智能体评测**<br>11月5日，现有评测仅关注固定问题或子任务。FrontierPhysics引入56个由物理学家设计的任务，要求智能体完成文献综述、实验和论文撰写。评测发现智能体主要在推理严谨性和专家直觉上存在不足。<br><sub>（来源：[arXiv · 智能体](https://arxiv.org/abs/2611.06910)）</sub>

**DreamX：视频扩散模型作为通用潜在动作学习器**<br>11月6日消息，现有模型难以从视觉变化中分离出动作本质。DreamX利用预训练视频扩散模型提取紧凑的潜在动作，压缩视频帧并捕捉动作相关动态。该模型在LARY-Bench上表现优异，支持跨具身和环境的动作迁移。<br><sub>（来源：[Hugging Face 热门论文](https://arxiv.org/abs/2611.05377)）</sub>

**SWE-Trail：编码智能体训练的历史引导轨迹收集**<br>11月6日消息，现有轨迹收集方法导致数据冗余且存在训练测试不匹配。SWE-Trail利用历史轨迹指导后续收集，同时保持历史在智能体上下文之外。该方法通过执行候选动作选择有效路径，提升了学生模型的训练效果。<br><sub>（来源：[arXiv · 智能体](https://arxiv.org/abs/2611.02074)）</sub>

### 活动预告

**CVPR 2027 论文截稿**<br>11月17日，IEEE/CVF Conference on Computer Vision and Pattern Recognition（CVPR 2027，CCF-A 类，人工智能）论文提交截止时间为北京时间11月17日 19:59，摘要截止时间为11月11日 19:59。会议将于 June 20-25, 2027 在 Seattle, WA, United States 举行。<br><sub>（来源：[会议官网](https://cvpr.thecvf.com/Conferences/2027)）</sub>

<sub>标题和正文由 AI 根据原文整理（glm-4.7-flash），可能有误，请以原文为准。 俱乐部动态的统计日期为11月5日，数据来自[俱乐部开源仪表盘](https://osd.openatom.club/)。 会议截稿时间来自[CCFDDL](https://ccfddl.com/)，已换算成北京时间，请以会议官网为准。 有新闻线索欢迎[提交 Issue](https://github.com/game-life04/weekly-tech-agent/issues)。 本期由[每周科技收集 Agent](https://github.com/game-life04/weekly-tech-agent)于 2026-11-06 08:15（北京时间）自动生成。</sub>

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
