import re
from urllib.parse import urlparse
from services.constants import CUSTOM_MD_NAVBAR_REGEX, MD_LINK_REGEX, CUSTOM_MD_CODE_CITATION_REGEX

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

# class CodeCitationConverterExtension(BaseMDConverterExtension):
#     def convert_md_extension_el_to_html(self, md_input: str) -> str:
#         matches = re.findall(CUSTOM_MD_CODE_CITATION_REGEX, md_input, flags=re.DOTALL)

#         if not matches:
#             return md_input

#         code_cite_list = [f"<pre><code>{capture[0]}</code></pre>" for capture in matches]
#         result = md_input

#         return ""