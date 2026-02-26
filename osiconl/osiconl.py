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
        # Hero section: image + OSICO bar, always exactly one screen tall
        rx.box(
            # Background image fills the space above the bar
            rx.box(
                rx.color_mode.button(position="top-right"),
                flex="1",
                background_image="url('Gerard-Koster-Koolzaad-2012-98kb.jpg')",
                background_position="center",
                background_size="cover",
                background_repeat="no-repeat",
                width="100%",
            ),
            # OSICO bar at the bottom of the viewport
            rx.hstack(
                rx.box(
                    rx.heading("OSICO", size="5"),
                    rx.text("Nanne Osinga"),
                ),
                rx.spacer(),
                rx.link(
                    rx.box(rx.icon(tag="arrow-down")),
                    href="/#contact",
                ),
                padding="1em",
                width="100%",
            ),
            display="flex",
            flex_direction="column",
            height="100vh",
        ),
        # Text content
        rx.box(
            rx.text("ZOVER HET OOG REIKT ...", font_weight="bold"),
            rx.html("<br/>"),
            rx.text("Landschapsschilder Gerard Koster"),
            rx.html("<br/>"),
            rx.text("Eens, 2012, zei hij"),
            rx.html("<br/>"),
            rx.text("\u201cHoe leger het landschap, hoe meer ik zie, hoe meer ik beleef\u201d"),
            rx.html("<br/>"),
            rx.text("Vertaald naar onze wereld"),
            rx.html("<br/>"),
            rx.text("\u201cMet clean software, zie je meer, kom je verder, beleef je meer\u201d"),
            rx.html("<br/>"),
            padding="1em",
        ),
        rx.divider(orientation="horizontal", border_color="black"),
        # Contact bar
        rx.vstack(
            rx.hstack(
                rx.link(
                    rx.button(rx.image(src="linkedin-icon-2.svg", height="1.75em"), variant="ghost"),
                    href="https://www.linkedin.com/in/nanneosinga/",
                    is_external=True,
                ),
                rx.link(
                    rx.button(rx.image(src="whatsapp.png", height="1.75em"), variant="ghost"),
                    href="https://wa.me/31653362179",
                    is_external=True,
                ),
                rx.button(
                    rx.icon(tag="phone"),
                    variant="ghost",
                    on_click=AlertDialogState.change,
                ),
                rx.alert_dialog.root(
                    rx.alert_dialog.content(
                        rx.alert_dialog.title("Bellen"),
                        rx.alert_dialog.description("+31 (0) 6 5336 2179"),
                        rx.flex(
                            rx.alert_dialog.cancel(
                                rx.button("Sluiten", on_click=AlertDialogState.change),
                            ),
                            justify="end",
                        ),
                    ),
                    open=AlertDialogState.show,
                ),
                rx.link(
                    rx.button(rx.icon(tag="mail"), variant="ghost"),
                    href="mailto:nanne@osico.nl",
                ),
                rx.spacer(),
                rx.color_mode.button(position="top-right"),
                width="100%",
            ),
            padding="1em",
            bg="rgba(247, 247, 250, 0.6)",
            id="contact",
        ),
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index, title="Osico")
