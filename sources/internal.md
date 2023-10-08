title: Internal details

# Templates

Each produced HTML file follows a given template, which can be selected by the `layout` key in the meta-data.
This implementation only provides a single default template (which is selected if the `layout` key is not present).

The default layout adds an `<h1>` tag at the top of the page with the title set in the metadata.
It also creates a header and a footer, using the information from the global setup.

## Adding a new template

The following code registers a new template called `example` that simply returns the HTML body.

```python
import builder.templates

class ExampleTemplate(builder.templates.Template):
  name = "example"

  def build_document(self, body: str, metadata: Dict[str, Any], global_setup: builder.Global, toc: str) -> str:
    # body is the Markdown file already converted to HTML
    # metadata contains the key-value pairs defined at the top of the Markdown file
    # global_setup is the setup provided to the builder
    # toc is the table of contents as HTML tags
    return body
```

The file must be present in the `builder/templates` folder to be seen by the builder.
The `Template` base class offers some utilities to construct the HTML output:

  - `self._head(title: str, global_setup: builder.Global)` that creates the `<head>` part.
      - The page's title is `{title} &ndhash; {global_setup.title}`.
      - CSS and JavaScript files are linked by reading the arrays `self.css_files` (which contains URLs) and `self.script_files` (which contains instances of the `JavaScript` class to hold the source, script_id, and other tags).
      If a provided URL is not absolute, the `global_setup.base_url` is prepended.
  - `self._build_link(link: builder.Link)` which produces a link with an icon before it.
