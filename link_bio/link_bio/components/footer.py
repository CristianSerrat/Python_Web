import reflex as rx
import datetime


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="favicon.ico"
        ),
        rx.link("Link de Cristian Serrat", href="http://www.code.org", is_external="true"),
        rx.text(f"{datetime.date.today().year} Cristian Serrat CopyRight"),
        align="center"
    )
