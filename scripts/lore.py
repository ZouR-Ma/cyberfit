"""
CyberFit lore text packs.
"""

import random

from . import i18n

BREAK_REMINDERS_ZH = [
    "⚠️ 警告：检测到操作员连续在线超时。肉体硬件过热风险 +15%。建议执行冷却协议。",
    "⚠️ 义体维护 AI 提示：你的生物组件需要维护。暂停数据流，执行物理校准。",
    "⚠️ 系统通知：操作员久坐时长超标。核心框架结构应力累积中，请立即干预。",
    "⚠️ 来自夜之城的忠告：再强的义体也撑不住一个报废的身体。起来动动，佣兵。",
    "⚠️ 维护优先级提升：你的碳基组件发出了保养请求。忽略它可比忽略段错误严重多了。",
    "⚠️ 神经接口注意：持续高负载操作导致接口温度异常。休息是最好的散热。",
]

BREAK_REMINDERS_EN = [
    "⚠️ Warning: Operator online duration exceeded threshold. Biological hardware overheat risk +15%. Initiate cooling protocol.",
    "⚠️ Cybernetic maintenance AI: your bio-components require service. Pause the data stream and run physical calibration.",
    "⚠️ System notice: prolonged sitting detected. Core frame stress is accumulating. Intervene now.",
    "⚠️ Night City memo: even chrome cannot save a body pushed to scrap. Move, merc.",
    "⚠️ Maintenance priority raised: your carbon chassis requested service. Ignoring this is worse than ignoring a segfault.",
    "⚠️ Neural interface alert: sustained high-load operation triggered thermal drift. Rest is your best heat sink.",
]

EXERCISE_INTROS_ZH = [
    "启动义体维护程序... 准备好了吗，佣兵？",
    "义体校准程序已加载。开始物理层优化。",
    "夜之城不需要坐废了的 netrunner。让我们保持战斗状态。",
    "正在连接你的运动协处理器... 执行以下维护指令：",
    "肉体是无法热插拔的硬件。现在进行定期保养。",
    "义体维护 AI 已接管。请跟随指令完成校准流程。",
]

EXERCISE_INTROS_EN = [
    "Booting cybernetic maintenance protocol... ready, merc?",
    "Calibration package loaded. Begin physical-layer optimization.",
    "Night City has no use for burned-out netrunners. Stay combat-ready.",
    "Linking your motion co-processor... execute the following maintenance steps:",
    "Your body is not hot-swappable hardware. Perform scheduled maintenance now.",
    "Cybernetic maintenance AI online. Follow the instructions for full calibration.",
]

EXERCISE_COMPLETIONS_ZH = [
    "维护完毕。系统性能恢复至最优状态。干得好，V。",
    "校准完成。你的战斗效能提升了。继续保持。",
    "义体状态已更新。你比夜之城 90% 的佣兵都保养得好。",
    "物理层优化完毕。回到数据洪流中去吧，但别忘了你是碳基的。",
    "程序执行成功。经验值已入账，街头信誉 +1。",
    "维护报告：所有模块运行正常。操作员状态——就绪。",
]

EXERCISE_COMPLETIONS_EN = [
    "Maintenance complete. System performance restored to optimal levels. Good work, V.",
    "Calibration successful. Combat efficiency increased. Keep this cadence.",
    "Cybernetic status updated. You maintain better than 90% of Night City mercs.",
    "Physical-layer optimization complete. Return to the data stream, but remember you're carbon-based.",
    "Execution successful. XP credited. Street Cred +1.",
    "Maintenance report: all modules nominal. Operator status: ready.",
]

ACHIEVEMENT_UNLOCKS_ZH = [
    "🏆 新成就解锁！你的街头信誉又提升了。夜之城开始注意到你了。",
    "🏆 义体升级完成！新的能力已写入你的神经接口。",
    "🏆 系统通知：操作员已达成里程碑。传奇之路又近一步。",
]

ACHIEVEMENT_UNLOCKS_EN = [
    "🏆 Achievement unlocked. Street Cred increased. Night City is starting to notice you.",
    "🏆 Cyberware upgrade complete. New capabilities written to your neural interface.",
    "🏆 System notice: milestone achieved. One step closer to legend status.",
]

DAILY_QUOTES_ZH = [
    "「在夜之城，身体就是最贵的投资。那些只升级大脑的 netrunner，最终都成了轮椅上的传说。」—— 维克多·韦克托",
    "「义体再强，也需要一副好底子。记住，你是在给原装硬件做保养。」—— 义体医生手册",
    "「每次休息都是一次系统重启。不要等到蓝屏了才想起来。」—— 夜之城健康公告",
    "「荒坂的精英们每天训练两小时。不是因为他们有时间，而是因为他们知道身体是真正的资产。」—— 企业内部报告",
    "「街上的佣兵分两种：保养身体的，和英年早逝的。」—— 来路人酒吧涂鸦",
    "「代码可以重构，Bug 可以修复，但你的脊椎只有一根。」—— 赛博朋克程序员守则",
]

DAILY_QUOTES_EN = [
    '"In Night City, your body is your most expensive investment. Netrunners who only upgrade the brain end up as legends in wheelchairs." - Viktor Vektor',
    '"Even top-tier chrome needs a solid foundation. You are maintaining original hardware." - Ripperdoc Manual',
    '"Every break is a system reboot. Do not wait for a blue screen to remember." - Night City Health Bulletin',
    '"Arasaka elites train two hours a day. Not because they have time, because they know the body is the real asset." - Internal Report',
    '"Street mercs come in two types: those who maintain their body, and those who burn out early." - Afterlife Graffiti',
    '"Code can be refactored. Bugs can be fixed. You only get one spine." - Cyberpunk Developer Rulebook',
]

STATUS_DESCRIPTIONS_ZH = {
    "excellent": "所有系统运行良好。义体状态：最优。你是夜之城最健康的佣兵。",
    "good": "系统状态正常。常规维护保持中。继续保持这个节奏。",
    "warning": "检测到轻微性能下降。建议增加维护频率。",
    "critical": "⚠️ 警告：多个子系统报告异常。需要立即执行全面维护！",
    "offline": "系统处于离线状态。执行 init 命令启动义体维护程序。",
}

STATUS_DESCRIPTIONS_EN = {
    "excellent": "All systems nominal. Cybernetic status: optimal. You are one of Night City's healthiest mercs.",
    "good": "System status stable. Routine maintenance in progress. Keep this rhythm.",
    "warning": "Mild performance degradation detected. Increase maintenance frequency.",
    "critical": "⚠️ Warning: multiple subsystems report anomalies. Immediate full maintenance required.",
    "offline": "System is offline. Run `init` to start cybernetic maintenance.",
}

RANK_TITLES_ZH = {
    1: ("流浪者", "刚踏入夜之城的新人，一切从零开始。"),
    2: ("街头小混混", "开始在街头混出名堂，但还有很长的路。"),
    3: ("网络浪人", "掌握了基本生存技能的数字游民。"),
    4: ("赏金猎人", "开始接到像样的委托了。"),
    5: ("V级佣兵", "夜之城公认的实力派，委托不断。"),
    6: ("荒坂精英", "企业级的战斗力与自律性。"),
    7: ("传奇佣兵", "名字在夜之城无人不知。"),
    8: ("夜之城传奇", "站在这座城市顶端的存在。"),
}

RANK_TITLES_EN = {
    1: ("Nomad", "A newcomer to Night City. Starting from zero."),
    2: ("Street Hustler", "Making a name on the streets, but the road is long."),
    3: ("Net Drifter", "A digital wanderer with core survival protocols online."),
    4: ("Bounty Hunter", "Real contracts are starting to land."),
    5: ("Tier-V Merc", "A proven operator in Night City with nonstop gigs."),
    6: ("Arasaka Elite", "Corporate-grade discipline and combat capability."),
    7: ("Legendary Merc", "A name known across the city."),
    8: ("Legend of Night City", "A figure standing at the top of the city."),
}

POSTURE_CHECKS_ZH = [
    "🔍 体态扫描启动...\n\n检查以下项目：\n• 肩膀是否耸起？放松下沉它们\n• 背部是否弓起？坐直，想象一根线从头顶拉起你\n• 双脚是否平放地面？调整椅子高度\n• 屏幕是否在视线水平？调整显示器位置\n• 手腕是否悬空？使用腕托或调整键盘位置",
    "🔍 义体姿态校准系统激活...\n\n扫描结果：\n• 颈部前倾角度检测 → 下巴收回，耳朵对齐肩膀\n• 脊柱曲度分析 → 保持自然 S 曲线\n• 骨盆倾斜检测 → 坐在坐骨上，不要歪斜\n• 呼吸模式分析 → 腹式呼吸，3 次深呼吸",
]

POSTURE_CHECKS_EN = [
    "🔍 Posture scan initiated...\n\nChecklist:\n• Are your shoulders raised? Relax and drop them\n• Is your back rounded? Sit tall, imagine a line pulling from your crown\n• Are both feet flat on the floor? Adjust chair height\n• Is the screen at eye level? Reposition monitor\n• Are your wrists floating? Use wrist support or adjust keyboard height",
    "🔍 Cyber posture calibration activated...\n\nScan result:\n• Forward-head angle detected -> tuck chin, align ears over shoulders\n• Spinal curvature analysis -> maintain natural S-curve\n• Pelvic tilt check -> sit on your sit bones, avoid leaning\n• Breathing pattern -> diaphragmatic breathing, 3 deep cycles",
]

# Backward compatibility aliases.
STATUS_DESCRIPTIONS = STATUS_DESCRIPTIONS_ZH
RANK_TITLES = RANK_TITLES_ZH


def _resolve_lang(lang=None):
    return i18n.normalize_lang(lang or i18n.get_lang())


def _pick(zh_data, en_data, lang=None):
    return en_data if _resolve_lang(lang) == "en" else zh_data


def random_break_reminder(lang=None):
    return random.choice(_pick(BREAK_REMINDERS_ZH, BREAK_REMINDERS_EN, lang))


def random_exercise_intro(lang=None):
    return random.choice(_pick(EXERCISE_INTROS_ZH, EXERCISE_INTROS_EN, lang))


def random_exercise_completion(lang=None):
    return random.choice(_pick(EXERCISE_COMPLETIONS_ZH, EXERCISE_COMPLETIONS_EN, lang))


def random_achievement_unlock(lang=None):
    return random.choice(_pick(ACHIEVEMENT_UNLOCKS_ZH, ACHIEVEMENT_UNLOCKS_EN, lang))


def random_daily_quote(lang=None):
    return random.choice(_pick(DAILY_QUOTES_ZH, DAILY_QUOTES_EN, lang))


def random_posture_check(lang=None):
    return random.choice(_pick(POSTURE_CHECKS_ZH, POSTURE_CHECKS_EN, lang))


def get_status_description(status, lang=None):
    descriptions = _pick(STATUS_DESCRIPTIONS_ZH, STATUS_DESCRIPTIONS_EN, lang)
    return descriptions.get(status, descriptions["good"])


def get_rank_info(level, lang=None):
    level = max(1, min(level, 8))
    ranks = _pick(RANK_TITLES_ZH, RANK_TITLES_EN, lang)
    return ranks.get(level, ranks[1])
