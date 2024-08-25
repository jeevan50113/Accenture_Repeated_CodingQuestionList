def LetteredNumberSum(str1, length):
    letter_map = {
                'A': 1,
                'B': 10, 
                'C': 100, 
                'D': 1000, 
                'E': 10000, 
                'F': 100000, 
                'G': 1000000
                 }
    total_sum = 0
    for char in str1:
        total_sum += letter_map.get(char, 0)
    return total_sum

if __name__ == "__main__":
    str1 = input("enter string : ")
    length = len(str1)
    print(LetteredNumberSum(str1, length))
