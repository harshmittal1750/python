class Solution:
    s = {
        "I": 1,
        "V": 5,
        "x": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    print("Enter Any Roman number : \n(I V X L C D M)")

    var = input()

    if var in s:
        print(s.values)
