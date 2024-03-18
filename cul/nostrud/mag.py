from rich.console import Console

console = Console()

def cprint(text, color):
    """
    Prints text in a specific color.

    Args:
        text (str): The text to print.
        color (str): The color to print the text in.
    """

    console.print(text, style=f"bold {color}")

cprint(f'\n>>> swap VST | {address_wallet} | {error}', 'red')
