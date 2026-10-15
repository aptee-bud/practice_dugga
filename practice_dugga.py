nums = [12, -1, -4, 0, 7, 7, -9, 3]

sum = 0
for num in nums:
    if num > 5:
        sum = sum + num

print(sum) # a) --> 26

def bucket(n):
    if n <= -5:
        return "LOW"
    elif n < 5 and n > -5:
        return "MID"
    else:
        return "HIGH"

print(bucket(-9)) # b) --> LOW
print(bucket(7)) # --> HIGH


no_of_lows = 0
no_of_mids = 0
no_of_highs = 0
odd_high = []

for num in nums:
    if bucket(num) == "LOW":
        no_of_lows += 1
    elif bucket(num) == "MID":
        no_of_mids += 1
    elif bucket(num) == "HIGH":
        no_of_highs += 1 
        if bucket(num) == "HIGH" and num % 2 != 0:
            odd_high.append(num)

print(f"Number of lows: {no_of_lows}")
print(f"Number of mids: {no_of_mids}")
print(f"Number of highs: {no_of_highs}")
print(f"The list of odd AND high numbers: {odd_high}")