import os

TEXT = (
    "Morning comes through the window in a slow square, moving across the "
    "floor an inch at a time. Dust turns in it, unhurried. You watch it reach "
    "the chair, the table, the far wall, and you are not late for anything. "
    "The light will find you wherever you stand."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()