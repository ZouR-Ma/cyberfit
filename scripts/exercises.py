"""
CyberFit 运动数据库
赛博朋克命名的健身动作库
"""

CATEGORIES = {
    "neural": {
        "name": "神经接口校准",
        "cyber_desc": "优化你的神经-肉体接口，防止信号衰减",
        "icon": "🧠"
    },
    "upper": {
        "name": "上肢动力模块",
        "cyber_desc": "强化上肢义体动力输出，提升操作精度",
        "icon": "💪"
    },
    "lower": {
        "name": "液压腿部系统",
        "cyber_desc": "维护下肢液压驱动单元，保持机动性",
        "icon": "🦿"
    },
    "core": {
        "name": "核心稳定器",
        "cyber_desc": "校准躯干核心框架，增强结构完整性",
        "icon": "⚡"
    },
    "cooldown": {
        "name": "义体冷却程序",
        "cyber_desc": "执行全身散热与系统恢复协议",
        "icon": "❄️"
    }
}

EXERCISES = [
    # === 神经接口校准 (颈部/眼部) ===
    {
        "id": "neural_01",
        "cyber_name": "光学植入体重置",
        "real_name": "眼部放松运动",
        "category": "neural",
        "difficulty": 1,
        "duration_seconds": 30,
        "reps": None,
        "description": "闭眼 → 缓慢转动眼球 → 注视远处。重启你的光学模块，消除数据流过载。",
        "instructions": "1. 闭上双眼，深呼吸 3 次\n2. 缓慢顺时针转动眼球 5 圈\n3. 逆时针转动 5 圈\n4. 睁眼注视 6 米外的物体 20 秒"
    },
    {
        "id": "neural_02",
        "cyber_name": "颈椎数据线维护",
        "real_name": "颈部拉伸",
        "category": "neural",
        "difficulty": 1,
        "duration_seconds": 40,
        "reps": None,
        "description": "活动颈部关节，防止神经接口处的信号线缠绕和老化。",
        "instructions": "1. 头部缓慢向右倾斜，保持 10 秒\n2. 向左倾斜，保持 10 秒\n3. 低头看地板，保持 10 秒\n4. 缓慢旋转头部一圈（左右各一次）"
    },
    {
        "id": "neural_03",
        "cyber_name": "20-20-20 协议",
        "real_name": "20-20-20 护眼法则",
        "category": "neural",
        "difficulty": 1,
        "duration_seconds": 20,
        "reps": None,
        "description": "每 20 分钟，注视 20 英尺外的目标 20 秒。标准的光学模组保养程序。",
        "instructions": "1. 视线离开屏幕\n2. 注视约 6 米远的物体\n3. 保持 20 秒\n4. 缓慢眨眼几次"
    },
    # === 上肢动力模块 (手腕/手臂/肩膀) ===
    {
        "id": "upper_01",
        "cyber_name": "腕部伺服电机润滑",
        "real_name": "手腕旋转拉伸",
        "category": "upper",
        "difficulty": 1,
        "duration_seconds": 30,
        "reps": None,
        "description": "旋转腕部关节，为精密操作伺服电机注入润滑。",
        "instructions": "1. 双手伸直，缓慢顺时针旋转手腕 10 圈\n2. 逆时针旋转 10 圈\n3. 握拳 → 张开，重复 10 次\n4. 手指交叉拉伸 10 秒"
    },
    {
        "id": "upper_02",
        "cyber_name": "肩甲动力铰链校准",
        "real_name": "肩部环绕运动",
        "category": "upper",
        "difficulty": 1,
        "duration_seconds": 30,
        "reps": None,
        "description": "释放肩部义体铰链的积累张力，恢复全范围活动能力。",
        "instructions": "1. 双肩向前环绕 10 圈\n2. 向后环绕 10 圈\n3. 耸肩保持 5 秒，放松\n4. 重复耸肩 5 次"
    },
    {
        "id": "upper_03",
        "cyber_name": "大力神臂推送测试",
        "real_name": "桌面俯卧撑",
        "category": "upper",
        "difficulty": 2,
        "duration_seconds": 60,
        "reps": 15,
        "description": "利用桌面进行低负载推送测试，验证上肢动力模块输出。",
        "instructions": "1. 双手撑在桌边，身体倾斜\n2. 弯曲手肘，身体靠近桌面\n3. 推起回到起始位置\n4. 重复 15 次"
    },
    {
        "id": "upper_04",
        "cyber_name": "螳螂刀片展开",
        "real_name": "手指拉伸",
        "category": "upper",
        "difficulty": 1,
        "duration_seconds": 30,
        "reps": None,
        "description": "展开并测试每根手指的独立控制回路，预防键盘操作疲劳。",
        "instructions": "1. 双手张开，用力伸展手指 5 秒\n2. 握拳 5 秒\n3. 逐根弯曲伸展手指\n4. 双手合十，缓慢下压拉伸"
    },
    # === 液压腿部系统 (腿部) ===
    {
        "id": "lower_01",
        "cyber_name": "液压腿部升级",
        "real_name": "深蹲",
        "category": "lower",
        "difficulty": 2,
        "duration_seconds": 60,
        "reps": 15,
        "description": "全行程液压活塞测试，强化下肢驱动单元的力量输出。",
        "instructions": "1. 双脚与肩同宽站立\n2. 臀部向后坐，弯曲膝盖下蹲\n3. 大腿与地面平行时停顿\n4. 站起回到起始位置，重复 15 次"
    },
    {
        "id": "lower_02",
        "cyber_name": "强化跳跃模组",
        "real_name": "踮脚提踵",
        "category": "lower",
        "difficulty": 1,
        "duration_seconds": 40,
        "reps": 20,
        "description": "激活小腿液压弹射模块，为紧急机动储备动力。",
        "instructions": "1. 双脚与肩同宽站立\n2. 缓慢踮起脚尖，感受小腿收紧\n3. 保持 2 秒后缓慢落下\n4. 重复 20 次"
    },
    {
        "id": "lower_03",
        "cyber_name": "二段跳初始化",
        "real_name": "原地高抬腿",
        "category": "lower",
        "difficulty": 2,
        "duration_seconds": 30,
        "reps": 20,
        "description": "高频率交替抬腿，初始化二段跳系统的响应速度。",
        "instructions": "1. 原地站立\n2. 交替抬起膝盖至腰部高度\n3. 保持节奏，持续 30 秒\n4. 共完成约 20 次（每侧 10 次）"
    },
    {
        "id": "lower_04",
        "cyber_name": "弓步推进器测试",
        "real_name": "弓步蹲",
        "category": "lower",
        "difficulty": 2,
        "duration_seconds": 60,
        "reps": 10,
        "description": "单腿推进器负载测试，确认双腿动力输出对称。",
        "instructions": "1. 站直，一脚向前迈出一大步\n2. 后膝下蹲接近地面\n3. 推起回到站立\n4. 换腿，每侧 10 次"
    },
    # === 核心稳定器 (腰腹) ===
    {
        "id": "core_01",
        "cyber_name": "装甲框架强化",
        "real_name": "平板支撑",
        "category": "core",
        "difficulty": 2,
        "duration_seconds": 30,
        "reps": None,
        "description": "启动躯干装甲框架的全面张力测试，强化核心结构完整性。",
        "instructions": "1. 俯卧，前臂撑地\n2. 身体绷直如一条线\n3. 收紧腹部，保持 30 秒\n4. 呼吸保持平稳"
    },
    {
        "id": "core_02",
        "cyber_name": "陀螺仪校准",
        "real_name": "站立转体",
        "category": "core",
        "difficulty": 1,
        "duration_seconds": 30,
        "reps": 20,
        "description": "旋转躯干校准内部陀螺仪，保持运动中的平衡精度。",
        "instructions": "1. 双脚与肩同宽站立\n2. 双手抱胸或叉腰\n3. 上身向左转，保持 2 秒\n4. 向右转，保持 2 秒\n5. 交替重复共 20 次"
    },
    {
        "id": "core_03",
        "cyber_name": "腹压稳定程序",
        "real_name": "椅子卷腹",
        "category": "core",
        "difficulty": 2,
        "duration_seconds": 45,
        "reps": 15,
        "description": "坐姿激活核心稳定器，建立内部腹压保护系统。",
        "instructions": "1. 坐在椅子前半部分\n2. 身体略向后倾\n3. 双腿并拢抬起膝盖\n4. 缓慢放下，不要触地\n5. 重复 15 次"
    },
    # === 义体冷却程序 (拉伸放松) ===
    {
        "id": "cooldown_01",
        "cyber_name": "系统散热序列",
        "real_name": "全身拉伸",
        "category": "cooldown",
        "difficulty": 1,
        "duration_seconds": 60,
        "reps": None,
        "description": "执行全身散热程序，降低各模块运行温度。",
        "instructions": "1. 双手交叉高举过头，拉伸侧腰各 10 秒\n2. 弯腰触碰脚尖，保持 15 秒\n3. 坐姿，一腿伸直前压，每侧 15 秒\n4. 深呼吸 5 次收尾"
    },
    {
        "id": "cooldown_02",
        "cyber_name": "义体排气阀释放",
        "real_name": "深呼吸放松",
        "category": "cooldown",
        "difficulty": 1,
        "duration_seconds": 60,
        "reps": None,
        "description": "打开排气阀释放系统内部积压，平衡身心负载。",
        "instructions": "1. 闭眼，用鼻子深吸气 4 秒\n2. 屏住呼吸 4 秒\n3. 用嘴缓慢呼气 6 秒\n4. 重复 5-8 个循环"
    },
    {
        "id": "cooldown_03",
        "cyber_name": "背部散热板展开",
        "real_name": "猫牛式伸展",
        "category": "cooldown",
        "difficulty": 1,
        "duration_seconds": 40,
        "reps": None,
        "description": "交替弓背与塌腰，展开背部散热结构释放久坐热量。",
        "instructions": "1. 四肢着地（桌面旁可用椅子辅助）\n2. 弓背低头（猫式），保持 5 秒\n3. 塌腰抬头（牛式），保持 5 秒\n4. 交替重复 8 次"
    },
    {
        "id": "cooldown_04",
        "cyber_name": "液压关节释压",
        "real_name": "坐姿脊柱扭转",
        "category": "cooldown",
        "difficulty": 1,
        "duration_seconds": 40,
        "reps": None,
        "description": "旋转释放脊柱各关节积压，恢复椎间灵活度。",
        "instructions": "1. 端坐椅上，双脚平放地面\n2. 左手放右膝外侧\n3. 身体缓慢向右旋转，保持 15 秒\n4. 换另一侧，保持 15 秒"
    },
]


def get_exercises_by_category(category):
    """按分类获取运动"""
    return [e for e in EXERCISES if e["category"] == category]


def get_exercise_by_id(exercise_id):
    """按 ID 获取运动"""
    for e in EXERCISES:
        if e["id"] == exercise_id:
            return e
    return None


def find_exercise(query):
    """模糊搜索运动（按ID、赛博名称、真实名称）"""
    query_lower = query.lower()
    for e in EXERCISES:
        if (query_lower == e["id"].lower() or
            query_lower in e["cyber_name"].lower() or
            query_lower in e["real_name"].lower()):
            return e
    return None


def get_exercises_by_difficulty(max_difficulty):
    """按最大难度获取运动"""
    return [e for e in EXERCISES if e["difficulty"] <= max_difficulty]


def get_quick_exercises(max_duration=60):
    """获取快速运动（按时长）"""
    return [e for e in EXERCISES if e["duration_seconds"] <= max_duration]
