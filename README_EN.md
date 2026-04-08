<div align="center">

# CyberFit 🦾

> *"Your coworker dumped the legacy mess on you and bounced. Your ex wrecked your sleep and left. But they both forgot one thing: the one who shouldn't rot at the desk is you."*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3](https://img.shields.io/badge/Python-3-blue.svg)](https://python.org)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)

**English | [中文](README.md)**

<br>

Coworkers keep handing you inherited code ruins while they job-hop for a raise?<br>
Your ex keeps detonating your nights while you push code all day with zero sleep?<br>
You're swallowing every fire, skipping water, skipping breaks, skipping life?<br>
You've been glued to the chair so long your neck, wrists, and lower back are all filing incident reports?<br>
Your body is quietly failing and you don't even notice anymore?<br>

**That's the edge. Keep going like this and your hardware goes down first.**

<br>

These messes already stole your time, energy, and focus.<br>
They should not get your body too.<br>
CyberFit exists for one reason:<br>
**Protect the only non-replaceable hardware you have before everything else burns it out.**

<br>

[Install](#install) · [Usage](#usage) · [Exercise Library](#exercise-categories) · [Ranks](#rank-system)

</div>

---

## Not Another Fitness App

There are thousands of fitness apps. Most assume you have spare time, stable mood, and life margin.

You don't.

You're getting buried by deadlines, message pings, random requests, and inherited systems that never stop breaking. You sit for 10-12 hours, and pain moves from neck to back to mind. You don't need a "30-day abs challenge." You need **something that drags you back before you collapse**.

CyberFit is that something.

It doesn't whisper generic motivation. It speaks like a Night City cybernetic maintenance AI:
**"Your carbon-based hardware is overheating. Run cooling protocol now. Stand up."**

---

## Why Cyberpunk

Because software work is already cyberpunk.

In cyberpunk worlds, humans are consumable parts in an optimization engine. Sound familiar? Your desk is the coffin. Your task list is your implant load. The codebase you inherited is the wreckage from the previous merc.

The only difference: people in cyberpunk at least choose to fight back.

**Squat is "Hydraulic Leg Upgrade." Plank is "Armor Frame Reinforcement." Eye rest is "Optical Implant Reset."** Not for cosplay. For framing maintenance as what it is: critical ops.

---

## Features

| Feature | Description |
|------|------|
| **Maintenance Alerts** | Detects long sedentary sessions and pushes break protocols |
| **Cyberpunk Exercise Library** | 20+ exercises with cyberpunk naming and practical instructions |
| **Adaptive Plan Generator** | Builds plans from your level and current condition |
| **Workout Logging + XP** | Every session grants XP and visible progression |
| **Achievement System** | 15 achievements, from "Awakening" to "Cyber Deity" |
| **Rank Titles** | Progress from "Nomad" to "Legend of Night City" |
| **Posture Scan** | Quick posture diagnostics in cyberpunk flavor |
| **ASCII Dashboard** | Terminal-native UI with full status readout |
| **Bilingual UI** | Built-in English/Chinese switching via CLI command |

---

## Install

### Claude Code (Recommended)

```bash
# Install globally (available in all projects)
git clone git@github.com:ZouR-Ma/cyberfit.git ~/.claude/skills/cyberfit

# Or install in current project
mkdir -p .claude/skills
git clone git@github.com:ZouR-Ma/cyberfit.git .claude/skills/cyberfit
```

### Initialize

```bash
cd cyberfit
python3 scripts/cli.py init
```

If you see the large ASCII banner, the maintenance system is online.

---

## Usage

### Slash Commands

Use directly in Claude Code:

| Command | Description |
|------|------|
| `/cyberfit` | Main entry with quick dashboard |
| `/cyberfit-break` | Immediate cooling protocol and movement instructions |
| `/cyberfit-plan` | Generate today's maintenance blueprint |
| `/cyberfit-log <exercise>` | Log workout and gain XP |
| `/cyberfit-status` | Full diagnostics panel |
| `/cyberfit-posture` | Posture scan |

### CLI Commands

```bash
python3 scripts/cli.py init            # boot system
python3 scripts/cli.py status          # dashboard
python3 scripts/cli.py break-suggest   # recommend break exercises
python3 scripts/cli.py log <exercise>  # record training
python3 scripts/cli.py plan [level]    # generate training plan
python3 scripts/cli.py achievements    # view Street Cred
python3 scripts/cli.py posture-check   # posture scan
python3 scripts/cli.py check-session   # check sitting duration risk
python3 scripts/cli.py lang <en|zh>    # switch language
```

---

## Exercise Categories

| Category | CyberFit Name | What This Targets |
|------|-------------|------------------------|
| neural | Neural Interface Calibration | Eye strain and forward-head posture from screen overload |
| upper | Upper Limb Power Module | Wrists, forearms, shoulders stressed by long coding sessions |
| lower | Hydraulic Leg System | Legs and circulation degraded by prolonged sitting |
| core | Core Stabilizer | Lower back and trunk support capacity |
| cooldown | Cooling Protocol | Stress release, breathing, and full-body decompression |

---

## Rank System

| Level | Title | Meaning |
|------|------|------|
| LV.1 | Nomad | You just recognized the body-burnout trajectory |
| LV.2 | Street Hustler | First signs of resistance |
| LV.3 | Net Drifter | Baseline maintenance habit formed |
| LV.4 | Bounty Hunter | Body starts responding |
| LV.5 | Tier-V Merc | Health discipline above most devs |
| LV.6 | Arasaka Elite | Better resilience under pressure |
| LV.7 | Legendary Merc | Body becomes a force multiplier |
| LV.8 | Legend of Night City | **The chaos didn't break you.** |

---

## Output Example

> After 2 hours of continuous coding:

```text
⚠️ Warning: Operator online duration exceeded threshold.
Biological hardware overheat risk +15%.
Initiate cooling protocol.

┌─────────────────────────────────────────────┐
│  🦾 Optical Implant Reset                    │
│  (Eye Relaxation Drill)                      │
├─────────────────────────────────────────────┤
│  Difficulty: ★☆☆   Time/Reps: 30 sec        │
│                                             │
│  Close your eyes, rotate your gaze, then    │
│  focus at distance to reboot optics.        │
└─────────────────────────────────────────────┘
```

> After workout completion:

```text
✅ Maintenance complete. System performance restored.

  XP Earned: +15 XP
  Level: LV.1 - Nomad
  Streak: 1 day

🏆 Achievement unlocked: "Awakening"
```

---

## Project Structure

```text
cyberfit/
├── SKILL.md              # AgentSkills entry
├── CLAUDE.md             # Claude Code persona instructions
├── README.md
├── README_EN.md
├── LICENSE
├── package.json
├── requirements.txt      # Python dependencies
├── .gitignore
├── .claude-plugin/       # Claude Code plugin config
│   ├── plugin.json
│   └── marketplace.json
├── prompts/              # Prompt templates
│   ├── cyberfit.md
│   ├── cyberfit-break.md
│   ├── cyberfit-plan.md
│   ├── cyberfit-log.md
│   ├── cyberfit-status.md
│   └── cyberfit-posture.md
├── skills/               # Sub-skills
│   ├── cyberfit-break/
│   ├── cyberfit-plan/
│   ├── cyberfit-log/
│   ├── cyberfit-status/
│   ├── cyberfit-posture/
│   └── cyberfit-achievements/
├── scripts/              # Python CLI tools
│   ├── cli.py
│   ├── core.py
│   ├── data.py
│   ├── i18n.py
│   ├── exercises.py
│   ├── achievements.py
│   ├── planner.py
│   ├── ascii_art.py
│   └── lore.py
├── hooks/                # Claude Code hooks
│   ├── hooks.json
│   └── session-start/
└── data/
    └── .gitkeep
```

---

## Data Storage

User data is stored under `~/.cyberfit/`:

```text
~/.cyberfit/
├── profile.json       # operator profile
├── logs.json          # workout logs
├── achievements.json  # unlocked achievements
├── sessions.json      # coding sessions
└── config.json        # language preference (en/zh)
```

---

## Why This Exists

Because too many developers normalize pain until it becomes permanent.

We keep saying, "I'll stand up after this function," then three hours vanish. We keep fixing systems while ignoring the one system that runs all of it.

Code can be refactored. Bugs can be fixed. You only get one spine.

**CyberFit will not turn you into a fitness influencer. It does one thing well: every ~45 minutes, it pulls you out of the chair before burnout wins.**

---

## Related Projects

- [同事.skill](https://github.com/titanwings/colleague-skill) - Coworker disappeared? Let AI pick up the work
- [前任.skill](https://github.com/titanwings/ex-skill) - Breakup chaos? Cyber coping toolkit

---

<div align="center">

**Your body is core hardware. Not replaceable.**

**Stand up before the system fails.**

MIT License © [ZouR-Ma](https://github.com/ZouR-Ma)

</div>
