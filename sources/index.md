title: Documentation's homepage

# Principles

The project reads Markdown files and outputs HTML files.
Configuring the input and output folders, the website's title, the base url, and so on is really easy:

```python
import builder

global_setup = builder.Global(
  title = "Your website title",
  base_url = "https://website.url", # You can also specify "file://path/to/local/output" to test CSS files locally
  links_in_header = [
    ("Homepage", "index.html"),
    ("Some other page", "folder/other.html")
  ],
  footer = builder.Footer(
    description = "A short description that appears in the footer.",
    links = [
      builder.Link("Category", "https://link/to/thing", "Text displayed")
    ]
  )
)
builder.build_site("input_folder/", "output_folder/", global_setup)
```

For now, the project offers a single template, called `default`.
See the [internal details](internal.md) page to add a new template.[^1]

[^1]: Observe that this framework supports building multiple pages.

## Link category in footer and icons

In the footer, one can provide links to be shown (see the above code example).
Each link has an associated (case-insensitive) category that is used to produce an icon that is prepended to the text to display.
By default, no icon is produced, no matter the category.
You an associate an icon to a category in two ways:

  - If the icon is present in the [iconoir library](https://iconoir.com/), call `builder.templates.category_to_icon.add_iconoir("Category", "iconoir-name")`.
    For instance, to obtain the GitHub icon as on this website

```python
builder.templates.category_to_icon.add_iconoir("github", "iconoir-github")
```

  - If the icon is not present in the library, call `builder.templates.category_to_icon.add_icon("category", lambda: "HTML tags producing the icon")`.
    For instance, the ORCID icon can be obtained via

```python
builder.templates.category_to_icon.add_icon("orcid", lambda: '<img class="contact-icon orcid" src="https://info.orcid.org/wp-content/uploads/2018/11/orcid_16x16.png" alt=""/>',)
```

# Enabled extensions

The following extensions provided by `Python-Markdown` are enabled.
See [their documentation](https://python-markdown.github.io/extensions/) for more information.

  - Extra
  - CodeHilite
  - Table of Contents
  - Meta-Data
  - Admonition
  - Sane Lists
  - WikiLinks
  - SmartyPants

Additional extensions are provided:

  - [Markdown katex](https://github.com/mbarkhau/markdown-katex)
  - [Replace `.md` by `.html` in links](https://github.com/ricmua/markdown-md2html_links)
  - [Caption for figures, tables, and Listings](https://github.com/flywire/caption)
  - [All images can be clicked to open the image in big](https://github.com/DocSkellington/WebsiteBuilder/builder/extensions.py) (implemented specifically for the current project).