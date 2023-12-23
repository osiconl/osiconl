from rxconfig import config

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""

    pass


class AlertDialogState(rx.State):
    show: bool = False

    def change(self):
        self.show = not (self.show)


def index() -> rx.Component:
    return rx.fragment(
        rx.box(
            rx.color_mode_button(rx.color_mode_icon(), float="right", color="dark",),
            rx.box(
                spacing="1.5em",
                font_size="2em",
                padding_top="100%",
                ),
            background_image="Gerard-Koster-Koolzaad-2012-98kb.jpg",
            background_position="center",
            background_size="cover",
            background_repeat="no-repeat"),
        rx.hstack(
            rx.box(
                rx.heading("OSICO"),
                rx.text("Nanne Osinga"),
                ),
            rx.spacer(),
            rx.link(rx.box(
                rx.icon(
                    tag="arrow_down",
                ),),href="/#contact"),
            class_name="sticky bottom-0", padding="1em", width="100%", ),
        rx.box(
            rx.text("ZOVER HET OOG REIKT ...", font_weight="bold"),
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
            padding="1em"
            ),
        rx.divider(
            orientation="horizontal", border_color="black"
        ),
        rx.vstack(
            rx.hstack(
                rx.link(rx.button(rx.image(src="linkedin-icon-2.svg", height="1.75em")),
                        href="https://www.linkedin.com/in/nanneosinga/",
                        is_external=True),
                rx.link(rx.button(rx.image(src="whatsapp.png", height="1.75em")),
                        href="https://wa.me/31653362179",
                        is_external=True),
                rx.button(
                    rx.icon(tag="phone",),
                    on_click=AlertDialogState.change,
                ),
                rx.alert_dialog(
                    rx.alert_dialog_overlay(
                        rx.alert_dialog_content(
                            rx.alert_dialog_header("Bellen"),
                            rx.alert_dialog_body(
                                "+31 (0) 6 5336 2179"
                            ),
                            rx.alert_dialog_footer(
                                rx.button(
                                    "Sluiten",
                                    on_click=AlertDialogState.change,
                                )
                            ),
                        )
                    ),
                    is_open=AlertDialogState.show,
                ),
                rx.link(rx.button(rx.icon(tag="email",),),
                        href="mailto:nanne@osico.nl"),
                rx.spacer(),
                rx.color_mode_button(rx.color_mode_icon(), float="right", color="dark",)
                ,width="100%",),
                padding="1em",
                bg="rgba(247, 247, 250, 0.6);",
                id="contact",
        ),
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index, title="Osico")
app.compile()
