"""
CyberFit 数据持久化模块
数据存储路径: ~/.cyberfit/
"""

import json
import os
from datetime import datetime, date
from pathlib import Path

DATA_DIR = Path.home() / ".cyberfit"

PROFILE_FILE = DATA_DIR / "profile.json"
LOGS_FILE = DATA_DIR / "logs.json"
ACHIEVEMENTS_FILE = DATA_DIR / "achievements.json"
SESSIONS_FILE = DATA_DIR / "sessions.json"


def ensure_data_dir():
    """确保数据目录存在"""
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def _read_json(filepath):
    """读取 JSON 文件"""
    if filepath.exists():
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    return None


def _write_json(filepath, data):
    """写入 JSON 文件"""
    ensure_data_dir()
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# === 用户档案 ===

def get_default_profile():
    """返回默认用户档案"""
    return {
        "created_at": datetime.now().isoformat(),
        "cyber_name": "V",
        "level": 1,
        "title": "流浪者",
        "fitness_level": "beginner",
        "total_xp": 0,
        "preferences": {
            "break_interval_minutes": 45,
            "exercise_difficulty": "easy",
            "focus_areas": ["neural", "upper", "lower", "core", "cooldown"]
        },
        "stats": {
            "total_sessions": 0,
            "total_exercises": 0,
            "streak_days": 0,
            "best_streak": 0,
            "last_exercise_date": None,
            "last_session_start": None
        }
    }


def load_profile():
    """加载用户档案"""
    return _read_json(PROFILE_FILE)


def save_profile(profile):
    """保存用户档案"""
    _write_json(PROFILE_FILE, profile)


def init_profile():
    """初始化用户档案（如果不存在）"""
    if not PROFILE_FILE.exists():
        save_profile(get_default_profile())
        _write_json(LOGS_FILE, [])
        _write_json(ACHIEVEMENTS_FILE, [])
        _write_json(SESSIONS_FILE, [])
        return True
    return False


def ensure_initialized():
    """确保用户数据已初始化，若不存在则自动创建"""
    if not PROFILE_FILE.exists():
        init_profile()


# === 训练日志 ===

def load_logs():
    """加载训练日志"""
    return _read_json(LOGS_FILE) or []


def save_logs(logs):
    """保存训练日志"""
    _write_json(LOGS_FILE, logs)


def add_log_entry(exercise_id, exercise_name, cyber_name, category, xp_earned):
    """添加训练日志条目"""
    logs = load_logs()
    entry = {
        "timestamp": datetime.now().isoformat(),
        "date": date.today().isoformat(),
        "exercise_id": exercise_id,
        "exercise_name": exercise_name,
        "cyber_name": cyber_name,
        "category": category,
        "xp_earned": xp_earned
    }
    logs.append(entry)
    save_logs(logs)
    return entry


# === 成就 ===

def load_achievements():
    """加载已解锁成就"""
    return _read_json(ACHIEVEMENTS_FILE) or []


def save_achievements(achievements):
    """保存成就"""
    _write_json(ACHIEVEMENTS_FILE, achievements)


def unlock_achievement(achievement_id, name, description):
    """解锁新成就"""
    achievements = load_achievements()
    if any(a["id"] == achievement_id for a in achievements):
        return None  # 已解锁
    entry = {
        "id": achievement_id,
        "name": name,
        "description": description,
        "unlocked_at": datetime.now().isoformat()
    }
    achievements.append(entry)
    save_achievements(achievements)
    return entry


# === 会话记录 ===

def load_sessions():
    """加载编码会话记录"""
    return _read_json(SESSIONS_FILE) or []


def save_sessions(sessions):
    """保存会话记录"""
    _write_json(SESSIONS_FILE, sessions)


def record_session_start():
    """记录会话开始"""
    sessions = load_sessions()
    sessions.append({
        "start": datetime.now().isoformat(),
        "end": None
    })
    save_sessions(sessions)
    # 同时更新 profile
    profile = load_profile()
    if profile:
        profile["stats"]["last_session_start"] = datetime.now().isoformat()
        save_profile(profile)


def get_today_logs():
    """获取今日训练记录"""
    logs = load_logs()
    today = date.today().isoformat()
    return [l for l in logs if l.get("date") == today]


def get_streak():
    """计算连续打卡天数"""
    logs = load_logs()
    if not logs:
        return 0
    dates = sorted(set(l["date"] for l in logs), reverse=True)
    if not dates:
        return 0
    streak = 0
    current = date.today()
    for d_str in dates:
        d = date.fromisoformat(d_str)
        diff = (current - d).days
        if diff <= 1:
            streak += 1
            current = d
        else:
            break
    return streak
