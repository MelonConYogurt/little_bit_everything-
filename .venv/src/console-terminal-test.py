from rich.console import Console
import time
import itertools

console = Console()

def spinner_animation():
    spinner = itertools.cycle(["-", "\\", "|", "/"])
    for _ in range(100):
        console.print(next(spinner), end="\r")
        time.sleep(0.1)

spinner_animation()
