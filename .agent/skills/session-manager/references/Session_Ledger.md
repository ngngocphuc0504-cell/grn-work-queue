# Cấu trúc Ghi log Phiên Làm Việc (Session Ledger)

Mọi tóm tắt báo cáo phiên làm việc (Checkpoint / End-session) sinh ra bởi agent `session-manager` BẮT BUỘC phải tuân theo cấu trúc Markdown cứng sau đây để AssemblerAgent dễ dàng load cho phiên kế tiếp.

```markdown
## [YYYY-MM-DD HH:MM] Session Checkpoint

**State:** [Completed | Suspended | Halted]
**Primary Objectives Achieved:**
- [Thành quả 1 - Có ID Commit nếu có]
- [Thành quả 2]

**Knowledge Synced:**
- [Tên KI 1 mới sinh ra (nếu có)]

**Handoff Queue (Dang dở cho AI/Human phiên sau):**
- [ ] Cần làm tiếp việc A
- [ ] Đợi User duyệt file B
```
