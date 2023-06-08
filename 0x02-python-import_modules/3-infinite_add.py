#!/usr/bin/python3

if __name__ == "__main__":
    """a program that prints all the names defined by the compiled module hidden_4.pyc"""
    import sys

    total = 0
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])
    print("{}".format(total))

