#!/usr/bin/python2

def bubblesort(array):
    n = len(array)-1
    for i in range(0, len(array)):
        for j in range(0, n):
            if array[j] > array[j+1]:
                array[j+1], array[j] = array[j], array[j+1] 
        n -= 1

if __name__ == "__main__":
    array = [17, 9, 13, 8, 7, -5, 6, 11, 3, 4, 1, 2]
    bubblesort(array)
    print array

