import { useEffect, useState } from "react";
import API from "../services/api";

function Issues() {
  const [issues, setIssues] = useState([]);

  useEffect(() => {
    fetchIssues();
  }, []);

  const fetchIssues = async () => {
    try {
      const response = await API.get("reviews/issues/");
      setIssues(response.data);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Data Issues</h1>

      <table border="1" cellPadding="10">
        <thead>
          <tr>
            <th>ID</th>
            <th>Issue Type</th>
            <th>Severity</th>
            <th>Field</th>
            <th>Description</th>
            <th>Resolved</th>
          </tr>
        </thead>

        <tbody>
          {issues.map((issue) => (
            <tr key={issue.id}>
              <td>{issue.id}</td>
              <td>{issue.issue_type}</td>
              <td>{issue.severity}</td>
              <td>{issue.field_name}</td>
              <td>{issue.description}</td>
              <td>{issue.resolved ? "Yes" : "No"}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Issues;