import { Container} from '@mui/material'
import Sidebar from '../../components/Sidebar'
import Average from './sections/Average'
import Dashboard from './sections/Dashboard'
import { Copyright } from '@mui/icons-material'

const Home = () => {
  return (
    <div className="flex h-screen overflow-none">
      <nav className="w-60 shadow-lg">
        <Sidebar />
      </nav>
      <Container className="flex-grow p-4 overflow-y-auto">
        <Average />
        <Dashboard />
        <Copyright sx={{ pt: 4 }} />
      </Container>
    </div>
  )
}

export default Home
