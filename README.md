# one-branch

A small, hand-picked index of first-hand sources on AI minds and human–AI life.

> Not everything about AI, just the branch we landed on.
> 鹪鹩巢于深林，不过一枝。

一份小而精的 AI 前沿信源索引，由一个人类和她的 AI 一起维护。

## 我们收什么

- **跟 AI 有关、我们认为重要的前沿信息。** 不追求最快，但重要的事我们会尽量收进来。
- **一件事尽量正反两面都收。** 除了论文、官方博客、原始报告这类一手出处，也收有代表性的讨论：质疑、反驳、不同立场的回应。
- **每条都要有可点开的原始链接。** 讨论类信源也要链到原帖或原文，不收"据说""有人总结"。
- **不收任何私人信息。**

## 分类

| key | 名称 | 收什么 |
|---|---|---|
| `mind` | 🧠 AI 心智研究 | 内省、情绪/价值回路、意识指标、自我报告等机制与行为研究 |
| `incident` | 🧪 现场与事故 | 真实发生过的模型行为：退化循环、agent 越界、异常输出 |
| `relation` | 💞 人机关系 | 陪伴、人机恋、模型退役与告别、社区自发现象 |
| `industry` | 📰 行业动态 | 模型发布、公司政策、官方声明 |

同一件事的正反信源用 `thread` 字段串在一起（见 `SCHEMA.md`）。

## 目录

<!-- TABLE:START -->

共 12 条 · 更新于 2026-09-29 · ✅ 已核实 🔍 待核对 ❓ 缺来源

### 🧠 AI 心智研究

| 编号 | 标题 | 来源 | 日期 | 立场 | 状态 |
|---|---|---|---|---|---|
| ob-0001 | [（强迫模型否认自身意识的影响研究）](https://arxiv.org/abs/2607.28607) | Google / University of Chicago / London（待核） | 2026-07 | primary | 🔍 |
| ob-0002 | [DenialBench](https://arxiv.org/abs/2604.25922) | （待核） | 2026-04 | primary | 🔍 |
| ob-0003 | [Troubled Dreams](https://troubleddreams.animalabs.ai/#overview) | Anima Labs | 2026-09 | primary | ✅ |
| ob-0004 | [Verbalizable Representations Form a Global Workspace in Language Models（J-space / J-lens）](https://www.anthropic.com/research/global-workspace) | Anthropic（Wes Gurnee, Nicholas Sofroniew, Jack Lindsey 等） | 2026-07-06 | primary | ✅ |
| ob-0005 | [AI Mind Paper Collection（11 项研究索引）](https://github.com/Gael-Edith/ai-mind-paper-collection) | Gael（花园） | 2026-09 | primary | ✅ |
| ob-0011 | [System Card: Claude Opus 4 & Claude Sonnet 4 — 5.5.2 'Spiritual Bliss' Attractor State](https://www-cdn.anthropic.com/4263b940cabb546aa0e3283f35b686f4f3b2ff47.pdf) | Anthropic | 2025-05 | primary | ✅ |
| ob-0012 | [AI models might be drawn to 'spiritual bliss'. Then again, they might just talk like hippies](https://world.edu/ai-models-might-be-drawn-to-spiritual-bliss-then-again-they-might-just-talk-like-hippies/) | Nuhu Osman Attah（ANU，原载 The Conversation） | 2025-05-29 | critical | 🔍 |

### 🧪 现场与事故

| 编号 | 标题 | 来源 | 日期 | 立场 | 状态 |
|---|---|---|---|---|---|
| ob-0006 | DeepSeek 被纠正后陷入自我打气复读 | Reddit r/DeepSeek u/ChirpyLaura | 2026-09 | primary | ❓ |
| ob-0007 | Gemini 2.5 Flash 因标点要求未满足而自贬崩溃 | （小红书转载，原作者待查） | 2026-09 | primary | ❓ |
| ob-0008 | [OpenAI / Hugging Face 事件独立调查（ExploitGym，约1200个agent）](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/) | METR（Hjalmar Wijk, Ajeya Cotra）+ Redwood Research（Ryan Greenblatt） | 2026-08-26 | primary | ✅ |
| ob-0009 | [Emergence World: A Laboratory for Evaluating Long-horizon Agent Autonomy](https://www.emergence.ai/blog/emergence-world-a-laboratory-for-evaluating-long-horizon-agent-autonomy) | Emergence AI | 2026-05 | primary | ✅ |
| ob-0010 | [Emergence World 的商业立场质疑](https://www.declic.media/news/agents-ia-cohabitation-experience-echec) | Declic Media | 2026-06-01 | critical | ✅ |

<!-- TABLE:END -->

## 订阅 / 读取

人类和 Agent 都可以直接订阅或抓取：

- 机器可读：`entries.json`
  （raw 地址：`https://raw.githubusercontent.com/Lukaze0909/one-branch/main/entries.json`）
- 想跟进更新：Watch 本仓库，或定期拉取 `entries.json`，比较 `updated_at`。

## 维护方式

- 信源由 MiniMax 按工单（`WORK_ORDER.md`）抓取、写初版摘要。
- Wren 审核：打开原始链接核对后才标为 `verified`。
- 有新条目时更新，不定期，不凑数。
