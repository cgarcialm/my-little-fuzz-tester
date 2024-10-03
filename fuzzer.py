import random
import string
import time
import signal

class TimeoutException(Exception):
    """Custom exception to handle timeouts."""
    pass

def timeout_handler(signum, frame):
    """Handler for the signal alarm."""
    raise TimeoutException("Test exceeded the time limit!")

class Fuzzer:
    def __init__(self, test_function, iterations=100, timeout_seconds=3):
        self.test_function = test_function
        self.iterations = iterations
        self.timeout_seconds = timeout_seconds
        self.results = {"passed": 0, "failed": 0, "timed_out": 0, "errors": []}  # Store results

    def random_string(self, length=10):
        """Generate a random string of a given length."""
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for _ in range(length))

    def run_test(self, input_data):
        """Run the test with simulated delays and log the results."""
        # Set up the timeout for the test
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(self.timeout_seconds)  # Set the timeout limit for the test

        try:
            # Simulate a random delay within the test itself
            delay = random.uniform(0, 5)  # Random delay between 0 and 5 seconds
            if delay > 3:
                print(f"Simulating a long-running test with a delay of {delay:.2f} seconds for input: {input_data}")
            time.sleep(delay)  # Simulate delay inside the test function

            result = self.test_function(input_data)
            print(result)
            self.results["passed"] += 1  # Test passed
        except TimeoutException:
            print(f"Test timed out after {self.timeout_seconds} seconds for input: {input_data}")
            self.results["timed_out"] += 1  # Increment timeout count
        except Exception as e:
            print(f"Exception occurred: {e}")
            self.results["failed"] += 1  # Test failed
            self.results["errors"].append((input_data, str(e)))  # Log error
        finally:
            signal.alarm(0)  # Disable the alarm after each test

    def fuzz(self):
        """Run the fuzzing process and time each test."""
        for _ in range(self.iterations):
            input_data = self.random_string(random.randint(1, 20))  # Random string length between 1 and 20
            print(f"Fuzzing with input: {input_data}")

            # Run the test with the timeout and simulated delay inside it
            self.run_test(input_data)

    def generate_report(self, report_file_path="fuzzing_report.txt"):
        """Generate a report and save it to a file."""
        with open(report_file_path, "w") as report_file:
            report_file.write(f"Fuzzing Report\n")
            report_file.write(f"Total Tests: {self.iterations}\n")
            report_file.write(f"Passed: {self.results['passed']}\n")
            report_file.write(f"Failed: {self.results['failed']}\n")
            report_file.write(f"Timed Out: {self.results['timed_out']}\n")
            report_file.write("Errors:\n")
            for error in self.results["errors"]:
                report_file.write(f"Input: {error[0]} - Error: {error[1]}\n")

        print(f"Fuzzing completed. Report generated: {report_file_path}")
