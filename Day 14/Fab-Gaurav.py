"""
Original file is located at
    https://colab.research.google.com/drive/1mLWNb036HzxwZg_ZZ9hfLbu6a-DEevId
"""

num = int(input(" Please Enter the Number: "))
sum = 0

for i in range(1, num):
    if(num % i == 0):
        sum = sum + i

if (sum == num):
    print(" %d is a Perfect Number" %num)
else:
    print(" %d is not a Perfect Number" %num)
