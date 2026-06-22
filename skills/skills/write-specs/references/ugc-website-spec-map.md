# UGC Website Spec Map

Map này giúp `write-specs` hiểu shape thật của `ugc-website` khi user yêu cầu viết hoặc cập nhật specs.

## Shared layer anchors

Ưu tiên đọc các anchor sau để hiểu app shell và route map:

- `src/components/AdminPageLayout.jsx`
- `src/routes/appRoutes.jsx`

Lưu ý: nếu workspace mở ở level cha, project app có thể nằm dưới thư mục `ugc-website/`. Khi đó prepend `ugc-website/` vào các path trên.

## Canonical module map

### Business modules

- `Dashboard`
- `Creator`
- `Mission`
- `Reward Request`
- `Website`

### Navigation grouping

- `Settings`

### Settings children

- `Shop Config`
- `Notification`
- `UGC Config`
- `System`

## Role rules cho Outline

- `11 Canonical — Module Catalog` là `catalog`
- `00 Global UI Patterns & Platform` là `shared-platform`
- `06 Settings` là `navigation-group`, không phải business module riêng
- `05 Website` là `module-owner`
- `06.03 UGC Config` là `module-owner`

## Code-to-outline caveat

- top-level routes trong code không map 1-1 hoàn toàn với tree trong Outline;
- `Settings` trong Outline là page cha để nhóm navigation, còn code có nhiều route con độc lập;
- hidden surfaces vẫn phải được tính là spec surfaces.

## Hidden surfaces phải bóc khi viết spec

- tabs
- drawer
- modal
- detail panel
- row actions
- form subpage nếu có

## Module anchors trong code

### Shared shell

- `src/components/AdminPageLayout.jsx`
- `src/routes/appRoutes.jsx`

### Creator

- `src/pages/Creator/index.jsx`
- `src/pages/Creator/CreatorTabs.jsx`
- `src/pages/Creator/CreatorDrawer.jsx`
- `src/pages/Creator/CreatorModals.jsx`

Child surfaces thường cần đọc:

- review
- rank change
- profile
- criteria
- label
- config
- drawer / modal actions

### Mission

- `src/pages/Mission/index.jsx`
- `src/pages/Mission/MissionCard.jsx`
- `src/pages/Mission/MissionFormModal.jsx`
- `src/pages/Mission/PostComponents.jsx`

Child surfaces thường cần đọc:

- list
- posts
- channel
- template
- add / edit / clone
- detail / modal flows

### Reward Request

- `src/pages/RewardRequest/index.jsx`
- `src/pages/RewardRequest/RewardRequestCard.jsx`

### Website

- `src/pages/Website/index.jsx`

Child surfaces cần split hoặc kiểm tra:

- Banner
- Article
- Media Library
- Sub-page

### Notification

- `src/pages/Notification/index.jsx`
- `src/pages/Notification/NotificationFormModal.jsx`
- `src/pages/Notification/AdminNotificationSettingsPanel.jsx`

### UGC Config

Trong code hiện tại route nằm trong nhóm settings.

Child surfaces cần split hoặc kiểm tra:

- Workflow
- Registration Config
- Supported Metrics
- Supported Field
- Point Config
- Contract

### Shop Config

- `src/pages/Reward/index.jsx`

Child surfaces thường cần đọc:

- gift code
- redeem
- shop item
- rewards
- point log
- lootable
- distribution history

### System

- `src/pages/System/index.jsx`
- `src/pages/System/AdminUsersPanel.jsx`
- `src/pages/System/PermissionGroupPanel.jsx`
