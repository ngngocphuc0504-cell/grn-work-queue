# Tech Spec Format

Dùng khi bàn giao cho dev team hoặc document hệ thống.

## Template

```markdown
# Tech Spec: [Tên Tool]
**Status:** Draft / Review / Approved
**PM:** [tên] | **Dev:** [tên] | **Date:** [ngày]

## Overview
- **Mục đích:** [1-2 câu]
- **Users:** [số lượng ước tính, role]
- **Timeline:** [deadline]

## Tech Stack
- Frontend: [React / HTML / ...]
- Backend: [nếu có]
- Database: [nếu có]
- Hosting: [nếu có]

## Features & Scope

### In Scope
| Feature | Priority | Notes |
|---|---|---|
| [Feature 1] | P0 | [ghi chú] |

### Out of Scope
- [Tính năng sẽ không làm trong version này]

## Data Model
[Mô tả các entity chính và relationship]

## API Endpoints (nếu có)
| Method | Endpoint | Description |
|---|---|---|
| GET | /api/... | ... |

## Permission Matrix
| Action | Viewer | Editor | Admin |
|---|---|---|---|
| Xem dashboard | ✓ | ✓ | ✓ |
| Chỉnh sửa | ✗ | ✓ | ✓ |

## Non-functional Requirements
- Performance: load < 3s
- Browser support: Chrome, Edge (latest 2 versions)
- Data retention: [...]
```
