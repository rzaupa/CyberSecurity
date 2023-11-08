import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--x1", type = int)
parser.add_argument("--x2", type = int)
parser.add_argument("--y", type = int)
args = parser.parse_args()


def main():
    #get the arguments
    x1 = args.x1
    x2 = args.x2
    operation = args.y

    #adding f before the " allows you to insert variables
    #inside the string
    print(f"x1={x1}\tx2={x2}")

    if operation == 0:
        print(f"solution={x1 + x2}")
    elif operation == 1:
        print(f"solution={x1 - x2}")
    elif operation == 2:
        print(f"solution={x1 * x2}")
    if operation == 3:
        print(f"solution={x1 / x2}")


if __name__ == '__main__':
    #usage example: python solution.py --x1 1 --x2 2 --y 3
    main()
