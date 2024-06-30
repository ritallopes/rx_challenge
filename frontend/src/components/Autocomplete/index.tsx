import React, { SyntheticEvent } from 'react'
import {
  Autocomplete,
  AutocompleteChangeDetails,
  AutocompleteChangeReason,
  AutocompleteRenderInputParams,
  Stack,
  TextField,
} from '@mui/material'

export interface IAutocomplete {
  options: string[]
  selectedOption: string | undefined
  onOptionSelect: (
    event: React.ChangeEvent<string>,
    value: string | undefined,
  ) => void
}

const AutocompleteComponent = (props: IAutocomplete) => {
  const { options, selectedOption } = props

  const handleOptionSelect = (
    event: SyntheticEvent<Element, Event>,
    value: string | undefined,
    reason: AutocompleteChangeReason,
    details?: AutocompleteChangeDetails<string>,
  ) => {
    console.log('Selected option:', value)
    console.log(event + ' ' + details) + ' ' + reason
  }
  return (
    <Stack spacing={2} sx={{ width: 300 }}>
      <Autocomplete
        freeSolo
        id="autocomplete"
        disableClearable
        options={options}
        value={selectedOption}
        onChange={handleOptionSelect}
        renderInput={(params: AutocompleteRenderInputParams) => (
          <TextField
            {...params}
            label="Search input"
            InputProps={{
              ...params.InputProps,
              type: 'search',
            }}
          />
        )}
      />
    </Stack>
  )
}

export default AutocompleteComponent
