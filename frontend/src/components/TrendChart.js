import {
  Line,
  LineChart,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";

function normalizeTrendData(data) {
  if (Array.isArray(data)) {
    return data;
  }

  if (
    data &&
    Array.isArray(data.months) &&
    Array.isArray(data.actual) &&
    Array.isArray(data.predicted)
  ) {
    return data.months.map((month, index) => ({
      month,
      actual: data.actual[index],
      predicted: data.predicted[index],
    }));
  }

  return [];
}

export default function TrendChart({ data }) {
  const chartData = normalizeTrendData(data);

  return (
    <div className="mt-8 rounded-2xl border border-border bg-card p-5">
      <h3 className="mb-4 text-sm text-gray-400">Incident vs Risk</h3>
      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={chartData}>
          <XAxis dataKey="month" stroke="#9ca3af" tickLine={false} axisLine={false} />
          <YAxis stroke="#9ca3af" tickLine={false} axisLine={false} />
          <Tooltip
            contentStyle={{
              backgroundColor: "#16181d",
              border: "1px solid #23262d",
              borderRadius: "16px",
              color: "#e5e7eb",
            }}
          />
          <Line type="monotone" dataKey="actual" stroke="#22c55e" strokeWidth={2} dot={false} />
          <Line type="monotone" dataKey="predicted" stroke="#f97316" strokeWidth={2} dot={false} />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}
