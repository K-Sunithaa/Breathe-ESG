# DECISIONS.md

## SAP Data Source

Decision:
Handle SAP data as CSV uploads.

Reason:
SAP exports are commonly shared as spreadsheets or CSV files during reporting processes.

Handled:
- Plant codes
- Fuel consumption
- Procurement quantities
- Costs

Ignored:
- SAP IDocs
- BAPI integrations
- Complex SAP master data relationships

---

## Utility Data Source

Decision:
Handle utility data using CSV uploads.

Reason:
Facilities teams often export consumption data from utility portals.

Handled:
- Electricity consumption
- Meter information
- Billing periods

Ignored:
- OCR extraction from PDF bills
- Direct utility APIs

---

## Travel Data Source

Decision:
Handle travel data using CSV exports.

Reason:
Travel platforms such as Concur and Navan commonly support downloadable reports.

Handled:
- Flights
- Hotels
- Ground transportation

Ignored:
- Real-time API integrations

---

## Unit Normalization

Decision:
Store both original unit and normalized unit.

Reason:
Auditors may need to see original values while analysts require standardized units.

---

## Audit Trail

Decision:
Track all important actions in AuditLog.

Reason:
Audit readiness is a key ESG reporting requirement.

---

## Review Workflow

Decision:
Require analyst review before records are considered audit-ready.

Reason:
Manual verification is important for ESG reporting accuracy.