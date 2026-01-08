from langchain_core.tools import tool
from src.skills.val_pdb.test_valpdb import test_valpdb
from src.skills.val_pdb.ramachandran import plot_ramachandran


@tool
def val_pdb_smoke_test() -> str:
    """
    Run a smoke test for the val_pdb skill.
    Use this to verify the PDB evaluation pipeline is callable.
    """
    return test_valpdb()

@tool
def plot_ramachandran_tool(
    pdb_path: str,
    output_png_path: str,
) -> str:
    """
    Generate a Ramachandran plot image for a protein structure.

    Use this tool when the user asks to:
    - assess backbone torsion angle quality
    - generate a Ramachandran plot
    - visualize phi/psi angle distributions

    Parameters:
    - pdb_path: path to a PDB file
    - output_png_path: path to save the PNG image

    Returns:
    - Path to the generated Ramachandran plot image.
    """
    return plot_ramachandran(
        pdb_path=pdb_path,
        output_png_path=output_png_path,
    )
