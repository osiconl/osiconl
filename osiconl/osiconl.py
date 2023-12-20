from rxconfig import config

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

    pass


def index() -> rx.Component:
    return rx.fragment(
        rx.box(
            rx.color_mode_button(rx.color_mode_icon(), float="right", color="dark"),
            rx.box(
                spacing="1.5em",
                font_size="2em",
                padding_top="100%",
                ),
            background_image="Gerard-Koster-Koolzaad-2012-93kb.jpg",
            background_position="center",
            background_size="cover",
            background_repeat="no-repeat",
            ),
        rx.box(
            rx.heading("OSICO"),
            rx.text("Nanne Osinga"),
            class_name="sticky bottom-0", padding="1em"),
        rx.box(
            rx.text("ZOVER HET OOG REIKT", font_weight="bold"),
            rx.html("<br/>"),
            rx.text("Landschapsschilder Gerard Koster"),
            rx.html("<br/>"),
            rx.text("Eens, 2012, zei hij", class_name="whitespace-pre-line"),
            rx.html("<br/>"),
            rx.text("“Hoe leger het landschap, hoe meer ik zie, hoe meer ik beleef”"),
            rx.html("<br/>"),
            rx.text("Vertaald naar onze wereld"),
            rx.html("<br/>"),
            rx.text("“Met clean software, zie je meer, kom je verder, beleef je meer”"),
            rx.html("<br/>"),
            rx.text("Hieronder vind je meer info"),
            padding="1em"
            ),
        rx.divider(
            orientation="horizontal", border_color="black"
        ),
        rx.box(
            rx.text("Footer"),
            padding="1em",
            bg="rgba(247, 247, 250, 0.6);",
            ),
        padding="1.5em",
        bg="rgba(247, 247, 250, 0.6);",
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
