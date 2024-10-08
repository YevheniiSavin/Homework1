# Exercise 1

# n = float(input('Enter your number: '))

# if n % 2 == 0:
#     print('Even')
# else:
#     print('Odd')

# Exercise 2

# day = input("Enter day of the week: ")

# if day == 'Saturday' or day == 'Sunday':
    # print('Today is weekend')
# elif day == 'Wednesday':
    # print('I have a dentist appointment today at 3:30 pm.')
# else:
    # print('Today is an ordinary day')

# Exercise 3

# n = int(input('Enter whole number: '))

# text = input('Enter your text: ')

# for i in range(n):
    # print(text)

# Exercise 4

# message = input('Enter text data: ')
# count = 0

# for c in message:
    # if c in 'ауоиэыяюеё':
        # count += 1

# print(count)

# Exercise 5

total = 0

while True:
    n = int(input("Enter whole and positive number: "))
    if n < 0:
        break
    total += n

print(total)