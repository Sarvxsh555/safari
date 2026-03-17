import { useEffect, useState } from "react";
import { getShapGlobal } from "../api/api";
import PageWrapper from "../components/PageWrapper";

export default function Shap() {
  const [data, setData] = useState({});

  useEffect(() => {
    getShapGlobal().then((res) => setData(res.data));
  }, []);

  return (
    <PageWrapper>
      <div className="mx-auto max-w-7xl p-10">
        <h1 className="text-3xl font-semibold tracking-tight">Explainability</h1>
        <p className="mt-2 text-sm text-gray-400">Global feature importance from the latest SHAP analysis.</p>
        <div className="mt-8 space-y-3 rounded-2xl border border-border bg-card p-6">
          {data.features?.map((f, i) => (
            <div
              key={f}
              className="flex items-center justify-between rounded-xl border border-border px-4 py-3 transition duration-200 ease-in-out hover:bg-[#1a1d23]"
            >
              <span>{f}</span>
              <span className="text-sm text-gray-400">{data.importance[i]}</span>
            </div>
          ))}
        </div>
      </div>
    </PageWrapper>
  );
}
