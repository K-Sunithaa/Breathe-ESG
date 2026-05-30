# MODEL.md

## Overview

The system ingests ESG-related data from SAP, Utility, and Travel sources, normalizes the data into a common structure, identifies quality issues, supports analyst reviews, and maintains an audit trail.

---

## RawUpload

Purpose:
Stores uploaded source files before processing.

Fields:
- file
- source_type (SAP, UTILITY, TRAVEL)
- uploaded_at

Why:
Provides source-of-truth tracking and allows traceability back to the original uploaded file.

---

## NormalizedRecord

Purpose:
Stores standardized records generated from uploaded data.

Key Fields:
- tenant_id
- source_type
- source_system
- source_record_id
- source_file_name
- scope_category
- activity_type
- quantity
- unit
- normalized_unit
- facility_code
- plant_code
- billing_period_start
- billing_period_end
- status
- locked_for_audit

Why:
Different source systems use different formats. NormalizedRecord creates a common structure for reporting and auditing.

---

## DataIssue

Purpose:
Stores validation issues discovered during processing.

Fields:
- record
- issue_type
- severity
- description
- resolved

Examples:
- Missing quantity
- Invalid unit
- Negative values

---

## RecordReview

Purpose:
Supports analyst review and approval workflow.

Fields:
- record
- reviewer_name
- status
- reviewer_comment
- review_round

Workflow:
PENDING → APPROVED / REJECTED

---

## AuditLog

Purpose:
Maintains an immutable audit trail.

Fields:
- record
- action
- performed_by
- notes
- timestamp

Examples:
- UPLOAD
- NORMALIZED
- ISSUE_CREATED
- REVIEWED
- APPROVED
- REJECTED
- LOCKED

---

## Multi-Tenancy

The tenant_id field supports storing records belonging to multiple client organizations while using the same platform.

---

## ESG Scope Mapping

Scope 1:
Fuel consumption data.

Scope 2:
Purchased electricity.

Scope 3:
Business travel.