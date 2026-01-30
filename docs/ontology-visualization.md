# Knowledge Graph Ontology Visualization

## Core Ontology Diagram

```mermaid
graph TB
    %% Geography Hierarchy
    Region[Geography: Region<br/>Asia Pacific]
    Country[Geography: Country<br/>India]

    %% Category Hierarchy
    Industry[Category: Level 0<br/>Toys and Games]
    Segment[Category: Level 1<br/>Video Games]
    Category[Category: Level 2<br/>Video Games Software]
    Subcategory[Category: Level 3<br/>Hand-Held Consoles]

    %% Companies & Brands
    GBO[Company: GBO<br/>Sony Corporation]
    NBO[Company: NBO<br/>Sony India Pvt Ltd]
    GBN[Brand: GBN<br/>PlayStation Global]
    LBN[Brand: LBN<br/>PlayStation India]

    %% Market Data
    MarketSize[MarketSize<br/>India Toys 2010-2029<br/>data: 2024=2795M CHF]
    MarketShare[MarketShare<br/>Sony India Market Share<br/>2024=18.5%]

    %% Sources & Citations
    Source1[Source<br/>Euromonitor Passport<br/>Toys India 2025]
    Source2[Source<br/>NCAER<br/>Official Statistics]

    %% Reports (Phase 3)
    Report[Report<br/>Toys and Games in India<br/>embedding: 1536-dim vector]

    %% Relationships
    Country -->|LOCATED_IN| Region

    Segment -->|BELONGS_TO| Industry
    Category -->|BELONGS_TO| Segment
    Subcategory -->|BELONGS_TO| Category

    NBO -->|PARENT_COMPANY| GBO
    LBN -->|OWNED_BY| NBO
    LBN -->|PARENT_BRAND| GBN

    Country -->|HAS_MARKET_SIZE| MarketSize
    MarketSize -->|HAS_MARKET_SIZE| Industry

    MarketSize -->|SOURCED_FROM| Source1
    MarketSize -->|SOURCED_FROM| Source2

    NBO -->|HAS_SHARE| MarketShare
    MarketShare -->|FOR_CATEGORY| Industry
    MarketShare -->|IN_GEOGRAPHY| Country

    NBO -->|COMPETES_IN| Category
    NBO -->|OPERATES_IN| Country

    Report -->|MENTIONS| NBO
    Report -->|MENTIONS| Category
    Report -->|CITES| Source1

    %% Styling
    classDef geography fill:#e1f5ff,stroke:#01579b
    classDef category fill:#fff9c4,stroke:#f57f17
    classDef company fill:#f3e5f5,stroke:#4a148c
    classDef brand fill:#fce4ec,stroke:#880e4f
    classDef data fill:#e8f5e9,stroke:#1b5e20
    classDef source fill:#fff3e0,stroke:#e65100
    classDef report fill:#f1f8e9,stroke:#33691e

    class Region,Country geography
    class Industry,Segment,Category,Subcategory category
    class GBO,NBO company
    class GBN,LBN brand
    class MarketSize,MarketShare data
    class Source1,Source2 source
    class Report report
```

## Detailed Node Structure

### Geography Node
```mermaid
classDiagram
    class Geography {
        +String id
        +String name
        +String type
        +int level
        +String iso_code
        +String region
        +long population_2024
    }
```

### Category Node
```mermaid
classDiagram
    class Category {
        +String id
        +String name
        +String full_name
        +int level
        +String industry
        +String parent_id
        +String definition
        +boolean is_lowest_level
    }
```

### MarketSize Node
```mermaid
classDiagram
    class MarketSize {
        +String id
        +String geography_id
        +String category_id
        +String data_type
        +String unit
        +Map historical_data
        +Map forecast_data
        +double historic_cagr
        +double forecast_cagr
        +List source_ids
    }

    class Source {
        +String id
        +String name
        +String type
        +String url
        +Date publication_date
    }

    MarketSize --> Source : SOURCED_FROM
```

## Relationship Types Summary

| Relationship | From | To | Purpose |
|--------------|------|-----|---------|
| `LOCATED_IN` | Geography (Country) | Geography (Region) | Geographic hierarchy |
| `BELONGS_TO` | Category (child) | Category (parent) | Category taxonomy |
| `HAS_MARKET_SIZE` | Geography/Category | MarketSize | Data linkage |
| `SOURCED_FROM` | MarketSize/MarketShare | Source | Citation tracking |
| `OWNED_BY` | Brand | Company | Brand ownership |
| `PARENT_COMPANY` | Company (NBO) | Company (GBO) | Corporate hierarchy |
| `COMPETES_IN` | Company | Category | Market participation |
| `OPERATES_IN` | Company | Geography | Geographic presence |
| `HAS_SHARE` | Company/Brand | MarketShare | Market share data |
| `MENTIONS` | Report | Category/Company/Brand | Content reference |
| `CITES` | Report | Source | Report citations |

## Example Query Paths

### Path 1: Market Size Query
```mermaid
flowchart LR
    A[User Query:<br/>Toys market in India] --> B[Geography: India]
    A --> C[Category: Toys and Games]
    B --> D[MarketSize]
    C --> D
    D --> E[Source: Passport]
    D --> F[Historical Data:<br/>2024=2795M CHF]

    style A fill:#ffeb3b
    style D fill:#4caf50
    style E fill:#ff9800
```

### Path 2: Company Analysis
```mermaid
flowchart LR
    A[User Query:<br/>Sony's market position] --> B[Company: Sony India]
    B --> C[OPERATES_IN]
    C --> D[Geography: India]
    B --> E[COMPETES_IN]
    E --> F[Category: Video Games]
    B --> G[HAS_SHARE]
    G --> H[MarketShare: 18.5%]
    H --> I[Source: Company Reports]

    style A fill:#ffeb3b
    style B fill:#9c27b0
    style H fill:#4caf50
```

### Path 3: Citation Validation
```mermaid
flowchart LR
    A[AI Generated Claim:<br/>India toys market = 2796M CHF] --> B[Extract Metric ID]
    B --> C[Query: MarketSize]
    C --> D[Validate Value:<br/>2795.55 ≈ 2796 ✓]
    C --> E[SOURCED_FROM]
    E --> F[Source: Euromonitor Passport]
    F --> G[Return Citation:<br/>Dataset, URL, Date]

    style A fill:#ffeb3b
    style D fill:#4caf50
    style F fill:#ff9800
```

## Hybrid: Structured + Unstructured (Phase 3)

```mermaid
graph TB
    subgraph Structured Data
        Geo[Geography: India]
        Cat[Category: Toys]
        MS[MarketSize<br/>2795M CHF 2024]
        Comp[Company: Sony India]
    end

    subgraph Unstructured Data
        R1[Report: Toys in India 2025<br/>embedding: vector]
        R2[Report: Regulatory Brief<br/>embedding: vector]
    end

    subgraph Query Flow
        Q[User Query:<br/>Regulatory changes toys India]
        VQ[Vector Query<br/>embedding]
        GQ[Graph Query<br/>MATCH paths]
    end

    Q --> VQ
    VQ --> R1
    VQ --> R2
    R1 -->|MENTIONS| Cat
    R1 -->|MENTIONS| Comp
    R2 -->|MENTIONS| Cat

    Q --> GQ
    GQ --> Geo
    GQ --> Cat
    Geo --> MS
    Cat --> MS

    style Q fill:#ffeb3b
    style R1 fill:#8bc34a
    style R2 fill:#8bc34a
    style MS fill:#4caf50
```

---

## How to View This

### In GitHub/GitLab:
Markdown files with Mermaid diagrams render automatically in most Git UIs.

### In VS Code:
1. Install extension: "Markdown Preview Mermaid Support"
2. Open this file: `docs/ontology-visualization.md`
3. Press `Cmd+Shift+V` (Mac) or `Ctrl+Shift+V` (Windows) to preview

### In Browser:
Copy the Mermaid code to https://mermaid.live for interactive editing.

