import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path';

export default defineConfig({
  plugins: [
    react(),
  ],
  build: {
    manifest: true,  
    rollupOptions: {
      input: './src/main.tsx', 
    },
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
      '@assets/*': path.resolve(__dirname, './src/assets/*'),
      '@components/*': path.resolve(__dirname, './src/components/*'),
      '@models/*': path.resolve(__dirname, './src/models/*'),
      '@services/*': path.resolve(__dirname, './src/services/*'),
    },

  },
});

