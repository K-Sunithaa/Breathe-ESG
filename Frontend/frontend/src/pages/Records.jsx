import { useEffect, useState } from "react";
import API from "../services/api";

function Records() {
  const [records, setRecords] = useState([]);

  useEffect(() => {
    fetchRecords();
  }, []);

  const fetchRecords = async () => {
    try {
      const response = await API.get("records/");
      setRecords(response.data);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>ESG Records Dashboard</h1>

      <table border="1" cellPadding="10" style={{ borderCollapse: "collapse" }}>
        <thead>
          <tr>
            <th>ID</th>
            <th>Source</th>
            <th>Source System</th>
            <th>Tenant</th>
            <th>Scope</th>
            <th>Activity</th>
            <th>Quantity</th>
            <th>Unit</th>
            <th>Normalized Unit</th>
            <th>Cost (INR)</th>
            <th>Facility</th>
            <th>Plant</th>
            <th>Billing Start</th>
            <th>Billing End</th>
            <th>Status</th>
            <th>Audit Locked</th>
          </tr>
        </thead>

        <tbody>
          {records.map((record) => (
            <tr key={record.id}>
              <td>{record.id}</td>

              <td>{record.source_type}</td>

              <td>{record.source_system || "-"}</td>

              <td>{record.tenant_id}</td>

              <td>{record.scope_category}</td>

              <td>{record.activity_type || "-"}</td>

              <td>{record.quantity}</td>

              <td>{record.unit}</td>

              <td>{record.normalized_unit || "-"}</td>

              <td>{record.cost_inr}</td>

              <td>{record.facility_code || "-"}</td>

              <td>{record.plant_code || "-"}</td>

              <td>{record.billing_period_start || "-"}</td>

              <td>{record.billing_period_end || "-"}</td>

              <td>{record.status}</td>

              <td>
                {record.locked_for_audit ? "Yes" : "No"}
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      <br />

      <p>
        Total Records: <b>{records.length}</b>
      </p>
    </div>
  );
}

export default Records;