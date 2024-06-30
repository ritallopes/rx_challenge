import { Typography, Link, Grid } from '@mui/material'
import Title from '../../../../components/Title'
import { AdsClickOutlined } from '@mui/icons-material'

const Average = () => {
  return (
    <Grid container spacing={2}>
      <Grid item xs={12}>
        <Title>
          <AdsClickOutlined />
          Medidas recentes
        </Title>
      </Grid>
      <Grid item xs={12}>
        <Typography component="p" variant="h4">
          123,45
        </Typography>
      </Grid>
      <Grid item md={6} sm={12}>
        <Typography color="text.secondary" sx={{ flex: 1 }}>
          18 de Junho de 2014 a 30 de Junho de 2024
        </Typography>
      </Grid>
      <Grid item md={6} sm={12}>
        <Link color="primary" href="/list/equipaments">
          Visualizar lista de equipamentos
        </Link>
      </Grid>
    </Grid>
  )
}

export default Average
