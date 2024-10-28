# Function with a default parameter value
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Calling the function with and without the default parameter
greet("Alice")           # Uses the default greeting "Hello"
greet("Bob", "Hi")       # Uses the custom greeting "Hi"
