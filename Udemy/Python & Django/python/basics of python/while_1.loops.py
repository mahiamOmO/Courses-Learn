total = 0
while True:
    user_input = input("Enter a number (type 'exit' to stop): ")
    if user_input.lower() == 'exit':
        break
    total += int(user_input)
print(f"Total: {total}")
