import pathlib
import builder


def remove_dir(directory: pathlib.Path):
    if not directory.exists():
        return
    for child in directory.iterdir():
        if child.is_file():
            child.unlink()
        else:
            remove_dir(child)
    directory.rmdir()


input_folder = pathlib.Path("sources/")
output_folder = pathlib.Path("output/")
global_setup = builder.Global(
    title="Documentation of Website Builder",
    base_url="https://docskellington.github.io/WebsiteBuilder/",
    links_in_header=[
        ("Home page", "index.html"),
        ("Internal details", "internal.html"),
    ],
    footer=builder.Footer(
        "Website Builder.",
        [
            builder.Link(
                "Github", "https://github.com/DocSkellington/WebsiteBuilder", "GitHub project"
            ),
        ],
    ),
)

remove_dir(output_folder)

builder.templates.category_to_icon.add_iconoir("github", "iconoir-github")

builder.build_site(input_folder, output_folder, global_setup)
