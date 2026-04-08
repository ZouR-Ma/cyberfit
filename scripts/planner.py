"""
CyberFit 健身计划生成器
"""

import random
from . import exercises, data


def generate_plan(level=None, focus_areas=None, count=5):
    """
    生成健身计划
    - level: 义体等级 (决定难度)
    - focus_areas: 专注区域列表
    - count: 动作数量
    """
    profile = data.load_profile()
    if profile and level is None:
        level = profile.get("level", 1)
    if level is None:
        level = 1

    if profile and focus_areas is None:
        focus_areas = profile.get("preferences", {}).get("focus_areas", list(exercises.get_categories().keys()))
    if focus_areas is None:
        focus_areas = list(exercises.get_categories().keys())

    # 根据等级确定最大难度
    max_difficulty = min(level, 3)

    # 收集可用运动
    available = []
    for ex in exercises.get_exercises():
        if ex["difficulty"] <= max_difficulty and ex["category"] in focus_areas:
            available.append(ex)

    if not available:
        available = exercises.get_exercises_by_difficulty(max_difficulty)

    # 尽量每个分类选一个，然后补齐
    plan = []
    categories_used = set()

    # 第一轮：每个分类选一个
    for cat in focus_areas:
        cat_exercises = [e for e in available if e["category"] == cat and e not in plan]
        if cat_exercises:
            chosen = random.choice(cat_exercises)
            plan.append(chosen)
            categories_used.add(cat)
            if len(plan) >= count:
                break

    # 第二轮：补齐
    remaining = [e for e in available if e not in plan]
    while len(plan) < count and remaining:
        chosen = random.choice(remaining)
        plan.append(chosen)
        remaining.remove(chosen)

    return plan[:count]


def generate_quick_break(max_duration=120):
    """生成快速休息方案（2分钟内）"""
    quick = exercises.get_quick_exercises(max_duration=60)
    if len(quick) >= 3:
        return random.sample(quick, 3)
    return quick


def generate_focused_plan(category, count=3):
    """生成专项训练计划"""
    cat_exercises = exercises.get_exercises_by_category(category)
    if len(cat_exercises) >= count:
        return random.sample(cat_exercises, count)
    return cat_exercises
