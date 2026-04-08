"""
CyberFit 核心引擎：计时、状态管理
"""

from datetime import datetime
from . import data, exercises, achievements, lore, i18n


def init_user():
    """初始化用户档案"""
    is_new = data.init_profile()
    profile = data.load_profile()
    if profile:
        profile["title"] = achievements.get_title_for_level(profile.get("level", 1))
        data.save_profile(profile)

    if is_new:
        return {
            "status": "new",
            "message": i18n.t("core.init_new"),
        }
    return {
        "status": "exists",
        "message": i18n.t("core.init_exists"),
    }


def get_status():
    """获取当前状态"""
    data.ensure_initialized()
    profile = data.load_profile()

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

    level = profile.get("level", 1)
    title = achievements.get_title_for_level(level)
    profile_display = dict(profile)
    profile_display["title"] = title

    return {
        "status": status,
        "description": lore.get_status_description(status),
        "profile": profile_display,
        "today_count": len(today_logs),
        "streak": streak,
        "total_exercises": len(logs),
        "achievements_count": len(unlocked),
        "quote": lore.random_daily_quote()
    }


def check_session():
    """检查是否需要休息提醒"""
    data.ensure_initialized()
    profile = data.load_profile()

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
            "reason": i18n.t("core.today_no_maintenance"),
        }

    # 检查最后一次运动时间
    last_log_time = datetime.fromisoformat(today_logs[-1]["timestamp"])
    minutes_since = (datetime.now() - last_log_time).total_seconds() / 60
    if minutes_since > break_interval:
        return {
            "needs_break": True,
            "message": lore.random_break_reminder(),
            "reason": i18n.t("core.minutes_since_maintenance", minutes=int(minutes_since)),
            "minutes_since": int(minutes_since),
        }

    return {
        "needs_break": False,
        "message": i18n.t("core.system_normal"),
        "today_count": len(today_logs),
    }


def log_exercise(exercise_query):
    """记录一次训练"""
    data.ensure_initialized()
    profile = data.load_profile()

    exercise = exercises.find_exercise(exercise_query)
    if not exercise:
        return {"error": i18n.t("core.exercise_not_found", query=exercise_query)}

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
    data.ensure_initialized()
    profile = data.load_profile()

    unlocked = data.load_achievements()
    all_defs = achievements.get_all_achievement_defs()
    unlocked_ids = {a["id"] for a in unlocked}
    defs_by_id = {a["id"]: a for a in all_defs}

    localized_unlocked = []
    for item in unlocked:
        definition = defs_by_id.get(item["id"], {})
        localized_unlocked.append({
            **item,
            "name": definition.get("name", item.get("name", "")),
            "description": definition.get("description", item.get("description", "")),
            "xp": definition.get("xp", item.get("xp", 0)),
        })

    return {
        "unlocked": localized_unlocked,
        "locked": [a for a in all_defs if a["id"] not in unlocked_ids],
        "total": len(all_defs),
        "unlocked_count": len(localized_unlocked)
    }
