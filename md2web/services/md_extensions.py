import re
from urllib.parse import urlparse
from services.constants import (
    CUSTOM_MD_NAVBAR_REGEX, 
    MD_LINK_REGEX, 
    CUSTOM_MD_STYLING_PROPERTY_REGEX,
    EXT_MD_MARKERS
)

class BaseMDConverterExtension:
    def convert_md_extension_el_to_html(md_input: str):
        return md_input

class NavigationConverterExtension(BaseMDConverterExtension):
    def convert_md_extension_el_to_html(self, md_input: str) -> str:
        match = re.search(CUSTOM_MD_NAVBAR_REGEX, md_input, flags=re.DOTALL)
        
        if not match:
            return md_input
    
        nav_links = self.convert_nav_links(match.group(1))
        result = re.sub(CUSTOM_MD_NAVBAR_REGEX, f"<nav>\n{nav_links}</nav>", md_input, flags=re.DOTALL)
    
        return result

    def convert_nav_links(self, nav_links: str) -> str:
        raw_link_list = nav_links.split(";")
        link_list: list[dict] = []

        for link in raw_link_list:
            match = re.search(MD_LINK_REGEX, link, flags=re.DOTALL)

            if match:
                title = match.group(1)
                url = match.group(2)

                if url.endswith(".md") and not self._url_is_absolute(url=url):
                    url = url.replace(".md", ".html")

                link_list.append({"title": title, "url": url})

        formatted_links = [f"<a href=\"{link["url"]}\">{link["title"]}</a>\n" for link in link_list]

        return "\n".join(formatted_links)

    def _url_is_absolute(self, url: str) -> bool:
        return bool(urlparse(url).netloc)

class TextStylingConverterExtension(BaseMDConverterExtension):
    def convert_md_extension_el_to_html(self, md_input: str) -> str:
        html_output = md_input

        while True:
            match = re.search(CUSTOM_MD_STYLING_PROPERTY_REGEX, html_output)

            if not match:
                break

            match_index = match.span()
            style_properties = match.group("property")
            content = match.group("content")

            converted_html_element = self.convert_property_to_tag(style_properties, content)

            html_output = html_output[:match_index[0]] + converted_html_element + html_output[match_index[1]:]

        return html_output

    def convert_property_to_tag(self, properties: str, content: str) -> str:
        property_list = properties.split(";")
        inline_css_styles = []

        for p in property_list:
            splitted_property = p.split(":")

            if len(splitted_property) > 1:
                rule = splitted_property[0].strip()
                value = splitted_property[1].strip()

                if rule == "fg-color":
                    inline_css_styles.append("color: " + value)

                elif rule == "bg-color":
                    inline_css_styles.append("background-color: " + value)

                elif rule == "border-color":
                    inline_css_styles.append("border: solid 1px " + value)

        if len(inline_css_styles) > 0:
            return f"<span style=\"{"; ".join(inline_css_styles)}\">{content}</span>"

        else:
            return content

class MarkerConverterExtension(BaseMDConverterExtension):
    def convert_md_extension_el_to_html(self, md_input: str) -> str:
        html_output = md_input

        for marker in EXT_MD_MARKERS:
            while True:
                match = re.search(marker[0], html_output)
    
                if not match:
                    break
    
                match_index = match.span()
                content = match.group(1)
                converted_html_element = marker[1][0] + content + marker[1][1]

                print(f"Match at {match_index} from {content} regex: {marker[0]}")

                html_output = html_output[:match_index[0]] + converted_html_element + html_output[match_index[1]:]

        return html_output

# class CodeCitationConverterExtension(BaseMDConverterExtension):
#     def convert_md_extension_el_to_html(self, md_input: str) -> str:
#         matches = re.findall(CUSTOM_MD_CODE_CITATION_REGEX, md_input, flags=re.DOTALL)

#         if not matches:
#             return md_input

#         code_cite_list = [f"<pre><code>{capture[0]}</code></pre>" for capture in matches]
#         result = md_input

#         return ""