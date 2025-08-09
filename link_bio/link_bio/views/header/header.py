import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TextColor

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(fallback="CS", size="6", radius="full", text_align="center"),
            rx.vstack(
                rx.heading(
                    "Cristian Serrat", 
                    size="5",
                    color = TextColor.HEADER.value
                    ),
                rx.text("@CristianSerrat", 
                        size="2", 
                        margin_top=Size.ZERO.value,
                        color = TextColor.BODY.value),
                rx.hstack(
                    link_icon("www.iconos.org"),
                    link_icon("www.iconos.org"),
                    link_icon("www.iconos.org"),
                    link_icon("www.iconos.org"),
                    style={"padding_top": "0.5em"},
                ),
                spacing="0",
                align_items="start",
            ),
        spacing = "3"
        ),
        rx.flex(
            info_text("+13", "años de experiencia"),
            rx.spacer(),
            info_text("+7", "años en Colegios ISP"),
            rx.spacer(),
            info_text("", "Aplicaciones web"),
            width="100%"
        ),
        rx.text(
            """Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
            Donec elit justo, tempus vel pellentesque quis, ullamcorper quis nunc.
            Nam nec est a diam auctor blandit. Vivamus posuere leo sit amet bibendum lacinia.""",
            color=TextColor.BODY.value
        ),
        align_items="start",
        spacing="5",
    )
