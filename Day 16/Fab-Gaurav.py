"""
Original file is located at
    https://colab.research.google.com/drive/1Qepk9Pgjox9Jld2conJtpjp46RQRuE3A
"""

num = int(input("Enter the number : ")); 
temp=num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if temp==rev:
    print("%d is a palindrome number" %temp)
else:
    print("%d is not a palindrome number" %temp)
