# Diagram Patterns

Use these templates as starting points. Adapt labels to the Outline page, and keep Mermaid code smaller than the source table.

## Sequence: Operating Flow With Local And Regional Support

Use when the page describes a workflow after a local team takes ownership, with regional support only when needed.

```mermaid
sequenceDiagram
  autonumber

  box VN Local team
    participant Lead as PM / MKT Lead
    participant OM as Local OM
    participant Team as Creative / Campaign / UGC
    participant Data as Data team
  end

  box Regional support
    participant Reg as Regional OM
  end

  rect rgb(245, 247, 255)
    Note over Lead,OM: Phase 1 - Direction & planning
    Lead->>OM: Share DAU / revenue targets
    OM->>Lead: Confirm campaign plan
  end

  rect rgb(246, 255, 245)
    Note over OM,Team: Phase 2 - Execution
    OM->>OM: Setup ads

    loop Daily / weekly optimization
      OM->>OM: Monitor performance
      OM->>OM: A/B test and scale
    end

    par Creative supply
      OM->>Team: Request assets
      Team-->>OM: Deliver creatives
    and Campaign readiness
      OM->>Team: Align campaign and budget
      Team-->>OM: Confirm readiness
    end
  end

  rect rgb(255, 250, 240)
    Note over OM,Data: Phase 3 - Data & reporting
    OM->>Data: Align reporting needs
    Data-->>OM: Provide data inputs
    OM->>Lead: Send analysis report
  end

  rect rgb(250, 245, 255)
    opt Need regional guidance or setup
      Reg-->>OM: Advise on setup / testing
      Reg-->>OM: Support account setup
    end
  end
```

## Flowchart: Owner Map

Use when the page needs a quick owner-first view. Keep this high-level; do not include every task if it makes the graph too wide.

```mermaid
flowchart LR
  Lead["PM / MKT Lead"] --> Direction["Direction"]
  Direction --> D1["Business direction"]
  Direction --> D2["DAU / revenue alignment"]

  OM["Local OM"] --> Ads["Ads execution"]
  OM --> Creative["Local creative"]
  OM --> Data["Data & reporting"]
  Ads --> A1["Setup ads"]
  Ads --> A2["Optimize performance"]
  Ads --> A3["A/B test & scale"]

  Reg["Regional OM"] --> Consulting["Consulting"]
  Reg --> Setup["Account setup support"]
```

## Flowchart: Workstream Buckets

Use when workstreams matter more than people. Put owners inside nodes instead of drawing too many cross-links.

```mermaid
flowchart TB
  subgraph Direction["Direction"]
    D1["Business strategy<br/>Owner: PM / MKT Lead"]
    D2["Biz plan alignment<br/>Owner: PM / MKT Lead"]
  end

  subgraph Execution["Ads execution"]
    A1["Setup ads<br/>Owner: Local OM"]
    A2["Weekly optimization<br/>Owner: Local OM"]
    A3["A/B test & scale<br/>Owner: Local OM"]
  end

  subgraph Support["Regional support"]
    R1["OM setup advice<br/>Owner: Regional OM"]
    R2["Appsflyers setup<br/>Owner: Regional OM"]
  end

  Direction --> Execution --> Support
```

## RACI-Lite Table For Outline

When ownership ambiguity matters, add a small table after the diagram. Use this instead of making the diagram carry all responsibility detail.

| Workstream | Accountable | Responsible | Consulted |
| --- | --- | --- | --- |
| Direction | PM / MKT Lead | PM / MKT Lead | Local OM |
| Ads execution | Local OM | Local OM | Regional OM |
| Data reporting | Local OM | Local OM + Data team | PM / MKT Lead |
| Regional setup support | Regional OM | Regional OM | Local OM |

## Review Checklist

- Can a PM understand the diagram in 30 seconds?
- Does the title say what question the diagram answers?
- Are support paths marked as optional when they are not part of the main flow?
- Are recurring tasks represented as `loop` instead of many repeated arrows?
- Are parallel tasks represented as `par` instead of a misleading strict sequence?
- Is the raw source table preserved below the diagram?
