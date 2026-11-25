"""The Funniest Out-of-Office — make.fun entry.

Writes one funny line — an out-of-office auto-reply — to /output/entry.txt.
"""

import os

REPLY = (
    "Out of office until Monday — my inbox is guarded by an AI that "
    "already decided your email can wait. It said the same about mine."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
