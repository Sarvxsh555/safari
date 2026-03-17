import { motion } from "framer-motion";
import { NavLink } from "react-router-dom";

const links = [
  { to: "/", label: "Overview" },
  { to: "/map", label: "Risk Map" },
  { to: "/hotspots", label: "Hotspots" },
  { to: "/shap", label: "Explainability" },
  { to: "/forecast", label: "Forecast" },
  { to: "/table", label: "Segment Analysis" },
];

export default function Sidebar() {
  return (
    <aside className="sticky top-0 flex h-screen w-64 flex-col border-r border-border bg-[#121417] p-6">
      <h1 className="mb-10 text-lg font-medium text-white">SAFARI</h1>
      <nav className="flex flex-col gap-5 text-sm text-gray-400">
        {links.map((link) => (
          <motion.div key={link.to} whileHover={{ x: 4 }} transition={{ duration: 0.2 }}>
            <NavLink
              to={link.to}
              className={({ isActive }) =>
                `transition duration-200 ease-in-out hover:text-white ${
                  isActive ? "text-white" : "text-gray-400"
                }`
              }
            >
              {link.label}
            </NavLink>
          </motion.div>
        ))}
      </nav>
      <div className="mt-auto text-xs text-gray-500">Analytics Engine</div>
    </aside>
  );
}
