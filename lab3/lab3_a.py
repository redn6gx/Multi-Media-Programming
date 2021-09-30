# LAB SUMMARY
    # I was able to complete the whole lab.
    # The only challange I ran into was trying to print a value
    # from the dictionary inside an f-string. I got syntax errors when
    # trying to reference the value as so: print(f'{color_dictionary['magenta']}').
    # To fix this I instead had to save the value in a variable first. I was then
    # able to print the variable in the f-string just fine.

# Task 1
color_dictionary = { 'red' : (255, 0, 0), 'green' : (0, 255, 0), 'blue' : (0, 0, 255), 'magenta' : (255,0,255), 'cyan' : (0,255,255), 'yellow' : (255,255,0)}

print('Task 1')
print(f'color_dictionary: {color_dictionary}')

# Task 2
magenta = color_dictionary.get('magenta')
yellow = color_dictionary.get('yellow')
cyan = color_dictionary.get('cyan')

print('\nTask 2')
print(f'The blue channel of magenta has value {magenta[2]}')
print(f'The green channel of yellow has value {yellow[1]}')
print(f'The red channel of cyan has value {cyan[0]}')

print('\nTuples where the second letter of the color is \'e\':')
for color in color_dictionary:
    if color[1] == 'e':
        print(f'{color} = {color_dictionary[color]}')

# Task 3
tineye_sample = {
 "status": "ok",
 "error": [],
 "method": "extract_collection_colors",
 "result": [
 {
 "color": (141,125,83),
 "weight": 76.37,
 "name": "Clay Creek",
 "rank": 1,
 "class": "Grey"
 },
 {
 "color": (35,22,19),
 "weight": 23.63,
 "name": "Seal Brown",
 "rank": 2,
 "class": "Black"
 }
 ]
}

print('\nTask 3')
print('Clay Creek(Red Channel): ' + str(tineye_sample.get('result')[0].get('color')[0]))
print('Seal Brown(Blue Channel): ' + str(tineye_sample.get('result')[1].get('color')[2]))

for index in range(4,7):
    print('Everything is fine')