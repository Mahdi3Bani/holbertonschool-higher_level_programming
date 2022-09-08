#!/usr/bin/python3
from re import S


if __name__ == "__main__":
    import sys
    s = 0
    for i in range(1, len(sys.argv)):
        s = s + int(sys.argv[i])
    print(s)
