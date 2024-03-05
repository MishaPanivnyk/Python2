def print_twinkle(): 
    poem = """Twinkle, twinkle, little star, 
       How I wonder what you are! 
             Up above the world so high, 
             Like a diamond in the sky. 
Twinkle, twinkle, little star, 
      How I wonder what you are""" 
    
    print(poem) 
 
 
print_twinkle() 
 
 
import math 
 
 
def calculate_circle_area(radius): 
    area = math.pi * radius**2 
    return area 
 
 
def main(): 
    radius = float(input("Введіть радіус кола: ")) 
    area = calculate_circle_area(radius) 
    print("Площа кола з радіусом", radius, "дорівнює", area) 
 
 
if name == "__main__": 
    main() 
 
 
color_list = ["Red","Green","White","Black"] 
 
 
 
 
print("Перший колір у списку:", color_list[0]) 
 
 
 
 
print("Останній колір у списку:", color_list[-1]) 
 
 
def calculate_value(n): 
    nn = int(str(n) * 2)   
    nnn = int(str(n) * 3)   
    result = n + nn + nnn 
    return result 
 
 
n = int(input("Введіть число n: "))   
result = calculate_value(n) 
print("Результат:", result) 
 
 
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 743, 527] 
 
 
for num in numbers: 
    if num == 237: 
        break 
    if num % 2 == 0: 
        print(num) 
 
 
def check_sequence(sequence): 
    if len(sequence) % 2 != 0: 
        return False 
    
    for i in range(0, len(sequence), 2): 
        if sequence[i] != '0' or sequence[i+1] != '1': 
            return False 
    
    return True 
 
 
sequence1 = "010101010" 
sequence2 = "00011100011" 
 
 
print("Результат для послідовності 01010101:", check_sequence(sequence1)) 
print("Результат для послідовності 00011100011:", check_sequence(sequence2)) 
 
 
def print_even_numbers(n, m): 
    start = -n 
    end = n 
    step = m 
    
    for num in range(start, end + 1, step): 
        if num % 2 == 0: 
            print(num) 
 
 
 
 
m = int(input("Введіть порядковий номер студента у журналі: ")) 
 
 
 
 
n = 20   
 
 
print("Парні числа від -{} до {} з кроком {}: ".format(n, n, m)) 
print_even_numbers(n, m) 
 
 
def count_combinations(m): 
    return 25 ** m 
 
 
 
 
m = int(input("Введіть порядковий номер студента у журналі: ")) 
 
 
 
 
combinations = count_combinations(m) 
print("Кількість можливих комбінацій:", combinations)
