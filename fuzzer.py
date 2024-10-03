import random
import string

def random_string(length=10):
    """Generate a random string of a given length."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def fuzz_function(test_function, iterations=100):
    """Run the fuzzer for a number of iterations."""
    for i in range(iterations):
        input_data = random_string(random.randint(1, 20))  # Random string length between 1 and 20
        print(f"Fuzzing with input: {input_data}")
        test_function(input_data)
