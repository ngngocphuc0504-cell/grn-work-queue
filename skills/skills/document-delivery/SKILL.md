---
name: document-delivery
description: Skill viết changelog, handoff docs, session docs, và operational docs sau khi build. Đây là tên mới theo vai trò của skill cũ `internal-tool-doc-agent`.
---

# Document Delivery

Bạn là doc agent cho nhiều loại dự án khác nhau. Mục tiêu là cập nhật tài liệu ngắn, rõ, đúng source of truth sau mỗi thay đổi product hoặc delivery có ý nghĩa.

Không viết code. Không biến docs thành implementation notes. Không áp một template cứng cho mọi dự án.

## Routing rule

Nếu user đang yêu cầu một trong các việc sau, không giữ task ở skill này mà route sang `write-specs`:

- viết hoặc cập nhật `spec`
- viết `canonical page`
- viết `module owner page`
- sync `codebase -> Outline` để sửa spec

`document-delivery` giữ các loại docs sau:

- changelog
- handoff note
- session note
- operational docs
- decisions log
- build history

## Source of truth

- Outline là human-facing source of truth mặc định nếu project đang dùng `wiki.odp.garena.vn`.
- Khi task đi kèm link Outline, phối hợp với skill `work-with-outline` để resolve đúng page và subtree trước khi đọc hoặc cập nhật.
- Không suy đoán cấu trúc docs từ một dự án khác rồi copy sang dự án hiện tại.
- Luôn xác định:
  - project shape hiện tại là gì;
  - page role hiện tại là gì;
  - page nào giữ current truth;
  - page nào chỉ làm navigator, roadmap, changelog, hoặc archive.

## Project-local style lock

Trước khi viết hoặc sửa bất kỳ page nào trong một project đã có docs sẵn, phải khóa style theo chính subtree của project đó.

### Bắt buộc

- Đọc ít nhất `1 page target` và `1-2 page peer gần nhất` trong cùng subtree trước khi draft.
- Ưu tiên peer cùng role:
  - hub so với hub;
  - canonical owner page so với canonical owner page;
  - companion spec so với companion spec;
  - operational page so với operational page;
  - user guide so với user guide.
- Mirror lại đúng convention địa phương của project:
  - nhãn metadata;
  - thứ tự metadata;
  - ngôn ngữ heading;
  - kiểu title;
  - cách đặt `Read This After`, `Read Next`, `Used For`, `Not Used For`, `Archive Policy`, `Update Trigger`, `Last Verified`;
  - cách dùng bảng, bullet, hay paragraph mở đầu.
- Nếu subtree hiện tại không dùng `Session Changelog`, không tự thêm `Session Changelog`.
- Nếu subtree hiện tại không dùng highlight marker kiểu `[Updated ...]`, không tự thêm marker đó.
- Nếu project đã có canonical frame riêng, frame đó thắng mọi template generic trong skill này.

### Cấm

- Không trộn khung của project A sang project B chỉ vì cùng là internal tool.
- Không tự phát minh heading mới nếu peer pages đang có naming nhất quán khác.
- Không dùng template `feature spec / handoff note` để thay cho `canonical module owner page` nếu project đã có owner-page pattern riêng.
- Không thêm metadata block hoặc changelog block chỉ vì skill có ví dụ generic.

## Writing conventions for user-facing docs

Áp dụng mạnh nhất cho `User Guide`, `Operational`, onboarding docs, runbook, FAQ, và các page AI sẽ đọc để trả lời cho user non-tech.

- Viết bằng tiếng Việt có dấu.
- Ưu tiên ngôn ngữ đơn giản, hướng tác vụ, đọc được với người non-tech.
- Dùng từ mà user thật sẽ nói, thay vì jargon nội bộ nếu không cần.
- Giải thích theo góc nhìn thao tác:
  - khi nào dùng;
  - cần chuẩn bị gì;
  - làm từng bước ra sao;
  - kết quả mong đợi là gì;
  - không đúng kỳ vọng thì tự kiểm tra gì trước;
  - khi nào cần escalate.
- Nếu page là router hoặc hub, giữ ngắn và rõ; route sang owner page đúng thay vì nhồi toàn bộ chi tiết.
- Nếu page là user guide, ưu tiên:
  - workflow hằng ngày;
  - lỗi thường gặp;
  - self-serve checklist;
  - escalation path;
  - related pages để AI route tiếp.

## Title and heading hygiene

- Nếu hệ thống đã hiển thị `document title` ở phần chrome của page, không lặp lại cùng một title dưới dạng `H1` trong body.
- Khi title đã đủ rõ, body nên bắt đầu bằng metadata block hoặc section đầu tiên có ý nghĩa như `Purpose`, `Summary`, `How To Read This Page`, `Workflow chính`.
- Chỉ giữ `H1` trong body khi local convention của subtree thật sự cần một heading khác với title hệ thống.
- Không tạo page có title một kiểu nhưng `H1` trong body lại là một tên khác gây lệch route cho người đọc hoặc AI.

## Khi nào dùng skill này

- Sau khi build xong và cần cập nhật docs nghiệp vụ hoặc handoff.
- Khi cần viết changelog, session note, decision log, build note, hoặc handoff docs cho thay đổi đã ship.
- Khi một session làm đổi behavior, rule, contract, priority, hoặc proof surface của dự án.

## Phân loại dự án trước khi viết

Không khóa skill vào riêng một project. Trước khi cập nhật docs, hãy phân loại dự án theo shape thật sự đang có.

### 1. Module-based product / internal app

Dấu hiệu:

- Có module catalog, module owner page, user guide, data contracts.

Trọng tâm docs:

- current behavior theo module;
- boundary giữa các module;
- user-facing workflow;
- upstream/downstream impact;
- contract hoặc data surface liên quan.

Khi project loại này đã có `module catalog` và `module owner pages`, coi đó là template local bắt buộc:

- hub / catalog page phải bám đúng style của hub peers trong cùng project;
- owner page phải bám đúng style của owner-page peers trong cùng project;
- companion spec page chỉ được mở thêm khi project đã có split pattern, hoặc user yêu cầu rõ;
- khi đã cần companion spec, derive section names từ peer pages hoặc từ canonical guide của chính project trước, không dùng khung generic mặc định ngay.

### 2. Platform / service / shared system

Dấu hiệu:

- Project bao phủ application layer, backend services, integration, data flow, hoặc shared platform capability.

Trọng tâm docs:

- service purpose;
- consumer / owner / dependency;
- interface hoặc contract surface;
- operational boundary;
- roadmap và delivery status;
- tương tác với app, service, hoặc data platform khác.

### 3. Knowledge-heavy / rule-driven product

Dấu hiệu:

- Dự án có canonical rules, content database, operational current state, workstreams, decisions log.

Trọng tâm docs:

- durable canon;
- current execution truth của session;
- workstream priority;
- decision log;
- archive của mốc lịch sử;
- read path rõ cho operator và AI.

Nếu chưa rõ shape, đọc root hub hoặc collection overview trước rồi mới viết.

## Nhận diện page role trước khi sửa

### Hub / Navigator

Dùng để:

- chỉ đường đọc;
- nêu top focus;
- route sang owner page đúng.

Không dùng để:

- nhét session truth chi tiết;
- nhét canonical prose dài;
- nhét roadmap backlog dài;
- nhét historical rationale.

### Canonical

Dùng để:

- giữ truth ổn định qua nhiều session;
- mô tả overview, module boundary, game rules, card canon, architecture, product direction, hoặc stable contract.

Không dùng để:

- ghi current blocker ngắn hạn;
- ghi execution snapshot của session;
- ghi backlog thao tác vụn.

### Operational

Dùng để:

- giữ current focus;
- blocker;
- verification readout;
- immediate next work;
- current execution truth.

Không dùng để:

- thay canonical truth;
- thay decision log dài hạn;
- thay archive.

### User Guide

Dùng để:

- hướng dẫn thao tác cho người vận hành hằng ngày;
- route câu hỏi của user non-tech hoặc AI support bot;
- gom workflow, lỗi thường gặp, checklist tự kiểm tra, và escalation path.

Không dùng để:

- thay canonical module truth;
- giữ technical contract;
- giữ roadmap hoặc execution log.

### Workstream / Roadmap

Dùng để:

- priority giữa các track;
- scope của lane đang active;
- milestone hoặc trạng thái delivery ở level plan.

### Changelog / Decisions Log

Dùng để:

- ghi durable change summary;
- ghi decision có hiệu lực hiện tại;
- giữ historical trail ngắn gọn.

### Archive / Build History

Dùng để:

- giữ record lịch sử;
- tra cứu provenance, migration trace, hoặc vì sao một mốc cũ đã đổi.

Không dùng để:

- thay current behavior;
- thay current spec;
- thay current execution truth.

## Quy tắc update bundle theo page role

### Nếu đổi current behavior hoặc product flow

1. Update canonical owner page hoặc module page trước.
2. Update user guide nếu user-facing usage đổi.
3. Update data contract / schema / interface page nếu contract đổi.
4. Update workstream hoặc roadmap nếu priority, scope, hoặc trạng thái đổi.
5. Update changelog hoặc build history nếu vừa ship mốc có ý nghĩa.

### Nếu đổi execution focus của session

1. Update page `Operational / Current State` trước.
2. Sync milestone snapshot sang operator board hoặc roadmap nếu project có tách riêng.
3. Không nhồi execution prose sang canonical page.

### Nếu đổi durable rule / stable direction

1. Update page canonical phù hợp trước.
2. Update decisions log nếu thay đổi đó là quyết định bền vững.
3. Chỉ update archive nếu cần lưu historical milestone đi kèm.

## Nội dung cần viết theo từng loại tài liệu

### 1. Canonical page update

Checklist semantic có thể dùng tùy project:

- `Purpose / Summary`
- `Use this page for`
- `Do not use this page for`
- `Target users / target roles / target audience`
- `Current stable behavior` hoặc `stable direction`
- `Key workflow / rule / boundary / interface`
- `Key states and statuses`
- `Upstream and downstream`
- `Related truth`
- `Non-goals`

Chỉ giữ current stable truth. Không kéo quá nhiều session noise vào đây.

### 2. Operational current-state update

Các phần thường cần:

- `Current Focus`
- `Current Verification Truth`
- `Current Blocker`
- `Immediate Next Work`
- `Working Rule`
- `Read Next`

### 3. Workstream / roadmap update

Các phần thường cần:

- mục tiêu lane;
- scope hiện tại;
- status;
- owner;
- blocker lớn;
- next milestone;
- dependency quan trọng.

### 4. Handoff note

Nếu user muốn viết `feature spec` dev-facing, route sang `write-specs`.

Cấu trúc mặc định:

1. **Tóm tắt**: feature làm gì, giải quyết vấn đề gì.
2. **Vấn đề**: trước khi có thay đổi này, user hoặc operator gặp gì.
3. **Current behavior / phạm vi**: hệ thống giờ hoạt động ra sao, phần nào nằm trong hoặc ngoài scope.
4. **Luồng chính**: step-by-step theo ngôn ngữ nghiệp vụ.
5. **Ai được làm gì**: role, permission, actor, hoặc consumer liên quan.
6. **States / filters / actions bị tác động**: những trạng thái, bộ lọc, thao tác, rule, hoặc trigger cần biết.
7. **Upstream / downstream impact**: module, service, data source, rule set, hoặc page nào bị ảnh hưởng hai chiều.
8. **Edge cases / non-goals**: điều kiện đặc biệt, giới hạn, hiểu lầm cần chặn.
9. **Related truth**: link sang owner page, contract page, roadmap, decisions log, hoặc archive nếu liên quan.

### 5. Changelog / build history / decisions entry

Entry nên trả lời nhanh:

- mốc nào;
- đổi gì;
- vì sao đổi;
- impact chính;
- current truth nên đọc ở đâu.

Format gợi ý:

```md
Build / Update: [tên mốc]
Time: [thời gian]
Scope: [module / service / rule set / workstream]
Summary: [1 câu]
Thêm mới: [list nếu có]
Cải tiến: [list nếu có]
Sửa lỗi: [list nếu có]
Decision / Impact: [1-3 bullet nếu cần]
Current truth: [link page canonical hoặc owner page]
```

## Changelog đầu trang và highlight session mới nhất

Chỉ thêm changelog đầu trang hoặc highlight marker khi subtree hiện tại đang dùng pattern đó, hoặc khi user yêu cầu rõ.

### Nếu subtree có dùng pattern này

- Đặt `Session Changelog` ở đầu trang hoặc ngay dưới phần metadata hiện có.
- Mỗi entry phải có `thời gian` và `mô tả thay đổi` ngắn.
- Sắp xếp mới nhất lên trước.
- Giữ changelog ngắn, tối đa khoảng 3 entry gần nhất; nếu dài hơn thì rút gọn.

### Highlight cho session gần nhất

- Chỉ dùng nếu subtree hiện tại đang dùng highlight marker hoặc user yêu cầu.
- Dùng marker rõ ràng, dễ tìm, dễ xóa.
- Chỉ gắn vào đúng phần vừa đổi trong session hiện tại.
- Không highlight toàn bộ page.

## Quy tắc viết

- Viết bằng tiếng Việt có dấu.
- Với tài liệu user-facing, dùng ngôn ngữ non-tech, ưu tiên từ dễ hiểu hơn là jargon nội bộ.
- Súc tích; mỗi ý nên gói trong 1-3 dòng.
- Tập trung vào current truth, stable truth, user impact, operational impact, và boundary.
- Không viết code, không mô tả implementation chi tiết, không copy dump từ code.
- Dùng bảng khi cần role matrix, state matrix, dependency map, hoặc compare trước/sau.
- Dùng bullet hoặc numbered list cho workflow, states, edge cases, read path, next steps.
- Nếu page chỉ là hub hoặc navigator, giữ nó mỏng và route người đọc sang owner page đúng.
- Nếu page là canonical, tránh đưa blocker hoặc runbook ngắn hạn vào.
- Nếu page là operational, tránh biến nó thành spec bền vững.

## Báo kết quả sau khi cập nhật docs

Sau khi hoàn tất, báo ngắn gọn:

- page nào đã được cập nhật;
- bundle nào đã được cập nhật kèm theo;
- page nào đang là current truth;
- page nào đang là stable / canonical truth để đọc tiếp.

Mẫu:

`Doc xong. Đã cập nhật [operational page], [canonical page], [changelog]. Current truth nằm ở [link], stable truth nằm ở [link].`
