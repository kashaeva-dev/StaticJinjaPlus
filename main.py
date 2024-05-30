import argparse
import os
from pathlib import Path

from staticjinja import Site


def get_context():
    context = {}
    prefix = "SJP_"
    for key in os.environ.keys():
        if key.startswith(prefix):
            context[key.removeprefix(prefix).lower()] = os.environ[key]
    return context


def main():
    parser = argparse.ArgumentParser(
        description="Render HTML pages from Jinja2 new_templates"
    )
    parser.add_argument(
        "-w",
        "--watch",
        help="Render the site, and re-render on changes to <srcpath>",
        action="store_true"
    )
    parser.add_argument(
        "--srcpath",
        help="The directory to look in for new_templates (defaults to './new_templates)'",
        default=Path(".") / "new_templates",
        type=Path
    )
    parser.add_argument(
        "--outpath",
        help="The directory to place rendered files in (defaults to './build')",
        default=Path(".") / "build",
        type=Path
    )

    args = parser.parse_args()

    src_path = args.srcpath
    output_path = args.outpath
    static_path = Path(src_path) / "assets"

    site = Site.make_site(
        searchpath=src_path,
        outpath=output_path,
        staticpaths=[static_path],
        contexts=[(".*.html", get_context)]
    )

    site.render(use_reloader=args.watch)


if __name__ == '__main__':
    main()
