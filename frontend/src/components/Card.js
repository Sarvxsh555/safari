import { motion } from "framer-motion";

export default function Card({ title, value }) {
  return (
    <motion.div
      whileHover={{ y: -3 }}
      transition={{ duration: 0.25 }}
      className="rounded-2xl border border-border bg-card p-6 shadow-sm"
    >
      <p className="mb-2 text-xs tracking-wide text-gray-400">{title}</p>
      <h2 className="text-2xl font-semibold tracking-tight text-white">{value}</h2>
    </motion.div>
  );
}
