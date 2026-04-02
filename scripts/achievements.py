"""
CyberFit 成就/称号系统
"""

from . import data, lore

# 成就定义
ACHIEVEMENT_DEFS = [
    # 连续打卡
    {
        "id": "streak_3",
        "name": "系统启动",
        "description": "连续 3 天完成训练",
        "condition": lambda profile, logs: data.get_streak() >= 3,
        "xp": 50
    },
    {
        "id": "streak_7",
        "name": "稳定运行",
        "description": "连续 7 天完成训练",
        "condition": lambda profile, logs: data.get_streak() >= 7,
        "xp": 150
    },
    {
        "id": "streak_14",
        "name": "钢铁意志协议",
        "description": "连续 14 天完成训练",
        "condition": lambda profile, logs: data.get_streak() >= 14,
        "xp": 300
    },
    {
        "id": "streak_30",
        "name": "不灭传奇",
        "description": "连续 30 天完成训练",
        "condition": lambda profile, logs: data.get_streak() >= 30,
        "xp": 1000
    },
    # 累计训练次数
    {
        "id": "total_10",
        "name": "初次改装",
        "description": "累计完成 10 次训练",
        "condition": lambda profile, logs: len(logs) >= 10,
        "xp": 30
    },
    {
        "id": "total_50",
        "name": "银手之路",
        "description": "累计完成 50 次训练",
        "condition": lambda profile, logs: len(logs) >= 50,
        "xp": 100
    },
    {
        "id": "total_100",
        "name": "百战老兵",
        "description": "累计完成 100 次训练",
        "condition": lambda profile, logs: len(logs) >= 100,
        "xp": 300
    },
    {
        "id": "total_500",
        "name": "赛博之神",
        "description": "累计完成 500 次训练",
        "condition": lambda profile, logs: len(logs) >= 500,
        "xp": 1000
    },
    # 分类达成
    {
        "id": "cat_neural",
        "name": "神经先知",
        "description": "完成 10 次神经接口校准训练",
        "condition": lambda profile, logs: sum(1 for l in logs if l.get("category") == "neural") >= 10,
        "xp": 80
    },
    {
        "id": "cat_upper",
        "name": "大力神臂",
        "description": "完成 10 次上肢动力模块训练",
        "condition": lambda profile, logs: sum(1 for l in logs if l.get("category") == "upper") >= 10,
        "xp": 80
    },
    {
        "id": "cat_lower",
        "name": "弹跳大师",
        "description": "完成 10 次液压腿部系统训练",
        "condition": lambda profile, logs: sum(1 for l in logs if l.get("category") == "lower") >= 10,
        "xp": 80
    },
    {
        "id": "cat_core",
        "name": "铁壁堡垒",
        "description": "完成 10 次核心稳定器训练",
        "condition": lambda profile, logs: sum(1 for l in logs if l.get("category") == "core") >= 10,
        "xp": 80
    },
    {
        "id": "cat_cooldown",
        "name": "冰霜行者",
        "description": "完成 10 次义体冷却程序",
        "condition": lambda profile, logs: sum(1 for l in logs if l.get("category") == "cooldown") >= 10,
        "xp": 80
    },
    # 全分类
    {
        "id": "all_categories",
        "name": "全面改造",
        "description": "在所有 5 个分类中各完成至少 1 次训练",
        "condition": lambda profile, logs: len(set(l.get("category") for l in logs)) >= 5,
        "xp": 200
    },
    # 首次运动
    {
        "id": "first_exercise",
        "name": "觉醒",
        "description": "完成第一次训练",
        "condition": lambda profile, logs: len(logs) >= 1,
        "xp": 10
    },
]


# 等级经验阈值
def xp_for_level(level):
    """计算升级所需总经验值"""
    return level * 100


def calculate_level(total_xp):
    """根据总经验值计算等级"""
    level = 1
    while total_xp >= xp_for_level(level) and level < 8:
        total_xp -= xp_for_level(level)
        level += 1
    return level


def get_title_for_level(level):
    """获取等级对应称号"""
    title, _ = lore.get_rank_info(level)
    return title


def check_achievements(profile, logs):
    """检查并解锁新成就"""
    unlocked = data.load_achievements()
    unlocked_ids = {a["id"] for a in unlocked}
    newly_unlocked = []

    for ach_def in ACHIEVEMENT_DEFS:
        if ach_def["id"] not in unlocked_ids:
            try:
                if ach_def["condition"](profile, logs):
                    entry = data.unlock_achievement(
                        ach_def["id"],
                        ach_def["name"],
                        ach_def["description"]
                    )
                    if entry:
                        entry["xp"] = ach_def["xp"]
                        newly_unlocked.append(entry)
            except Exception:
                pass

    return newly_unlocked


def get_all_achievement_defs():
    """获取所有成就定义（用于展示）"""
    return [{"id": a["id"], "name": a["name"], "description": a["description"], "xp": a["xp"]} for a in ACHIEVEMENT_DEFS]
