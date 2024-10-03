from fuzzer import fuzz_function
from main import process_input

def run_fuzz_test():
    """Run the fuzz test on the process_input function."""
    fuzz_function(process_input, iterations=20)

if __name__ == "__main__":
    run_fuzz_test()
