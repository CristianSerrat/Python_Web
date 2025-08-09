import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size


def link_button(title: str, body:str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="message-circle-heart",
                    align_items="middle",
                    style=styles.icon_centered,
                    width=Size.BIG.value,
                    margin=Size.MEDIUM.value  
                    ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    spacing="0",
                    margin=Size.ZERO.value
                ),
                align="center", # Centra verticalmente icono y bloque de texto
                spacing="1"
            ),
            cursor="pointer",
            width="100%"
        ),
        href=url,
        is_external="true",
        width="100%",
    )