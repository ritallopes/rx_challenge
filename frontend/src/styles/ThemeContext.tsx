import { createContext, useState, useContext, ReactNode, useEffect } from 'react';
import { ThemeProvider as ThemeProviderMUI, CssBaseline } from '@mui/material';
import { darkTheme, lightTheme } from './theme';

interface IThemeData {
  lightMode: boolean;
  toggleTheme: () => void;
}

export const ThemeContext = createContext<IThemeData>({
  lightMode: true,
  toggleTheme: () => {},
});

export const useTheme = () => useContext(ThemeContext);

const ThemeProvider = ({ children }: { children: ReactNode }) => {
  const [lightMode, setLightMode] = useState(false);


  useEffect(() => {
    console.log(lightMode)
  },[])
  const toggleTheme = () => {
    console.log(lightMode)
    setLightMode((prevState) => !prevState);
  };

  return (
    <ThemeContext.Provider value={{ lightMode, toggleTheme }}>
      <ThemeProviderMUI theme={lightMode ? lightTheme : darkTheme}>
        <CssBaseline />
        {children}
      </ThemeProviderMUI>
    </ThemeContext.Provider>
  );
};

export default ThemeProvider;