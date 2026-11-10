# 每周科技收集 Agent

[![Daily digest](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/daily.yml)
[![CI](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/game-life04/weekly-tech-agent/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

每天早上整理 AI 与开源动态，参照《CCF开源快讯》的体例出一期「每日快讯」，8:30 推送到俱乐部 QQ 群；每周一再出一期「每周快讯」。全部由程序自动生成，内容就放在这个仓库里，打开就能看。

- **订阅**：[RSS 订阅源](https://raw.githubusercontent.com/game-life04/weekly-tech-agent/main/feed.xml)；或者在本仓库点 **Watch → Custom → Releases**，每周快讯出刊时 GitHub 会发邮件通知你。
- **投稿**：欢迎推荐值得一看的文章、开源项目、活动和俱乐部动态，请[提交 issue](https://github.com/game-life04/weekly-tech-agent/issues/new?template=submission.md)。
- **往期**：[每周快讯](weekly/README.md) · [每日快讯和日报](daily/README.md)

<!-- wta:latest:start -->

## 每日快讯 · 11.10（周二）

> 今日 AI 与开源要闻 **16** 条，3 分钟速读。<br>
> [单独打开](daily/2026/2026-11-10-kuaixun.md) · [公众号排版版](daily/2026/2026-11-10-kuaixun.html) · [完整日报（含热度和原题）](daily/2026/2026-11-10.md) · [往期日报](daily/README.md)

<details>
<summary>群消息文字版（点开后，点代码框右上角的按钮整段复制）</summary>

```text
【每日科技快讯】11月10日 周二
今日 AI 与开源要闻 16 条，3 分钟速读

【俱乐部动态】
1. 开放原子开源俱乐部合并 2 个 PR、提交 3 次
2. pwnhustcollege_skill 合并 1 个 PR
3. pwn.hust.college 合并 1 个 PR

【国内动态】
4. 赶在IPO前，Claude最强模型空降！宾大教授感慨“几乎达到AGI”
→ Anthropic 发布两款新模型，在基准测试中表现优异，已上线云服务。

【海外动态】
5. Claude Fable 5.2 和 Claude Mythos 5.2 发布
→ Anthropic推出Claude Fable 5.2和Claude Mythos 5.2两款新模型，在编程、金融和科学领域表现优异。
6. OpenAI推出Control Room管理系统
→ OpenAI发布了用于追踪和停止研究基础设施中模型工作负载的中央系统。
7. CodeRabbit利用OpenAI模型提升开发效率
→ CodeRabbit使用OpenAI模型治理AI生成代码，使团队交付量提升20倍。

【开源项目】
8. MuJoCo：通用多关节动力学物理模拟器
→ MuJoCo 是一个通用的多关节动力学物理模拟器，用于模拟多关节动力学与接触。
9. daily_stock_analysis：LLM驱动的多市场股票分析系统
→ LLM驱动的多市场股票分析系统支持多源行情、实时新闻和自动推送，可零成本定时运行。
10. Astryx：专为智能体准备的开源设计系统
→ Astryx 是一个完全可定制且专为智能体准备的开源设计系统。
11. Anthropic Claude 快速入门项目集合
→ Anthropic 提供的 Claude 快速入门项目集合，帮助开发者快速构建可部署应用。
12. pinky：让AI智能体使用你的手机
→ pinky 是一个让 AI 智能体使用你的手机，且你在循环中的开源项目。

【学术前沿】
13. 多轮强化学习在LLM智能体中的真实提升
→ 多轮强化学习在长任务上表现优异，但性能受交互预算限制。研究发现其优势集中在错误恢复和长时程韧性，而非单步决策质量。
14. PCBRouteAgent：PCB布线智能体
→ PCBRouteAgent利用多模态方法模拟人类工程师协调全局策略与局部执行，以解决复杂PCB布线问题。
15. BestRand：基准压缩方法
→ BestRand方法通过随机采样在高概率下表现良好，相比竞争方法将高误差风险降低50.2%。
16. LowRAM：KV缓存压缩
→ LowRAM通过值缓存摊销和跨层低秩键压缩实现高效压缩，在4倍压缩下实现5倍峰值解码吞吐量。

【活动预告】
· 11月17日 CVPR 2027 论文截稿

完整版（含原文链接）：https://github.com/game-life04/weekly-tech-agent/blob/main/daily/2026/2026-11-10-kuaixun.md
标题和要点由 AI 整理，可能有误，请以原文为准。
```

</details>

### 今日快讯

#### 俱乐部动态

**开放原子开源俱乐部合并 2 个 PR、提交 3 次**<br>11月9日，据俱乐部开源仪表盘统计，开放原子开源俱乐部跟踪的 122 个仓库中有 6 个有人参与开发，共新增 PR 6 个、合并 2 个，提交 3 次，新增代码 31 行、删除 0 行，3 位贡献者参与。<br><sub>（来源：[俱乐部开源仪表盘](https://osd.openatom.club/)）</sub>

**pwnhustcollege\_skill 合并 1 个 PR**<br>11月9日，pwn.hust.college SIG的 pwnhustcollege\_skill 仓库新增 PR 1 个、合并 1 个、提交 2 次、新增代码 31 行，1 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/pwnhustcollege_skill)）</sub>

**pwn.hust.college 合并 1 个 PR**<br>11月9日，pwn.hust.college SIG的 pwn.hust.college 仓库合并 1 个、提交 1 次，2 位贡献者参与。<br><sub>（来源：[GitHub](https://github.com/hust-open-atom-club/pwn.hust.college)）</sub>

#### 国内动态

**赶在IPO前，Claude最强模型空降！宾大教授感慨“几乎达到AGI”**<br>11月10日，Anthropic 发布两款新模型，在基准测试中表现优异，已上线云服务。<br><sub>（来源：[智东西](https://zhidx.com/p/608593.html)）</sub>

#### 海外动态

**Claude Fable 5.2 和 Claude Mythos 5.2 发布**<br>11月9日，Anthropic推出Claude Fable 5.2和Claude Mythos 5.2两款新模型，在编程、金融和科学领域表现优异。<br><sub>（来源：[Anthropic](https://www.anthropic.com/claude-fable-and-mythos-5-2)）</sub>

**OpenAI推出Control Room管理系统**<br>11月9日，OpenAI发布了用于追踪和停止研究基础设施中模型工作负载的中央系统。<br><sub>（来源：[OpenAI](https://openai.com/index/control-room)）</sub>

**CodeRabbit利用OpenAI模型提升开发效率**<br>11月9日，CodeRabbit使用OpenAI模型治理AI生成代码，使团队交付量提升20倍。<br><sub>（来源：[OpenAI](https://openai.com/index/coderabbit-codex-daybreak)）</sub>

#### 开源项目

**MuJoCo：通用多关节动力学物理模拟器**<br>11月10日消息，MuJoCo 是一个通用的多关节动力学物理模拟器，用于模拟多关节动力学与接触。<br><sub>（来源：[GitHub Trending](https://github.com/google-deepmind/mujoco)）</sub>

**daily\_stock\_analysis：LLM驱动的多市场股票分析系统**<br>11月10日消息，LLM驱动的多市场股票分析系统支持多源行情、实时新闻和自动推送，可零成本定时运行。<br><sub>（来源：[GitHub Trending](https://github.com/ZhuLinsen/daily_stock_analysis)）</sub>

**Astryx：专为智能体准备的开源设计系统**<br>11月10日消息，Astryx 是一个完全可定制且专为智能体准备的开源设计系统。<br><sub>（来源：[GitHub Trending](https://github.com/meta/astryx)）</sub>

**Anthropic Claude 快速入门项目集合**<br>11月10日消息，Anthropic 提供的 Claude 快速入门项目集合，帮助开发者快速构建可部署应用。<br><sub>（来源：[GitHub Trending](https://github.com/anthropics/claude-quickstarts)）</sub>

**pinky：让AI智能体使用你的手机**<br>11月10日消息，pinky 是一个让 AI 智能体使用你的手机，且你在循环中的开源项目。<br><sub>（来源：[GitHub 新项目](https://github.com/DIYgod/pinky)）</sub>

#### 学术前沿

**多轮强化学习在LLM智能体中的真实提升**<br>11月10日消息，多轮强化学习在长任务上表现优异，但性能受交互预算限制。研究发现其优势集中在错误恢复和长时程韧性，而非单步决策质量。<br><sub>（来源：[arXiv · 智能体](https://arxiv.org/abs/2611.06483)）</sub>

**PCBRouteAgent：PCB布线智能体**<br>11月10日消息，PCBRouteAgent利用多模态方法模拟人类工程师协调全局策略与局部执行，以解决复杂PCB布线问题。<br><sub>（来源：[arXiv · 智能体](https://arxiv.org/abs/2611.08175)）</sub>

**BestRand：基准压缩方法**<br>11月10日消息，BestRand方法通过随机采样在高概率下表现良好，相比竞争方法将高误差风险降低50.2%。<br><sub>（来源：[Hugging Face 热门论文](https://arxiv.org/abs/2611.00883)）</sub>

**LowRAM：KV缓存压缩**<br>11月10日消息，LowRAM通过值缓存摊销和跨层低秩键压缩实现高效压缩，在4倍压缩下实现5倍峰值解码吞吐量。<br><sub>（来源：[arXiv · 高效推理](https://arxiv.org/abs/2611.07025)）</sub>

### 活动预告

**CVPR 2027 论文截稿**<br>11月17日，IEEE/CVF Conference on Computer Vision and Pattern Recognition（CVPR 2027，CCF-A 类，人工智能）论文提交截止时间为北京时间11月17日 19:59，摘要截止时间为11月11日 19:59。会议将于 June 20-25, 2027 在 Seattle, WA, United States 举行。<br><sub>（来源：[会议官网](https://cvpr.thecvf.com/Conferences/2027)）</sub>

<sub>标题和正文由 AI 根据原文整理（glm-4.7-flash），可能有误，请以原文为准。 俱乐部动态的统计日期为11月9日，数据来自[俱乐部开源仪表盘](https://osd.openatom.club/)。 会议截稿时间来自[CCFDDL](https://ccfddl.com/)，已换算成北京时间，请以会议官网为准。 有新闻线索欢迎[提交 Issue](https://github.com/game-life04/weekly-tech-agent/issues)。 本期由[每周科技收集 Agent](https://github.com/game-life04/weekly-tech-agent)于 2026-11-10 16:25（北京时间）自动生成。</sub>

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
