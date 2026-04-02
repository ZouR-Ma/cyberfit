#!/usr/bin/env bash
# CyberFit 义体维护系统 — 会话启动检查
# 在每次 Claude Code 启动时运行，检查久坐状态并输出提醒

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

python3 "$SCRIPT_DIR/scripts/cli.py" check-session 2>/dev/null

exit 0
