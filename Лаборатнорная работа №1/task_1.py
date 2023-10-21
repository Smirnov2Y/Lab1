numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]


realnumbers = numbers[:4] + numbers[5:]
count = len (numbers)
sum_numbers = sum(realnumbers)
avg = sum_numbers/count
numbers[4] = avg
print("Измененный список:", numbers)
