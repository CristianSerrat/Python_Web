import reflex as rx
import datetime
from link_bio.styles.styles import Size as Size

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="favicon.ico", margin_bottom=Size.MEDIUM
        ),
        rx.link("Link de Cristian Serrat", href="http://www.code.org", is_external="true", font_size=Size.MEDIUM),
        rx.text(f"{datetime.date.today().year} Cristian Serrat Copyright", font_size=Size.MEDIUM),
        rx.text(
            "BUILDING SOFTWARE WITH 🤍", font_size=Size.MEDIUM
        ),
        align="center",
        margin_bottom=Size.BIG.value,
        spacing="1"

    )
