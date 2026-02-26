import reflex as rx

from dotenv import load_dotenv
from os import getenv

load_dotenv()

config = rx.Config(
    app_name="osiconl",
    api_url=getenv("API_URL", "http://www.osico.nl"),
    tailwind={},
    frontend_port=3000,
    backend_port=8000,
    show_built_with_reflex=False,
    cors_allowed_origins=["https://osico.nl", "https://www.osico.nl", "http://localhost:3000"],
)
