import { useEffect, useState } from "react";
import { motion } from "framer-motion";
import { CircleMarker, MapContainer, Popup, TileLayer } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import { getMapData } from "../api/api";
import PageWrapper from "../components/PageWrapper";

export default function RiskMap() {
  const [points, setPoints] = useState([]);

  useEffect(() => {
    getMapData().then((res) => {
      setPoints(res.data);
    });
  }, []);

  const getColor = (risk) => {
    if (risk > 0.75) return "red";
    if (risk > 0.5) return "orange";
    if (risk > 0.25) return "yellow";
    return "green";
  };

  return (
    <PageWrapper>
      <div className="mx-auto max-w-7xl p-10">
        <h1 className="text-3xl font-semibold tracking-tight">Risk Map</h1>
        <p className="mt-2 text-sm text-gray-400">Spatial distribution of current wildlife collision risk.</p>
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.4 }}
          className="mt-8 rounded-2xl border border-border bg-card p-4"
        >
          <MapContainer center={[20.5, 78.9]} zoom={5} className="h-[600px] rounded-xl">
            <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
            {points.map((p) => (
              <CircleMarker
                key={p.id}
                center={[p.lat, p.lon]}
                radius={8}
                color={getColor(p.risk_score)}
              >
                <Popup>
                  <b>{p.id}</b>
                  <br />
                  Risk: {p.risk_score.toFixed(2)}
                </Popup>
              </CircleMarker>
            ))}
          </MapContainer>
        </motion.div>
      </div>
    </PageWrapper>
  );
}
