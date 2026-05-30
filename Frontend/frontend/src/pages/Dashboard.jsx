import { Link } from "react-router-dom";

function Dashboard() {
  return (
    <div style={{ padding: "30px" }}>
      <h1>Breathe ESG Analyst Dashboard</h1>

      <p>
        Ingest, review, validate and approve ESG records before audit sign-off.
      </p>

      <hr />

      <div
        style={{
          display: "flex",
          gap: "20px",
          flexWrap: "wrap",
          marginTop: "20px",
        }}
      >
        <div
          style={{
            border: "1px solid #ccc",
            padding: "20px",
            width: "250px",
            borderRadius: "8px",
          }}
        >
          <h3>📂 Upload Data</h3>
          <p>
            Upload SAP, Utility or Travel source files for ingestion.
          </p>

          <Link to="/upload">
            <button>Open</button>
          </Link>
        </div>

        <div
          style={{
            border: "1px solid #ccc",
            padding: "20px",
            width: "250px",
            borderRadius: "8px",
          }}
        >
          <h3>📊 Records</h3>
          <p>
            View normalized ESG records across all source systems.
          </p>

          <Link to="/records">
            <button>View Records</button>
          </Link>
        </div>

        <div
          style={{
            border: "1px solid #ccc",
            padding: "20px",
            width: "250px",
            borderRadius: "8px",
          }}
        >
          <h3>⚠ Data Issues</h3>
          <p>
            Review validation failures, missing fields and data quality issues.
          </p>

          <Link to="/issues">
            <button>View Issues</button>
          </Link>
        </div>

        <div
          style={{
            border: "1px solid #ccc",
            padding: "20px",
            width: "250px",
            borderRadius: "8px",
          }}
        >
          <h3>✅ Reviews</h3>
          <p>
            Analyst approval workflow and record review decisions.
          </p>

          <Link to="/reviews">
            <button>View Reviews</button>
          </Link>
        </div>

        <div
          style={{
            border: "1px solid #ccc",
            padding: "20px",
            width: "250px",
            borderRadius: "8px",
          }}
        >
          <h3>📝 Audit Trail</h3>
          <p>
            Track every action performed on ESG records.
          </p>

          <Link to="/audit-trail">
            <button>View Audit Logs</button>
          </Link>
        </div>
      </div>

      <hr style={{ marginTop: "30px" }} />

      <h2>Supported Data Sources</h2>

      <ul>
        <li>SAP Fuel & Procurement Data</li>
        <li>Utility Electricity Consumption Data</li>
        <li>Corporate Travel Data</li>
      </ul>

      <h2>ESG Coverage</h2>

      <ul>
        <li>Scope 1 Emissions</li>
        <li>Scope 2 Emissions</li>
        <li>Scope 3 Emissions</li>
      </ul>
    </div>
  );
}

export default Dashboard;