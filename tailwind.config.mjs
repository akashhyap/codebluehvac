/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        accent: { DEFAULT: '#0055A5', dark: '#003B73' },
        dark: '#191919',
        light: '#F1F4F8',
        warm: '#E8EEF5',
        border: '#DEDEDE',
      },
      fontFamily: {
        heading: ['"Bebas Neue"', 'sans-serif'],
        body: ['Helvetica', 'Arial', 'sans-serif'],
        accent: ['"Pathway Extreme"', 'sans-serif'],
      },
      borderRadius: { card: '12px' },
    },
  },
  plugins: [],
};
