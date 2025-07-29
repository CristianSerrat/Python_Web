import reflex as rx

def link_button(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(text, cursor="pointer"),
        href=url,
        is_external="true"
    )
