/** @type {import(''tailwindcss'').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx}"],
  theme: {
    extend: {
      colors: {
        primary: "#22c55e",
        bgDark: "#0f1115",
        card: "#16181d",
        border: "#23262d",
        textMuted: "#9ca3af",
      },
    },
  },
  plugins: [],
};
