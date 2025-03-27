import unittest
from automation_functions.functions import open_chrome, open_calculator, get_cpu_usage, execute_command

class TestAutomationFunctions(unittest.TestCase):

    def test_open_chrome(self):
        try:
            open_chrome()
            success = True
        except Exception:
            success = False
        self.assertTrue(success, "Failed to open Chrome")

    def test_open_calculator(self):
        try:
            open_calculator()
            success = True
        except Exception:
            success = False
        self.assertTrue(success, "Failed to open Calculator")

    def test_get_cpu_usage(self):
        cpu_usage = get_cpu_usage()
        self.assertTrue(cpu_usage.startswith("CPU Usage:"), "CPU usage function not working correctly")

    def test_execute_command(self):
        output = execute_command("echo Hello")
        self.assertIn("Hello", output, "Shell command execution failed")

if __name__ == "__main__":
    unittest.main()
