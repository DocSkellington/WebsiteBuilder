import abc
import urllib
import importlib
from typing import Dict, Any, List, Callable, Type
from dataclasses import dataclass, field


@dataclass
class JavaScript:
    src: str
    script_id: str = ""
    other: List[str] = field(default_factory=list)


class CategoryToIcon:
    def __init__(self) -> None:
        self.dict: Dict[str, Callable[[], str]] = {}

    def add_iconoir(self, category: str, iconoir: str) -> None:
        self.add_icon(category, lambda: f'<i class="icon {iconoir}"></i>')

    def add_icon(self, category: str, icon_fct: Callable[[], str]) -> None:
        category = category.lower()
        self.dict[category] = icon_fct

    def get_icon(self, category: str) -> str:
        category = category.lower()
        return self.dict.get(category, lambda: "")()


category_to_icon: CategoryToIcon = CategoryToIcon()


class RegisteredTemplates:
    def __init__(self) -> None:
        self.registered: Dict[str, Type[Template]] = {}

    def register(self, name: str, template: type["Template"]) -> None:
        self.registered[name] = template

    def get(self, name: str) -> "Template":
        # Little hack to force the default template to be loaded
        importlib.import_module("builder.templates.load_default")
        if name in self.registered:
            return self.registered[name]()
        print(f"Could not find a template named {name}. Default layout will be used.")
        return self.registered["default"]()


registered_templates: RegisteredTemplates = RegisteredTemplates()


def add_base_url(base_url: str, link: str) -> str:
    try:
        url = urllib.parse.urlparse(link)
        if url.scheme == "":
            if base_url[-1] == "/":
                return base_url + link
            return base_url + "/" + link
        return link
    except ValueError:
        return None


class Template(abc.ABC):
    def __init__(self) -> None:
        self.css_files: List[str] = []
        self.script_files: List[JavaScript] = []

    def _head(self, title: str, global_setup: "builder.Global") -> str:
        head = f"""
<head>
<meta charset="utf-8" />
<title>{title} &ndash; {global_setup.title}</title>
    """
        for css in self.css_files:
            url = add_base_url(global_setup.base_url, css)
            if url is None:
                print(f"Invalid CSS path {css}")
            else:
                head += f'<link rel="stylesheet" href="{url}"/>\n'

        for script in self.script_files:
            url = add_base_url(global_setup.base_url, script.src)
            if url is None:
                print(f"Invalid script path {script}")
            else:
                js_id = f'id="{script.script_id}"' if script.script_id != "" else ""
                other = " ".join(script.other)
                head += f'<script type="text/javascript" {js_id} {other} src="{url}"></script>'

        head += "</head>"
        return head

    def build_document(
        self,
        body: str,
        metadata: Dict[str, Any],
        global_setup: "builder.Global",
        toc: str,
    ) -> str:
        raise NotImplementedError(
            "Each template must implement the method build_document"
        )

    def _build_link(self, link: "builder.Link") -> str:
        a_tag = f'<a class="{link.category.lower()}-link" href="{link.link}">{link.text}</a>'
        return category_to_icon.get_icon(link.category) + a_tag
