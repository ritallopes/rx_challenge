import * as React from 'react'
import Table from '@mui/material/Table'
import TableBody from '@mui/material/TableBody'
import TableCell from '@mui/material/TableCell'
import TableHead from '@mui/material/TableHead'
import TableRow from '@mui/material/TableRow'
import { IEquipmentData } from '../../../../../../models/equipament'
import { useEquipment } from '../../../../../../context/EquipmentContext'
import { useState } from 'react'
import Title from '../../../../../../components/Title'
import { TableSortLabel } from '@mui/material'

interface HeadCell {
  id: keyof IEquipmentData
  label: string
  numeric: boolean
}

const headCells: HeadCell[] = [
  { id: 'equipment_id', numeric: false, label: 'Id do equipamento' },
  { id: 'timestamp', numeric: false, label: 'Data' },
  { id: 'value', numeric: true, label: 'Valor' },
]

const descendingComparator = <T,>(a: T, b: T, orderBy: keyof T) => {
  if (b[orderBy] < a[orderBy]) {
    return -1
  }
  if (b[orderBy] > a[orderBy]) {
    return 1
  }
  return 0
}

type Order = 'asc' | 'desc'

const getComparator = <Key extends keyof any>(
  order: Order,
  orderBy: Key,
): ((
  a: { [key in Key]: number | string },
  b: { [key in Key]: number | string },
) => number) => {
  return order === 'desc'
    ? (a, b) => descendingComparator(a, b, orderBy)
    : (a, b) => -descendingComparator(a, b, orderBy)
}

const stableSort = <T,>(array: T[], comparator: (a: T, b: T) => number) => {
  if (!Array.isArray(array)) return []
  const stabilizedThis = array.map((el, index) => [el, index] as [T, number])
  stabilizedThis.sort((a, b) => {
    const order = comparator(a[0], b[0])
    if (order !== 0) return order
    return a[1] - b[1]
  })
  return stabilizedThis.map((el) => el[0])
}

const TableData = () => {
  const { equipmentDataList } = useEquipment() || []
  const [order, setOrder] = useState<Order>('asc')
  const [orderBy, setOrderBy] = useState<keyof IEquipmentData>('equipment_id')


  const handleRequestSort = (property: keyof IEquipmentData) => {
    const isAsc = orderBy === property && order === 'asc'
    setOrder(isAsc ? 'desc' : 'asc')
    setOrderBy(property)
  }

  const createSortHandler =
    (property: keyof IEquipmentData) => (event: React.MouseEvent<unknown>) => {
      console.log(event)
      handleRequestSort(property)
    }

  return (
    <>
      <Title>Dados do equipamento</Title>
      <Table size="small">
        <TableHead>
          <TableRow>
            {headCells.map((headCell) => (
              <TableCell
                key={headCell.id}
                align={headCell.numeric ? 'right' : 'left'}
                sortDirection={orderBy === headCell.id ? order : false}
              >
                <TableSortLabel
                  active={orderBy === headCell.id}
                  direction={orderBy === headCell.id ? order : 'asc'}
                  onClick={createSortHandler(headCell.id)}
                >
                  {headCell.label}
                </TableSortLabel>
              </TableCell>
            ))}
          </TableRow>
        </TableHead>
        <TableBody>
          {(
            stableSort(
              equipmentDataList,
              getComparator(order, orderBy),
            ) as IEquipmentData[]
          ).map((row) => (
            <TableRow key={row.id}>
              <TableCell>{row.equipment_id}</TableCell>
              <TableCell>{row.timestamp}</TableCell>
              <TableCell align="right">{row.value}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </>
  )
}

export default TableData
