"""
A demostration of multiple Python inheritance

In this exmaple we call super() instead of parent class


>>> s = Subclass()
>>> s.call_me()
Calling method on BaseClass
Calling method on RightSubclass
Calling method on LeftSubclass
Calling method on Subclass
"""
class BaseClass:
    num_base_calls = 0
    def call_me(self):
        print("Calling method on BaseClass")
        self.num_base_calls += 1

class LeftSubclass(BaseClass):
    num_left_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling method on LeftSubclass")
        self.num_left_calls += 1

class RightSubclass(BaseClass):
    num_right_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling method on RightSubclass")
        self.num_right_calls += 1

class Subclass(LeftSubclass, RightSubclass):
    num_sub_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling method on Subclass")
        self.num_sub_calls += 1