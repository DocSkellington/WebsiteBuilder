# Build static HTML pages from Markdown files

This project offers a light template system for [Python-Markdown](https://python-markdown.github.io/).

## Installation

### From release

Due to dependencies coming from GitHub, the wheel file is not enough.
So, download both the `.whl` and `requirements.txt` files of the latest release and run `pip install -r requirements.txt && pip install websitebuilder-1.1.0-py3-none-any.whl`.

### From source

Clone the repository locally and run `pip install -r requirements.txt && pip install .`.
Dependencies will be automatically installed.

## Usage

The documentation can be found at [https://docskellington.github.io/WebsiteBuilder/], generated by the configuration in [`documentation.py`](https://github.com/DocSkellington/WebsiteBuilder/documentation.py).
Moreover, my [personal website](https://github.com/DocSkellington/WebsiteBuilder) is built thanks to this project.

Here is a minimal working example:

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

If you do not want a footer, let `footer = None` (which is the default value).

The `category` field is used to infer which symbol to prepend before the link.
By default, nothing is recognized and no icon is produced.
See the [https://docskellington.github.io/WebsiteBuilder/index.html#link-category-in-footer-and-icons](online documentation) to know how to add icons.

## Development

Run `pipenv install --dev` at the root of the repository to install all (developing) dependencies.

Pull requests are welcome!

## License
This project is licensed under [MIT License](LICENSE).
