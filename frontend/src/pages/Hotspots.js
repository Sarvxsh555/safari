import { useEffect, useState } from "react";
import { getHotspots } from "../api/api";
import PageWrapper from "../components/PageWrapper";

export default function Hotspots() {
  const [data, setData] = useState([]);

  useEffect(() => {
    getHotspots().then((res) => setData(res.data));
  }, []);

  return (
    <PageWrapper>
      <div className="mx-auto max-w-7xl p-10">
        <h1 className="text-3xl font-semibold tracking-tight">Hotspots</h1>
        <p className="mt-2 text-sm text-gray-400">Segments with the highest predicted collision risk.</p>
        <div className="mt-8 space-y-3 rounded-2xl border border-border bg-card p-6">
          {data.map((h) => (
            <div
              key={h.id}
              className="flex items-center justify-between rounded-xl border border-border px-4 py-3 transition duration-200 ease-in-out hover:bg-[#1a1d23]"
            >
              <span className="text-white">{h.id}</span>
              <span className="text-sm text-gray-400">{h.risk_score.toFixed(2)}</span>
            </div>
          ))}
        </div>
      </div>
    </PageWrapper>
  );
}
