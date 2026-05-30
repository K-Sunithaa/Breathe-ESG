# TRADEOFFS.md

## 1. No OCR Support

Not implemented:
Extraction from PDF utility bills.

Reason:
CSV-based ingestion was prioritized due to time constraints.

Impact:
PDF documents must be converted to structured data before upload.

---

## 2. No Authentication System

Not implemented:
User login, roles, and permissions.

Reason:
Assignment focus was data ingestion and review workflows.

Impact:
All users currently have equal access.

---

## 3. No Emission Factor Engine

Not implemented:
Automatic carbon emissions calculations.

Reason:
The assignment primarily focuses on ingestion, normalization, issue management, and auditing.

Impact:
The platform stores activity data but does not calculate CO₂e values.

---

## 4. No External API Integrations

Not implemented:
Live SAP, utility, or travel platform integrations.

Reason:
A file-based ingestion approach allowed faster prototyping.

Impact:
Data must be uploaded manually.