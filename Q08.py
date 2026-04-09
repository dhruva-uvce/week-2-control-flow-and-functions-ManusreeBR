# Q08. Sum of Digits (while loop)
#
# Ask the user for a positive integer.
# Print the sum of its digits using a while loop.
#
# Sample Input:   Enter a number: 9876
# Sample Output:  Sum of digits of 9876 = 30

# --- YOUR CODE HERE ---
n=int(input("Enter a number: "))
sum=0
num=n
while(n>0):
  digit=n%10
  sum+=digit
  n=n//10
print("Sum of digits of ",num," = ",sum)
