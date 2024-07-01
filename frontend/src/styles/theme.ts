import { createTheme, responsiveFontSizes } from '@mui/material/styles'

let lightTheme = createTheme({
  palette: {
    mode: 'light',
    primary: {
      main: '#9C27B0',
    },
    secondary: {
      main: '#556B2F',
    },
    background: {
      default: '#ffffff',
      paper: '#f5f5f5',
    },
    text: {
      primary: '#000000',
      secondary: '#4f4f4f',
    },
  },
  typography: {
    h1: {
      fontSize: '2rem',
      '@media (min-width:600px)': {
        fontSize: '2.5rem',
      },
      '@media (min-width:960px)': {
        fontSize: '3rem',
      },
      '@media (min-width:1280px)': {
        fontSize: '3.5rem',
      },
    },
    h2: {
      fontSize: '1.75rem',
      '@media (min-width:600px)': {
        fontSize: '2.25rem',
      },
      '@media (min-width:960px)': {
        fontSize: '2.75rem',
      },
      '@media (min-width:1280px)': {
        fontSize: '3.25rem',
      },
    },
    h3: {
      fontSize: '1.5rem',
      '@media (min-width:600px)': {
        fontSize: '2rem',
      },
      '@media (min-width:960px)': {
        fontSize: '2.5rem',
      },
      '@media (min-width:1280px)': {
        fontSize: '3rem',
      },
    },
    h4: {
      fontSize: '1.25rem',
      '@media (min-width:600px)': {
        fontSize: '1.75rem',
      },
      '@media (min-width:960px)': {
        fontSize: '2.25rem',
      },
      '@media (min-width:1280px)': {
        fontSize: '2.75rem',
      },
    },
    h5: {
      fontSize: '1rem',
      '@media (min-width:600px)': {
        fontSize: '1.5rem',
      },
      '@media (min-width:960px)': {
        fontSize: '2rem',
      },
      '@media (min-width:1280px)': {
        fontSize: '2.5rem',
      },
    },
    h6: {
      fontSize: '0.875rem',
      '@media (min-width:600px)': {
        fontSize: '1.25rem',
      },
      '@media (min-width:960px)': {
        fontSize: '1.75rem',
      },
      '@media (min-width:1280px)': {
        fontSize: '2.25rem',
      },
    },
  },
})

let darkTheme = createTheme({
  palette: {
    mode: 'dark',
    primary: {
      main: '#9C27B0', // Roxo (Purple)
    },
    secondary: {
      main: '#556B2F', // Verde Militar (Olive Green)
    },
    background: {
      default: '#303030',
      paper: '#424242',
    },
    text: {
      primary: '#ffffff',
      secondary: '#b0b0b0',
    },
  },
  typography: {
    fontFamily: 'Poppins',
    h1: {
      fontSize: '2rem',
      '@media (min-width:600px)': {
        fontSize: '2.5rem',
      },
      '@media (min-width:960px)': {
        fontSize: '3rem',
      },
      '@media (min-width:1280px)': {
        fontSize: '3.5rem',
      },
    },
    h2: {
      fontSize: '1.75rem',
      '@media (min-width:600px)': {
        fontSize: '2.25rem',
      },
      '@media (min-width:960px)': {
        fontSize: '2.75rem',
      },
      '@media (min-width:1280px)': {
        fontSize: '3.25rem',
      },
    },
    h3: {
      fontSize: '1.5rem',
      '@media (min-width:600px)': {
        fontSize: '2rem',
      },
      '@media (min-width:960px)': {
        fontSize: '2.5rem',
      },
      '@media (min-width:1280px)': {
        fontSize: '3rem',
      },
    },
    h4: {
      fontSize: '1.25rem',
      '@media (min-width:600px)': {
        fontSize: '1.75rem',
      },
      '@media (min-width:960px)': {
        fontSize: '2.25rem',
      },
      '@media (min-width:1280px)': {
        fontSize: '2.75rem',
      },
    },
    h5: {
      fontSize: '1rem',
      '@media (min-width:600px)': {
        fontSize: '1.5rem',
      },
      '@media (min-width:960px)': {
        fontSize: '2rem',
      },
      '@media (min-width:1280px)': {
        fontSize: '2.5rem',
      },
    },
    h6: {
      fontSize: '0.875rem',
      '@media (min-width:600px)': {
        fontSize: '1.25rem',
      },
      '@media (min-width:960px)': {
        fontSize: '1.75rem',
      },
      '@media (min-width:1280px)': {
        fontSize: '2.25rem',
      },
    },
  },
})

lightTheme = responsiveFontSizes(lightTheme)
darkTheme = responsiveFontSizes(darkTheme)

export { lightTheme, darkTheme }
