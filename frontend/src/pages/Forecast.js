import { useEffect, useState } from "react";
import { getTrend } from "../api/api";
import PageWrapper from "../components/PageWrapper";
import TrendChart from "../components/TrendChart";

export default function Forecast() {
  const [trend, setTrend] = useState([]);

  useEffect(() => {
    getTrend().then((res) => setTrend(res.data));
  }, []);

  return (
    <PageWrapper>
      <div className="mx-auto max-w-7xl p-10">
        <h1 className="text-3xl font-semibold tracking-tight">Forecast</h1>
        <p className="mt-2 text-sm text-gray-400">Projected incident trend against predicted risk over time.</p>
        <TrendChart data={trend} />
      </div>
    </PageWrapper>
  );
}
