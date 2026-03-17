import { BrowserRouter, Route, Routes } from "react-router-dom";
import Sidebar from "./components/Sidebar";
import Forecast from "./pages/Forecast";
import Hotspots from "./pages/Hotspots";
import Overview from "./pages/Overview";
import RiskMap from "./pages/RiskMap";
import Shap from "./pages/Shap";
import Table from "./pages/Table";

function App() {
  return (
    <BrowserRouter>
      <div className="flex min-h-screen bg-bgDark">
        <Sidebar />
        <div className="flex-1">
          <Routes>
            <Route path="/" element={<Overview />} />
            <Route path="/map" element={<RiskMap />} />
            <Route path="/hotspots" element={<Hotspots />} />
            <Route path="/shap" element={<Shap />} />
            <Route path="/forecast" element={<Forecast />} />
            <Route path="/table" element={<Table />} />
          </Routes>
        </div>
      </div>
    </BrowserRouter>
  );
}

export default App;
