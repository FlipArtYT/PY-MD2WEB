import os
from pathlib import Path
from services.constants import THEME_TEMPLATE_DIR
from jinja2 import Environment, FileSystemLoader

env = Environment(loader = FileSystemLoader('themes'))

class TemplateHandler:
    def list_theme_templates(self):
        print("Available themes:\n")

        for (root, dirs, file) in os.walk(THEME_TEMPLATE_DIR):
            for theme in dirs:
                if (THEME_TEMPLATE_DIR / theme / "template.html") and (THEME_TEMPLATE_DIR / theme / "style.html"):
                    print(f"-   {theme}")

    def theme_exists(self, theme_name: Path):
        for (root, dirs, file) in os.walk(THEME_TEMPLATE_DIR):
                for theme in dirs:
                    if (THEME_TEMPLATE_DIR / theme / "template.html") and (THEME_TEMPLATE_DIR / theme / "style.html") and theme == theme_name:
                        return True

        return False

    def add_boilerplate_and_theme(self, html_input: str, theme: str) -> str:
        if not self.theme_exists(theme):
            print("Invalid theme")
            return html_input

        template = env.get_template(f"{theme}/template.html")
        output = template.render(body = html_input)

        return output