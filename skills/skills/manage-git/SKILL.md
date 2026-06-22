---
name: manage-git
description: |
  Skill quan ly Git va internal Git an toan cho nguoi khong biet code.
  Dung khi user muon status, diff, sync, branch, commit, push, merge, pull request,
  gitignore, hoac bat ky viec nao lien quan den version control.
---

# Manage Git Workflow

If the user wants to inspect, change, or repair this skill or any other skill, use `skill-creator` and the repo workflow. If `manage-skills` is available in the session, prefer it for lifecycle operations. Do not edit runtime copies under `%USERPROFILE%\.codex\skills` or `%USERPROFILE%\.claude\skills` directly.

Skill nay mac dinh cho workflow internal-only.

## Core defaults

- remote chuan duy nhat la `origin`
- `origin` phai tro internal git
- branch chinh la `main`
- branch lam viec mac dinh cua Hai-Son la `Hai-Son`
- trong repo local cua Hai-Son, current branch mac dinh khi lam viec la `Hai-Son`
- local `main` track `origin/main`
- local `<working_branch>` track `origin/<working_branch>`

## Determine `working_branch`

- truoc khi ap dung default `Hai-Son`, phai xac dinh repo da co `origin/main` hop le hay chua
- neu repo moi/trong, chua co commit, hoac `origin/main` missing/gone, khong dung `Hai-Son` lam branch bootstrap; xem `New/empty repo bootstrap`
- uu tien branch user noi ro trong request
- neu dang dung tren mot branch khac `main` va branch do track `origin/<same-name>`, coi do la `working_branch`
- voi profile Hai-Son, mac dinh dung `Hai-Son`
- chi hoi them neu dang o `main` va khong suy ra duoc branch ca nhan nao

## New/empty repo bootstrap

Dung section nay khi clone repo moi/trong, `git status --short --branch` hien `No commits yet`, hoac `origin/main` missing/gone.

- Branch bootstrap bat buoc la `main`, khong phai `Hai-Son`
- Tao first commit tren local `main`
- Push `main` truoc: `git push -u origin main`
- Sau khi `origin/main` ton tai, moi tao/push `Hai-Son` neu can branch ca nhan
- Voi repo deploy/CI/CD, pipeline deploy dau tien phai trigger tu `main` tru khi user noi ro branch deploy khac
- Khong push `Hai-Son` truoc `main`, vi GitLab co the tao/default pipeline dau tien tren branch ca nhan va runner protected/tagged co the khong pick branch do
- Sau bootstrap, sync local `main` tracking `origin/main`; neu tiep tuc lam viec thuong ngay sau do moi switch sang `Hai-Son`

## Local current branch guard

Voi profile Hai-Son, truoc khi bat dau viec git hoac truoc khi sua code trong repo local:

- chay `git status --short --branch` va `git branch -a -vv`
- neu repo moi/trong hoac chua co `origin/main`, dung `main` theo `New/empty repo bootstrap`; khong switch sang `Hai-Son`
- neu user khong yeu cau ro lam tren `main`, release branch, hay branch khac, dung `Hai-Son`
- neu dang o `main` va working tree sach, switch sang `Hai-Son` truoc khi tiep tuc
- neu local `Hai-Son` da co, dung `git switch Hai-Son`
- neu local `Hai-Son` chua co nhung `origin/Hai-Son` co, tao tracking branch bang `git switch --track origin/Hai-Son`
- neu ca local va remote `Hai-Son` deu chua co, chi tao tu `main` va push `origin/Hai-Son` khi user dang yeu cau chuan hoa mac dinh branch hoac da dong y ro
- neu working tree dirty, khong switch branch ngay; stash/commit/hoi user theo safety rules truoc
- sau khi switch, xac minh `git status --short --branch` hien `Hai-Son...origin/Hai-Son`

## Expected remote layout

- dung `git remote -v` de kiem tra
- neu `origin` chua tro internal git, giai thich trang thai hien tai bang tieng Viet don gian
- chi doi remote sau khi user dong y ro rang
- khong tao flow song song hai remote cho cung mot viec push
- khong dung nhung ten remote mo ho nhu `ved`, `gitlab`, `internalgit`

## Local helper scripts

Neu repo co helper script, chuan hien tai la internal-only:

- `push-origin.cmd` = helper chuan
- khong tao hoac giu `push-all.cmd`, `push-internal-git.cmd`, `push-github.cmd`
- neu thay cac helper legacy nay trong repo da chuyen internal-only, de xuat xoa chung va giu `push-origin.cmd`

## Default working flow

Moi yeu cau git thong thuong mac dinh theo chuoi:

1. `git status` + `git diff --stat` + `git diff`
2. xac nhan branch dang dung co dung khong
3. commit local tren `<working_branch>`
4. push len `origin/<working_branch>`
5. bao mo ta thay doi bang tieng Viet
6. tao MR/PR neu workflow repo can
7. merge `<working_branch> -> main` tren internal git khi da duyet
8. sync local `main` tu `origin/main`

Khong gop push branch review va merge `main` thanh mot thao tac.
Khong khuyen khich lam viec truc tiep tren `main` neu user khong noi rat ro.

## Reporting rules

Khi push:

- luon de xuat `commit message`
- luon tom tat thay doi bang tieng Viet
- luon noi ro da push len `origin/<branch>`
- neu push that bai, noi ro branch nao va buoc tiep theo

Khi merge:

- luon noi ro da merge branch nao vao `main`
- luon tom tat noi dung merge bang tieng Viet
- luon noi ro local `main` da sync chua

## Safety rules

### Ask before risky operations

Voi moi lenh co the doi lich su, doi remote, doi upstream, xoa branch, hoac lam mat code:

1. giai thich ngan se lam gi
2. noi ro tac dong
3. chi thuc hien sau khi user da dong y

Nhung lenh chi doc nhu `git status`, `git log`, `git diff`, `git remote -v`, `git branch -a -vv` duoc tu thuc hien.

### Never use casually

Khong tu y dung:

- `git push --force`
- `git reset --hard`
- `git clean -f`
- `git checkout .`
- `git restore .`
- `git branch -D`
- `git rebase` tren branch da push

Neu user yeu cau, phai giai thich rui ro va de xuat cach an toan hon.

### Sensitive file gate

Truoc moi lan commit/push, scan danh sach file thay doi. Canh bao neu co:

- `.env`, `.env.local`, `.env.production`, `.env.*`
- `*credentials*`, `*secret*`, `*token*`, `*password*`
- `*.pem`, `*.key`, `*.p12`, `*.pfx`
- `firebase*.json`
- `config.js`, `config.json` neu chua API key hoac database URL
- `node_modules/`
- `.DS_Store`, `Thumbs.db`

Neu phat hien:

1. noi ro file nao co rui ro
2. de xuat bo khoi commit hoac them `.gitignore`
3. khong commit/push neu user chua xac nhan ro

### Deploy-sensitive gate

Internal git la noi chay pipeline, nen diff co anh huong build/deploy phai duoc canh bao ro.

Xem la deploy-sensitive neu diff cham vao:

- `.gitlab-ci.yml`, `.github/workflows/**`
- `vite.config.*`, `webpack.config.*`, `next.config.*`, `nuxt.config.*`
- `package.json` neu doi `build`, `dev`, `preview`, `deploy`
- `.env.production`, `.env.staging`, `.env.*.local`
- `Dockerfile`, `docker-compose*.yml`, `nginx.conf`, `vercel.json`, `netlify.toml`
- `src/config/**`, `config/**`, `public/config/**`
- moi file co `base path`, `build path`, `deploy destination`, `asset prefix`, `host`, `API URL`

Neu gap nhom nay:

1. noi ro push sai co the lam CI/CD do
2. tom tat diff `old -> new`
3. neu co ban dang chay on dinh, uu tien diff voi ban do
4. hoi user/dev xac nhan thay doi nay la co y
5. neu chua duoc xac nhan, khong commit, khong push, khong khuyen khich merge

### Multi-repo deploy drift

Neu nhieu repo frontend cung nhom:

- khong coi moi `.gitlab-ci.yml` la doc lap mac dinh
- neu dev team da xac nhan shared template la source of truth, uu tien canh do
- neu repo co subpath rieng, giu deploy contract rieng cua repo do
- khi nghi co subpath, kiem tra dong bo ca 4 diem:
  - deploy destination
  - public URL
  - `base` trong `vite.config.*`
  - `basename` cua router neu dung browser routing

Mac dinh voi user nay:

- `UGC Website` la repo tham chieu ve nguyen tac CI/CD
- nhung repo co subpath rieng chi muon giong ve nguyen tac, khong copy may moc file config
