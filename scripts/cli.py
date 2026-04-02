#!/usr/bin/env python3
"""
CyberFit CLI 入口
供 hooks 和 skills 调用的命令行接口
"""

import sys
import os
import json

# 将 scripts 的父目录加入 path，以支持包导入
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts import core, data, planner, exercises, achievements, ascii_art, lore


def cmd_init():
    """初始化用户档案"""
    result = core.init_user()
    print(ascii_art.banner())
    print(result["message"])
    if result["status"] == "new":
        print("\n已创建用户档案于 ~/.cyberfit/")
        print("你的代号: V")
        print("义体等级: LV.1 — 流浪者")
        print("\n使用 'status' 查看仪表盘")
        print("使用 'break-suggest' 获取第一个维护指令")


def cmd_status():
    """输出仪表盘"""
    result = core.get_status()
    if result["status"] == "offline":
        print(result["message"])
        return

    print(ascii_art.dashboard(
        result["profile"],
        result["today_count"],
        result["streak"],
        result["achievements_count"]
    ))
    print(f"\n  状态: {result['description']}")
    print(f"\n  📡 {result['quote']}")


def cmd_check_session():
    """检查是否需要休息"""
    result = core.check_session()
    if not result.get("initialized"):
        print(ascii_art.mini_banner())
        print(result["message"])
        return

    if result["needs_break"]:
        print(ascii_art.break_banner())
        print(f"\n{result['message']}")
        if result.get("reason"):
            print(f"\n原因: {result['reason']}")
        print("\n输入 /cyberfit-break 获取维护指令")
    else:
        print(ascii_art.mini_banner())
        print(f"\n{result['message']}")
        if result.get("today_count"):
            print(f"今日已完成 {result['today_count']} 次维护。")


def cmd_log(exercise_query):
    """记录训练"""
    result = core.log_exercise(exercise_query)
    if result.get("error"):
        print(f"❌ {result['error']}")
        return

    ex = result["exercise"]
    print(f"\n✅ 训练记录已保存！")
    print(f"\n  动作: {ex['cyber_name']} ({ex['real_name']})")
    print(f"  经验值: +{result['xp_earned']} XP")
    print(f"  总经验: {result['total_xp']} XP")
    print(f"  等级: LV.{result['level']} — {result['title']}")
    print(f"  连续天数: {result['streak']} 天")

    if result.get("level_up"):
        print(f"\n🎉 等级提升! 你现在是 LV.{result['level']} — {result['title']}!")

    print(f"\n  {result['completion_message']}")

    if result.get("newly_unlocked"):
        for ach in result["newly_unlocked"]:
            print(ascii_art.achievement_card(ach))


def cmd_plan(level_arg=None):
    """生成健身计划"""
    profile = data.load_profile()
    if not profile:
        print("❌ 系统未初始化。请先运行 init。")
        return

    level = int(level_arg) if level_arg else profile.get("level", 1)
    title = profile.get("title", "流浪者")

    plan = planner.generate_plan(level=level)
    print(f"\n{lore.random_exercise_intro()}")
    print(ascii_art.plan_display(plan, level, title))

    total_time = sum(e["duration_seconds"] for e in plan)
    print(f"\n  预计总时长: {total_time // 60} 分 {total_time % 60} 秒")
    print(f"\n  完成后使用 'log <运动ID>' 记录训练")
    print(f"  例如: python3 scripts/cli.py log {plan[0]['id']}")


def cmd_achievements():
    """查看成就"""
    result = core.get_achievements_display()
    if result.get("error"):
        print(f"❌ {result['error']}")
        return

    print(ascii_art.achievements_list(result["unlocked"]))
    print(f"\n  已解锁: {result['unlocked_count']}/{result['total']}")

    if result["locked"]:
        print("\n  🔒 未解锁成就:")
        for a in result["locked"]:
            print(f"     • {a['name']} — {a['description']} (+{a['xp']} XP)")


def cmd_break_suggest():
    """推荐休息动作"""
    profile = data.load_profile()
    if not profile:
        print("❌ 系统未初始化。请先运行 init。")
        return

    print(f"\n{lore.random_exercise_intro()}")
    plan = planner.generate_quick_break()
    for ex in plan:
        print(ascii_art.exercise_card(ex))

    print(f"\n完成后使用 'log <运动ID>' 记录训练")
    if plan:
        print(f"例如: python3 scripts/cli.py log {plan[0]['id']}")


def cmd_posture_check():
    """体态检查"""
    profile = data.load_profile()
    if not profile:
        print("❌ 系统未初始化。请先运行 init。")
        return

    print(ascii_art.mini_banner())
    print(lore.random_posture_check())
    print("\n完成校准后，保持正确坐姿继续编码。你的脊椎会感谢你的。")


def cmd_help():
    """帮助信息"""
    print(ascii_art.mini_banner())
    print("""
  可用命令:
    init            初始化义体维护系统
    status          查看仪表盘
    check-session   检查是否需要休息
    log <exercise>  记录训练 (使用运动ID或名称)
    plan [level]    生成健身计划
    achievements    查看成就
    break-suggest   推荐休息运动
    posture-check   体态检查
    help            显示帮助

  运动分类:
    neural     神经接口校准 (颈部/眼部)
    upper      上肢动力模块 (手腕/手臂/肩膀)
    lower      液压腿部系统 (腿部)
    core       核心稳定器 (腰腹)
    cooldown   义体冷却程序 (拉伸放松)
    """)


def main():
    if len(sys.argv) < 2:
        cmd_help()
        return

    command = sys.argv[1]
    args = sys.argv[2:]

    commands = {
        "init": cmd_init,
        "status": cmd_status,
        "check-session": cmd_check_session,
        "log": lambda: cmd_log(args[0] if args else ""),
        "plan": lambda: cmd_plan(args[0] if args else None),
        "achievements": cmd_achievements,
        "break-suggest": cmd_break_suggest,
        "posture-check": cmd_posture_check,
        "help": cmd_help,
    }

    handler = commands.get(command)
    if handler:
        handler()
    else:
        print(f"❌ 未知命令: {command}")
        cmd_help()


if __name__ == "__main__":
    main()
