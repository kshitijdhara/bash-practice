print("Find the difference between the find the sum of squares of the find 100 numbers and the square of the sum of the first hundred numbers")

sum_of_squares=0
square_of_sum=0
for i in range (1,101):
    sum_of_squares += i**2
    square_of_sum += i
square_of_sum = square_of_sum**2
print(f"The difference between the sum of the squares {sum_of_squares} and the square of the sums {square_of_sum} is : {abs(sum_of_squares - square_of_sum)}")