print("--Number Converter---")

number = int(input("Enter a number: "))

print(f"Binary: {bin(number)[2:]}") ##[2:] remove first 2 characters
print(f"Octal: {oct(number)[2:]}")
print(f"Hexadecimal: {hex(number)[2:]}")