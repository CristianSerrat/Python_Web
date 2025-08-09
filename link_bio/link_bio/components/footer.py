import reflex as rx
import datetime
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TextColor

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="favicon.ico", margin_bottom=Size.MEDIUM
        ),
        rx.link("Link de Cristian Serrat", href="http://www.code.org", is_external="true", font_size=Size.MEDIUM),
        rx.text(f"{datetime.date.today().year} Cristian Serrat Copyright", font_size=Size.MEDIUM),
        rx.text(
            "BUILDING SOFTWARE WITH 🤍", font_size=Size.MEDIUM,
            margin_top= Size.ZERO.value
        ),
        align="center",
        margin_bottom=Size.BIG.value,
        spacing="1",
        color= TextColor.FOOTER.value


    )
