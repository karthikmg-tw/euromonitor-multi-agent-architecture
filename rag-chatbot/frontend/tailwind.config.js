/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'chat-bg': '#1e1e1e',
        'chat-secondary': '#212121',
        'chat-tertiary': '#2f2f2f',
        'chat-border': '#3f3f3f',
        'chat-accent': '#19c37d',
      }
    },
  },
  plugins: [],
}
