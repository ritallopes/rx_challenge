import {Toolbar, IconButton, Drawer, Divider, List } from "@mui/material"
import { mainListItems, secondaryListItems } from "../../pages/Home/sections/Dashboard/listItem"
import { useState } from "react"
import { ChevronLeft } from "@mui/icons-material"


const Sidebar = () => {
  const [open, setOpen] = useState(true)
  const toggleDrawer = () => {
    setOpen(!open)
  }
  return (
    <nav>
        <Drawer variant="permanent" open={open}>
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
            {mainListItems}
            <Divider sx={{ my: 1 }} />
            {secondaryListItems}
          </List>
        </Drawer>
    </nav>
  )
}

export default Sidebar