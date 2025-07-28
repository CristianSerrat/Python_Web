import reflex as rx

def header() -> rx.Component:
        return rx.vstack(
            rx.avatar(fallback="CS", size="5", radius="full", text_align="center"),
            rx.text("@CristianSerrat"),
            rx.text("Hola, Mi nombre es Cristian Serrat")
        )