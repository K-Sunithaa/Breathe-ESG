# SOURCES.md

## SAP Research

Reviewed:
- SAP CSV exports
- SAP OData services
- SAP IDoc concepts

Key Learnings:
- SAP exports often contain plant codes.
- Data may contain inconsistent units.
- Date formats vary across implementations.

Prototype Choice:
CSV upload.

---

## Utility Data Research

Reviewed:
Typical utility consumption exports from online utility portals.

Key Learnings:
- Consumption is commonly measured in kWh.
- Billing periods may not align with calendar months.
- Facilities teams frequently work with spreadsheets.

Prototype Choice:
CSV upload.

---

## Travel Platform Research

Reviewed:
Concur and Navan reporting structures.

Key Learnings:
- Travel records may include flights, hotels, and ground transport.
- Airport codes are frequently used.
- Distances are not always provided.

Prototype Choice:
CSV upload.

---

## Real-World Challenges

Future production deployments would require:

- Authentication and authorization
- OCR support for utility PDFs
- External API integrations
- Emission factor management
- Advanced validation workflows
- Large-scale tenant isolation

---

## Sample Data Used

SAP:
Fuel and procurement records with plant codes.

Utility:
Electricity consumption records with billing periods.

Travel:
Flight and hotel records representing Scope 3 activities.