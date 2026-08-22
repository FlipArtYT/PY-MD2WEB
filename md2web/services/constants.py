import re
from pathlib import Path

THEME_TEMPLATE_DIR = Path( "themes" )

# Custom MD Syntax Regexes
CUSTOM_MD_NAVBAR_REGEX = r":::([\s\S]*?):::"
CUSTOM_MD_STYLING_PROPERTY_REGEX = r"\{\{(?P<property>[\s\S]*?)\}(?P<content>[\s\S]*?)\}"
MD_LINK_REGEX = r"\[(.+)\]\((.+)\)"

# Extended MD Syntax Regexes
EXT_MD_STRIKETHROUGH = (r"~~([\s\S]*?)~~", ("<s>", "</s>"))
EXT_MD_MARKER = (r"==([\s\S]*?)==", ("<span>", "</span>"))
EXT_MD_SUBSCRIPT = (r"~([\s\S]*?)~", ("<sub>", "</sub>"))
EXT_MD_SUPERSCRIPT = (r"\^([\s\S]*?)\^", ("<sup>", "</sup>"))
EXT_MD_CODE_CITATION = (r"```([\s\S]*?)```", ("<pre><code>", "</code></pre>"))
EXT_MD_MARKERS = (
    EXT_MD_STRIKETHROUGH, 
    EXT_MD_MARKER, 
    EXT_MD_SUBSCRIPT, 
    EXT_MD_SUPERSCRIPT, 
    EXT_MD_CODE_CITATION
)