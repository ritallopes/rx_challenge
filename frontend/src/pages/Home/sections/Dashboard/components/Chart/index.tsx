import { useTheme } from '@mui/material/styles'
import { LineChart, axisClasses } from '@mui/x-charts'
import { ChartsTextStyle } from '@mui/x-charts/ChartsText'
import { useEquipment } from '../../../../../../context/EquipmentContext'
import { IEquipmentData } from '../../../../../../models/equipament'
import Title from '../../../../../../components/Title'

const Chart = () => {
  const theme = useTheme()
  const { equipmentDataList } = useEquipment() || []

  const formattedData = equipmentDataList.map((item: IEquipmentData) => ({
    time: new Date(item.timestamp).toLocaleTimeString('pt-BR', {
      hour: '2-digit',
      minute: '2-digit',
    }),
    amount: item.value,
  }))

  return (
    <>
      <Title>Data Over Time</Title>
      <div style={{ width: '100%', flexGrow: 1, overflow: 'hidden' }}>
        <LineChart
          dataset={formattedData}
          margin={{
            top: 16,
            right: 20,
            left: 70,
            bottom: 30,
          }}
          xAxis={[
            {
              scaleType: 'point',
              dataKey: 'time',
              tickNumber: 5,
              tickLabelStyle: theme.typography.body2 as ChartsTextStyle,
            },
          ]}
          yAxis={[
            {
              label: 'Valor',
              labelStyle: {
                ...(theme.typography.body1 as ChartsTextStyle),
                fill: theme.palette.text.primary,
              },
              tickLabelStyle: theme.typography.body2 as ChartsTextStyle,
              tickNumber: 4,
            },
          ]}
          series={[
            {
              dataKey: 'amount',
              showMark: true,
              color: theme.palette.primary.main,
            },
          ]}
          sx={{
            [`.${axisClasses.root} line`]: {
              stroke: theme.palette.text.secondary,
            },
            [`.${axisClasses.root} text`]: {
              fill: theme.palette.text.secondary,
            },
            [`& .${axisClasses.left} .${axisClasses.label}`]: {
              transform: 'translateX(-25px)',
            },
          }}
        />
      </div>
    </>
  )
}

export default Chart
