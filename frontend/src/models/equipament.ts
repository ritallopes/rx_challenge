export interface IStatistics {
  average_value: number
  median_value: number
  sum_value: number
}

export interface IEquipment {
  name: string
  equipment_id: string
}

export interface IEquipmentData {
  equipment_id: string
  id: number
  received_at: string
  timestamp: string
  value: number
}
