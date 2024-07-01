import { Notifications } from '@mui/icons-material'
import { Toolbar, IconButton, Typography, Badge } from '@mui/material'
import MuiAppBar, { AppBarProps as MuiAppBarProps } from '@mui/material/AppBar'
import { styled } from '@mui/material/styles'

interface AppBarProps extends MuiAppBarProps {
  open?: boolean
}

export const DRAWER_WIDTH: number = 240

const AppBarStyled = styled(MuiAppBar, {
  shouldForwardProp: (prop) => prop !== 'open',
})<AppBarProps>(({ theme, open }) => ({
  zIndex: theme.zIndex.drawer + 1,
  transition: theme.transitions.create(['width', 'margin'], {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.leavingScreen,
  }),
  ...(open && {
    marginLeft: DRAWER_WIDTH,
    width: `calc(100% - ${DRAWER_WIDTH}px)`,
    transition: theme.transitions.create(['width', 'margin'], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen,
    }),
  }),
}))

const CustomAppBar = ({
  open,
  toggleDrawer,
}: {
  open: boolean
  toggleDrawer: () => void
}) => {
  return (
    <AppBarStyled position="absolute" open={open}>
      <Toolbar
        sx={{
          pr: '24px',
        }}
      >
        <IconButton
          edge="start"
          aria-label="open drawer"
          onClick={toggleDrawer}
          sx={{
            marginRight: '36px',
            ...(open && { display: 'none' }),
          }}
        >
          {/* Adicione o ícone aqui se necessário */}
        </IconButton>
        <Typography component="h1" variant="h6" noWrap sx={{ flexGrow: 1 }}>
          Dashboard
        </Typography>
        <IconButton color="inherit">
          <Badge badgeContent={4} color="secondary">
            <Notifications />
          </Badge>
        </IconButton>
      </Toolbar>
    </AppBarStyled>
  )
}

export default CustomAppBar
