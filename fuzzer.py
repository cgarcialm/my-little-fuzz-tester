import random
import string

class Fuzzer:
    def __init__(self, test_function, iterations=100):
        self.test_function = test_function
        self.iterations = iterations
        self.results = {"passed": 0, "failed": 0, "errors": []}  # Store results

    def random_string(self, length=10):
        """Generate a random string of a given length."""
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for _ in range(length))

    def run_test(self, input_data):
        """Run the test and log the results."""
        try:
            result = self.test_function(input_data)
            print(result)
            # Test passed
            self.results["passed"] += 1  
        except Exception as e:
            # Test failed
            print(f"Exception occurred: {e}")
            self.results["failed"] += 1  
            # Log error
            self.results["errors"].append((input_data, str(e)))  

    def fuzz(self):
        """Run the fuzzing process."""
        for _ in range(self.iterations):
            # Random string length between 1 and 20
            input_data = self.random_string(random.randint(1, 20)) 
            print(f"Fuzzing with input: {input_data}")
            self.run_test(input_data)

    def generate_report(self, report_file_path="fuzzing_report.txt"):
        """Generate a report and save it to a file."""
        with open(report_file_path, "w") as report_file:
            report_file.write(f"Fuzzing Report\n")
            report_file.write(f"Total Tests: {self.iterations}\n")
            report_file.write(f"Passed: {self.results['passed']}\n")
            report_file.write(f"Failed: {self.results['failed']}\n")
            report_file.write("Errors:\n")
            for error in self.results["errors"]:
                report_file.write(f"Input: {error[0]} - Error: {error[1]}\n")

        print(f"Fuzzing completed. Report generated: {report_file_path}")
