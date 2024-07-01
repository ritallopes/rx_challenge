import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import CssBaseline from '@mui/material/CssBaseline'
import Provider from './components/Providers'
import './styles/index.css'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <Provider>
      <CssBaseline />
      <App />
    </Provider>
  </React.StrictMode>,
)
