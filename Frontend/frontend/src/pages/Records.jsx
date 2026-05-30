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
    <div>

      <h1>Records</h1>

      <table border="1" cellPadding="10">

        <thead>
          <tr>
            <th>ID</th>
            <th>Source</th>
            <th>Quantity</th>
            <th>Cost INR</th>
            <th>Unit</th>
            <th>Status</th>
          </tr>
        </thead>

        <tbody>

          {records.map((record) => (
            <tr key={record.id}>
              <td>{record.id}</td>
              <td>{record.source_type}</td>
              <td>{record.quantity}</td>
              <td>{record.cost_inr}</td>
              <td>{record.unit}</td>
              <td>{record.status}</td>
            </tr>
          ))}

        </tbody>

      </table>

    </div>
  );
}

export default Records;