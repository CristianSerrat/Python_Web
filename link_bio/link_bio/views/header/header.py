import reflex as rx

def header() -> rx.Component:
        return rx.vstack(
            rx.avatar(fallback="CS", size="5", radius="full", text_align="center"),
            rx.text("@CristianSerrat"),
            rx.text("Hola, Mi nombre es Cristian Serrat." \
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec elit justo, tempus vel pellentesque quis, ullamcorper quis nunc. " \
            "Nam nec est a diam auctor blandit. Vivamus posuere leo sit amet bibendum lacinia."),
            align="center"
        )