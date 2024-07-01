import Grid from '@mui/material/Grid'
import Paper from '@mui/material/Paper'

import TableData from './components/Table'
import Chart from './components/Chart'


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
