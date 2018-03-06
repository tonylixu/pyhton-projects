"""
A demostration of multiple Python inheritance

In this exmaple we call super() instead of parent class
"""
class BaseClass:
    num_base_calls = 0
    def call_me(self):
        print("Calling method on BaseClass")
        self.num_base_calls += 1

class LeftSubclass(BaseClass):
    num_left_calls = 0
    def call_me(self):
        print("Calling method on LeftSubclass")
        self.num_left_calls += 1

class RightSubclass(BaseClass):
    num_right_calls = 0
    def call_me(self):
        print("Calling method on RightSubclass")
        self.num_right_calls += 1
