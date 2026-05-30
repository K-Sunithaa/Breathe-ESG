import { BrowserRouter, Routes, Route, Link } from "react-router-dom";

import Dashboard from "./pages/Dashboard";
import Upload from "./pages/Upload";
import Records from "./pages/Records";
import Issues from "./pages/Issues";
import ReviewsPage from "./pages/Reviews";
import AuditTrailPage from "./pages/AuditTrailPage";

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

          <Link to="/records" style={{ marginRight: "15px" }}>
            Records
          </Link>

          <Link to="/issues" style={{ marginRight: "15px" }}>
            Issues
          </Link>

          <Link to="/reviews" style={{ marginRight: "15px" }}>
            Reviews
          </Link>

          <Link to="/audit-trail">
            Audit Trail
          </Link>
        </nav>

        <Routes>
          <Route path="/" element={<Dashboard />} />

          <Route path="/upload" element={<Upload />} />

          <Route path="/records" element={<Records />} />

          <Route path="/issues" element={<Issues />} />

          <Route path="/reviews" element={<ReviewsPage />} />

          <Route path="/audit-trail" element={<AuditTrailPage />} />
        </Routes>

      </div>
    </BrowserRouter>
  );
}

export default App;