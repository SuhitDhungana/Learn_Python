def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' was called with arguments: {args} and keyword arguments: {kwargs}")
        return func(*args, **kwargs)  # Call the original function
    return wrapper

@log_decorator
def add(a, b):
    return a + b

# Call the decorated function
result = add(5, 3)
print("Result:", result)
