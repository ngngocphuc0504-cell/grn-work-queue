# Outline Memory Page Map

## Write Policy

- Hard write lock: only documents inside collection `Hai Son` are writable by this skill.
- Collection URL: `https://wiki.odp.garena.vn/collection/hai-son-QaFXg2Zdw0/recent`
- Writable docs:
  - `HUB - Hai-Son Context`
  - `Personal Memory - Canonical`
  - `Personal Memory - Inbox Journal`
  - `Memory Router Map`
- All project documents listed below are read-only from the perspective of this skill.

## Global Memory Docs

- `HUB - Hai-Son Context`
  - id: `bd372ec3-f05f-4668-bc52-c03970528f4e`
  - url: `https://wiki.odp.garena.vn/doc/hub-hai-son-context-SPYq1L4Zq8`
- `Personal Memory - Canonical`
  - id: `b362f562-5d5a-43b2-a813-e58e4dfd9353`
  - url: `https://wiki.odp.garena.vn/doc/personal-memory-canonical-kmELel4mcP`
- `Personal Memory - Inbox Journal`
  - id: `2838f89c-ca0d-4233-9784-8792be374fac`
  - url: `https://wiki.odp.garena.vn/doc/personal-memory-inbox-journal-HigAWe1B6V`
- `Memory Router Map`
  - id: `845e77a3-4d62-4ffa-897c-2724ec3682a6`
  - url: `https://wiki.odp.garena.vn/doc/memory-router-map-w2R3bUTd57`

## Project Bootstraps

- `ugc-website`
  - bootstrap: `UGC Website Context`
  - id: `89a3629a-83e3-4c69-8131-f1be38f225f8`
  - url: `https://wiki.odp.garena.vn/doc/ugc-website-context-eOyKS2A1d1`
  - project hub: `https://wiki.odp.garena.vn/doc/ugc-website-3mC4RHXzh1`
  - write policy: `read-only`

- `social-listening`
  - bootstrap: `Social listening Context`
  - id: `26ffcdfe-6be7-471a-a33a-b96f670a34db`
  - url: `https://wiki.odp.garena.vn/doc/social-listening-context-vWVVGyNDuB`
  - project hub: `https://wiki.odp.garena.vn/doc/social-listening-ngIWEVuwP0`
  - write policy: `read-only`

- `aov-card-game`
  - bootstrap: `00 Agent Entry`
  - id: `709dce84-2484-4437-9de4-75110c1f77f9`
  - url: `https://wiki.odp.garena.vn/doc/00-agent-entry-oHEEyvTRej`
  - write policy: `read-only`

## Routing Reminder

- Default scope when unresolved: `global-default`
- Project-specific canonical docs override global context.
- If a page is outside collection `Hai Son`, do not write to it.
- If a page is not listed as a writable personal doc, do not auto-write to it.
