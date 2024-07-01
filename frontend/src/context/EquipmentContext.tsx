import {
  createContext,
  useState,
  ReactNode,
  useContext,
  useEffect,
} from 'react'
import { useQuery } from '@tanstack/react-query'
import { IEquipment, IEquipmentData, IStatistics } from '../models/equipament'
import {
  fetchAllEquipment,
  fetchAverage,
  fetchEquipmentData,
} from '../services/equipment'
import { formatDateWithOffset, timeHandler } from '../utils/date'

interface EquipmentContextProps {
  equipmentId: string
  startTime: string
  endTime: string
  setEquipmentId: (id: string) => void
  setStartTime: (time: string) => void
  setEndTime: (time: string) => void
  statisticsData: IStatistics | null
  errorStat?: Error
  isLoadingStat: boolean
  equipamentList: IEquipment[] | []
  equipmentDataList: IEquipmentData[] | []
  isLoadingEquipList: boolean
  fetchStatistics: () => void
}

const EquipmentContext = createContext<EquipmentContextProps>({
  equipmentId: '',
  startTime: 'oneDay',
  endTime: formatDateWithOffset(new Date()),
  setEquipmentId: () => {},
  setStartTime: () => {},
  setEndTime: () => {},
  statisticsData: null,
  errorStat: undefined,
  isLoadingStat: false,
  equipamentList: [],
  isLoadingEquipList: false,
  fetchStatistics: () => {},
  equipmentDataList: [],
})

export const EquipmentProvider = ({ children }: { children: ReactNode }) => {
  const [equipmentId, setEquipmentId] = useState<string>('EQ-001')
  const [startTime, setStartTime] = useState<string>('oneDay')
  const [endTime, setEndTime] = useState<string>(
    formatDateWithOffset(new Date()),
  )
  const {
    isLoading: isLoadingStat,
    error: errorStat,
    data: statisticsData,
    refetch,
  } = useQuery({
    initialData: null,
    queryKey: ['statistics', equipmentId],
    queryFn: async () =>
      fetchAverage(equipmentId, timeHandler[startTime || 'oneDay'](), endTime),
    enabled: !!equipmentId,
    refetchOnWindowFocus: true,
  })

  const { data: equipmentDataList, refetch: refetchList } = useQuery({
    initialData: [],
    queryKey: ['equipment_data', equipmentId],
    queryFn: async () =>
      fetchEquipmentData(
        equipmentId,
        '2024-06-16T13:32:28.328Z',
        '2024-06-30T13:32:28.328Z',
      ),
    enabled: !!equipmentId,
    refetchOnWindowFocus: true,
  })

  const { isLoading: isLoadingEquipList, data: equipamentList } = useQuery({
    initialData: [],
    queryKey: ['equipments'],
    queryFn: async () => fetchAllEquipment(),
    enabled: !!equipmentId,
    refetchOnWindowFocus: true,
  })

  const fetchStatistics = () => {
    refetch()
    refetchList()
  }
  useEffect(() => {
    console.log(equipmentDataList)
    console.log(statisticsData)
  }, [])

  return (
    <EquipmentContext.Provider
      value={{
        equipmentId,
        startTime,
        endTime,
        setEquipmentId,
        setStartTime,
        setEndTime,
        isLoadingStat,
        errorStat: errorStat === null ? undefined : errorStat,
        statisticsData: statisticsData,
        fetchStatistics,
        equipamentList: equipamentList,
        isLoadingEquipList,
        equipmentDataList: equipmentDataList,
      }}
    >
      {children}
    </EquipmentContext.Provider>
  )
}

export const useEquipment = () => {
  const context = useContext(EquipmentContext)
  if (context === undefined) {
    throw new Error('useEquipment must be used within a EquipmentProvider')
  }
  return context
}
