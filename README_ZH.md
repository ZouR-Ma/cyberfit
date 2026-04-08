<div align="center">

# CyberFit 🦾

> *"你的同事把屎山甩给你然后跑了，你的前任把你的心搞烂了然后走了——但他们都忘了一件事：最后坐在工位上烂掉的那个人，不该是你。"*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3](https://img.shields.io/badge/Python-3-blue.svg)](https://python.org)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)

**[English](README.md) | 中文**

<br>

你的同事把祖传屎山甩给你，然后跳槽涨薪 50% 了？<br>
你的前任半夜三点还在给你发消息折磨你，白天你顶着黑眼圈继续写代码？<br>
你接手了所有烂摊子，连口水都来不及喝？<br>
你坐在工位上从早到晚，脊椎侧弯、腱鞘炎、颈椎病，全是你一个人扛？<br>
你的身体一天不如一天，但你连站起来走两步的意识都快没了？<br>

**到头了。确实到头了。再不动，你的身体就真到头了。**

<br>

这些烂摊子毁掉了你的时间、你的精力、你的热情<br>
但它们**不该**连你的身体也一起毁掉<br>
CyberFit 存在的意义只有一个——<br>
**在这堆烂摊子把你的身体也搞烂之前，保住你唯一不可替换的硬件**

<br>

[安装](#安装) · [使用](#使用) · [运动库](#运动分类) · [成就系统](#等级系统)

</div>

---

## 这不是一个健身 App

健身 App 有几万个。它们都假设你有时间，有心情，有那个闲工夫。

但你没有。

你正在被同事甩锅、被前任的消息搞得心神不宁、被 deadline 追杀、被无尽的需求淹没。你坐在工位上 12 个小时，从颈椎痛到腰椎，从腰椎痛到灵魂。你不需要什么「30 天马甲线计划」——你需要的是**在被这堆破事压垮之前，有什么东西拉你一把**。

CyberFit 就是那个东西。

它不会说「加油你可以的」这种废话。它会用夜之城义体维护 AI 的身份告诉你：**「你的碳基硬件过热了，再不冷却就要报废。现在给我站起来。」**

---

## 凭什么是赛博朋克

因为程序员的处境**就是**赛博朋克。

在赛博朋克的世界里，人被当作零件用到报废为止。听着耳熟吗？你的工位不就是那个一平米的赛博格棺材吗？你的需求列表不就是义体负载吗？你接手的祖传代码不就是上一代佣兵留下的烂摊子吗？

唯一的区别是——赛博朋克里的人至少还知道反抗。

**深蹲叫「液压腿部升级」，平板支撑叫「装甲框架强化」，眼保健操叫「光学植入体重置」。** 不是因为中二，是因为你值得被认真对待。你不是在做工间操——你是在维护自己最重要的硬件。

---

## 功能特性

| 功能 | 说明 |
|------|------|
| **义体维护提醒** | 久坐超时自动警告，不给你烂在工位上的机会 |
| **赛博朋克运动库** | 20+ 个动作，每个都有赛博朋克命名，做运动不丢人 |
| **健身计划生成** | 根据你的等级和身体状态自动匹配，不用动脑 |
| **训练打卡系统** | 每次训练积累 XP，比写 JIRA 有成就感多了 |
| **成就系统** | 15 个赛博朋克成就，从「觉醒」到「赛博之神」 |
| **等级称号** | 从「流浪者」升到「夜之城传奇」，比任何 title 都靠谱 |
| **体态检查** | 用赛博朋克扫描仪告诉你坐姿有多烂 |
| **ASCII Art 仪表盘** | 终端里的赛博朋克 UI，比你们的管理后台好看 |

---

## 安装

### Claude Code（推荐）

```bash
# 安装到全局（所有项目都能用）
git clone git@github.com:ZouR-Ma/cyberfit.git ~/.claude/skills/cyberfit

# 或安装到当前项目
mkdir -p .claude/skills
git clone git@github.com:ZouR-Ma/cyberfit.git .claude/skills/cyberfit
```

---

## 使用

### 斜杠命令

在 Claude Code 里直接输入：

| 命令 | 说明 |
|------|------|
| `/cyberfit` | 主入口，显示你的义体仪表盘 |
| `/cyberfit-break` | **站起来。** 获取冷却协议和微运动指令 |
| `/cyberfit-plan` | 生成今日义体维护蓝图 |
| `/cyberfit-log <运动>` | 打卡记录，拿经验值 |
| `/cyberfit-status` | 完整诊断面板 |
| `/cyberfit-posture` | 扫描你那可怜的坐姿 |

### CLI 命令

```bash
python3 scripts/cli.py init            # 启动义体维护系统
python3 scripts/cli.py status          # 仪表盘
python3 scripts/cli.py break-suggest   # 推荐运动（你现在就该用这个）
python3 scripts/cli.py log <exercise>  # 记录训练
python3 scripts/cli.py plan [level]    # 生成健身计划
python3 scripts/cli.py achievements    # 查看你的街头信誉
python3 scripts/cli.py lang <en|zh>    # 切换语言
python3 scripts/cli.py posture-check   # 体态扫描
python3 scripts/cli.py check-session   # 检查你坐了多久了
```

---

## 运动分类

| 分类 | 赛博朋克名称 | 同事和前任毁掉了你的哪里 |
|------|-------------|------------------------|
| neural | 神经接口校准 | 盯着屏幕 12 小时的眼睛，前倾 45 度的脖子 |
| upper | 上肢动力模块 | 敲键盘敲到腱鞘炎的手腕，扛需求扛到僵硬的肩膀 |
| lower | 液压腿部系统 | 坐到血液不循环的双腿 |
| core | 核心稳定器 | 弓背弓到变形的腰椎 |
| cooldown | 义体冷却程序 | 被压力搞到无法放松的整个人 |

---

## 等级系统

| 等级 | 称号 | 含义 |
|------|------|------|
| LV.1 | 流浪者 | 刚意识到身体在报废的边缘 |
| LV.2 | 街头小混混 | 开始零星反抗了 |
| LV.3 | 网络浪人 | 形成了基本的维护习惯 |
| LV.4 | 赏金猎人 | 身体开始有了回应 |
| LV.5 | V级佣兵 | 你比 90% 的程序员都健康 |
| LV.6 | 荒坂精英 | 谁的烂摊子都压不垮你了 |
| LV.7 | 传奇佣兵 | 身体是你最强的武器 |
| LV.8 | 夜之城传奇 | **这些破事没有毁掉你。你赢了。** |

---

## 效果示例

> 连续编码 2 小时后——

```
⚠️ 警告：检测到操作员连续在线超时。肉体硬件过热风险 +15%。
建议执行冷却协议。

┌─────────────────────────────────────────────┐
│  🦾 光学植入体重置                              │
│  (眼部放松运动)                                 │
├─────────────────────────────────────────────┤
│  难度: ★☆☆   时长: 30 秒                      │
│                                             │
│  闭眼 → 缓慢转动眼球 → 注视远处。               │
│  重启你的光学模块，消除数据流过载。               │
└─────────────────────────────────────────────┘
```

> 完成训练后——

```
✅ 维护完毕。系统性能恢复至最优状态。干得好，V。

  经验值: +15 XP
  等级: LV.1 — 流浪者
  连续天数: 1 天

🏆 成就解锁！「觉醒」— 完成第一次训练
```

---

## 项目结构

```
cyberfit/
├── SKILL.md              # AgentSkills 标准入口
├── CLAUDE.md             # Claude Code 人格指令
├── README.md
├── README_ZH.md
├── LICENSE
├── package.json
├── requirements.txt      # Python 依赖声明
├── .gitignore
├── .claude-plugin/       # Claude Code 插件配置
│   ├── plugin.json
│   └── marketplace.json
├── prompts/              # Prompt 模板（AgentSkills 标准）
│   ├── cyberfit.md
│   ├── cyberfit-break.md
│   ├── cyberfit-plan.md
│   ├── cyberfit-log.md
│   ├── cyberfit-status.md
│   └── cyberfit-posture.md
├── skills/               # 子技能（各含 SKILL.md）
│   ├── cyberfit-break/
│   ├── cyberfit-plan/
│   ├── cyberfit-log/
│   ├── cyberfit-status/
│   ├── cyberfit-posture/
│   └── cyberfit-achievements/
├── scripts/              # Python CLI 工具
│   ├── cli.py
│   ├── core.py
│   ├── data.py
│   ├── exercises.py
│   ├── achievements.py
│   ├── planner.py
│   ├── ascii_art.py
│   └── lore.py
├── hooks/                # Claude Code hooks
│   ├── hooks.json
│   └── session-start/
└── data/
    └── .gitkeep
```

---

## 数据存储

用户数据保存在 `~/.cyberfit/` 目录下。这是**你自己的**数据，跟谁都没关系。

```
~/.cyberfit/
├── profile.json       # 你的义体档案
├── logs.json          # 训练日志
├── achievements.json  # 你的街头信誉
├── sessions.json      # 会话记录
└── config.json        # 语言偏好（en/zh）
```

---

## 为什么要做这个

因为我受够了。

受够了看到身边的程序员一个接一个地颈椎病、腰椎间盘突出、腱鞘炎、干眼症。受够了听到「年轻人不要在意这些小毛病」。受够了自己明明知道该站起来活动一下，却总是「再写完这个函数就去」，然后三个小时过去了。

你的同事把烂摊子甩给你然后跑了，你的前任把你的心搅碎了还不让你好好睡觉。**这些破事榨干了你的时间，但你的身体不该跟着一起报废。**

代码可以重构，Bug 可以修复，但你的脊椎只有一根。

**CyberFit 不会让你变成健身达人。它只做一件事：在这堆破事把你压垮之前，每 45 分钟拉你站起来一次。**

---

## 相关项目

- [同事.skill](https://github.com/titanwings/colleague-skill) — 同事跑了？让 AI 替他干活
- [前任.skill](https://github.com/titanwings/ex-skill) — 前任跑了？赛博永生一条龙

---

<div align="center">

**身体是最重要的硬件，不可替换。**

**这些破事没有毁掉你。站起来。**

MIT License © [ZouR-Ma](https://github.com/ZouR-Ma)

</div>
