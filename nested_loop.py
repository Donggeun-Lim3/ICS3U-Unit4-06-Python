#!/usr/bin/env python3

# Created by Donggeun Lim
# Created on December 2020
# This program is nested loop

def main():
    loop_counter1 = 0
    loop_counter2 = 0
    loop_counter3 = 0
    for loop_counter1 in range(256):
        for loop_counter2 in range(256):
            for loop_counter3 in range(256):
                print ("RGB({},{},{})".format(loop_counter1, loop_counter2, loop_counter3))


if __name__ == "__main__":
    main()
