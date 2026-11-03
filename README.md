# 每周科技收集 Agent

[![Daily digest](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml)
[![CI](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

每天早上整理 AI 与开源动态，参照《CCF开源快讯》的体例出一期「每日快讯」，8:30 推送到俱乐部 QQ 群；每周一再出一期「每周快讯」。全部由程序自动生成，内容就放在这个仓库里，打开就能看。

- **订阅**：[RSS 订阅源](https://raw.githubusercontent.com/game-life04/weekly-tech-agent/main/feed.xml)；或者在本仓库点 **Watch → Custom → Releases**，每周快讯出刊时 GitHub 会发邮件通知你。
- **投稿**：欢迎推荐值得一看的文章、开源项目、活动和俱乐部动态，请[提交 issue](https://github.com/game-life04/weekly-tech-agent/issues/new?template=submission.md)。
- **往期**：[每周快讯](weekly/README.md) · [每日快讯和日报](daily/README.md)

<!-- wta:latest:start -->

## 每日快讯 · 11.03（周二）

> 今日 AI 与开源要闻 **12** 条，3 分钟速读。<br>
> [单独打开](daily/2026/2026-11-03-kuaixun.md) · [公众号排版版](daily/2026/2026-11-03-kuaixun.html) · [完整日报（含热度和原题）](daily/2026/2026-11-03.md) · [往期日报](daily/README.md)

<details>
<summary>群消息文字版（点开后，点代码框右上角的按钮整段复制）</summary>

```text
【每日科技快讯】11月3日 周二
今日 AI 与开源要闻 12 条，3 分钟速读

【海外动态】
1. OpenAI 构建可扩展的 Git 后端 Pando
→ OpenAI 为 Codex 开发了一个兼容 Git 的后端 Pando，以应对大规模开发需求。
2. 推出 Grid Protectors 计划
→ OpenAI 将与公用事业公司合作，确保算力中心支持电网可靠性并保护消费者电费。

【开源项目】
3. agent-desktop：AI 智能体的计算机使用 CLI
→ vercel-labs/agent-desktop 提供计算机使用命令行接口，供 AI 智能体操作。
4. Handy：免费开源离线语音转文字应用
→ Handy 是一款免费、开源且可扩展的离线语音转文字应用。
5. OmniRoute：统一接入 1400+ 模型
→ OmniRoute 提供 MIT 许可的 AI 网关，统一端点接入 375 个提供商的 1400+ 模型。
6. BLA：保护二进制文件和 WebAssembly 免受 AI 反编译攻击
→ BLA 是一款对抗性防御盾，保护二进制文件、Electron 应用和 WebAssembly 免受 AI 反编译攻击。
7. last30days-skill：跨平台研究并生成摘要
→ 该技能可跨 Reddit、X、YouTube 等平台研究并生成摘要。

【学术前沿】
8. Astra：直接读写权重优化 Qwen
→ GPT-6 Astra 能直接读取和修改神经网络权重，无需梯度即可优化模型。
9. R^2Orch：递归自我博弈编排范式
→ R^2Orch提出通过技能内化循环中的自我博弈来改进智能体编排，在问答、数学和代码任务上表现优越。
10. WebAnything：全自动化智能体环境框架
→ WebAnything框架通过探索者-构建器和验证器模块，从真实URL构建可重用的源 grounded Web 环境，支持244个网站工件。
11. DAMI：门控线性注意力中增强长上下文检索的双轴记忆初始化
→ 论文提出双轴记忆初始化方法，通过联合配置门控参数优化记忆保留，在GDN、KDA、Mamba-2等模型上将平均检索准确率提高了5.29到16.71个百分点。

【产业纵横】
12. Anthropic 第三季度营收 170 亿美元
→ Anthropic 公布修订后的 S-1 文件，前三季度营收 332.4 亿美元。

【活动预告】
· 11月5日 RECOMB 2027 论文截稿

完整版（含原文链接）：https://github.com/game-life04/weekly-tech-agent/blob/main/daily/2026/2026-11-03-kuaixun.md
标题和要点由 AI 整理，可能有误，请以原文为准。
```

</details>

### 今日快讯

#### 海外动态

**OpenAI 构建可扩展的 Git 后端 Pando**<br>11月2日，OpenAI 为 Codex 开发了一个兼容 Git 的后端 Pando，以应对大规模开发需求。<br><sub>（来源：[OpenAI](https://openai.com/index/scaling-git-at-openai)）</sub>

**推出 Grid Protectors 计划**<br>11月2日，OpenAI 将与公用事业公司合作，确保算力中心支持电网可靠性并保护消费者电费。<br><sub>（来源：[OpenAI](https://openai.com/index/grid-protectors-program)）</sub>

#### 开源项目

**agent-desktop：AI 智能体的计算机使用 CLI**<br>11月3日消息，vercel-labs/agent-desktop 提供计算机使用命令行接口，供 AI 智能体操作。<br><sub>（来源：[GitHub Trending](https://github.com/vercel-labs/agent-desktop)）</sub>

**Handy：免费开源离线语音转文字应用**<br>11月3日消息，Handy 是一款免费、开源且可扩展的离线语音转文字应用。<br><sub>（来源：[GitHub Trending](https://github.com/cjpais/Handy)）</sub>

**OmniRoute：统一接入 1400+ 模型**<br>11月3日消息，OmniRoute 提供 MIT 许可的 AI 网关，统一端点接入 375 个提供商的 1400+ 模型。<br><sub>（来源：[GitHub Trending](https://github.com/cheaper-inference/OmniRoute)）</sub>

**BLA：保护二进制文件和 WebAssembly 免受 AI 反编译攻击**<br>11月3日消息，BLA 是一款对抗性防御盾，保护二进制文件、Electron 应用和 WebAssembly 免受 AI 反编译攻击。<br><sub>（来源：[GitHub 新项目](https://github.com/qybaihe/bla)）</sub>

**last30days-skill：跨平台研究并生成摘要**<br>11月3日消息，该技能可跨 Reddit、X、YouTube 等平台研究并生成摘要。<br><sub>（来源：[GitHub Trending](https://github.com/mvanhorn/last30days-skill)）</sub>

#### 学术前沿

**Astra：直接读写权重优化 Qwen**<br>11月3日，GPT-6 Astra 能直接读取和修改神经网络权重，无需梯度即可优化模型。<br><sub>（来源：[Hacker News](https://rikiyat.github.io/blog/weight-space-programming/)）</sub>

**R^2Orch：递归自我博弈编排范式**<br>11月3日消息，R^2Orch提出通过技能内化循环中的自我博弈来改进智能体编排，在问答、数学和代码任务上表现优越。<br><sub>（来源：[Hugging Face 热门论文](https://arxiv.org/abs/2610.22740)）</sub>

**WebAnything：全自动化智能体环境框架**<br>11月3日消息，WebAnything框架通过探索者-构建器和验证器模块，从真实URL构建可重用的源 grounded Web 环境，支持244个网站工件。<br><sub>（来源：[arXiv · 智能体](https://arxiv.org/abs/2610.37786)）</sub>

**DAMI：门控线性注意力中增强长上下文检索的双轴记忆初始化**<br>11月3日消息，论文提出双轴记忆初始化方法，通过联合配置门控参数优化记忆保留，在GDN、KDA、Mamba-2等模型上将平均检索准确率提高了5.29到16.71个百分点。<br><sub>（来源：[arXiv · 长上下文与检索](https://arxiv.org/abs/2610.41994)）</sub>

#### 产业纵横

**Anthropic 第三季度营收 170 亿美元**<br>11月2日，Anthropic 公布修订后的 S-1 文件，前三季度营收 332.4 亿美元。<br><sub>（来源：[Hacker News](https://www.cnbc.com/2026/11/02/anthropic-ant-s-1-quarter-financials.html)）</sub>

### 活动预告

**RECOMB 2027 论文截稿**<br>11月5日，International Conference on Research inComputational Molecular Biology（RECOMB 2027，CCF-B 类，交叉/综合/新兴）论文提交截止时间为北京时间11月5日 19:59，摘要截止时间为10月29日 19:59。会议将于 May 17-20, 2027 在 Toronto, Canada 举行。<br><sub>（来源：[会议官网](https://recomb.org/recomb2027/)）</sub>

<sub>标题和正文由 AI 根据原文整理（glm-4.7-flash），可能有误，请以原文为准。 会议截稿时间来自[CCFDDL](https://ccfddl.com/)，已换算成北京时间，请以会议官网为准。 有新闻线索欢迎[提交 Issue](https://github.com/game-life04/weekly-tech-agent/issues)。 本期由[每周科技收集 Agent](https://github.com/game-life04/weekly-tech-agent)于 2026-11-03 11:06（北京时间）自动生成。</sub>

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
