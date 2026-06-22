# Standard Module Library — Implementation Guide

Đây là component library chuẩn dùng cho tất cả internal tool.
Mỗi module được viết với Ant Design v5, props-driven, module hóa.

---

## DataTable — Chuẩn bảng dữ liệu

```jsx
import { Table, Button, Dropdown, Checkbox, Input, Space, Tooltip } from 'antd';
import { FullscreenOutlined, DownloadOutlined, SettingOutlined } from '@ant-design/icons';

// Props interface:
// columns: AntD column definitions
// dataSource: array of data
// filterByCountry?: boolean
// allowExport?: boolean
// frozenColumns?: string[]  — column keys bị freeze
// defaultSortField?: string
// onExport?: () => void

const DataTable = ({ 
  columns, 
  dataSource, 
  allowExport = false,
  defaultSortField,
  onExport 
}) => {
  const [isFullscreen, setIsFullscreen] = useState(false);
  const [hiddenCols, setHiddenCols] = useState([]);
  const [columnOrder, setColumnOrder] = useState(columns.map(c => c.key));

  // TODO: Add drag-to-reorder columns
  // TODO: Add column filter in header
  // TODO: Add freeze column logic

  const visibleColumns = columnOrder
    .filter(key => !hiddenCols.includes(key))
    .map(key => columns.find(c => c.key === key))
    .filter(Boolean);

  return (
    <div className={isFullscreen ? 'fullscreen-table' : ''}>
      <Space style={{ marginBottom: 8, justifyContent: 'flex-end', width: '100%' }}>
        {/* Column visibility toggle */}
        <Dropdown menu={{ items: columns.map(c => ({
          key: c.key,
          label: <Checkbox checked={!hiddenCols.includes(c.key)}>{c.title}</Checkbox>
        }))}} trigger={['click']}>
          <Button icon={<SettingOutlined />}>Cột</Button>
        </Dropdown>
        {allowExport && (
          <Button icon={<DownloadOutlined />} onClick={onExport}>Tải xuống</Button>
        )}
        <Tooltip title="Phóng to">
          <Button icon={<FullscreenOutlined />} onClick={() => setIsFullscreen(!isFullscreen)} />
        </Tooltip>
      </Space>
      <Table
        columns={visibleColumns}
        dataSource={dataSource}
        scroll={{ x: 'max-content', y: 500 }}
        pagination={{ showSizeChanger: true, pageSizeOptions: ['20', '50', '100'] }}
        // i18n: "Tải xuống", "Cột"
      />
    </div>
  );
};
```

---

## MetricCard — KPI với màu cảnh báo

```jsx
import { Card, Badge, Button } from 'antd';

// target: number — ngưỡng đạt
// value: number — giá trị hiện tại
// actionLabel: string — text nút action
// onAction: () => void

const MetricCard = ({ title, value, target, unit = '', actionLabel, onAction }) => {
  const getStatus = () => {
    const ratio = value / target;
    if (ratio < 0.8) return { color: '#ff4d4f', bg: '#fff2f0' };   // Đỏ: < 80% target
    if (ratio < 1.0) return { color: '#faad14', bg: '#fffbe6' };   // Vàng: 80-99%
    return { color: '#52c41a', bg: '#f6ffed' };                     // Xanh: đạt target
  };

  const { color, bg } = getStatus();

  return (
    <Card size="small" style={{ background: bg, borderColor: color }}>
      <div style={{ color: '#666', fontSize: 12 }}>{title}</div>
      <div style={{ color, fontSize: 24, fontWeight: 700 }}>
        {value}{unit}
      </div>
      <div style={{ color: '#999', fontSize: 11 }}>Target: {target}{unit}</div>
      {actionLabel && (
        <Button size="small" type="link" onClick={onAction} style={{ color, padding: 0 }}>
          {actionLabel} →
        </Button>
      )}
    </Card>
  );
};
```

---

## ActionableSummary — Danh sách việc cần làm

```jsx
import { List, Badge, Button, Typography } from 'antd';

// items: Array<{ key, label, count, urgent, actionLabel, onAction }>

const ActionableSummary = ({ items }) => {
  const sorted = [...items].sort((a, b) => b.urgent - a.urgent || b.count - a.count);

  return (
    <List
      size="small"
      dataSource={sorted}
      renderItem={item => (
        <List.Item
          style={{ background: item.urgent ? '#fff2f0' : 'white' }}
          actions={[
            <Button size="small" type={item.urgent ? 'primary' : 'default'} 
              danger={item.urgent} onClick={item.onAction}>
              {item.actionLabel || 'Xem'}  {/* i18n */}
            </Button>
          ]}
        >
          <Space>
            <Badge count={item.count} color={item.urgent ? 'red' : item.count > 0 ? 'orange' : 'green'} />
            <Typography.Text>{item.label}</Typography.Text>
          </Space>
        </List.Item>
      )}
    />
  );
};
```

---

## FilterBar — Bộ filter chuẩn

```jsx
import { Select, DatePicker, Button, Space, Row, Col } from 'antd';
import { FilterOutlined, ReloadOutlined } from '@ant-design/icons';

// CONFIG driven — truyền vào options cho từng filter
// onFilter: (filters) => void
// savedViews?: Array<{ id, name, filters }>

const FilterBar = ({ config, onFilter, savedViews = [], onSaveView }) => {
  const [filters, setFilters] = useState({});

  const handleChange = (key, value) => {
    const newFilters = { ...filters, [key]: value };
    setFilters(newFilters);
    onFilter(newFilters);
  };

  return (
    <Row gutter={[8, 8]} align="middle">
      {config.country && (
        <Col>
          <Select placeholder="Quốc gia" /* i18n */
            style={{ width: 120 }}
            options={config.country}
            onChange={v => handleChange('country', v)}
            allowClear
          />
        </Col>
      )}
      {config.game && (
        <Col>
          <Select placeholder="Game" style={{ width: 140 }}
            options={config.game}
            onChange={v => handleChange('game', v)}
            allowClear
          />
        </Col>
      )}
      {config.dateRange && (
        <Col>
          <DatePicker.RangePicker onChange={v => handleChange('dateRange', v)} />
        </Col>
      )}
      {config.status && (
        <Col>
          <Select placeholder="Trạng thái" /* i18n */
            style={{ width: 140 }}
            options={config.status}
            onChange={v => handleChange('status', v)}
            allowClear
          />
        </Col>
      )}
      <Col>
        <Button icon={<ReloadOutlined />} onClick={() => { setFilters({}); onFilter({}); }}>
          Reset {/* i18n */}
        </Button>
      </Col>
      {onSaveView && (
        <Col>
          <Button icon={<FilterOutlined />} onClick={() => onSaveView(filters)}>
            Lưu view {/* i18n */}
          </Button>
        </Col>
      )}
      {savedViews.length > 0 && (
        <Col>
          <Select placeholder="View đã lưu" /* i18n */
            style={{ width: 160 }}
            options={savedViews.map(v => ({ label: v.name, value: v.id }))}
            onChange={id => {
              const view = savedViews.find(v => v.id === id);
              if (view) { setFilters(view.filters); onFilter(view.filters); }
            }}
          />
        </Col>
      )}
    </Row>
  );
};
```

---

## AppLayout — Khung layout chuẩn

```jsx
import { Layout, Menu, Avatar, Badge, Space } from 'antd';
import { BellOutlined } from '@ant-design/icons';

const { Header, Sider, Content } = Layout;

const AppLayout = ({ menuItems, children, toolName, unreadNotifications = 0 }) => {
  const [collapsed, setCollapsed] = useState(false);

  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Header style={{ 
        position: 'fixed', zIndex: 100, width: '100%',
        display: 'flex', alignItems: 'center', justifyContent: 'space-between',
        padding: '0 24px', background: '#fff', borderBottom: '1px solid #f0f0f0'
      }}>
        <Space>
          {/* Logo placeholder */}
          <div style={{ fontWeight: 700, fontSize: 16 }}>{toolName}</div>
        </Space>
        <Space>
          {/* i18n: VI/EN switcher — implement ở bước cuối */}
          <Badge count={unreadNotifications}>
            <BellOutlined style={{ fontSize: 18, cursor: 'pointer' }} />
          </Badge>
          <Avatar>U</Avatar>
        </Space>
      </Header>
      <Layout style={{ marginTop: 64 }}>
        <Sider 
          collapsible collapsed={collapsed} onCollapse={setCollapsed}
          style={{ position: 'fixed', height: 'calc(100vh - 64px)', overflow: 'auto' }}
        >
          <Menu mode="inline" items={menuItems} />
        </Sider>
        <Content style={{ 
          marginLeft: collapsed ? 80 : 200,
          padding: 24, transition: 'margin 0.2s'
        }}>
          {children}
        </Content>
      </Layout>
    </Layout>
  );
};
```

---

## PermissionGate — Kiểm soát quyền

```jsx
// Dùng để wrap bất kỳ UI element nào cần permission
// action: string — tên action cụ thể, ví dụ: 'post:approve', 'creator:edit'
// userRole: string — role hiện tại của user

const PERMISSION_MAP = {
  // TODO: Replace with API-driven permission config
  admin: ['*'],
  editor: ['post:view', 'post:edit', 'creator:view', 'creator:edit'],
  viewer: ['post:view', 'creator:view'],
};

const PermissionGate = ({ action, userRole, children, fallback = null }) => {
  const permissions = PERMISSION_MAP[userRole] || [];
  const hasPermission = permissions.includes('*') || permissions.includes(action);
  return hasPermission ? children : fallback;
};

// Dùng:
// <PermissionGate action="post:approve" userRole={currentUser.role}>
//   <Button danger>Approve</Button>
// </PermissionGate>
```
