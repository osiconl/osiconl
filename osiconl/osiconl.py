from rxconfig import config

import reflex as rx
from osiconl.translations import TRANSLATIONS


class State(rx.State):
    """The app state."""

    lang: str = "en"

    def set_lang(self, lang: str):
        self.lang = lang

    def t(self, key: str) -> str:
        return TRANSLATIONS.get(self.lang, TRANSLATIONS["en"]).get(key, key)


class AlertDialogState(rx.State):
    show: bool = False

    def change(self):
        self.show = not (self.show)


def sticky_top_bar(lang: str) -> rx.Component:
    """Fixed top-right bar with language switcher and dark/light mode toggle."""
    tr = TRANSLATIONS[lang]
    other_lang_url = tr["switch_lang_url"]
    flag_icon = tr["switch_flag"]

    return rx.hstack(
        rx.link(
            rx.box(
                rx.image(
                    src=flag_icon,
                    height="15px",
                    width="15px",
                    border_radius="50%",
                    object_fit="cover",
                ),
                display="flex",
                align_items="center",
                justify_content="center",
                width="32px",
                height="32px",
                border_radius="8px",
                cursor="pointer",
                _hover={"background": "var(--gray-a4)"},
            ),
            href=other_lang_url,
        ),
        rx.color_mode.button(),
        spacing="2",
        align_items="center",
        position="fixed",
        top="1em",
        right="1em",
        z_index="1000",
    )


def page_content(lang: str) -> rx.Component:
    """Shared page layout. The `lang` parameter sets the static translation."""
    tr = TRANSLATIONS[lang]

    return rx.fragment(
        # Sticky top bar (always visible)
        sticky_top_bar(lang),
        # Hero section
        rx.box(
            rx.box(
                flex="1",
                background_image="url('/Gerard-Koster-Koolzaad-2012-98kb.jpg')",
                background_position="center",
                background_size="cover",
                background_repeat="no-repeat",
                width="100%",
            ),
            rx.hstack(
                rx.box(
                    rx.heading("OSICO", size="5"),
                    rx.text("Nanne Osinga"),
                ),
                rx.spacer(),
                rx.link(
                    rx.box(rx.icon(tag="arrow-down")),
                    href="/#contact" if lang == "en" else "/nl#contact",
                ),
                padding="1em",
                width="100%",
            ),
            display="flex",
            flex_direction="column",
            height="100vh",
        ),
        # Quote section
        rx.box(
            rx.text(tr["tagline"], font_weight="bold"),
            rx.html("<br/>"),
            rx.text(tr["painter_intro"]),
            rx.html("<br/>"),
            rx.text(tr["painter_said"]),
            rx.html("<br/>"),
            rx.text(tr["painter_quote"]),
            rx.html("<br/>"),
            rx.text(tr["translated"]),
            rx.html("<br/>"),
            rx.text(tr["software_quote"]),
            rx.html("<br/>"),
            padding="1em",
        ),
        rx.divider(orientation="horizontal", border_color="black"),
        # Contact bar
        rx.vstack(
            rx.hstack(
                rx.link(
                    rx.button(
                        rx.image(src="/linkedin-icon-2.svg", height="1.75em"),
                        variant="ghost",
                    ),
                    href="https://www.linkedin.com/in/nanneosinga/",
                    is_external=True,
                ),
                rx.link(
                    rx.button(
                        rx.image(src="/whatsapp.png", height="1.75em"),
                        variant="ghost",
                    ),
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
                        rx.alert_dialog.title(tr["call"]),
                        rx.alert_dialog.description("+31 (0) 6 5336 2179"),
                        rx.flex(
                            rx.alert_dialog.cancel(
                                rx.button(
                                    tr["close"],
                                    on_click=AlertDialogState.change,
                                ),
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
                rx.link(
                    rx.button(rx.icon(tag="notebook-pen"), variant="ghost"),
                    href="https://blog.osico.nl",
                    is_external=True,
                ),
                width="100%",
            ),
            padding="1em",
            bg="rgba(247, 247, 250, 0.6)",
            id="contact",
        ),
    )


def index() -> rx.Component:
    """English homepage (default)."""
    return page_content("en")


def index_nl() -> rx.Component:
    """Dutch homepage."""
    return page_content("nl")


# Add state and pages to the app.
app = rx.App()
app.add_page(index, route="/", title="Osico")
app.add_page(index_nl, route="/nl", title="Osico")
