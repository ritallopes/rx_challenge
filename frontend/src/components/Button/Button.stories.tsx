// src/components/Button.stories.tsx
import React from 'react'
import { StoryFn, Meta } from '@storybook/react'
import Button from '.'
interface ButtonProps {
  children: React.ReactNode
  disabled?: boolean
  color?:
    | 'inherit'
    | 'primary'
    | 'secondary'
    | 'success'
    | 'error'
    | 'info'
    | 'warning'
}

export default {
  title: 'Componentes/Button',
  component: Button,
} as Meta

const Template: StoryFn<ButtonProps> = (args) => <Button {...args} />

export const Primary = Template.bind({})
Primary.args = {
  children: 'Primary Button',
  color: 'primary',
}

export const Disabled = Template.bind({})
Disabled.args = {
  children: 'Disabled Button',
  disabled: true,
}
