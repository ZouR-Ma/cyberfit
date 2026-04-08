# /cyberfit — 义体维护系统主入口

CyberFit 赛博朋克健身插件主命令。

## 用法

```
/cyberfit [子命令]
```

## 子命令

- `/cyberfit` — 显示仪表盘 (等同 /cyberfit-status)
- `/cyberfit-break` — 休息提醒 & 微运动指导
- `/cyberfit-plan` — 生成健身计划
- `/cyberfit-log <运动>` — 记录训练
- `/cyberfit-status` — 赛博仪表盘
- `/cyberfit-posture` — 体态检查

## 执行

当用户输入 `/cyberfit` 时，使用 `cyberfit-status` 技能展示仪表盘。执行：

```bash
python3 scripts/cli.py status
```
