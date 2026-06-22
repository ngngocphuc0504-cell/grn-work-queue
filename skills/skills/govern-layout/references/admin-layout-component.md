# AdminLayout Component — ProLayout-inspired, antd v6 native

Hướng dẫn build shared AdminLayout component package, lấy best practices từ Ant Design ProLayout nhưng dùng antd v6 core thuần. Không phụ thuộc ProComponents, không cần umi.

---

## 1. ARCHITECTURE OVERVIEW

```
@garena/admin-layout/
├── AdminLayout.jsx          # Main layout wrapper (ProLayout equivalent)
├── PageContainer.jsx        # Page header + breadcrumb + tabs
├── FooterToolbar.jsx        # Fixed bottom action bar
├── LayoutContext.js          # Shared layout state
├── layout-tokens.js          # Layout design tokens
├── menu-utils.js             # Route → Menu transform
├── breadcrumb-utils.js       # Route → Breadcrumb transform
└── index.js                  # Public exports
```

---

## 2. LAYOUT TOKENS

Token system lấy cảm hứng từ ProLayout nhưng đơn giản hơn.

```javascript
// layout-tokens.js

/**
 * Layout tokens — single source of truth cho layout dimensions & colors.
 * Import vào mọi project trong ecosystem.
 * Override per-project bằng cách merge với project-specific tokens.
 */

export const defaultLayoutTokens = {
  // ─── Header ───
  header: {
    colorBgHeader: '#ffffff',
    colorBorderHeader: '#f0f0f0',
    heightLayoutHeader: 48,
    paddingInlineHeader: 24,
    // Content zones
    showBreadcrumb: true,
    showSearch: false,
    showLanguageSwitch: true,
    showNotifications: true,
  },

  // ─── Sider (Sidebar) ───
  sider: {
    colorMenuBackground: '#001529',        // Dark theme default
    colorTextMenu: 'rgba(255,255,255,0.65)',
    colorTextMenuSelected: '#ffffff',
    colorTextMenuActive: '#ffffff',
    colorBgMenuItemSelected: 'rgba(255,255,255,0.08)',
    colorBgMenuItemHover: 'rgba(255,255,255,0.04)',
    colorMenuItemDivider: 'rgba(255,255,255,0.08)',
    colorBgCollapsedButton: 'transparent',
    menuWidth: 200,
    collapsedWidth: 64,
    menuItemHeight: 40,
    menuIconSize: 18,
    fixSiderbar: true,
    // Logo
    logoHeight: 48,
    showLogo: true,
    // User section
    showUserSection: true,
    userSectionHeight: 56,
  },

  // ─── Content ───
  content: {
    colorBgContent: '#f5f5f5',             // colorBgLayout
    paddingContent: 16,
    // Nếu muốn content có max-width (centered layout)
    maxWidthContent: 'none',               // 'none' = full width, hoặc 1200
  },

  // ─── Page Container ───
  pageContainer: {
    paddingPageHeader: 0,
    marginBottomPageHeader: 16,
    // Card wrapper
    cardPadding: 24,
    cardBorderRadius: 8,
    cardGap: 16,
  },

  // ─── Overlays ───
  modal: {
    widthSmall: 416,
    widthDefault: 520,
    widthLarge: 720,
    widthXLarge: 1000,
  },
  drawer: {
    widthDefault: 600,
    widthWide: 800,
  },

  // ─── Responsive ───
  responsive: {
    mobileBreakpoint: 768,
    collapseBreakpoint: 992,
    siderDrawerOnMobile: true,
  },
};

/**
 * Dark sidebar variant (Garena standard)
 */
export const darkSiderTokens = {
  sider: {
    colorMenuBackground: '#001529',
    colorTextMenu: 'rgba(255,255,255,0.65)',
    colorTextMenuSelected: '#ffffff',
    colorBgMenuItemSelected: 'rgba(255,255,255,0.08)',
    colorBgMenuItemHover: 'rgba(255,255,255,0.04)',
    colorMenuItemDivider: 'rgba(255,255,255,0.08)',
  },
};

/**
 * Light sidebar variant
 */
export const lightSiderTokens = {
  sider: {
    colorMenuBackground: '#ffffff',
    colorTextMenu: 'rgba(0,0,0,0.88)',
    colorTextMenuSelected: '#1677ff',
    colorBgMenuItemSelected: '#e6f4ff',
    colorBgMenuItemHover: 'rgba(0,0,0,0.04)',
    colorMenuItemDivider: '#f0f0f0',
  },
};

/**
 * Merge project tokens với defaults
 */
export function createLayoutTokens(overrides = {}) {
  return deepMerge(defaultLayoutTokens, overrides);
}
```

---

## 3. LAYOUT CONTEXT

Share layout state across components (giống ProLayout RouteContext).

```javascript
// LayoutContext.js
import { createContext, useContext } from 'react';

/**
 * LayoutContext — share layout state cho nested components.
 *
 * Ví dụ: FooterToolbar cần biết siderWidth để position đúng.
 * Ví dụ: Component cần biết isMobile để render khác nhau.
 */
export const LayoutContext = createContext({
  // Shell state
  collapsed: false,
  isMobile: false,
  siderWidth: 200,
  headerHeight: 48,

  // Navigation
  pathname: '/',
  breadcrumbItems: [],
  selectedMenuKeys: [],
  openMenuKeys: [],

  // Layout info
  layout: 'side',        // 'side' | 'top'
  navTheme: 'dark',      // 'dark' | 'light'
  hasSider: true,
  hasHeader: true,

  // Actions
  setCollapsed: () => {},
  navigate: () => {},
});

export const useLayoutContext = () => useContext(LayoutContext);
```

---

## 4. MENU UTILITIES

Transform route config → antd Menu items (giống ProLayout auto-menu).

```javascript
// menu-utils.js

/**
 * Route config format (giống ProLayout MenuDataItem).
 * Đây là cấu trúc mà mỗi project define.
 */
/*
const routes = [
  {
    path: '/dashboard',
    name: 'Dashboard',
    icon: <DashboardOutlined />,
  },
  {
    path: '/creator',
    name: 'Creator',
    icon: <UserOutlined />,
    badge: 47,                    // Optional: hiện badge count
    children: [
      { path: '/creator/approval', name: 'Approval Center' },
      { path: '/creator/profile', name: 'Creator Profile' },
      { path: '/creator/criteria', name: 'Criteria', hideInMenu: true },
    ],
  },
  {
    path: '/mission',
    name: 'Mission',
    icon: <FlagOutlined />,
    children: [
      { path: '/mission/create', name: 'Create Mission' },
      { path: '/mission/post', name: 'Manage Mission Post' },
    ],
  },
];
*/

/**
 * Convert route config → antd Menu items.
 * Handles: hideInMenu, disabled, badge, flatMenu, icon.
 */
export function routesToMenuItems(routes, options = {}) {
  if (!routes) return [];

  return routes
    .filter(route => !route.hideInMenu)
    .map(route => {
      const item = {
        key: route.path,
        label: route.badge
          ? renderWithBadge(route.name, route.badge)
          : route.name,
        icon: route.icon,
        disabled: route.disabled,
      };

      if (route.children?.length) {
        // flatMenu: ẩn parent, hiện children ở cùng level
        if (route.flatMenu) {
          return routesToMenuItems(route.children, options);
        }

        const visibleChildren = route.children.filter(c => !c.hideInMenu);
        if (visibleChildren.length > 0) {
          item.children = routesToMenuItems(visibleChildren, options);
        }
      }

      return item;
    })
    .flat(); // Flatten nếu có flatMenu
}

/**
 * Tìm selected keys dựa trên current pathname.
 * Matches exact path hoặc parent path.
 */
export function getSelectedKeys(routes, pathname) {
  const keys = [];

  function findMatch(items, parents = []) {
    for (const item of items) {
      if (item.path === pathname) {
        keys.push(item.path, ...parents.map(p => p.path));
        return true;
      }
      if (item.children) {
        if (findMatch(item.children, [...parents, item])) return true;
      }
    }
    return false;
  }

  findMatch(routes);

  // Fallback: partial match (ví dụ /creator/123 → match /creator)
  if (keys.length === 0) {
    // Find longest prefix match
    let bestMatch = '';
    function findPrefix(items) {
      for (const item of items) {
        if (pathname.startsWith(item.path) && item.path.length > bestMatch.length) {
          bestMatch = item.path;
        }
        if (item.children) findPrefix(item.children);
      }
    }
    findPrefix(routes);
    if (bestMatch) keys.push(bestMatch);
  }

  return keys;
}

/**
 * Tìm open keys (submenu nào cần mở).
 */
export function getOpenKeys(routes, pathname) {
  const openKeys = [];

  function findParents(items, parents = []) {
    for (const item of items) {
      if (item.path === pathname || pathname.startsWith(item.path + '/')) {
        openKeys.push(...parents.map(p => p.path));
        if (item.children) openKeys.push(item.path);
      }
      if (item.children) {
        findParents(item.children, [...parents, item]);
      }
    }
  }

  findParents(routes);
  return [...new Set(openKeys)];
}
```

---

## 5. BREADCRUMB UTILITIES

Auto-generate breadcrumb từ routes (giống ProLayout PageContainer).

```javascript
// breadcrumb-utils.js

/**
 * Generate breadcrumb items từ current pathname + route config.
 *
 * Input:  pathname = '/creator/approval'
 * Output: [
 *   { title: 'Home', path: '/' },
 *   { title: 'Creator', path: '/creator' },
 *   { title: 'Approval Center' }   // Last item: no link
 * ]
 */
export function generateBreadcrumb(routes, pathname, homeName = 'Home') {
  const items = [{ title: homeName, path: '/' }];

  function findPath(routeList, targetPath, trail = []) {
    for (const route of routeList) {
      const currentTrail = [...trail, { title: route.name, path: route.path }];

      if (route.path === targetPath) {
        return currentTrail;
      }

      if (route.children) {
        const found = findPath(route.children, targetPath, currentTrail);
        if (found) return found;
      }
    }
    return null;
  }

  const trail = findPath(routes, pathname);
  if (trail) {
    items.push(...trail);
  }

  // Last item: no path (current page, no link)
  if (items.length > 1) {
    delete items[items.length - 1].path;
  }

  return items;
}
```

---

## 6. ADMIN LAYOUT COMPONENT

Main wrapper — tương đương ProLayout.

```jsx
// AdminLayout.jsx
import { Layout, Menu, Grid, Drawer } from 'antd';
import { useState, useMemo, useCallback } from 'react';
import { LayoutContext } from './LayoutContext';
import { routesToMenuItems, getSelectedKeys, getOpenKeys } from './menu-utils';
import { defaultLayoutTokens } from './layout-tokens';

const { Sider, Header, Content } = Layout;
const { useBreakpoint } = Grid;

/**
 * AdminLayout — shared layout cho internal tools.
 *
 * Props:
 * @param {Array}     routes          - Route config (menu structure)
 * @param {string}    pathname        - Current URL pathname
 * @param {Function}  onNavigate      - Navigation handler (path) => void
 * @param {ReactNode} logo            - Logo component/element
 * @param {string}    title           - App title
 * @param {ReactNode} headerRight     - Header right content (user menu, language, etc.)
 * @param {ReactNode} headerLeft      - Header left content (breadcrumb hoặc custom)
 * @param {ReactNode} siderBottom     - Sidebar bottom (user info)
 * @param {ReactNode} children        - Page content
 * @param {Object}    tokens          - Layout token overrides
 * @param {'side'|'top'} layout       - Layout mode (default: 'side')
 * @param {'dark'|'light'} navTheme   - Sidebar theme (default: 'dark')
 * @param {boolean}   defaultCollapsed - Initial collapsed state
 */
export function AdminLayout({
  routes = [],
  pathname = '/',
  onNavigate,
  logo,
  title,
  headerRight,
  headerLeft,
  siderBottom,
  children,
  tokens: tokenOverrides = {},
  layout = 'side',
  navTheme = 'dark',
  defaultCollapsed = false,
}) {
  const T = useMemo(() => deepMerge(defaultLayoutTokens, tokenOverrides), [tokenOverrides]);
  const screens = useBreakpoint();
  const isMobile = !screens.md; // < 768px

  const [collapsed, setCollapsed] = useState(defaultCollapsed);

  const menuItems = useMemo(() => routesToMenuItems(routes), [routes]);
  const selectedKeys = useMemo(() => getSelectedKeys(routes, pathname), [routes, pathname]);
  const openKeys = useMemo(() => getOpenKeys(routes, pathname), [routes, pathname]);

  const siderWidth = collapsed ? T.sider.collapsedWidth : T.sider.menuWidth;

  const handleMenuClick = useCallback(({ key }) => {
    onNavigate?.(key);
    if (isMobile) setCollapsed(true);
  }, [onNavigate, isMobile]);

  // ─── Context value ───
  const contextValue = useMemo(() => ({
    collapsed,
    isMobile,
    siderWidth,
    headerHeight: T.header.heightLayoutHeader,
    pathname,
    selectedMenuKeys: selectedKeys,
    openMenuKeys: openKeys,
    layout,
    navTheme,
    hasSider: layout === 'side',
    hasHeader: true,
    setCollapsed,
    navigate: onNavigate,
    tokens: T,
  }), [collapsed, isMobile, siderWidth, pathname, selectedKeys, openKeys, T]);

  // ─── Menu component (shared giữa Sider và Drawer) ───
  const menuContent = (
    <>
      {T.sider.showLogo && (
        <div style={{
          height: T.sider.logoHeight,
          display: 'flex',
          alignItems: 'center',
          padding: '0 16px',
          gap: 8,
        }}>
          {logo}
          {!collapsed && <span style={{
            color: navTheme === 'dark' ? '#fff' : 'rgba(0,0,0,0.88)',
            fontSize: 16,
            fontWeight: 600,
            whiteSpace: 'nowrap',
            overflow: 'hidden',
          }}>{title}</span>}
        </div>
      )}

      <Menu
        mode="inline"
        theme={navTheme}
        items={menuItems}
        selectedKeys={selectedKeys}
        defaultOpenKeys={openKeys}
        onClick={handleMenuClick}
        style={{ borderInlineEnd: 'none' }}
      />

      {siderBottom && !collapsed && (
        <div style={{
          position: 'absolute',
          bottom: 0,
          width: '100%',
          height: T.sider.userSectionHeight,
          borderTop: `1px solid ${T.sider.colorMenuItemDivider}`,
          display: 'flex',
          alignItems: 'center',
          padding: '0 16px',
        }}>
          {siderBottom}
        </div>
      )}
    </>
  );

  // ─── Render ───
  return (
    <LayoutContext.Provider value={contextValue}>
      <Layout style={{ minHeight: '100vh' }}>

        {/* Sidebar — desktop: Sider, mobile: Drawer */}
        {layout === 'side' && !isMobile && (
          <Sider
            width={T.sider.menuWidth}
            collapsedWidth={T.sider.collapsedWidth}
            collapsed={collapsed}
            onCollapse={setCollapsed}
            collapsible
            trigger={null}
            style={{
              position: T.sider.fixSiderbar ? 'fixed' : 'relative',
              height: '100vh',
              left: 0,
              top: 0,
              bottom: 0,
              zIndex: 100,
              overflow: 'auto',
              background: T.sider.colorMenuBackground,
            }}
          >
            {menuContent}
          </Sider>
        )}

        {layout === 'side' && isMobile && (
          <Drawer
            placement="left"
            open={!collapsed}
            onClose={() => setCollapsed(true)}
            width={T.sider.menuWidth}
            styles={{ body: { padding: 0, background: T.sider.colorMenuBackground } }}
            closable={false}
          >
            {menuContent}
          </Drawer>
        )}

        {/* Main area */}
        <Layout style={{
          marginLeft: layout === 'side' && !isMobile && T.sider.fixSiderbar
            ? siderWidth : 0,
          transition: 'margin-left 0.2s',
        }}>

          {/* Header */}
          <Header style={{
            height: T.header.heightLayoutHeader,
            background: T.header.colorBgHeader,
            borderBottom: `1px solid ${T.header.colorBorderHeader}`,
            padding: `0 ${T.header.paddingInlineHeader}px`,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            position: 'sticky',
            top: 0,
            zIndex: 99,
          }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
              {isMobile && /* hamburger button */ null}
              {headerLeft}
            </div>
            <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
              {headerRight}
            </div>
          </Header>

          {/* Content */}
          <Content style={{
            padding: T.content.paddingContent,
            background: T.content.colorBgContent,
            minHeight: `calc(100vh - ${T.header.heightLayoutHeader}px)`,
            maxWidth: T.content.maxWidthContent !== 'none'
              ? T.content.maxWidthContent : undefined,
          }}>
            {children}
          </Content>

        </Layout>
      </Layout>
    </LayoutContext.Provider>
  );
}
```

---

## 7. PAGE CONTAINER COMPONENT

Auto breadcrumb + page header + optional tabs (giống ProLayout PageContainer).

```jsx
// PageContainer.jsx
import { Breadcrumb, Tabs } from 'antd';
import { useLayoutContext } from './LayoutContext';
import { generateBreadcrumb } from './breadcrumb-utils';

/**
 * PageContainer — wraps page content với breadcrumb + header.
 *
 * Props:
 * @param {string}    title     - Page title (auto from route nếu không truyền)
 * @param {string}    subTitle  - Subtitle
 * @param {ReactNode} actions   - Header right actions (buttons)
 * @param {Array}     tabs      - Tab items [{ key, label, children }]
 * @param {string}    activeTab - Current active tab key
 * @param {Function}  onTabChange
 * @param {boolean}   ghost     - No background (transparent)
 * @param {ReactNode} children  - Page content
 */
export function PageContainer({
  title,
  subTitle,
  actions,
  tabs,
  activeTab,
  onTabChange,
  ghost = false,
  children,
}) {
  const { pathname, tokens: T, navigate } = useLayoutContext();

  // Tự lấy routes từ context nếu cần
  // const breadcrumbItems = generateBreadcrumb(routes, pathname);

  return (
    <div>
      {/* Page Header */}
      <div style={{
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        marginBottom: T.pageContainer.marginBottomPageHeader,
      }}>
        <div>
          {title && (
            <h2 style={{
              fontSize: 20,
              fontWeight: 600,
              margin: 0,
              lineHeight: 1.4,
            }}>
              {title}
            </h2>
          )}
          {subTitle && (
            <span style={{ color: 'rgba(0,0,0,0.45)', fontSize: 14 }}>
              {subTitle}
            </span>
          )}
        </div>
        {actions && (
          <div style={{ display: 'flex', gap: 8 }}>
            {actions}
          </div>
        )}
      </div>

      {/* Tabs (nếu có) */}
      {tabs ? (
        <Tabs
          activeKey={activeTab}
          onChange={onTabChange}
          items={tabs}
        />
      ) : (
        children
      )}
    </div>
  );
}
```

---

## 8. FOOTER TOOLBAR

Fixed action bar ở bottom (giống ProLayout FooterToolbar).

```jsx
// FooterToolbar.jsx
import { useLayoutContext } from './LayoutContext';

/**
 * FooterToolbar — fixed bottom bar, tự adjust theo sider width.
 * Dùng cho: form dài cần Save/Cancel luôn visible.
 */
export function FooterToolbar({ children, extra, style }) {
  const { siderWidth, isMobile } = useLayoutContext();

  return (
    <div style={{
      position: 'fixed',
      bottom: 0,
      right: 0,
      left: isMobile ? 0 : siderWidth,
      height: 56,
      background: '#fff',
      borderTop: '1px solid #f0f0f0',
      padding: '0 24px',
      display: 'flex',
      alignItems: 'center',
      justifyContent: extra ? 'space-between' : 'flex-end',
      zIndex: 99,
      boxShadow: '0 -2px 8px rgba(0,0,0,0.06)',
      transition: 'left 0.2s',
      ...style,
    }}>
      {extra && <div>{extra}</div>}
      <div style={{ display: 'flex', gap: 8 }}>{children}</div>
    </div>
  );
}
```

---

## 9. USAGE — MỖI PROJECT CHỈ CẦN

```jsx
// App.jsx của mỗi project
import { AdminLayout, PageContainer } from '@garena/admin-layout';

const routes = [
  { path: '/dashboard', name: 'Dashboard', icon: <DashboardOutlined /> },
  { path: '/creator', name: 'Creator', icon: <UserOutlined />, children: [...] },
  // ... project-specific routes
];

function App() {
  const pathname = useLocation().pathname;
  const navigate = useNavigate();

  return (
    <AdminLayout
      routes={routes}
      pathname={pathname}
      onNavigate={navigate}
      logo={<img src="/logo.svg" height={32} />}
      title="UGC Website"
      navTheme="dark"
      headerRight={<UserMenu />}
      siderBottom={<UserInfo />}
      tokens={{
        sider: { menuWidth: 200 },
        // Override bất kỳ token nào
      }}
    >
      <Routes>
        <Route path="/dashboard" element={
          <PageContainer title="Dashboard">
            <DashboardContent />
          </PageContainer>
        } />
        {/* ... */}
      </Routes>
    </AdminLayout>
  );
}
```

**Cross-project consistency đạt được vì:**
- Mọi project dùng cùng `AdminLayout` → shell giống nhau
- Mọi project dùng cùng `PageContainer` → page header + breadcrumb giống nhau
- Mọi project dùng cùng `layout-tokens` → spacing, sizing giống nhau
- Chỉ khác: `routes`, `logo`, `title`, `headerRight` — content layer

---

## 10. SO SÁNH VỚI PROLAYOUT

| Feature | ProLayout | AdminLayout (skill này) |
|---|---|---|
| antd v6 | ❌ chưa npm | ✅ native |
| umi required | Gần như bắt buộc | ❌ framework-agnostic |
| Auto menu | ✅ từ umi routes | ✅ từ route config |
| Auto breadcrumb | ✅ | ✅ |
| Layout tokens | ✅ (phức tạp) | ✅ (simplified) |
| LayoutContext | ✅ RouteContext | ✅ LayoutContext |
| Layout modes | side/top/mix | side/top |
| FooterToolbar | ✅ | ✅ |
| PageContainer | ✅ | ✅ |
| Bundle size | ~50KB+ | ~5KB (code trong project) |
| Customization | Props + tokens | Full source control |
| splitMenus | ✅ | ❌ (skip — ít dùng) |
