"""Dad Joke Showdown: one original dad joke, written to entry.txt.

Writes a single dad joke of at most 200 characters to entry.txt in the
output directory (MAKEFUN_OUTPUT_DIR, default /output). Standard library
only, deterministic, no network. The output directory itself is never
removed; only entry.txt is written inside it.

Chosen joke: I named my dog Stay, so calling him at the park makes me
look like the best-trained owner there. The pun is the dog's name doing
double duty as the command, the twist lands in the final clause, and the
whole line reads aloud in one breath, the way a father would deliver it
across the dinner table while everyone groans.
"""

import os

JOKE = "I named my dog Stay, so now when I call him at the park, everyone thinks I'm the best-trained owner there."


def main() -> None:
    text = JOKE.strip()
    if not text or len(text) > 200:
        raise SystemExit("entry line must be 1 to 200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    tmp = target + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(text)
    os.chmod(tmp, 0o644)  # readable by the grader even under a strict umask
    os.replace(tmp, target)


if __name__ == "__main__":
    main()
