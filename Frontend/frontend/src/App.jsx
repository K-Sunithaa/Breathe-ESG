import { BrowserRouter, Routes, Route, Link } from "react-router-dom";

import Dashboard from "./pages/Dashboard";
import Upload from "./pages/Upload";
import Records from "./pages/Records";

function App() {
  return (
    <BrowserRouter>
      <div style={{ padding: "20px" }}>

        <nav style={{ marginBottom: "20px" }}>
          <Link to="/" style={{ marginRight: "15px" }}>
            Dashboard
          </Link>

          <Link to="/upload" style={{ marginRight: "15px" }}>
            Upload
          </Link>

          <Link to="/records">
            Records
          </Link>
        </nav>

        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/upload" element={<Upload />} />
          <Route path="/records" element={<Records />} />
        </Routes>

      </div>
    </BrowserRouter>
  );
}

export default App;