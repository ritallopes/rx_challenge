const formatDateWithOffset = (date: Date) => {
  const offset = new Date().getTimezoneOffset()
  const dateWithOffset = new Date(date.getTime() - offset * 60 * 60 * 1000)
  return dateWithOffset.toISOString()
}

function oneDayHandler(): string {
  const now = new Date()
  const start = new Date(now.getTime() - 24 * 60 * 60 * 1000)
  return formatDateWithOffset(start)
}

function twoDaysHandler(): string {
  const now = new Date()
  const start = new Date(now.getTime() - 2 * 24 * 60 * 60 * 1000)
  return formatDateWithOffset(start)
}

function oneWeekHandler(): string {
  const now = new Date()
  const start = new Date(now.getTime() - 7 * 24 * 60 * 60 * 1000)
  return formatDateWithOffset(start)
}

function oneMonthHandler(): string {
  const now = new Date()
  const start = new Date(now)
  start.setMonth(now.getMonth() - 1)
  return formatDateWithOffset(start)
}

const timeHandler: { [key: string]: () => string } = {
  oneDay: oneDayHandler,
  twoDays: twoDaysHandler,
  oneWeek: oneWeekHandler,
  oneMonth: oneMonthHandler,
}

export {
  timeHandler,
  oneDayHandler,
  twoDaysHandler,
  oneMonthHandler,
  oneWeekHandler,
  formatDateWithOffset,
}
