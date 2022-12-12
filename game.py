from util import generate_moves


def main():
    print("Welcome, to the world of Pokemon...")

    moves = generate_moves()

    for move in moves:
        print(move.details())


if __name__ == "__main__":
    main()
