---
name: cyberfit
description: 赛博朋克主题程序员健身插件 — 义体维护系统。帮助程序员在编码间隙保持身体健康，提供运动提醒、健身计划、训练记录、成就系统和体态检查。
license: MIT
compatibility: Requires Python 3 and Claude Code (or similar agent products)
metadata:
  author: ZouR-Ma
  version: "1.0"
---

# CyberFit — 义体维护系统

> 身体是最重要的硬件，不可替换。

CyberFit 是一个赛博朋克主题的程序员健身插件，将日常健身包装为义体维护程序，让枯燥的运动变得有趣。

## 子技能列表

| 技能 | 说明 |
|------|------|
| `cyberfit-break` | 义体冷却协议 — 久坐提醒与微运动指令 |
| `cyberfit-plan` | 义体升级蓝图 — 生成个性化健身计划 |
| `cyberfit-log` | 训练数据记录 — 打卡记录与经验值积累 |
| `cyberfit-status` | 义体诊断仪表盘 — 查看当前状态与进度 |
| `cyberfit-posture` | 义体姿态校准 — 体态检查与改善建议 |
| `cyberfit-achievements` | 街头信誉系统 — 成就与等级称号 |

## CLI 用法

```bash
python3 scripts/cli.py init            # 初始化义体维护系统
python3 scripts/cli.py status          # 仪表盘
python3 scripts/cli.py check-session   # 检查休息时间
python3 scripts/cli.py log <exercise>  # 记录训练
python3 scripts/cli.py plan [level]    # 生成计划
python3 scripts/cli.py achievements    # 查看成就
python3 scripts/cli.py break-suggest   # 推荐运动
python3 scripts/cli.py posture-check   # 体态检查
```

## 数据存储

用户数据存储在 `~/.cyberfit/` 目录下，通过 `scripts/cli.py` 进行读写操作。

## Prompt 模板

Prompt 文件位于 `prompts/` 目录，提供各子技能的交互模板。

## 兼容性

- **AgentSkills 标准**：通过本文件 (`SKILL.md`) 及 `skills/` 子目录提供标准化技能描述
- **Claude Code**：通过 `.claude-plugin/` 目录和 `hooks/` 目录提供原生集成
