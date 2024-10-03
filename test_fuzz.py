from fuzzer import fuzz_function

def test_function(input_data):
    """A dummy test function that you want to fuzz. 
    Replace this with the function you want to test."""
    try:
        # Example function that could raise an error with bad input
        if len(input_data) > 5:
            raise ValueError("Input too long!")
        elif "error" in input_data:
            raise RuntimeError("Error keyword found!")
        print(f"Input is: {input_data}")
    except Exception as e:
        print(f"Exception occurred: {e}")

if __name__ == "__main__":
    fuzz_function(test_function, iterations=20)
