#!/usr/bin/env python3
"""
CyberFit CLI 入口
供 hooks 和 skills 调用的命令行接口
"""

import sys
import os

# 将 scripts 的父目录加入 path，以支持包导入
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts import core, data, planner, achievements, ascii_art, lore, i18n


def _print_error(message):
    print(f"❌ {message}")


def cmd_init():
    """初始化用户档案"""
    result = core.init_user()
    print(ascii_art.banner())
    print(result["message"])
    if result["status"] == "new":
        title = achievements.get_title_for_level(1)
        print(f"\n{i18n.t('cli.profile_created')}")
        print(i18n.t("cli.codename"))
        print(i18n.t("cli.level_default", title=title))
        print(f"\n{i18n.t('cli.hint_status')}")
        print(i18n.t("cli.hint_break"))


def cmd_status():
    """输出仪表盘"""
    result = core.get_status()

    print(
        ascii_art.dashboard(
            result["profile"],
            result["today_count"],
            result["streak"],
            result["achievements_count"],
        )
    )
    print(f"\n  {i18n.t('cli.status_label')}: {result['description']}")
    print(f"\n  📡 {result['quote']}")


def cmd_check_session():
    """检查是否需要休息"""
    result = core.check_session()

    if result["needs_break"]:
        print(ascii_art.break_banner())
        print(f"\n{result['message']}")
        if result.get("reason"):
            print(f"\n{i18n.t('cli.reason_label')}: {result['reason']}")
        print(f"\n{i18n.t('cli.break_hint')}")
    else:
        print(ascii_art.mini_banner())
        print(f"\n{result['message']}")
        if result.get("today_count"):
            print(i18n.t("cli.today_completed", count=result["today_count"]))


def cmd_log(exercise_query):
    """记录训练"""
    result = core.log_exercise(exercise_query)
    if result.get("error"):
        _print_error(result["error"])
        return

    ex = result["exercise"]
    print(f"\n✅ {i18n.t('cli.log_saved')}")
    print(f"\n  {i18n.t('cli.action_label')}: {ex['cyber_name']} ({ex['real_name']})")
    print(f"  {i18n.t('cli.xp_earned')}: +{result['xp_earned']} XP")
    print(f"  {i18n.t('cli.total_xp')}: {result['total_xp']} XP")
    print(f"  {i18n.t('cli.level')}: LV.{result['level']} - {result['title']}")
    print(f"  {i18n.t('cli.streak_days')}: {result['streak']} {i18n.t('cli.days_suffix')}")

    if result.get("level_up"):
        print(f"\n🎉 {i18n.t('cli.level_up', level=result['level'], title=result['title'])}")

    print(f"\n  {result['completion_message']}")

    if result.get("newly_unlocked"):
        for ach in result["newly_unlocked"]:
            print(ascii_art.achievement_card(ach))


def cmd_plan(level_arg=None):
    """生成健身计划"""
    data.ensure_initialized()
    profile = data.load_profile()

    level = int(level_arg) if level_arg else profile.get("level", 1)
    title = achievements.get_title_for_level(level)

    plan = planner.generate_plan(level=level)
    print(f"\n{lore.random_exercise_intro()}")
    print(ascii_art.plan_display(plan, level, title))

    total_time = sum(e["duration_seconds"] for e in plan)
    print(
        f"\n  {i18n.t('cli.plan_total_time', minutes=total_time // 60, seconds=total_time % 60)}"
    )
    print(f"\n  {i18n.t('cli.plan_log_hint')}")
    if plan:
        print(i18n.t("cli.plan_log_example", exercise_id=plan[0]["id"]))


def cmd_achievements():
    """查看成就"""
    result = core.get_achievements_display()
    if result.get("error"):
        _print_error(result["error"])
        return

    print(ascii_art.achievements_list(result["unlocked"]))
    print(i18n.t("cli.achievements_unlocked", unlocked=result["unlocked_count"], total=result["total"]))

    if result["locked"]:
        print(f"\n  🔒 {i18n.t('cli.achievements_locked')}")
        for item in result["locked"]:
            print(f"     • {item['name']} - {item['description']} (+{item['xp']} XP)")


def cmd_break_suggest():
    """推荐休息动作"""
    data.ensure_initialized()

    print(f"\n{lore.random_exercise_intro()}")
    plan = planner.generate_quick_break()
    for ex in plan:
        print(ascii_art.exercise_card(ex))

    print(f"\n{i18n.t('cli.break_log_hint')}")
    if plan:
        print(i18n.t("cli.plan_log_example", exercise_id=plan[0]["id"]))


def cmd_posture_check():
    """体态检查"""
    data.ensure_initialized()

    print(ascii_art.mini_banner())
    print(lore.random_posture_check())
    print(f"\n{i18n.t('cli.posture_done')}")


def cmd_lang(lang_code=None):
    """切换语言"""
    if not lang_code:
        print(i18n.t("cli.lang_usage"))
        print(i18n.t("cli.lang_current", code=i18n.get_lang()))
        return

    if lang_code not in i18n.SUPPORTED_LANGS:
        _print_error(i18n.t("cli.lang_invalid", code=lang_code))
        print(i18n.t("cli.lang_usage"))
        return

    i18n.set_lang(lang_code)
    print(i18n.t("cli.lang_changed"))
    print(i18n.t("cli.lang_current", code=i18n.get_lang()))


def cmd_help():
    """帮助信息"""
    print(ascii_art.mini_banner())

    print(f"\n  {i18n.t('help.commands_header')}")
    print(f"    init            {i18n.t('help.init')}")
    print(f"    status          {i18n.t('help.status')}")
    print(f"    check-session   {i18n.t('help.check_session')}")
    print(f"    log <exercise>  {i18n.t('help.log')}")
    print(f"    plan [level]    {i18n.t('help.plan')}")
    print(f"    achievements    {i18n.t('help.achievements')}")
    print(f"    break-suggest   {i18n.t('help.break_suggest')}")
    print(f"    posture-check   {i18n.t('help.posture_check')}")
    print(f"    lang <en|zh>    {i18n.t('help.lang')}")
    print(f"    help            {i18n.t('help.help')}")

    print(f"\n  {i18n.t('help.exercise_categories')}")
    print(f"    neural     {i18n.t('help.cat_neural')}")
    print(f"    upper      {i18n.t('help.cat_upper')}")
    print(f"    lower      {i18n.t('help.cat_lower')}")
    print(f"    core       {i18n.t('help.cat_core')}")
    print(f"    cooldown   {i18n.t('help.cat_cooldown')}")


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
        "lang": lambda: cmd_lang(args[0] if args else None),
        "help": cmd_help,
    }

    handler = commands.get(command)
    if handler:
        handler()
    else:
        _print_error(i18n.t("cli.unknown_command", command=command))
        cmd_help()


if __name__ == "__main__":
    main()
