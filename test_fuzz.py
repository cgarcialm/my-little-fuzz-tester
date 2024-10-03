from fuzzer import Fuzzer
from main import process_input

def run_fuzz_test():
    """Run the fuzz test on the process_input function."""
    # Set up the fuzzer with 20 iterations
    fuzzer = Fuzzer(test_function=process_input, iterations=20)  
    # Run the fuzzing process
    fuzzer.fuzz()  
    # Generate the report
    fuzzer.generate_report()  

if __name__ == "__main__":
    run_fuzz_test()
