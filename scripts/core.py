"""
CyberFit 核心引擎：计时、状态管理
"""

from datetime import datetime, timedelta
from . import data, exercises, achievements, lore


def init_user():
    """初始化用户档案"""
    is_new = data.init_profile()
    if is_new:
        return {
            "status": "new",
            "message": "义体维护系统初始化完成。欢迎来到夜之城，佣兵。"
        }
    return {
        "status": "exists",
        "message": "义体维护系统已在线。操作员档案完整。"
    }


def get_status():
    """获取当前状态"""
    profile = data.load_profile()
    if not profile:
        return {"status": "offline", "message": lore.STATUS_DESCRIPTIONS["offline"]}

    logs = data.load_logs()
    today_logs = data.get_today_logs()
    streak = data.get_streak()
    unlocked = data.load_achievements()

    # 判断状态
    if streak >= 7:
        status = "excellent"
    elif streak >= 3 or len(today_logs) > 0:
        status = "good"
    elif streak == 0 and len(today_logs) == 0:
        status = "warning"
    else:
        status = "good"

    return {
        "status": status,
        "description": lore.STATUS_DESCRIPTIONS[status],
        "profile": profile,
        "today_count": len(today_logs),
        "streak": streak,
        "total_exercises": len(logs),
        "achievements_count": len(unlocked),
        "quote": lore.random_daily_quote()
    }


def check_session():
    """检查是否需要休息提醒"""
    profile = data.load_profile()
    if not profile:
        return {
            "needs_break": False,
            "message": "义体系统未初始化。运行 init 命令开始。",
            "initialized": False
        }

    # 记录会话开始
    data.record_session_start()

    stats = profile.get("stats", {})
    last_exercise = stats.get("last_exercise_date")
    break_interval = profile.get("preferences", {}).get("break_interval_minutes", 45)

    today_logs = data.get_today_logs()

    if not today_logs:
        return {
            "needs_break": True,
            "message": lore.random_break_reminder(),
            "reason": "今日尚未进行义体维护",
            "initialized": True
        }

    # 检查最后一次运动时间
    if today_logs:
        last_log_time = datetime.fromisoformat(today_logs[-1]["timestamp"])
        minutes_since = (datetime.now() - last_log_time).total_seconds() / 60
        if minutes_since > break_interval:
            return {
                "needs_break": True,
                "message": lore.random_break_reminder(),
                "reason": f"距上次维护已过 {int(minutes_since)} 分钟",
                "minutes_since": int(minutes_since),
                "initialized": True
            }

    return {
        "needs_break": False,
        "message": "系统状态正常。继续编码。",
        "today_count": len(today_logs),
        "initialized": True
    }


def log_exercise(exercise_query):
    """记录一次训练"""
    profile = data.load_profile()
    if not profile:
        return {"error": "系统未初始化。请先运行 init。"}

    exercise = exercises.find_exercise(exercise_query)
    if not exercise:
        return {"error": f"未找到运动: {exercise_query}。使用 break-suggest 查看可用运动。"}

    # 计算经验值
    xp = exercise["difficulty"] * 10 + 5

    # 记录日志
    entry = data.add_log_entry(
        exercise["id"],
        exercise["real_name"],
        exercise["cyber_name"],
        exercise["category"],
        xp
    )

    # 更新 profile
    profile["total_xp"] = profile.get("total_xp", 0) + xp
    profile["stats"]["total_exercises"] = profile["stats"].get("total_exercises", 0) + 1
    profile["stats"]["last_exercise_date"] = entry["date"]

    # 重新计算等级
    new_level = achievements.calculate_level(profile["total_xp"])
    level_up = new_level > profile.get("level", 1)
    profile["level"] = new_level
    profile["title"] = achievements.get_title_for_level(new_level)

    # 更新连续天数
    streak = data.get_streak()
    profile["stats"]["streak_days"] = streak
    if streak > profile["stats"].get("best_streak", 0):
        profile["stats"]["best_streak"] = streak

    data.save_profile(profile)

    # 检查成就
    logs = data.load_logs()
    newly_unlocked = achievements.check_achievements(profile, logs)

    # 成就经验
    for ach in newly_unlocked:
        profile["total_xp"] += ach.get("xp", 0)
    if newly_unlocked:
        data.save_profile(profile)

    return {
        "success": True,
        "exercise": exercise,
        "xp_earned": xp,
        "total_xp": profile["total_xp"],
        "level": new_level,
        "title": profile["title"],
        "level_up": level_up,
        "streak": streak,
        "newly_unlocked": newly_unlocked,
        "completion_message": lore.random_exercise_completion()
    }


def get_achievements_display():
    """获取成就展示数据"""
    profile = data.load_profile()
    if not profile:
        return {"error": "系统未初始化。"}

    unlocked = data.load_achievements()
    all_defs = achievements.get_all_achievement_defs()
    unlocked_ids = {a["id"] for a in unlocked}

    return {
        "unlocked": unlocked,
        "locked": [a for a in all_defs if a["id"] not in unlocked_ids],
        "total": len(all_defs),
        "unlocked_count": len(unlocked)
    }
