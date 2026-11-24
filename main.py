import pathlib

# The One-Line Laugh: one funny line, <=200 chars, on any subject.
# Judge weighs (in order): actually funny + <=200, a real turn at the end,
# an everyday truth people nod at, economy of words, freshness.
ENTRY = "My side project finally works. It does exactly one thing: remind me why I started it."


def main() -> None:
    assert len(ENTRY) <= 200, len(ENTRY)
    out = pathlib.Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
