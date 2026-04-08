"""
CyberFit ASCII Art terminal UI.

All box-drawing uses display-width-aware padding so CJK / Emoji
content never misaligns the right border.
"""

import unicodedata
from . import i18n, lore


def _is_en() -> bool:
    return i18n.get_lang() == "en"


# ── display-width helpers ──────────────────────────────────────

def _display_width(s):
    """Calculate terminal display width, handling CJK and Emoji."""
    width = 0
    for ch in s:
        cp = ord(ch)
        # Zero-width: combining marks, variation selectors, ZWJ, ZWSP
        if unicodedata.category(ch).startswith('M') or cp in (0xFE0E, 0xFE0F, 0x200D, 0x200B):
            continue
        # Supplementary emoji (U+1F000+) are typically 2 columns
        if cp >= 0x1F000:
            width += 2
        # CJK and fullwidth characters
        elif unicodedata.east_asian_width(ch) in ('W', 'F'):
            width += 2
        else:
            width += 1
    return width


def _rpad(s, target_width):
    """Right-pad string with spaces to reach *target_width* display columns."""
    pad = target_width - _display_width(s)
    return s + ' ' * max(0, pad)


def _box(content, inner_width, l='║', r='║'):
    """Build one box line: left-border + content padded to inner_width + right-border."""
    return l + _rpad(content, inner_width) + r


# ── banners ────────────────────────────────────────────────────

_FIGLET = [
    "   ██████╗██╗   ██╗██████╗ ███████╗██████╗ ███████╗██╗████████╗  ",
    "  ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗██╔════╝██║╚══██╔══╝  ",
    "  ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝█████╗  ██║   ██║     ",
    "  ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗██╔══╝  ██║   ██║     ",
    "  ╚██████╗   ██║   ██████╔╝███████╗██║  ██║██║     ██║   ██║     ",
    "   ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝   ╚═╝     ",
]


def banner():
    """CyberFit 主横幅"""
    W = 62
    top = "╔" + "═" * W + "╗"
    bot = "╚" + "═" * W + "╝"

    lines = ["", top]
    for art in _FIGLET:
        lines.append(_box(art, W))
    lines.append(_box("", W))

    if _is_en():
        lines.append(_box('         "Body is your core hardware, not replaceable"', W))
        lines.append(_box("               Night City · Cybernetic Maintenance v1.0", W))
    else:
        lines.append(_box('           「身体是最重要的硬件，不可替换」', W))
        lines.append(_box("                  夜之城 · 义体维护系统 v1.0", W))

    lines.append(bot)
    return "\n".join(lines)


def mini_banner():
    """小型横幅"""
    W = 37
    top = "┌" + "─" * W + "┐"
    bot = "└" + "─" * W + "┘"
    b = lambda c: _box(c, W, "│", "│")

    if _is_en():
        return "\n".join(["", top,
            b("  CYBERFIT // MAINTENANCE SYSTEM"),
            b('  "Body is core hardware"'),
            bot])

    return "\n".join(["", top,
        b("  CYBERFIT // 义体维护系统"),
        b("  「身体是最重要的硬件」"),
        bot])


# ── progress bars ──────────────────────────────────────────────

def progress_bar(current, total, width=20, fill="█", empty="░"):
    """生成进度条"""
    if total == 0:
        ratio = 0
    else:
        ratio = min(current / total, 1.0)
    filled = int(width * ratio)
    bar = fill * filled + empty * (width - filled)
    percent = int(ratio * 100)
    return f"[{bar}] {percent}%"


def xp_bar(current_xp, next_level_xp, level):
    """经验值进度条"""
    bar = progress_bar(current_xp, next_level_xp, width=25)
    return f"  LV.{level} {bar} ({current_xp}/{next_level_xp} XP)"


# ── dashboard ──────────────────────────────────────────────────

def dashboard(profile, today_count, streak, achievements_count):
    """生成赛博朋克仪表盘"""
    W = 50
    level = profile.get("level", 1)
    title, _ = lore.get_rank_info(level)
    total_xp = profile.get("total_xp", 0)
    next_xp = level * 100
    stats = profile.get("stats", {})
    total_sessions = stats.get("total_sessions", 0)
    total_exercises = stats.get("total_exercises", 0)
    xp = xp_bar(total_xp % next_xp, next_xp, level)
    name = profile.get('cyber_name', 'V')

    top = "╔" + "═" * W + "╗"
    mid = "╠" + "═" * W + "╣"
    bot = "╚" + "═" * W + "╝"
    b = lambda c: _box(c, W)

    if _is_en():
        lines = [
            "", top,
            b("      CYBERFIT MAINTENANCE DASHBOARD"),
            mid,
            b(""),
            b(f"  Operator: {_rpad(name, 10)}  Title: {_rpad(title, 12)}"),
            b(f"  Cyber Level: LV.{level}"),
            b(""),
            b("  XP:"),
            b(f"  {xp}"),
            b(""),
            mid,
            b(f"  ▸ Workouts Today:    {today_count}"),
            b(f"  ▸ Streak Days:       {streak}"),
            b(f"  ▸ Total Workouts:    {total_exercises}"),
            b(f"  ▸ Achievements:      {achievements_count}"),
            b(f"  ▸ Total Sessions:    {total_sessions}"),
            b(""),
            bot,
        ]
    else:
        lines = [
            "", top,
            b("      CYBERFIT 义体维护仪表盘"),
            mid,
            b(""),
            b(f"  操作员: {_rpad(name, 10)}  称号: {_rpad(title, 12)}"),
            b(f"  义体等级: LV.{level}"),
            b(""),
            b("  经验值:"),
            b(f"  {xp}"),
            b(""),
            mid,
            b(f"  ▸ 今日训练次数:  {today_count}"),
            b(f"  ▸ 连续打卡天数:  {streak}"),
            b(f"  ▸ 累计训练总数:  {total_exercises}"),
            b(f"  ▸ 已解锁成就:    {achievements_count}"),
            b(f"  ▸ 累计会话数:    {total_sessions}"),
            b(""),
            bot,
        ]

    return "\n".join(lines)


# ── exercise card ──────────────────────────────────────────────

def exercise_card(exercise):
    """运动卡片"""
    W = 45
    duration = exercise.get("duration_seconds", 0)
    reps = exercise.get("reps")

    if _is_en():
        metric = f"{reps} reps" if reps else f"{duration} sec"
        difficulty_label = "Difficulty"
        metric_label = "Time/Reps"
        instruction_label = "Instructions"
    else:
        metric = f"{reps} 次" if reps else f"{duration} 秒"
        difficulty_label = "难度"
        metric_label = "时长/次数"
        instruction_label = "操作指令"

    diff_stars = "★" * exercise["difficulty"] + "☆" * (3 - exercise["difficulty"])

    top = "┌" + "─" * W + "┐"
    sep = "├" + "─" * W + "┤"
    bot = "└" + "─" * W + "┘"
    b = lambda c: _box(c, W, "│", "│")

    lines = [
        "", top,
        b(f"  🦾 {exercise['cyber_name']}"),
        b(f"  ({exercise['real_name']})"),
        sep,
        b(f"  {_rpad(difficulty_label, 4)}: {diff_stars}   {_rpad(metric_label, 6)}: {metric}"),
        b(""),
        b(f"  {exercise['description']}"),
        b(""),
        b(f"  {instruction_label}:"),
    ]
    for instr_line in exercise['instructions'].split('\n'):
        lines.append(b(f"  {instr_line}"))
    lines.append(bot)
    return "\n".join(lines)


# ── achievement card ───────────────────────────────────────────

def achievement_card(achievement):
    """成就卡片"""
    W = 39
    top = "╔" + "═" * W + "╗"
    bot = "╚" + "═" * W + "╝"
    b = lambda c: _box(c, W)

    if _is_en():
        title = "Achievement Unlocked"
        time_label = "Unlocked"
    else:
        title = "成就解锁！"
        time_label = "解锁时间"

    lines = [
        "", top,
        b(f"  🏆 {title}"),
        b(""),
        b(f"  {achievement['name']}"),
        b(f"  {achievement['description']}"),
        b(""),
        b(f"  {time_label}: {achievement.get('unlocked_at', 'N/A')[:10]}"),
        bot,
    ]
    return "\n".join(lines)


# ── break banner ───────────────────────────────────────────────

def break_banner():
    """休息提醒横幅"""
    W = 50
    top = "╔" + "═" * W + "╗"
    bot = "╚" + "═" * W + "╝"
    b = lambda c: _box(c, W)

    if _is_en():
        lines = [
            "", top,
            b(""),
            b("   ⚠️  CYBERNETIC MAINTENANCE AI ALERT"),
            b(""),
            b("   Physical-layer maintenance required"),
            b("   Pause data flow and run the protocol below"),
            b(""),
            bot,
        ]
    else:
        lines = [
            "", top,
            b(""),
            b("   ⚠️  义体维护 AI 紧急通知"),
            b(""),
            b("   检测到操作员需要物理层维护"),
            b("   请暂停数据流，执行以下维护程序"),
            b(""),
            bot,
        ]
    return "\n".join(lines)


# ── session warning ────────────────────────────────────────────

def session_warning(minutes):
    """久坐警告"""
    W = 42
    top = "┌" + "─" * W + "┐"
    bot = "└" + "─" * W + "┘"
    b = lambda c: _box(c, W, "│", "│")

    if _is_en():
        lines = [
            "", top,
            b("  ⚠️ Sitting Alert"),
            b(""),
            b(f"  Continuous coding time: {minutes} min"),
            b("  Recommended maintenance: every 45 min"),
            b(""),
            b("  Run /cyberfit-break for protocol"),
            bot,
        ]
    else:
        lines = [
            "", top,
            b(f"  ⚠️ 久坐警告"),
            b(""),
            b(f"  当前连续编码: {minutes} 分钟"),
            b("  建议每 45 分钟进行一次义体维护"),
            b(""),
            b("  输入 /cyberfit-break 获取维护指令"),
            bot,
        ]
    return "\n".join(lines)


# ── plan display ───────────────────────────────────────────────

def plan_display(exercises, level, title):
    """健身计划展示"""
    W = 50
    top = "╔" + "═" * W + "╗"
    mid = "╠" + "═" * W + "╣"
    bot = "╚" + "═" * W + "╝"
    b = lambda c: _box(c, W)

    if _is_en():
        lines = [
            top,
            b("          CYBERFIT MAINTENANCE PLAN"),
            b(f"  Level: LV.{level}  Title: {_rpad(title, 22)}"),
            mid,
        ]
        for i, ex in enumerate(exercises, 1):
            reps = ex.get("reps")
            metric = f"{reps} reps" if reps else f"{ex['duration_seconds']} sec"
            lines.append(b(f"  {i}. {_rpad(ex['cyber_name'], 20)} ({ex['real_name']}) {metric}"))
    else:
        lines = [
            top,
            b("          CYBERFIT 义体维护计划"),
            b(f"  等级: LV.{level}  称号: {_rpad(title, 20)}"),
            mid,
        ]
        for i, ex in enumerate(exercises, 1):
            reps = ex.get("reps")
            metric = f"{reps}次" if reps else f"{ex['duration_seconds']}秒"
            lines.append(b(f"  {i}. {_rpad(ex['cyber_name'], 20)} ({ex['real_name']}) {metric}"))

    lines.append(b(""))
    lines.append(bot)
    return "\n".join(lines)


# ── achievements list ──────────────────────────────────────────

def achievements_list(achievements):
    """成就列表展示"""
    if not achievements:
        W2 = 37
        top = "┌" + "─" * W2 + "┐"
        bot = "└" + "─" * W2 + "┘"
        b2 = lambda c: _box(c, W2, "│", "│")
        if _is_en():
            return "\n".join(["", top,
                b2("  No unlocked achievements yet"),
                b2("  Start training to earn Street Cred"),
                bot])
        return "\n".join(["", top,
            b2("  暂无解锁成就"),
            b2("  开始训练以获取街头信誉！"),
            bot])

    W = 50
    top = "╔" + "═" * W + "╗"
    mid = "╠" + "═" * W + "╣"
    bot = "╚" + "═" * W + "╝"
    b = lambda c: _box(c, W)

    if _is_en():
        lines = [top,
            b("          🏆 STREET CRED ACHIEVEMENTS"),
            mid,
        ]
        time_label = "Unlocked"
    else:
        lines = [top,
            b("          🏆 街头信誉 — 成就系统"),
            mid,
        ]
        time_label = "解锁"

    for a in achievements:
        lines.append(b(f"  🏆 {a['name']}"))
        lines.append(b(f"     {a['description']}"))
        lines.append(b(f"     {time_label}: {a.get('unlocked_at', 'N/A')[:10]}"))
        lines.append(b(""))

    lines.append(bot)
    return "\n".join(lines)
