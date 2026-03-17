import { useEffect, useState } from "react";
import { getOverview, getTrend } from "../api/api";
import Card from "../components/Card";
import PageWrapper from "../components/PageWrapper";
import TrendChart from "../components/TrendChart";

export default function Overview() {
  const [data, setData] = useState({});
  const [trend, setTrend] = useState([]);

  useEffect(() => {
    getOverview().then((res) => setData(res.data));
    getTrend().then((res) => setTrend(res.data));
  }, []);

  return (
    <PageWrapper>
      <div className="mx-auto max-w-7xl p-10">
        <h1 className="text-3xl font-semibold tracking-tight">Intelligence Overview</h1>
        <p className="mt-2 text-sm text-gray-400">Operational snapshot of segment risk and model health.</p>
        <div className="mt-8 grid gap-8 md:grid-cols-2 xl:grid-cols-4">
          <Card title="Critical Segments" value={data.critical_segments ?? "--"} />
          <Card title="Hotspots" value={data.emerging_hotspots ?? "--"} />
          <Card title="Segments" value={data.segments_monitored ?? "--"} />
          <Card title="Accuracy" value={data.model_accuracy != null ? `${data.model_accuracy}%` : "--"} />
        </div>
        <TrendChart data={trend} />
      </div>
    </PageWrapper>
  );
}
