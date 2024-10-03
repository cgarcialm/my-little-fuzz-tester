def process_input(input_data):
    """A simple function that processes input and raises exceptions based on conditions."""
    try:
        if len(input_data) > 5:
            raise ValueError("Input too long!")
        elif "error" in input_data:
            raise RuntimeError("Error keyword found!")
        return f"Processed: {input_data}"
    except Exception as e:
        return f"Exception occurred: {e}"
