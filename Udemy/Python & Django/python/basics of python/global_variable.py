global_var = "I am global"

def print_global():
    global global_var  # Corrected the typo here
    global_var = "I am modified"  # Modifying the global variable
    print(global_var)  # Prints the modified global variable

print_global()  # Function call
print(global_var)  # Check if the global variable is modified outside the function
