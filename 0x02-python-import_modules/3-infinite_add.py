#!/usr/bin/python3
def main():
    import sys

    sum = 0
    list = sys.argv[:]
    for item in list:
        try:
            sum = sum + int(item)
        except ValueError:
            sum = 0
    print("{}".format(sum))


if __name__ == "__main__":
    main()
