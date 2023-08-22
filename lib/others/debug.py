import os
import shutil
import click

@click.command()
@click.argument('directory', default=".")
def remove_pycache(directory):
    for root, dirs, _ in os.walk(directory):
        if "__pycache__" in dirs:
            pycache_path = os.path.join(root, "__pycache__")
            try:
                shutil.rmtree(pycache_path)
                click.echo(f"Removed: {pycache_path}")
            except Exception as e:
                click.echo(f"Error removing {pycache_path}: {e}")

if __name__ == "__main__":
    remove_pycache()
