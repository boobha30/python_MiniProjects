start_number=int(input("Enter the starting number: "))
end_number=int(input("Enter the ending number: "))
total_sum=0
for num in range(start_number, end_number + 1):
    total_sum += num
print(f"The sum of numbers from {start_number} to {end_number} is: {total_sum}")