from pathlib import Path
from services.md_extensions import BaseMDConverterExtension
from services.template import TemplateHandler
import markdown

class MDtoHTMLConverter:
    def __init__(self, md_extensions: list = []):
        self.md_extension: list[BaseMDConverterExtension] = md_extensions

    def convert_custom_md_to_html(self, md_input: str) -> str:
        current_html = md_input

        # Convert custom Markdown elements
        for extension in self.md_extension:
            current_html = extension.convert_md_extension_el_to_html(current_html)
        
        current_html = markdown.markdown(current_html)

        return current_html


    def convert_md_files_in_dir_to_html(input_path: Path) -> str:
        pass

class FullMDtoHTMLFileConverter:
    def __init__(self, md_extensions: list = []):
        self.converter_engine = MDtoHTMLConverter(md_extensions)

    def convert_single_md_file_to_html(self, input_path: Path, output_path: Path, theme_name: str = None):
        try:
            with open(input_path, "r") as f:
                input_content = f.read()

            html_contents = self.converter_engine.convert_custom_md_to_html(input_content)

            # Apply theme if specified
            if theme_name is not None:
                template_handler = TemplateHandler()
                html_contents = template_handler.add_boilerplate_and_theme(html_input=html_contents, theme=theme_name)

            output_path.parents[0].mkdir(exist_ok=True)

            # Add new file to path if input path points to folder
            if input_path.is_dir():
                output_path = output_path / Path(input_path.stem + ".html")

            with open(output_path, "w") as f:
                f.write(html_contents)

        except Exception as e:
            print(f"Failed to convert markdown file to HTML: {e}")

    def convert_multiple_md_files_to_html(self, input_path: Path, output_path: Path, theme_name: str = None):
        pass
        # try:
        #     if not output_path.is_dir():
        #         raise ValueError("Output path must be a directory, not a file.")

        #     output_path.mkdir(exist_ok=True)

        # except Exception as e:
        #     print(f"Failed to convert markdown files from folder to HTML: {e}")