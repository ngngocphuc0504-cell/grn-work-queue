# Restructure Rules

## Purpose

Turn an existing Outline subtree into a clean owner-based project knowledge base without throwing away useful information.

## Default Policy

- preserve first
- preview before apply
- archive early when a page is stale or superseded

## Page Classification

Classify each page as one of:

- `owner-live`
- `hub-live`
- `support-live`
- `stale-but-salvageable`
- `superseded`
- `archive`
- `unknown`

## Decision Rules

### Keep

Keep the page live when:

- it already owns a distinct type of truth
- its role is still valid
- its content is not materially stale

### Rewrite or Repurpose

Rewrite or repurpose when:

- the page title or role is wrong but the content still has value
- the page overlaps a future owner page but can be turned into that owner page cleanly
- the page is a thin placeholder that should become a real hub or owner page

### Split

Split when:

- one page mixes multiple truths that should have different owners
- a hub page has grown into a spec page plus a navigator at the same time

### Archive

Archive when:

- the page is clearly superseded by a new owner page
- the content is stale enough that keeping it live would misroute readers
- the page still has provenance value or might still be linked elsewhere

Default archive move:

- keep the original content
- add a superseded note or pointer if needed
- remove the page from the default reading path

### Delete

Delete only when all are true:

- the content is clearly wrong or outdated
- provenance value is negligible
- archive would add clutter without preserving anything useful

## Duplicate Truth Rules

- Never leave two live pages owning the same type of truth.
- If two live pages overlap, choose one owner and either repurpose or archive the other.
- Prefer the page with better existing structure or stronger incoming links as the surviving owner when both are plausible.

## Pointer Rules

Use `archive + pointer` when:

- a page was recently live
- many other pages likely link to it
- the new owner page is different enough that readers need redirect help

Pointer note should state:

- why the page is no longer live
- which page replaces it
- whether it is historical only

## Reading Path Rules

- Live root and hub pages must link toward current owner pages.
- Archive pages must not appear in default reading paths.
- Operational pages must not duplicate canonical truth; they should summarize and route.

