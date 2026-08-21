import os
import argparse
from services.template import TemplateHandler
from services.converter import FullMDtoHTMLFileConverter
from services.md_extensions import NavigationConverterExtension, TextStylingConverterExtension
from pathlib import Path

def handle_args(args: argparse.Namespace):
    
    if args.list_themes == True:
        template_handler = TemplateHandler()
        template_handler.list_theme_templates()

    if args.input_path is not None:
        input_path = Path(args.input_path)
        output_path = Path(args.output_path) if args.output_path is not None else Path.cwd() / Path(input_path.stem + ".html")
        theme_name = args.theme_name
        md_file_converter = FullMDtoHTMLFileConverter([NavigationConverterExtension(), TextStylingConverterExtension()])

        if input_path.exists():

            if input_path.is_file():
                md_file_converter.convert_single_md_file_to_html(input_path, output_path, theme_name)

            else:
                md_file_converter.convert_multiple_md_files_to_html(input_path, output_path, theme_name)

        else:

            print("Input path does not exist.")