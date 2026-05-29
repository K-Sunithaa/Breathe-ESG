import axios from "axios";

function Upload() {

  const handleUpload = async () => {

    if (!selectedFile) {
      alert("Please select a file");
      return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile);
    formData.append("source_type", sourceType);

    try {

      const response = await axios.post(
        "http://127.0.0.1:8000/upload/",
        formData
      );

      console.log(response.data);
      alert("Upload successful");

    } catch (error) {
      console.error(error);
      alert("Upload failed");
    }
  };

  return (
    <div>
      Upload Page
    </div>
  );
}

export default Upload;