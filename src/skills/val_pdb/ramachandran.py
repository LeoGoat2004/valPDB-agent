from ramachandraw.utils import plot
import matplotlib.pyplot as plt
import os
from typing import Optional


def plot_ramachandran(
    pdb_path: str,
    output_png_path: str,
    title: Optional[str] = None,
) -> str:
    """
    Generate a Ramachandran plot for a given PDB file.

    Parameters
    ----------
    pdb_path : str
        Path to the input PDB file.
    output_png_path : str
        Path to save the output PNG image. Must end with '.png'.
    title : Optional[str]
        Optional plot title. If None, derived from pdb file name.

    Returns
    -------
    str
        The path to the generated PNG file.
    """
    if not output_png_path.lower().endswith(".png"):
        raise ValueError("output_png_path must end with .png")

    if not os.path.isfile(pdb_path):
        raise FileNotFoundError(f"PDB file not found: {pdb_path}")

    output_dir = os.path.dirname(output_png_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    if title is None:
        base_name = os.path.splitext(os.path.basename(pdb_path))[0]
        title = "".join(
            c if c.isalnum() or c in "._-" else "_" for c in base_name
        )

    # Generate plot (do not show, do not save inside the library)
    plot([pdb_path], save=False, show=False)

    plt.title(title)
    plt.savefig(output_png_path, dpi=300, bbox_inches="tight")
    plt.close()

    return output_png_path
