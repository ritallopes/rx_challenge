import {
  Typography,
  Link,
  Grid,
  FormControl,
  InputLabel,
  MenuItem,
  Select,
  SelectChangeEvent,
  Container,
  CircularProgress,
  Paper,
} from '@mui/material'
import Title from '../../../../components/Title'
import { AdsClickOutlined } from '@mui/icons-material'
import { useState } from 'react'
import { useEquipment } from '../../../../context/EquipmentContext'
import { IEquipment } from '../../../../models/equipament'
import { timeHandler } from '../../../../utils/date'

type IOptionValue = 'oneDay' | 'twoDays' | 'oneWeek' | 'oneMonth'

const OPTIONS: Array<{ label: string; value: IOptionValue }> = [
  { label: '24 horas', value: 'oneDay' },
  { label: '48 horas', value: 'twoDays' },
  { label: '1 semana', value: 'oneWeek' },
  { label: '1 mês', value: 'oneMonth' },
]

const Average = () => {
  const {
    equipmentId,
    setEquipmentId,
    setStartTime,
    statisticsData,
    isLoadingStat,
    errorStat,
    fetchStatistics,
    equipamentList,
    startTime,
    endTime,
  } = useEquipment()
  const [selectedTime, setSelectedTime] = useState<IOptionValue>('oneDay')

  if (isLoadingStat) {
    return <p>Loading...</p>
  }

  if (errorStat) {
    return <p>Um erro ocorreu: {errorStat.message}</p>
  }

  const handleChange = (event: SelectChangeEvent<any>) => {
    const value = event.target.value
    if (value === selectedTime) return
    setStartTime(event.target.value)
    setSelectedTime(event.target.value)
    fetchStatistics()
  }
  const handleChangeEquipment = (event: SelectChangeEvent<any>) => {
    const value = event.target.value
    if (value === equipmentId) return
    setEquipmentId(event.target.value)
    fetchStatistics()
  }

  const getInterval = (): string => {
    try {
      const startDate = new Date(timeHandler[startTime]())
      const endDate = new Date()

      const options: Intl.DateTimeFormatOptions = {
        day: '2-digit',
        month: 'long',
        year: 'numeric',
      }

      const startFormatted = startDate.toLocaleDateString('pt-BR', options)
      const endFormatted = endDate.toLocaleDateString('pt-BR', options)
      return `${startFormatted} até ${endFormatted}`
    } catch (error) {
      return ''
    }
  }

  const formatAverage = (value: number | undefined): string => {
    if (value === undefined || isNaN(value)) {
      return '--'
    }
    return value.toFixed(2)
  }

  return (
    <Paper sx={{ p: 2, display: 'flex', flexDirection: 'column' }}>
      <Grid container spacing={2}>
        <Grid item xs={4}>
          <Title>
            <AdsClickOutlined />
            Medidas recentes{` `}
            {(isLoadingStat || !Array.isArray(equipamentList)) && (
              <CircularProgress color="secondary" />
            )}
          </Title>
        </Grid>
        <Grid item xs={4}>
          {Array.isArray(equipamentList) && (
            <FormControl fullWidth>
              <InputLabel id="select-measurements">Média do sensor</InputLabel>
              <Select
                labelId="select-measurements"
                id="select-measurements"
                value={equipmentId}
                label="Equipamento"
                onChange={handleChangeEquipment}
              >
                {equipamentList.map((option: IEquipment) => (
                  <MenuItem
                    value={option.equipment_id}
                    key={`option-${option.equipment_id}`}
                  >
                    {option.equipment_id}: {option.name}
                  </MenuItem>
                ))}
              </Select>
            </FormControl>
          )}
        </Grid>
        <Grid item xs={4}>
          <FormControl fullWidth>
            <InputLabel id="select-measurements">Média do sensor</InputLabel>
            <Select
              labelId="select-measurements"
              id="select-measurements"
              value={selectedTime}
              label="Média do sensor"
              onChange={handleChange}
              disabled={isLoadingStat}
            >
              {OPTIONS.map((option) => (
                <MenuItem value={option.value} key={`option-${option.value}`}>
                  {option.label}
                </MenuItem>
              ))}
            </Select>
          </FormControl>
        </Grid>
        <Grid item xs={12}>
          <Grid item xs={12}>
            <Typography component="p" variant="h4">
              {formatAverage(statisticsData?.average_value)}
            </Typography>
          </Grid>
        </Grid>
        <Grid item md={6} sm={12}>
          <Typography color="text.secondary" sx={{ flex: 1 }}>
            {getInterval()}
          </Typography>
        </Grid>
      </Grid>
    </Paper>
  )
}

export default Average
