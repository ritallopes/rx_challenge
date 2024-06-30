import { QueryClientProvider } from '@tanstack/react-query'
import queryClient from '../../lib/reactQuery'

type ProviderProps = {
  children: React.ReactNode
}

const Provider = ({ children }: ProviderProps) => {
  return (
    <QueryClientProvider client={queryClient}>{children}</QueryClientProvider>
  )
}

export default Provider
