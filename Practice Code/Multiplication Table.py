number=int(input("Enter a number to generate its multiplication table: "))
print(f"Multiplication Table for {number}:")
a=int(input("Enter the range for the multiplication table (e.g., 10 for up to 10): "))
for i in range(1, a + 1):
    print(f"{number} x {i} = {number * i}") 
