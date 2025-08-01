import reflex as rx
import link_bio.styles.styles as styles

def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        size="3",
        style=styles.title_style
    )
