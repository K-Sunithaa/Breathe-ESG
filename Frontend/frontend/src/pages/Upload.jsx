import axios from "axios";
import { useState } from "react";

export default function Upload() {

  const [selectedFile, setSelectedFile] = useState(null);
  const [sourceType, setSourceType] = useState("SAP");

  const handleUpload = async () => {

    if (!selectedFile) {
      alert("Please select a file");
      return;
    }

    const formData = new FormData();

    formData.append("file", selectedFile);

    // SEND BUSINESS SOURCE TYPE
    formData.append("source_type", sourceType);

    try {

      const response = await axios.post(
        "http://127.0.0.1:8000/upload/",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      console.log(response.data);

      alert("Upload successful");

    } catch (error) {

      console.error(error);

      alert("Upload failed");
    }
  };

  return (
    <div style={{ padding: "20px" }}>

      <h1>Upload ESG File</h1>

      <input
        type="file"
        accept=".csv,.xlsx,.xls,.pdf"
        onChange={(e) => setSelectedFile(e.target.files[0])}
      />

      <br /><br />

      <select
        value={sourceType}
        onChange={(e) => setSourceType(e.target.value)}
      >
        <option value="SAP">SAP</option>
        <option value="UTILITY">UTILITY</option>
        <option value="TRAVEL">TRAVEL</option>
      </select>

      <br /><br />

      <button onClick={handleUpload}>
        Upload
      </button>

    </div>
  );
}