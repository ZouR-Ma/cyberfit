"""
CyberFit ASCII Art & 赛博朋克终端 UI
"""


def banner():
    """CyberFit 主横幅"""
    return r"""
╔══════════════════════════════════════════════════════════════╗
║   ██████╗██╗   ██╗██████╗ ███████╗██████╗ ███████╗██╗████████╗  ║
║  ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗██╔════╝██║╚══██╔══╝  ║
║  ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝█████╗  ██║   ██║     ║
║  ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗██╔══╝  ██║   ██║     ║
║  ╚██████╗   ██║   ██████╔╝███████╗██║  ██║██║     ██║   ██║     ║
║   ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝   ╚═╝     ║
║                                                                  ║
║           「身体是最重要的硬件，不可替换」                              ║
║                  夜之城 · 义体维护系统 v1.0                           ║
╚══════════════════════════════════════════════════════════════╝
"""


def mini_banner():
    """小型横幅"""
    return """
┌─────────────────────────────────────┐
│  CYBERFIT // 义体维护系统            │
│  「身体是最重要的硬件」               │
└─────────────────────────────────────┘"""


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


def dashboard(profile, today_count, streak, achievements_count):
    """生成赛博朋克仪表盘"""
    level = profile.get("level", 1)
    title = profile.get("title", "流浪者")
    total_xp = profile.get("total_xp", 0)
    next_xp = level * 100
    stats = profile.get("stats", {})
    total_sessions = stats.get("total_sessions", 0)
    total_exercises = stats.get("total_exercises", 0)

    return f"""
╔══════════════════════════════════════════════════╗
║          CYBERFIT 义体维护仪表盘                   ║
╠══════════════════════════════════════════════════╣
║                                                  ║
║  操作员: {profile.get('cyber_name', 'V'):<10}  称号: {title:<12}   ║
║  义体等级: LV.{level:<5}                              ║
║                                                  ║
║  经验值:                                          ║
║  {xp_bar(total_xp % next_xp, next_xp, level):<46} ║
║                                                  ║
╠══════════════════════════════════════════════════╣
║  ▸ 今日训练次数:  {today_count:<5}                       ║
║  ▸ 连续打卡天数:  {streak:<5}                       ║
║  ▸ 累计训练总数:  {total_exercises:<5}                       ║
║  ▸ 已解锁成就:    {achievements_count:<5}                       ║
║  ▸ 累计会话数:    {total_sessions:<5}                       ║
║                                                  ║
╚══════════════════════════════════════════════════╝"""


def exercise_card(exercise):
    """运动卡片"""
    duration = exercise.get("duration_seconds", 0)
    reps = exercise.get("reps")
    metric = f"{reps} 次" if reps else f"{duration} 秒"
    diff_stars = "★" * exercise["difficulty"] + "☆" * (3 - exercise["difficulty"])

    return f"""
┌─────────────────────────────────────────────┐
│  🦾 {exercise['cyber_name']:<38} │
│  ({exercise['real_name']})                            │
├─────────────────────────────────────────────┤
│  难度: {diff_stars}   时长/次数: {metric:<10}       │
│                                             │
│  {exercise['description']:<43} │
│                                             │
│  操作指令:                                   │
│  {exercise['instructions'].replace(chr(10), chr(10) + '│  '):<43} │
└─────────────────────────────────────────────┘"""


def achievement_card(achievement):
    """成就卡片"""
    return f"""
╔═══════════════════════════════════════╗
║  🏆 成就解锁！                         ║
║                                       ║
║  {achievement['name']:<35} ║
║  {achievement['description']:<35} ║
║                                       ║
║  解锁时间: {achievement.get('unlocked_at', 'N/A')[:10]:<24} ║
╚═══════════════════════════════════════╝"""


def break_banner():
    """休息提醒横幅"""
    return """
╔══════════════════════════════════════════════════╗
║                                                  ║
║   ⚠️  义体维护 AI 紧急通知                         ║
║                                                  ║
║   检测到操作员需要物理层维护                         ║
║   请暂停数据流，执行以下维护程序                      ║
║                                                  ║
╚══════════════════════════════════════════════════╝"""


def session_warning(minutes):
    """久坐警告"""
    return f"""
┌──────────────────────────────────────────┐
│  ⚠️ 久坐警告                              │
│                                          │
│  当前连续编码: {minutes} 分钟                │
│  建议每 45 分钟进行一次义体维护              │
│                                          │
│  输入 /cyberfit-break 获取维护指令          │
└──────────────────────────────────────────┘"""


def plan_display(exercises, level, title):
    """健身计划展示"""
    lines = [
        "╔══════════════════════════════════════════════════╗",
        "║          CYBERFIT 义体维护计划                     ║",
        f"║  等级: LV.{level}  称号: {title:<20}           ║",
        "╠══════════════════════════════════════════════════╣",
    ]
    for i, ex in enumerate(exercises, 1):
        reps = ex.get("reps")
        metric = f"{reps}次" if reps else f"{ex['duration_seconds']}秒"
        line = f"║  {i}. {ex['cyber_name']:<20} ({ex['real_name']}) {metric:<8} ║"
        lines.append(line)
    lines.append("║                                                  ║")
    lines.append("╚══════════════════════════════════════════════════╝")
    return "\n".join(lines)


def achievements_list(achievements):
    """成就列表展示"""
    if not achievements:
        return """
┌─────────────────────────────────────┐
│  暂无解锁成就                        │
│  开始训练以获取街头信誉！              │
└─────────────────────────────────────┘"""

    lines = [
        "╔══════════════════════════════════════════════════╗",
        "║          🏆 街头信誉 — 成就系统                    ║",
        "╠══════════════════════════════════════════════════╣",
    ]
    for a in achievements:
        lines.append(f"║  🏆 {a['name']:<40}   ║")
        lines.append(f"║     {a['description']:<40}   ║")
        lines.append(f"║     解锁: {a.get('unlocked_at', 'N/A')[:10]:<34}   ║")
        lines.append("║                                                  ║")
    lines.append("╚══════════════════════════════════════════════════╝")
    return "\n".join(lines)
