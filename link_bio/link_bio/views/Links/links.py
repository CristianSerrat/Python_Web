import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title


def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button("Twitch", "Directos de lunes a viernes", "http://twitch"),
        link_button(
            "Instagram",
            "Stories con la últimas novedades",
            "http://www.colegiosisp.com",
        ),
        link_button(
            "Youtube (Canal Secundario)",
            "Tutoriales semanales",
            "http://www.youtube.es",
        ),
        link_button("Discord", "Quedadas en directo", "http://www.discord.com"),
        title("Comunidad"),
        link_button("Twitch", "Directos de lunes a viernes", "http://twitch"),
        link_button(
            "Instagram",
            "Stories con la últimas novedades",
            "http://www.colegiosisp.com",
        ),
        link_button(
            "Youtube (Canal Secundario)",
            "Tutoriales semanales",
            "http://www.youtube.es",
        ),
        link_button("Discord", "Quedadas en directo", "http://www.discord.com"),
        width="100%",
        align="center",
        spacing="2",
    )
