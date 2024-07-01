import axios from 'axios'
import { IEquipment, IEquipmentData, IStatistics } from '../models/equipament'
const API_URL = import.meta.env.VITE_API_URL

const fetchAverage = async (
  equipmentId: string,
  startTime: string,
  endTime: string,
): Promise<IStatistics> => {
  console.log(startTime)
  console.log(endTime)
  const response = await axios.get<IStatistics>(
    `${API_URL}equipments_data_statistics/${equipmentId}?start_time=${startTime}&end_time=${endTime}`,
  )
  console.log(response)
  return response.data
}
const fetchEquipmentData = async (
  equipmentId: string,
  startTime: string,
  endTime: string,
): Promise<IEquipmentData[]> => {
  const response = await axios.get<IEquipmentData[]>(
    `${API_URL}equipments_data/${equipmentId}?start_time=${startTime}&end_time=${endTime}`,
  )
  console.log(response)
  return response.data
}

const fetchAllEquipment = async (): Promise<IEquipment[]> => {
  const response = await axios.get<IEquipment[]>(`${API_URL}equipments/`)
  console.log(response)
  return response.data
}

export { fetchAverage, fetchAllEquipment, fetchEquipmentData }
