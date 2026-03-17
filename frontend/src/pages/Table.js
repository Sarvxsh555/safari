import { useEffect, useState } from "react";
import { getTable } from "../api/api";
import PageWrapper from "../components/PageWrapper";

export default function Table() {
  const [data, setData] = useState([]);

  useEffect(() => {
    getTable().then((res) => setData(res.data));
  }, []);

  return (
    <PageWrapper>
      <div className="mx-auto max-w-7xl p-10">
        <h1 className="text-3xl font-semibold tracking-tight">Segment Analysis</h1>
        <p className="mt-2 text-sm text-gray-400">Ranked segments with risk level and incident history.</p>
        <div className="mt-8 overflow-hidden rounded-2xl border border-border bg-card">
          <table className="w-full">
            <thead className="bg-[#0f172a] text-left text-sm text-gray-400">
              <tr>
                <th className="px-6 py-4 font-medium">ID</th>
                <th className="px-6 py-4 font-medium">Risk</th>
                <th className="px-6 py-4 font-medium">Level</th>
                <th className="px-6 py-4 font-medium">Incidents</th>
              </tr>
            </thead>
            <tbody>
              {data.map((row) => (
                <tr key={row.id} className="border-t border-border transition duration-200 ease-in-out hover:bg-[#1a1d23]">
                  <td className="px-6 py-4">{row.id}</td>
                  <td className="px-6 py-4">{row.risk_score.toFixed(2)}</td>
                  <td className="px-6 py-4">{row.risk_level}</td>
                  <td className="px-6 py-4">{row.historical_incidents}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </PageWrapper>
  );
}
