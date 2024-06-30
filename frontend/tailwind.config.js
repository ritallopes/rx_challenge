/** @type {import('tailwindcss').Config} */
import { theme } from './theme'

export default {
  content: ['./src/**/*.{js,jsx,ts,tsx}', './public/index.html'],
  darkMode: 'class',
  theme,
  plugins: [],
}