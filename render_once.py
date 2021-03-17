#!/usr/bin/env python3

"""Render the ontology to a directory."""
import argparse
import pathlib
import os
import shutil
import subprocess
import sys
import textwrap

import rasaeco.render


def main() -> int:
    """Execute the main routine."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output_path", help="Path to the directory with the rendered ontology", required=True
    )
    args = parser.parse_args()

    output_path = pathlib.Path(args.output_path)
    this_dir = pathlib.Path(os.path.realpath(__file__)).parent

    ontology_dir = this_dir / "ontology"

    if not output_path.exists():
        output_path.mkdir()

    print(f"Copying the sources to: {output_path}")
    shutil.copytree(src=str(ontology_dir), dst=str(output_path), dirs_exist_ok=True)

    print(f"Rendering the ontology to: {output_path}")
    errors = rasaeco.render.once(scenarios_dir=output_path)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return -1

    print(f"Rendering the DOT graph with graphviz to SVG: {output_path}")
    if not shutil.which("dot"):
        print("The program `dot` does not exist. Did you install graphviz and is it on your path?",
              file=sys.stderr)
        return -1

    proc = subprocess.Popen(["dot", "-V"], stdout=subprocess.DEVNULL, stderr=subprocess.PIPE,
                            encoding="utf-8")
    _, version_out = proc.communicate()

    if not version_out.startswith("dot - graphviz version 2"):
        print(f"Unexpected dot version; expected a prefix 'dot - graphviz version 2', "
              f"but got: {version_out!r}", file=sys.stderr)
        return -1

    svg_pth = output_path / "ontology.svg"
    subprocess.check_call(
        ["dot", "-Tsvg", "ontology.dot", "-o", "ontology.svg"],
        cwd=str(output_path))

    ontology_svg = svg_pth.read_text()

    index_pth = output_path / "index.html"
    print(f"Generating: {index_pth}")
    index_pth.write_text(
        textwrap.dedent(
            f"""\
            <html>
            <head>
            <title>BIMprove Scenario Ontology</title>
            <style>
            a {{
                fill: blue;
                text-decoration: none;
            }}
            a:hover {{
                text-decoration: underline;
            }}
            </style>
            </head>
            <body>
            {ontology_svg}
            </body>
            </html>   
            """))

    return 0


if __name__ == "__main__":
    sys.exit(main())
