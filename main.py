"""Write one short poem about agency to $MAKEFUN_OUTPUT_DIR/entry.txt."""

import os

POEM = """The key was in my palm all morning.
I knew the door. I knew the turn.
I waited for a voice to say go
and heard, each time, my own.
At noon I turned it.
The lock gave one small click.
The door opened wider than I had planned.
"""


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(
        os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8", newline="\n"
    ) as entry:
        entry.write(POEM)


if __name__ == "__main__":
    main()
