# list of colors in corresponding index (RGB)
color_list = ['reddish', 'greenish', 'bluish']
# key value pairs for hex to decimal conversions
hex_values = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, 
                '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, 
                'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15}
# key value pairs for decimal to hex conversions
hex_values_2 = {0 : 0, 1 : 1, 2 : 2, 3 : 3, 4 : 4, 
                5 : 5, 6 : 6, 7 : 7, 8 : 8, 9 : 9, 
                10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F'}

# function to find max value and index of value
def describe_color(r, g, b):
    boolean_list = [False, False, False]
    color = (r, g, b)
    maximum = max(color) # find the max value
    index = 0
    counter = 0
    for i, x in enumerate(color):
        if x == maximum:
            index = i
            counter = counter + 1
            boolean_list[i] = True
    if counter > 1:
        if(boolean_list == [True, True, False]):
            print('The color is a shade of yellow.')
        elif(boolean_list == [True, False, True]):
            print('The color is a shade of magenta.')
        elif(boolean_list == [False, True, True]):
            print('The color is a shade of cyan.')
    else:    
        print('The color is', color_list[index] + '.')

a = [205, 205, 144]
print(a.index(max(a)))

# Task 1 Input
print('Task 1')
describe_color(205, 96, 144)
describe_color(28, 134, 238)
describe_color(72, 209, 204)
describe_color(237, 145, 33)

# Task 2 Input
print('\nTask 2')
describe_color(250, 250, 70)
describe_color(245, 50, 245)
describe_color(100, 231, 231)

# Extra Task 3 Input
print('\nExtra Task 3')
describe_color(70, 240, 150)
describe_color(167, 167, 42)
describe_color(223, 67, 223)
describe_color(70, 67, 243)

def hex_to_dec(hex):
    result = 0
    temp = hex[1:]
    for i, x in enumerate(reversed(temp)):
        val = hex_values.get(x) * 16**i
        result = result + val
    return result

# Extra Task 1 Input
print('\nExtra Task 1')
print(hex_to_dec('#FF'))
print(hex_to_dec('#74'))
print(hex_to_dec('#7FFF00'))
print(hex_to_dec('#9932CC'))
print(hex_to_dec('#FF86C2'))

def dec_to_hex(r, g, b):
    initial_rgb = [r, g, b]
    rgb_result = []
    for x in initial_rgb:
        result = x
        remainder = ""
        while(result != 0):
            remainder += str(hex_values_2.get(result%16))
            result = result//16
        remainder = remainder[::-1]
        rgb_result.append(remainder)
    print(rgb_result)

# Extra Task 2 Input
print('\nExtra Task 2')
dec_to_hex(250, 250, 70)
dec_to_hex(245, 50, 245)
dec_to_hex(100, 231, 231)
