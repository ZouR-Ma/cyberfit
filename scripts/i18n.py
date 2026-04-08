"""
CyberFit 国际化配置与字符串管理。
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

DATA_DIR = Path.home() / ".cyberfit"
CONFIG_FILE = DATA_DIR / "config.json"

DEFAULT_LANG = "en"
SUPPORTED_LANGS = {"en", "zh"}

UI_STRINGS = {
    "en": {
        "core": {
            "init_new": "Cybernetic maintenance system initialized. Welcome to Night City, merc.",
            "init_exists": "Cybernetic maintenance system already online. Operator profile verified.",
            "not_initialized": "System is not initialized. Run `init` to start.",
            "today_no_maintenance": "No cybernetic maintenance logged today.",
            "minutes_since_maintenance": "{minutes} minutes since last maintenance.",
            "system_normal": "System status stable. Keep coding.",
            "exercise_not_found": "Exercise not found: {query}. Use `break-suggest` to list options.",
            "achievements_not_initialized": "System is not initialized.",
        },
        "cli": {
            "profile_created": "Profile created at ~/.cyberfit/",
            "codename": "Codename: V",
            "level_default": "Cyber Level: LV.1 - {title}",
            "hint_status": "Use `status` to view your dashboard.",
            "hint_break": "Use `break-suggest` to get your first maintenance protocol.",
            "status_label": "Status",
            "reason_label": "Reason",
            "break_hint": "Run /cyberfit-break for a maintenance protocol.",
            "today_completed": "Maintenance sessions completed today: {count}.",
            "log_saved": "Workout log saved.",
            "action_label": "Action",
            "xp_earned": "XP Earned",
            "total_xp": "Total XP",
            "level": "Level",
            "streak_days": "Streak",
            "days_suffix": "days",
            "level_up": "Level up! You are now LV.{level} - {title}!",
            "plan_total_time": "Estimated total duration: {minutes} min {seconds} sec",
            "plan_log_hint": "Log completion with `log <exercise_id>`",
            "plan_log_example": "Example: python3 scripts/cli.py log {exercise_id}",
            "achievements_unlocked": "Unlocked: {unlocked}/{total}",
            "achievements_locked": "Locked achievements:",
            "break_log_hint": "After finishing, log with `log <exercise_id>`",
            "posture_done": "After calibration, keep proper posture while coding. Your spine will thank you.",
            "lang_usage": "Usage: python3 scripts/cli.py lang <en|zh>",
            "lang_changed": "Language switched to English.",
            "lang_invalid": "Invalid language code: {code}. Use `en` or `zh`.",
            "lang_current": "Current language: {code}",
            "unknown_command": "Unknown command: {command}",
            "error_prefix": "Error",
            "success_prefix": "Done",
        },
        "help": {
            "commands_header": "Available commands:",
            "exercise_categories": "Exercise categories:",
            "init": "Initialize CyberFit system",
            "status": "Show dashboard",
            "check_session": "Check whether a break is needed",
            "log": "Log workout (use exercise ID or name)",
            "plan": "Generate workout plan",
            "achievements": "Show achievements",
            "break_suggest": "Suggest break exercises",
            "posture_check": "Posture check",
            "lang": "Switch UI language",
            "help": "Show help",
            "cat_neural": "Neural Interface Calibration (neck/eyes)",
            "cat_upper": "Upper Limb Power Module (wrist/arm/shoulder)",
            "cat_lower": "Hydraulic Leg System (legs)",
            "cat_core": "Core Stabilizer (waist/abs)",
            "cat_cooldown": "Cooling Protocol (stretch/recovery)",
        },
    },
    "zh": {
        "core": {
            "init_new": "义体维护系统初始化完成。欢迎来到夜之城，佣兵。",
            "init_exists": "义体维护系统已在线。操作员档案完整。",
            "not_initialized": "义体系统未初始化。运行 init 命令开始。",
            "today_no_maintenance": "今日尚未进行义体维护",
            "minutes_since_maintenance": "距上次维护已过 {minutes} 分钟",
            "system_normal": "系统状态正常。继续编码。",
            "exercise_not_found": "未找到运动: {query}。使用 break-suggest 查看可用运动。",
            "achievements_not_initialized": "系统未初始化。",
        },
        "cli": {
            "profile_created": "已创建用户档案于 ~/.cyberfit/",
            "codename": "你的代号: V",
            "level_default": "义体等级: LV.1 - {title}",
            "hint_status": "使用 `status` 查看仪表盘",
            "hint_break": "使用 `break-suggest` 获取第一个维护指令",
            "status_label": "状态",
            "reason_label": "原因",
            "break_hint": "输入 /cyberfit-break 获取维护指令",
            "today_completed": "今日已完成 {count} 次维护。",
            "log_saved": "训练记录已保存！",
            "action_label": "动作",
            "xp_earned": "经验值",
            "total_xp": "总经验",
            "level": "等级",
            "streak_days": "连续天数",
            "days_suffix": "天",
            "level_up": "等级提升! 你现在是 LV.{level} - {title}!",
            "plan_total_time": "预计总时长: {minutes} 分 {seconds} 秒",
            "plan_log_hint": "完成后使用 `log <运动ID>` 记录训练",
            "plan_log_example": "例如: python3 scripts/cli.py log {exercise_id}",
            "achievements_unlocked": "已解锁: {unlocked}/{total}",
            "achievements_locked": "未解锁成就:",
            "break_log_hint": "完成后使用 `log <运动ID>` 记录训练",
            "posture_done": "完成校准后，保持正确坐姿继续编码。你的脊椎会感谢你的。",
            "lang_usage": "用法: python3 scripts/cli.py lang <en|zh>",
            "lang_changed": "语言已切换为中文。",
            "lang_invalid": "无效语言代码: {code}。仅支持 `en` 或 `zh`。",
            "lang_current": "当前语言: {code}",
            "unknown_command": "未知命令: {command}",
            "error_prefix": "错误",
            "success_prefix": "完成",
        },
        "help": {
            "commands_header": "可用命令:",
            "exercise_categories": "运动分类:",
            "init": "初始化义体维护系统",
            "status": "查看仪表盘",
            "check_session": "检查是否需要休息",
            "log": "记录训练 (使用运动ID或名称)",
            "plan": "生成健身计划",
            "achievements": "查看成就",
            "break_suggest": "推荐休息运动",
            "posture_check": "体态检查",
            "lang": "切换界面语言",
            "help": "显示帮助",
            "cat_neural": "神经接口校准 (颈部/眼部)",
            "cat_upper": "上肢动力模块 (手腕/手臂/肩膀)",
            "cat_lower": "液压腿部系统 (腿部)",
            "cat_core": "核心稳定器 (腰腹)",
            "cat_cooldown": "义体冷却程序 (拉伸放松)",
        },
    },
}


def _ensure_data_dir() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def normalize_lang(lang: str | None) -> str:
    if lang in SUPPORTED_LANGS:
        return lang
    return DEFAULT_LANG


def _read_config() -> dict[str, Any]:
    if not CONFIG_FILE.exists():
        return {}
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            loaded = json.load(f)
            if isinstance(loaded, dict):
                return loaded
    except (OSError, json.JSONDecodeError):
        return {}
    return {}


def get_lang() -> str:
    config = _read_config()
    return normalize_lang(config.get("lang"))


def set_lang(lang: str) -> str:
    if lang not in SUPPORTED_LANGS:
        raise ValueError(f"Unsupported language: {lang}")

    config = _read_config()
    config["lang"] = lang

    _ensure_data_dir()
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)
    return lang


def _resolve_dotted_key(source: dict[str, Any], key: str) -> Any:
    current: Any = source
    for part in key.split("."):
        if not isinstance(current, dict):
            return None
        current = current.get(part)
    return current


def t(key: str, lang: str | None = None, **kwargs: Any) -> str:
    active_lang = normalize_lang(lang or get_lang())
    text = _resolve_dotted_key(UI_STRINGS.get(active_lang, {}), key)

    if text is None:
        text = _resolve_dotted_key(UI_STRINGS[DEFAULT_LANG], key)
    if not isinstance(text, str):
        return key

    if kwargs:
        return text.format(**kwargs)
    return text
