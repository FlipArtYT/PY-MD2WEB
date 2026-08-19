import argparse
from services.cli import handle_args

def main():
    parser = argparse.ArgumentParser(description="Convert Markdown to HTML")
    parser.add_argument("-v", "--version", action="version", version="MD2WEB 1.0")
    parser.add_argument("-i", "--input-path", required=False, help="Path to the input Markdown file")
    parser.add_argument("-o", "--output-path", required=False, help="Path to the output HTML file")
    parser.add_argument("-t", "--theme-name", required=False, help="Name of the theme to use for HTML conversion")
    parser.add_argument("-l", "--list-themes", action="store_true", required=False, help="List available theme templates")
    args = parser.parse_args()

    if not any(vars(args).values()):
        parser.print_help()
        return

    handle_args(args)

if __name__ == "__main__":
    main()