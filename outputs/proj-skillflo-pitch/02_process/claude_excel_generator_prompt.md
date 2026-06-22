# Ready-to-use Claude Prompt for Excel Generation

Copy the prompt below and paste it into Claude to generate the styled Excel file using Python (`openpyxl`) or to let Claude output the formatted data blocks.

***

```markdown
You are a senior Financial Analyst & Data Presentation Expert. I need your help to generate a professional, presentation-ready Excel spreadsheet based on the raw Airtable database query from OAC (a boutique recruitment/headhunting firm) which is preparing for M&A and fundraising discussions with a partner named Skillflo.

### 📋 Objective:
Write a Python script using `openpyxl` that generates a beautifully styled Excel workbook named `OAC_Fundraising_Database_Analysis.xlsx`. The workbook must contain exactly 2 worksheets:
1. **`OAC_Raw_Data_Summary`**: A sheet summarizing the raw data categorized, including active accounts, candidate completeness, database limits, and explicitly stating missing/unverifiable fields.
2. **`Pitch_Deck_Metrics_Ratio`**: A sheet containing calculated performance ratios, funnel metrics, speed timelines, client stickiness, and geographic distributions that are beneficial for a pitch deck.

---

### 🎨 Visual & Styling Guidelines:
To match high-level professional standards:
- **Theme Color (Primary Headers):** Steel Blue (`#1F4E79`), Font: white, bold, 11pt.
- **Limitation/Warning Headers:** Soft Peach (`#FCE4D6`), Font: dark brown (`#5B2C00`), bold, 11pt (to emphasize data diligence).
- **Zebra Striping:** Alternating data rows filled with very light gray (`#F2F2F2`).
- **Total Rows:** Filled with light green Accent (`#E2EFDA`), font bold, with a double bottom border.
- **Font:** Calibri throughout (16pt for Title, 12pt for Section Headers, 10pt for data, 9pt italic for footnotes).
- **Alignment:** Left-align text, right-align numeric values, center status and percentages.
- **Formats:**
  - VND: `#,##0` (with Currency label or notes)
  - USD: `"$#,##0.00"`
  - Percentage: `0.0%`
  - Floating numbers (Days): `0.0`
- **Auto-fit Columns:** Automatically adjust column widths with padding, ensuring no text is clipped. Set manual widths for text-heavy columns (e.g. Wrap Text).
- **Gridlines:** Force gridlines to be visible (`ws.views.sheetView[0].showGridLines = True`).

---

### 📊 Raw Data Source (Airtable Live Query):
Here is the exact dataset retrieved from OAC Airtable:
- Total Records: Zoho Applications (3,823), Daily Performance Tracker (1,482), Screening (1,351), Candidates (810), Jobs (410), Weekly Performance Tracker (422), Applications (464), Clients (72), Activity Log (2,317), Placement (38), Users (22), KPI & Actual (12).
- Placements: 38 records. Onboard Date populated for 37/38 (2024: 4, 2025: 25, 2026: 8, Unknown: 1). Jobs status Filled: 51, Filled out of warranty: 6. Total Deal Size: 4,351,478,357 VND / 167,224.22 USD.
- Client Statuses (72 clients): Current Client: 18, Active Opportunity: 10, Inactive: 23, Dead Opportunity: 12, Drop and Stop: 5, Dead Client: 4. Clients with linked jobs: 66/72. Repeat clients (linked jobs): 2+ jobs (46), 3+ jobs (33), 5+ jobs (22).
- Geographic revenue (Placement): Vietnam (2.951B VND), Australia (1.008B VND), Singapore (214.9M VND), Japan (90.2M VND), Canada (86.7M VND).
- Sourcing Locations (Job Count): Vietnam: 159, Singapore: 80, Australia: 23, Japan: 22, Thailand: 20, US: 18, HCM: 17, HN: 8, Canada: 6, Malaysia: 6, Poland: 5, UK: 3.
- Candidate database (810 candidates): Sent out: 428, New: 133, Rejected by AM: 133, Rejected by client: 51, Approved: 30, Screened: 15, Job Pending: 14, Hired: 4, Dropped: 2.
- Completeness: CV Link (808/810), Summary Note (746/810), Email (645/810), Phone (585/810), LinkedIn (427/810), CV + contact (646/810), Email+Phone+LinkedIn (411/810), Salary expectation (501/810), Linked screening (209/810), AI evaluation (122/810).
- Zoho applications: 3,823 records (combined raw database candidate records = 4,633).
- Client Concentration (Deal Size): RightShip (1.097B VND, 10 placements), Omnistream (1.022B VND, 6 placements), StoryCO (526.7M VND, 2 placements), Prudential (492M VND, 2 placements), AIA (271.8M VND), Luke (237.4M VND), Everfit (155.5M VND), TC Advisor (138.4M VND, 5 placements), Eduholic (132.4M VND, 5 placements), Pueo International (90.2M VND). Top 1 concentration: 25.2%, Top 3: 60.8%, Top 5: 78.4%.
- Recruiter Performance (Selling Value): Peter (1.453B VND), Lauren (883.2M VND), Serena (763.8M VND), Ellie (714.4M VND), Vicky (492.5M VND), Đào Hà (482.1M VND), Amy (242.7M VND), Tina (216.0M VND), Anna (141.6M VND), Alice (110.2M VND).
- Operational Funnel Timelines (Median & Averages):
  - Time to 1st Source: Median 4 days (Avg 16 days)
  - Time to 1st Sent-out: Median 8.5 days (Avg 22.5 days)
  - Time to 1st Interview: Median 18 days (Avg 28 days)
  - Time to Onboard (JD to Onboard): Median 93.5 days (Avg 128.6 days)
- Funnel Conversion: Total applications: 464. 1st interview achieved: 155/464. Sent-out to 1st interview average: 14.2 days (Median 8 days). Late-stage pipeline count: 21 (Offer Made + To be onboarded + Onboarded).
- Limitations/Missing fields: 0 cash received data (VND/USD/SGD received fields blank), KPI actuals are all 0 (no GP/OP trend), no Academy cohort records, no Alumni status tags, no Warranty/Retention outcomes, no contracting/retainer headcount metrics.

---

### 📝 Instructions for Code Generation:
Write a Python script using `openpyxl` that builds the sheets with the following exact layout and logic. 

**Sheet 1: `OAC_Raw_Data_Summary` Layout:**
- A Title Block starting at Row 1, Column B.
- **Table 1.1:** Database Tables & Record Count (B5:C18).
- **Table 1.2:** Placement & Financial Metrics (B21:E30) - VND and USD rows.
- **Table 1.3:** Client Engagement Status (G5:I13) - including a total row.
- **Table 1.4:** Candidate Database Completeness (G16:I27).
- **Table 1.5:** Airtable Limitations & Missing Fields (B34:E42) - Using soft-orange warning fills for primary headers, wrapping text, listing all unconfigured metrics (Gross Profit, Academy trained counts, Alumni, Warranty, Retained tag, Contracting).

**Sheet 2: `Pitch_Deck_Metrics_Ratio` Layout:**
- **Table 2.1:** Operational Speed & Sourcing Funnel Timelines (B5:E10) - Median vs Average comparison columns.
- **Table 2.2:** Sourcing Funnel Conversion Rates (B12:E18) - CV Submitted, 1st Interview, Placements (conservative: 8.2%), Placements (broad ATS: 12.3%), and Late-stage Pipeline (4.5%).
- **Table 2.3:** Client Account Stickiness & Concentration (G5:I11) - Client Repeat Mandate Rate (69.7%), High-Volume Client Rate (33.3%), Top 1/3/5 concentrations.
- **Table 2.4:** Geographic Revenue Allocation (G12:I19) - placement revenue and percentage share per country.
- **Table 2.5:** Sourcing Channels Distribution (B21:D28) - LinkedIn, FB, referrals, others.
- **Table 2.6:** Top 10 Recruiter Performance Selling Value (G21:I32) - absolute VND values and percentage shares.

Ensure all calculations are precise. Double check cell formatting, row heights, column auto-fit, and gridlines before finishing.
```
***
