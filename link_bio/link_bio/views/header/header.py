import reflex as rx


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(fallback="CS", size="5", radius="full", text_align="center"),
            rx.vstack(
                rx.text("Cristian Serrat", size="6"),
                rx.text("@CristianSerrat", size="2"),
                spacing="1"
            ),
        ),
        rx.text(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec elit justo, tempus vel pellentesque quis, ullamcorper quis nunc. "
            "Nam nec est a diam auctor blandit. Vivamus posuere leo sit amet bibendum lacinia."
        )
    )
