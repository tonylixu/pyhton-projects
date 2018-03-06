"""
A demostration of multiple Python inheritance

In this exmaple we call super() instead of parent class
"""
class BaseClass:
    num_base_calls = 0
    def call_me(self):
        print("Calling method on BaseClass")
        self.num_base_calls += 1

