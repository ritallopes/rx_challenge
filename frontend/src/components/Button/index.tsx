import MuiButton, { ButtonProps as MuiButtonProps } from '@mui/material/Button'

interface ButtonProps extends MuiButtonProps {}

const Button = (props: ButtonProps) => {
  return <MuiButton {...props} />
}

export default Button
