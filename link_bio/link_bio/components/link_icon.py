import reflex as rx
import link_bio.styles.styles as styles


def link_icon(url: str) -> rx.Component:
    return rx.link(
        rx.icon(
            tag="link",
            size=20
        ),
        href=url,
        is_external="true"
    )
