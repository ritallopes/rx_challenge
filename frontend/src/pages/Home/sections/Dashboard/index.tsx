import Box from '@mui/material/Box'
import Toolbar from '@mui/material/Toolbar'
import Typography from '@mui/material/Typography'
import Container from '@mui/material/Container'
import Grid from '@mui/material/Grid'
import Paper from '@mui/material/Paper'
import Link from '@mui/material/Link'

import Chart from '../../../../components/Chart'
import TableData from './components/Table'
import { Computer } from '@mui/icons-material'

function Copyright(props: any) {
  return (
    <Typography
      variant="body2"
      color="text.secondary"
      align="center"
      {...props}
    >
      <Computer className="m-2" />
      <Link color="inherit" href="https://www.linkedin.com/in/ritallopes/">
        Rita Lopes
      </Link>{' '}
      {new Date().getFullYear()}
    </Typography>
  )
}

export default function Dashboard() {
  return (
    <Grid container spacing={3} marginTop={3}>
      <Grid item xs={12}>
        <Paper
          sx={{
            p: 2,
            display: 'flex',
            flexDirection: 'column',
            height: 240,
          }}
        >
          <Chart />
        </Paper>
      </Grid>

      <Grid item xs={12}>
        <Paper sx={{ p: 2, display: 'flex', flexDirection: 'column' }}>
          <TableData />
        </Paper>
      </Grid>
    </Grid>
  )
}
