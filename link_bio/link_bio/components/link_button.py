import reflex as rx
import link_bio.styles.styles as styles

def link_button(title: str, body:str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="message-circle-heart",
                    align_items="middle",
                    style=styles.icon_centered,
                    width=styles.Size.BIG.value                    ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    align_items="start",
                    spacing="1"
                )
            ),
            cursor="pointer", 
        ),
        href=url,
        is_external="true",
        width="100%",
    )
