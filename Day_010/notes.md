📝 Day 10 - Functions, Docstrings & Recursion

📌 Today I Learned:  
Today, I dove deeper into Python functions and explored more advanced concepts. Here’s what I learned:

🧠 Function Definitions and Return Values  
I practiced defining functions using `def`, and learned how to return single or multiple values.  
Example:
```python
def calculate(a, b):
    return a + b, a * b

sum_, product = calculate(3, 4)
📚 Docstrings
I learned how to document functions using triple-quoted docstrings to describe their purpose.
Example:

def greet(name):
    """Returns a personalized greeting."""
    return f"Hello, {name}!"
🔁 Recursive Functions
I explored recursion—functions that call themselves—to solve problems like factorials.
Example:

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
🎯 Summary:
By the end of the day, I became comfortable with writing functions that return multiple values, documenting them clearly using docstrings, and implementing recursive logic. These skills are fundamental for writing clean, reusable, and scalable Python code.