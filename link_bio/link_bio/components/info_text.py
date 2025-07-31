import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size


def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.text(title, weight="bold", color="blue", as_="span"),
        f" {body}",
        font_size=Size.MEDIUM
    )