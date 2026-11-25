# 每周科技收集 Agent

[![Daily digest](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml)
[![CI](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

每天早上整理 AI 与开源动态，参照《CCF开源快讯》的体例出一期「每日快讯」，8:30 推送到俱乐部 QQ 群；每周一再出一期「每周快讯」。全部由程序自动生成，内容就放在这个仓库里，打开就能看。

- **订阅**：[RSS 订阅源](https://raw.githubusercontent.com/game-life04/weekly-tech-agent/main/feed.xml)；或者在本仓库点 **Watch → Custom → Releases**，每周快讯出刊时 GitHub 会发邮件通知你。
- **投稿**：欢迎推荐值得一看的文章、开源项目、活动和俱乐部动态，请[提交 issue](https://github.com/game-life04/weekly-tech-agent/issues/new?template=submission.md)。
- **往期**：[每周快讯](weekly/README.md) · [每日快讯和日报](daily/README.md)

<!-- wta:latest:start -->

## 每日快讯 · 11.25（周三）

> 今日 AI 与开源要闻 **17** 条，3 分钟速读。<br>
> [单独打开](daily/2026/2026-11-25-kuaixun.md) · [公众号排版版](daily/2026/2026-11-25-kuaixun.html) · [完整日报（含热度和原题）](daily/2026/2026-11-25.md) · [往期日报](daily/README.md)

<details>
<summary>群消息文字版（点开后，点代码框右上角的按钮整段复制）</summary>

```text
【每日科技快讯】11月25日 周三
今日 AI 与开源要闻 17 条，3 分钟速读

【俱乐部动态】
1. 开放原子开源俱乐部合并 1 个 PR、提交 1 次
2. AtomGit-Mobile4Android 合并 1 个 PR
3. AtomGit-mobile4Harmony 新增 1 个 PR

【国内动态】
4. 智谱刚刚发了GLM-5.4，全新架构的那种！网友直呼：超过预期
→ 纯代码手搓了一个MV！

【海外动态】
5. GPT-6 models demonstrate intrinsic protein-design capabilities
→ GPT-6 models design protein structures and sequences using reasoning and code. Lab tests found evidence of binding acro…
6. Searching for distant planets with Astra
→ See how two amateur astronomers used Codex and Astra to find potential exoplanets in public data from NASA’s Kepler and…
7. Three LLM inflection points in twelve months
→ I gave a keynote at the AI Engineer Code Summit a couple of weeks ago, constructed around the idea that there have been…
8. Claude Opus 5.6灰测效果来了
→ 整体效率大约是此前Opus版本的2到3倍。

【开源项目】
9. vLLM Day-0 Support for ERNIE 5.5 Flash Preview: Plugin Deployment and E2E Infer…
→ vLLM supports Baidu's ERNIE 5.5 Flash Preview on day 0 through the vLLM-ERNIE plugin on the released vllm==0.32.0 wheel…
10. The Agent Lake
→ An agent lake holds every trace your agents produce. See how LangSmith finds high-signal traces at scale and turns them…
11. INK-Q/agy-fast
→ Non-invasive MCP accelerator plugin for Google Antigravity (CLI/Desktop/IDE): cuts LLM turns (-34%), token quota (-31%)…
12. pierridotite/mobile-agent-testers
→ 20 AI testers on 20 different phones, in parallel, on GitHub's free runners: Claude Code agents on iOS Simulators and A…
13. SulphurAI/Sulphur-3
→ 许可证 other。

【学术前沿】
14. WeMM-Ecom: Advancing Multimodal Content Understanding for WeChat E-Commerce
→ We present WeMM-Ecom, a family of multimodal large language models that deliver frontier e-commerce capabilities while…
15. What Makes Good Data for Training Coding Agents? A Systematic Study on SWE-Gym
→ Reinforcement learning (RL) trains coding agents on software tasks whose hidden tests decide the reward, yet task colle…
16. Nemotron-Labs-VisualCreation: Pixel as Code for Agentic Visual Creation
→ Visual creation demands expressive imagery together with precise control over text, layout, and structure. We introduce…
17. Unjamming Deferrals: Supporting Students Through JAMN Bot, a Mobile RAG-Grounde…
→ In some educational institutions, workflows such as the exam deferral process can be slow, inconvenient, and inconsiste…

【活动预告】
· 12月3日 EuroVis 2027 论文截稿

完整版（含原文链接）：https://github.com/game-life04/weekly-tech-agent/blob/main/daily/2026/2026-11-25-kuaixun.md
```

</details>

### 今日快讯

#### 俱乐部动态

**开放原子开源俱乐部合并 1 个 PR、提交 1 次**<br>11月24日，据俱乐部开源仪表盘统计，开放原子开源俱乐部跟踪的 122 个仓库中有 3 个有人参与开发，共新增 PR 4 个、合并 1 个，提交 1 次，新增代码 1500 行、删除 130 行，3 位贡献者参与，其中 1 位是第一次贡献。<br><sub>（来源：[俱乐部开源仪表盘](https://osd.openatom.club/)）</sub>

**AtomGit-Mobile4Android 合并 1 个 PR**<br>11月24日，Agent SIG的 AtomGit-Mobile4Android 仓库新增 PR 1 个、合并 1 个、提交 1 次、新增代码 1500 行，1 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/AtomGit-Mobile4Android)）</sub>

**AtomGit-mobile4Harmony 新增 1 个 PR**<br>11月24日，Agent SIG的 AtomGit-mobile4Harmony 仓库新增 PR 1 个，1 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/AtomGit-mobile4Harmony)）</sub>

#### 国内动态

**智谱刚刚发了GLM-5.4，全新架构的那种！网友直呼：超过预期**<br>11月24日，纯代码手搓了一个MV！<br><sub>（来源：[量子位](https://www.qbitai.com/2026/11/512423.html)）</sub>

#### 海外动态

**GPT-6 models demonstrate intrinsic protein-design capabilities**<br>11月24日，GPT-6 models design protein structures and sequences using reasoning and code. Lab tests found evidence of binding acro…<br><sub>（来源：[OpenAI](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities)）</sub>

**Searching for distant planets with Astra**<br>11月24日，See how two amateur astronomers used Codex and Astra to find potential exoplanets in public data from NASA’s Kepler and…<br><sub>（来源：[OpenAI](https://openai.com/index/searching-for-distant-planets-with-astra)）</sub>

**Three LLM inflection points in twelve months**<br>11月25日，I gave a keynote at the AI Engineer Code Summit a couple of weeks ago, constructed around the idea that there have been…<br><sub>（来源：[Simon Willison](https://simonwillison.net/2026/Nov/24/llm-inflection-points/)）</sub>

**Claude Opus 5.6灰测效果来了**<br>11月25日，整体效率大约是此前Opus版本的2到3倍。<br><sub>（来源：[量子位](https://www.qbitai.com/2026/11/512478.html)）</sub>

#### 开源项目

**vLLM Day-0 Support for ERNIE 5.5 Flash Preview: Plugin Deployment and E2E Infer…**<br>11月24日，vLLM supports Baidu's ERNIE 5.5 Flash Preview on day 0 through the vLLM-ERNIE plugin on the released vllm==0.32.0 wheel…<br><sub>（来源：[vLLM 博客](https://vllm.ai/blog/2026-11-24-ernie-5-5-flash-preview)）</sub>

**The Agent Lake**<br>11月25日，An agent lake holds every trace your agents produce. See how LangSmith finds high-signal traces at scale and turns them…<br><sub>（来源：[LangChain 博客](https://www.langchain.com/blog/the-agent-lake)）</sub>

**INK-Q/agy-fast**<br>11月25日消息，Non-invasive MCP accelerator plugin for Google Antigravity (CLI/Desktop/IDE): cuts LLM turns (-34%), token quota (-31%)…<br><sub>（来源：[GitHub 新项目](https://github.com/INK-Q/agy-fast)）</sub>

**pierridotite/mobile-agent-testers**<br>11月25日消息，20 AI testers on 20 different phones, in parallel, on GitHub's free runners: Claude Code agents on iOS Simulators and A…<br><sub>（来源：[GitHub 新项目](https://github.com/pierridotite/mobile-agent-testers)）</sub>

**SulphurAI/Sulphur-3**<br>11月25日消息，许可证 other。<br><sub>（来源：[Hugging Face 热门模型](https://huggingface.co/SulphurAI/Sulphur-3)）</sub>

#### 学术前沿

**WeMM-Ecom: Advancing Multimodal Content Understanding for WeChat E-Commerce**<br>11月23日，We present WeMM-Ecom, a family of multimodal large language models that deliver frontier e-commerce capabilities while…<br><sub>（来源：[Hugging Face 热门论文](https://arxiv.org/abs/2611.30662)）</sub>

**What Makes Good Data for Training Coding Agents? A Systematic Study on SWE-Gym**<br>11月23日，Reinforcement learning (RL) trains coding agents on software tasks whose hidden tests decide the reward, yet task colle…<br><sub>（来源：[arXiv · 智能体](https://arxiv.org/abs/2611.30207)）</sub>

**Nemotron-Labs-VisualCreation: Pixel as Code for Agentic Visual Creation**<br>11月24日，Visual creation demands expressive imagery together with precise control over text, layout, and structure. We introduce…<br><sub>（来源：[arXiv · 智能体](https://arxiv.org/abs/2611.31358)）</sub>

**Unjamming Deferrals: Supporting Students Through JAMN Bot, a Mobile RAG-Grounde…**<br>11月24日，In some educational institutions, workflows such as the exam deferral process can be slow, inconvenient, and inconsiste…<br><sub>（来源：[arXiv · 长上下文与检索](https://arxiv.org/abs/2611.32266)）</sub>

### 活动预告

**EuroVis 2027 论文截稿**<br>12月3日，Eurographics Conference on Visualization（EuroVis 2027，CCF-B 类，图形学与多媒体）Full papers的论文提交截止时间为北京时间12月3日 19:59，摘要截止时间为11月24日 19:59。会议将于 May 31-June 4, 2027 在 Stuttgart, Germany 举行。<br><sub>（来源：[会议官网](https://eurovis27.github.io/web/)）</sub>

<sub>俱乐部动态的统计日期为11月24日，数据来自[俱乐部开源仪表盘](https://osd.openatom.club/)。 会议截稿时间来自[CCFDDL](https://ccfddl.com/)，已换算成北京时间，请以会议官网为准。 有新闻线索欢迎[提交 Issue](https://github.com/game-life04/weekly-tech-agent/issues)。 本期由[每周科技收集 Agent](https://github.com/game-life04/weekly-tech-agent)于 2026-11-25 11:01（北京时间）自动生成。</sub>

## 每周快讯 第 6 期 · 11.16–11.22

> 本期头条：OpenAI发布GPT-6.2 Astra和Sol模型<br>
> 上周 AI 与开源要闻 **27** 条，5 分钟速读。<br>
> [阅读全文](weekly/2026-W47.md) · [公众号排版版](weekly/2026-W47.html) · [往期快讯](weekly/README.md)

**俱乐部动态**<br>
✨ [开放原子开源俱乐部一周合并 16 个 PR、提交 28 次](https://osd.openatom.club/)<br>
✨ [AtomGit-mobile4Harmony 一周合并 8 个 PR](https://github.com/hust-open-atom-club/AtomGit-mobile4Harmony)<br>
✨ [AtomGit-Mobile4Android 一周合并 4 个 PR](https://github.com/hust-open-atom-club/AtomGit-Mobile4Android)<br>
✨ [Open-Source-Dashboard 一周合并 2 个 PR](https://github.com/hust-open-atom-club/Open-Source-Dashboard)

**国内动态**<br>
✨ [阿里通义千问发布 Qwen4-Max 模型](https://qwen.ai/blog?id=qwen4-max)<br>
✨ [DeepSeek 开放全家桶应用 API](https://aiera.com.cn/2026/11/15/other/admin/123914/%e5%88%9a%e5%88%9a%ef%bc%8cdeepseek%e5%85%a8%e5%ae%b6%e6%a1%b6api%e6%ad%a3%e5%bc%8f%e5%bc%80%e6%94%be%ef%bc%81%e4%bd%a0%e4%b9%9f%e8%83%bd%e9%80%a0%e4%b8%80%e4%b8%aadeepseek%e4%ba%86/)<br>
✨ [华为云上线 openPangu-2.1-Pro 开源模型](https://www.ithome.com/1/027/450.htm)<br>
✨ [华为云发布 CloudRobo-WM1.2 具身世界模型](https://zhidx.com/p/610813.html)

**海外动态**<br>
✨ [OpenAI扩大对科学家的AI访问权限](https://openai.com/index/expanding-chatgpt-for-academic-researchers)<br>
✨ [OpenAI发布GPT-6.2 Astra和Sol模型](https://openai.com/index/introducing-gpt-6-2-astra-sol)<br>
✨ [Google DeepMind上线Genie 4](https://deepmind.google/blog/genie-4-is-now-available/)<br>
✨ [Google DeepMind发布Gemini 4 Neon](https://deepmind.google/blog/introducing-gemini-4-neon/)

**开源项目**<br>
✨ [vLLM 发布 v0.34.0 版本](https://github.com/vllm-project/vllm/releases/tag/v0.34.0)<br>
✨ [Claude-BugHunter 技能包](https://github.com/elementalsouls/Claude-BugHunter)<br>
✨ [Inkling 2 Mini：可在笔记本运行的模型](https://thinkingmachines.ai/news/inkling-2-mini/)<br>
✨ [autoclip 开源视频剪辑工具](https://github.com/zhouxiaoka/autoclip)

**学术前沿**<br>
✨ [科学家如何使用ChatGPT进行研究](https://openai.com/index/science-at-the-frontier)<br>
✨ [OpenAI分析编码智能体如何加速AI研究](https://openai.com/index/research-acceleration-jagged-frontier)<br>
✨ [语言模型可自行重写权重](https://arxiv.org/abs/2611.21885)

**产业纵横**<br>
✨ [KPMG 使用 AI 代理进行审计](https://europeanbusinessmagazine.com/ai-agents-better-questions-kpmg/)<br>
✨ [Anthropic 定价首次公开募股](https://www.anthropic.com/news/anthropic-prices-initial-public-offering)<br>
✨ [Anthropic 上市次日股价下跌](https://www.theguardian.com/business/2026/nov/20/global-stock-markets-slump-anthropic-ipo-ai-sell-off)

**活动预告**<br>
✨ [EuroVis 2027 论文截稿](https://eurovis27.github.io/web/)<br>
✨ [AAMAS 2027 论文截稿](https://warwick.ac.uk/fac/sci/dcs/aamas2027/)<br>
✨ [ICAPS 2027 论文截稿](https://icaps27.icaps-conference.org/)<br>
✨ [COLING 2027 论文截稿](https://2027.coling-iccl.org/)<br>
✨ [NAACL 2027 论文截稿](https://2027.naacl.org/)

<!-- wta:latest:end -->

---

## 关于这个项目

内容由程序自动抓取、去重、打分，再由大模型分栏和改写（页面上都有标注，可能有误，请以原文为准），GitHub Actions 每天定时运行，不需要服务器。收集哪些来源、怎么工作、怎么在本地运行和加一个信息来源，见 [docs/about.md](docs/about.md)；参与贡献见 [CONTRIBUTING.md](CONTRIBUTING.md)。

### 致谢

设计上参考了 [Horizon](https://github.com/Thysrael/Horizon)、[agents-radar](https://github.com/duanyytop/agents-radar) 和 [AIHOT](https://github.com/KKKKhazix/AIHOT)。每周快讯的体例参照 CCF 开源发展技术委员会的《CCF开源快讯》，俱乐部数据来自俱乐部的 [Open-Source-Dashboard](https://github.com/hust-open-atom-club/Open-Source-Dashboard)，会议截稿数据来自 [ccf-deadlines](https://github.com/ccfddl/ccf-deadlines)。

### 许可证

[MIT](LICENSE)
