import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header.header import header
from link_bio.views.Links.links import links


class State(rx.State): 
    pass

def index () -> rx.Component:
    return rx.box(
            navbar(),
            rx.center(
                rx.vstack(
                    header(),
                    links(),
                    align='center',
                    max_width="600px",
                    width="100%",
                    margin_y="20px"
                )
            ),
            footer()
    ) 
    

app = rx.App()
app.add_page(index)
