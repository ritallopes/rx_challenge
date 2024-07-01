import { QueryClientProvider } from '@tanstack/react-query'
import queryClient from '../../lib/reactQuery'
import ThemeProvider from '../../styles/ThemeContext'
import { EquipmentProvider } from '../../context/EquipmentContext'

type ProviderProps = {
  children: React.ReactNode
}

const Provider = ({ children }: ProviderProps) => {
  return (
    <QueryClientProvider client={queryClient}>
      <ThemeProvider>
        <EquipmentProvider>{children}</EquipmentProvider>
      </ThemeProvider>
    </QueryClientProvider>
  )
}

export default Provider
