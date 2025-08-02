#!/usr/bin/env python3
"""
Sample Python file for testing the automated code review workflow.
This file demonstrates various code patterns that the linter should catch.
"""

def hello_world():
    """Print a hello world message."""
    print("Hello, World!")

def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b

def main():
    """Main function to demonstrate the workflow."""
    hello_world()
    result = add_numbers(5, 3)
    print(f"5 + 3 = {result}")

if __name__ == "__main__":
    main()