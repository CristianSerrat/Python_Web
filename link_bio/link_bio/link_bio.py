import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.views.header.header import header
from link_bio.views.Links.links import links

class State(rx.State): 
    pass

def index () -> rx.Component:
    return rx.vstack(
        navbar(),
        header(),
        links(),
        align='center'
    
    )

app = rx.App()
app.add_page(index)
