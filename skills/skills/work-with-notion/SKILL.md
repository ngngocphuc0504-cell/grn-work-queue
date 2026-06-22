---
name: work-with-notion
description: Huong dan lam viec voi Notion - doc, phan tich, tao va cap nhat page. Day la ten moi theo vai tro cua skill cu `notion`.
---

# Work With Notion

## Nguyen tac quan trong nhat

Khong bao gio tu y thay doi Notion khi nguoi dung chua yeu cau ro rang.
Phan tich va trinh bay noi dung trong chat truoc. Chi thuc hien thay doi tren Notion sau khi nguoi dung confirm bang loi ro rang nhu "ok", "luu vao", "tao di", "cap nhat di", "bo sung vao".

Neu khong chac nguoi dung muon luu vao Notion hay chi muon xem trong chat, hoi truoc.

## Phan loai hanh dong

### Luon hoi truoc - khong bao gio tu lam

- Tao page moi hoac sub-page moi (`create_pages`)
- Xoa hoac archive page
- Ghi de toan bo noi dung (`replace_content`)
- Thay doi title hoac properties cua page (`update_properties`)
- Di chuyen page sang parent moi (`move_pages`)

**Cach hoi:**
"Minh du kien [mo ta hanh dong cu the] trong Notion. Ban muon minh thuc hien khong?"

### Mo ta truoc khi lam

- Chinh sua mot phan noi dung (`update_content`)
- Them section moi vao cuoi page
- Them cross-reference, related documents, backlink
- Cap nhat page hub, index, hoac doc map

**Cach mo ta:**
"Minh se sua doan [X] trong section [Y] cua page [ten page], va neu can se them link lien quan o page hub/page ky thuat."

Neu nguoi dung khong phan doi trong cung turn, tien hanh.

### Tu do lam - khong can hoi

- Doc noi dung page (`fetch`)
- Tim kiem trong workspace (`search`)
- Doc comment (`get_comments`)
- Kiem tra structure page, ancestor path, sibling pages

## Workflow chuan

1. Fetch/search page nguoi dung nhac toi
2. Kiem tra information architecture truoc khi sua
3. Xac dinh dung loai tai lieu va page dich
4. Trinh bay de xuat thay doi trong chat
5. Duoc confirm thi moi update
6. Bao lai page da cap nhat, page lien quan da doi, va neu co conflict thi ghi ro

## Writing convention cho noi dung luu vao Notion

Khi viet hoac sua noi dung user-facing trong Notion, mac dinh:

- viet bang tieng Viet co dau
- dung ngon ngu non-tech, de doc voi operator hoac stakeholder khong ky thuat
- neu he thong dang render page title san o phan chrome, khong lap lai title y het thanh H1 trong body
- bat dau body bang metadata block hoac section dau tien co nghia nhu `Purpose`, `Summary`, `How To Read This Page`, `Workflow chinh`

Neu subtree cua project dang co convention khac ro rang, follow convention local do.

## Information Architecture Check

Truoc moi lan update Notion, agent phai tu tra loi 5 cau hoi:

1. Page nguoi dung dua ra dang thuoc nhom nao:
- project hub
- section hub
- spec
- data contract
- database schema
- build history
- task / operations
- team / process

2. Trong cung nhanh Notion co page chuyen biet nao phu hop hon khong?

3. Noi dung dang dinh luu thuoc lop nao:
- business behavior
- UI flow
- component/data payload
- backend entity/schema
- thay doi theo thoi gian
- task/tracking

4. Cap nhat nay co can sua them page hub hoac index nao khong?

5. Co can them cross-reference/backlink de page moi khong bi "dung mot minh" khong?

Neu phat hien dang sua sai page, dung lai va de xuat remap truoc khi update.

## Document Type Routing

Khong duoc luu tat ca vao spec page. Phai route dung loai noi dung:

### Specs

Luu tai day khi noi dung tra loi:
- feature hoat dong nhu the nao
- user flow
- business rules
- permissions
- states
- edge cases

Khong nen nhoi field-level data shape vao spec neu da co page technical rieng.

### Data Contracts

Luu tai day khi noi dung tra loi:
- component props
- payload shape
- response shape
- data source cho widget
- sort keys, filter keys, field names
- display contract giua UI va data

### Database Schema

Luu tai day khi noi dung tra loi:
- entities
- fields va types
- enums
- relationships
- persistence model
- storage-ready schema

### Build History

Luu tai day khi noi dung tra loi:
- da sua gi
- sua o file nao
- ly do sua
- tradeoff, known gaps, release notes

### Tasks / Operations

Luu tai day khi noi dung tra loi:
- feature request
- backlog
- follow-up
- owner
- due date
- status tracking

## Source of Truth Priority

Khi co xung dot, uu tien theo thu tu:

1. Specs la source of truth cho business behavior
2. Data Contracts la source of truth cho UI/component payload
3. Database Schema la source of truth cho storage/backend model
4. Build History la source of truth cho timeline thay doi

Neu specs thay doi va lam contract/schema cu khong con khop:
- khong im lang bo qua
- phai note ro page nao can sync tiep
- neu duoc nguoi dung yeu cau, update theo thu tu specs -> data contracts -> database schema

## Cross-reference va Wiki-linking

Muc tieu la moi page quan trong deu nam trong mang lien ket de nguoi doc va AI scan nhanh duoc.

### Nguyen tac

- Page quan trong khong dung mot minh
- Moi page quan trong nen co link toi page cha va page lien quan
- Khi hop ly, phai co backlink tu hub page hoac page lien quan tro lai

### Related Documents block

Khi tao page moi hoac cap nhat page quan trong, can can nhac them mot block ngan gan dau page:

`Related Documents`

- Parent / Module / Hub
- Spec
- Data Contract
- Database Schema
- Related Tasks
- Build History

Khong can ep buoc du tat ca muc. Chi giu cac muc that su ton tai va co ich.

### Wiki-link va direct link

Neu workspace dung naming ro rang va wikilink hoat dong tot, co the dung `[[Page Name]]` trong ban nhap/y tuong.

Khi update Notion that:
- uu tien page link truc tiep neu can do chinh xac cao
- chi dung wikilink neu chac chan ten page on dinh va khong trung

### Bidirectional linking

Khi tao hoac cap nhat page con, luon kiem tra:
- page hub da co link den page con chua
- page con da tro ve hub/page lien quan chua

Khong bat buoc sua ca hai phia moi lan, nhung phai danh gia va neu can thi de xuat.

## Hub va Index Maintenance

Nhieu du an co structure gan giong nhau, thuong se co:
- mot project hub
- mot so section hub
- cac page chi tiet ben duoi

Skill nay khong duoc hardcode theo ten page cua mot du an cu the. Thay vao do, agent phai nhan dien theo vai tro:

- Project hub: page tong cua du an
- Section hub: page tong cua mot nhanh nhu Product, Technical, Operations
- Detail page: spec, contract, schema, task, guide

Khi sua detail page, phai can nhac:
- co can bo sung vao hub/index khong
- co can them dong "see also" khong
- co can cap nhat doc map hay table danh sach page con khong

Neu project da co page hub va section hub, uu tien giu noi dung ngan gon o hub, chi dat link va tom tat, khong nhoi chi tiet ky thuat vao hub.

## Muc tieu quan ly tri thuc cap du an

Skill nay phai ho tro quan ly tri thuc cho nhieu du an co structure tuong tu, khong chi mot du an cu the.

De lam duoc viec do, agent can:

- route dung noi dung vao dung lop tai lieu
- giu lien ket giua cac lop tai lieu
- giu page hub de dieu huong
- tranh duplicate source of truth
- danh dau conflict va de xuat dong bo

## Output format truoc khi sua

Truoc khi update Notion, neu cong viec co tac dong den noi dung, agent nen bao ngan gon:

- Page dich
- Pages lien quan da kiem tra
- Loai noi dung se luu
- Neu can, page hub/index nao se duoc sua them
- Neu phat hien remap, noi ro se chuyen phan nao sang page nao

## Luu y ky thuat

### Luon fetch truoc khi update

`update_content` dung `old_str` de tim dung vi tri. Neu khong fetch truoc, `old_str` co the khong khop va gay sai cho hoac that bai.

Bat buoc:
fetch -> doc noi dung -> moi update

### Uu tien update_content hon replace_content

- `update_content`: chi sua dung doan can, risk thap
- `replace_content`: ghi de toan bo, risk cao

Chi dung `replace_content` khi nguoi dung yeu cau viet lai toan bo page.

### replace_content co the xoa sub-page

Neu `new_str` khong khai bao lai the `<page url="...">` cho sub-page dang ton tai thi sub-page co the bi xoa.
Khong bao gio tu dong set `allow_deleting_content: true` neu chua liet ke ro nhung gi se bi xoa va duoc nguoi dung xac nhan.

### Database page khac regular page

- Regular page: thuong chi co property `title`
- Database page/data source: fetch truoc de lay dung schema, property names, data source id

### Duplicate page va apply template la bat dong bo

Page duoc tao ngay nhung noi dung co the chua xuat hien ngay.
Khong fetch ngay sau do de ket luan thieu noi dung. Neu can, bao nguoi dung kiem tra lai sau.

### Notion markdown co cu phap rieng

Khong doan cu phap cua block phuc tap.
Neu can block nang cao, fetch tai lieu `notion://docs/enhanced-markdown-spec` truoc.

## Checklist tu kiem tra truoc khi ket thuc

- Da xac dinh dung page dich chua?
- Da kiem tra co page chuyen biet phu hop hon chua?
- Da fetch page truoc khi update chua?
- Da note page lien quan can sync chua?
- Da can nhac them cross-reference/backlink chua?
- Da tranh hardcode structure cua mot du an cu the chua?
