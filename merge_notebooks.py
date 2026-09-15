from pathlib import Path
import nbformat
import uuid

ROOT = Path(__file__).resolve().parent

notebooks = sorted(
    ROOT.glob("day*/STUDENT.ipynb")
)

if not notebooks:
    raise FileNotFoundError(
        "No STUDENT.ipynb notebooks were found."
    )

merged = nbformat.v4.new_notebook()

merged.cells.append(
    nbformat.v4.new_markdown_cell(
        "# Masar Modern Data Engineering\n"
        "## Complete Labs"
    )
)

for notebook_path in notebooks:

    print("Adding:", notebook_path)

    nb = nbformat.read(
        notebook_path,
        as_version=4
    )

    day_name = notebook_path.parent.name

    merged.cells.append(
        nbformat.v4.new_markdown_cell(
            f"# {day_name.upper()}"
        )
    )

    for cell in nb.cells:

        cell["id"] = uuid.uuid4().hex[:8]

        merged.cells.append(cell)

output = ROOT / "Masar_All_Labs.ipynb"

nbformat.write(
    merged,
    output
)

print()
print("Created:", output)
print("Total notebooks:", len(notebooks))
print("Total cells:", len(merged.cells))