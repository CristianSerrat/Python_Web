import reflex as rx
from link_bio.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("Twitch", "http://twitch"),
        link_button("Instagram", "http://www.colegiosisp.com"),
        link_button("Youtube", "http://www.youtube.es"),
        link_button("Discord", "http://www.discord.com"),
        align = 'center'
    )
