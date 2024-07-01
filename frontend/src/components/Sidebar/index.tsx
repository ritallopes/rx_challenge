import React, { useContext, useState } from 'react'
import {
  Toolbar,
  IconButton,
  Divider,
  List,
  ListItemButton,
  ListItemIcon,
  ListItemText,
} from '@mui/material'
import { ChevronLeft, Dashboard } from '@mui/icons-material'
import Brightness4Icon from '@mui/icons-material/Brightness4'
import Brightness7Icon from '@mui/icons-material/Brightness7'
import { ThemeContext } from '../../styles/ThemeContext'
import Drawer from './Drawer'

const Sidebar = () => {
  const [open, setOpen] = useState(true)
  const toggleDrawer = () => setOpen(!open)

  const { lightMode, toggleTheme } = useContext(ThemeContext)!

  return (
    <Drawer open={open} variant="permanent" onClose={toggleDrawer}>
      <Toolbar
        sx={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'flex-end',
          px: [1],
        }}
      >
        <IconButton onClick={toggleDrawer}>
          <ChevronLeft />
        </IconButton>
      </Toolbar>
      <Divider />
      <List component="nav">
        <ListItemButton>
          <ListItemIcon>
            <Dashboard />
          </ListItemIcon>
          <ListItemText primary="Dashboard" />
        </ListItemButton>
        <Divider sx={{ my: 1 }} />
        <ListItemButton onClick={toggleTheme}>
          <ListItemIcon>
            {lightMode ? <Brightness4Icon /> : <Brightness7Icon />}
          </ListItemIcon>
          <ListItemText primary={lightMode ? 'Dark Mode' : 'Light Mode'} />
        </ListItemButton>
      </List>
    </Drawer>
  )
}

export default Sidebar
