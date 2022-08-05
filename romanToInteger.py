class Solution:

    s = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    print("Enter Any Roman number/n IVXLCDM")

    arr = list(map(str, input().split()))

    print(arr.sum())
