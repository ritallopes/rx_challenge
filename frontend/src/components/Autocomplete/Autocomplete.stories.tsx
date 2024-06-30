import { Meta, StoryObj } from '@storybook/react'
import Autocomplete, { IAutocomplete } from '.'

const AutocompleteComponent: Meta<typeof Autocomplete> = {
  component: Autocomplete,
  title: 'Components/Autocomplete',
  argTypes: {},
}
export default AutocompleteComponent

type Story = StoryObj<IAutocomplete>

const options = ['Primeira opção', 'Segunda opção', 'Terceira opção']

export const CustomAutocomplete: Story = {
  args: {
    options: options,
  },
}
