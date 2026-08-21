import re
from pathlib import Path

THEME_TEMPLATE_DIR = Path( "themes" )

# Custom MD Syntax Regexes
CUSTOM_MD_NAVBAR_REGEX = r":::([\s\S]*?):::"
CUSTOM_MD_CODE_CITATION_REGEX = r"```([\s\S])```"
CUSTOM_MD_STYLING_PROPERTY_REGEX = r"\{\{(?P<property>[\s\S]*?)\}(?P<content>[\s\S]*?)\}"
MD_LINK_REGEX = r"\[(.+)\]\((.+)\)"