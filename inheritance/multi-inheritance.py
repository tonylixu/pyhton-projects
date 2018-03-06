"""
A demostration of multiple Python inheritance

In this exmaple we call super() instead of parent class


>>> s = Subclass()
>>> s.call_me()
Calling method on BaseClass
Calling method on RightSubclass
Calling method on LeftSubclass
Calling method on Subclass

First call_me of Subclass calls super().call_me(), which happens to refer 
to LeftSubclass.call_me().
LeftSubclass.call_me() then calls super().call_me(), but in this case,
super() is referring to RightSubclass.call_me().

Pay particular attention to this, the super call is not calling
the method on the superclass of LeftSubclass (Which is BaseClass), it is
calling RightSubclass, even though it is not a parent of LeftSubclass! This is
the "next" method, not the parent method. RightSubclass then calls BaseClass, and
the super calls have ensured each method in the calss hierarchy is executed once.
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
