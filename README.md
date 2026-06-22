# Career Twin Workspace v1.0
**Platform:** Google Antigravity | **Architecture:** Standard Swarm | **Build:** 2026-04-07

---

## Đây là gì?

Career Twin Workspace là hệ thống **phát triển năng lực qua công việc thật**, vận hành bởi ba lớp Digital Twin và một MAS Swarm gồm 7 agents. Mỗi task bạn làm là một sự kiện học tập — không phải mô phỏng, không phải bài tập, mà là công việc thật với twin dẫn dắt, challenge và ghi nhận sự trưởng thành của bạn.

## Triết lý cốt lõi

> Twin không làm thay. Twin buộc bạn làm tốt hơn.

Ba nguyên tắc không thể vi phạm:
1. **Human First** — Bạn phải đưa ra approach trước, twin mới respond.
2. **Co-Work Mandatory** — Mọi task quan trọng đều có checkpoint của bạn.
3. **Reflection Required** — Không có reflection = session chưa đóng.

## 3 Lớp Twin

| Twin | Vai trò | Trạng thái |
|------|---------|-----------|
| **Core Professional Twin (CPT)** | Bộ kỹ năng nền tảng cho mọi knowledge worker | IMMUTABLE |
| **Current Self Twin (CST)** | Bản đồ năng lực thực tế của bạn hôm nay | READ-WRITE |
| **Future Role Twin (FRT)** | Model năng lực của vai trò bạn muốn trở thành | SEMI-IMMUTABLE |

## Bắt đầu ngay

```
1. Mở ONBOARDING.md → hoàn thành trong 30 phút
2. Chạy WF-INF-01 (Start Session)
3. Submit task đầu tiên của bạn
4. Để twin dẫn qua Lab 1
```

## Structure

```
ws-career-twin-v1/
├── manifest.yaml          ← Assembly blueprint
├── README.md              ← File này
├── ONBOARDING.md          ← Bắt đầu tại đây
├── QUICKSTART.md          ← Reference nhanh
├── COWORK-METHODOLOGY.md  ← Phương pháp co-work
├── .context/              ← Project context
├── KB/                    ← Knowledge Base
├── rules/                 ← Memory contract + governance
├── .agent/skills/         ← Skill modules (human + agent)
├── workflows/             ← 11 workflow definitions
├── agents/                ← 7 agent system instructions
├── twin-core/             ← CPT (immutable)
├── twin-current/          ← CST per user
├── twin-future/           ← FRT per user
├── projects/              ← Folder-based project system
└── training/              ← Onboarding + 5 Labs
```
