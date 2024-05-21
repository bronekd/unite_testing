# třída kalkulačka

class Calculator:
    ans = 0
    ans2 = 0

    @staticmethod #decorater
    def add(a, b):
        return a+b
    @staticmethod #decorater
    def divide(a, b):
        return a / b

    @classmethod #decorater
    def ans_add(cls, a):
        cls.ans += a
        return cls.ans

    @classmethod #decorater
    def clean_ans(cls):
        cls.ans += 0

    @staticmethod
    def minus(a, b):
        return a - b

    @classmethod
    def ans2_minus(cls, b):
        cls.ans2 -= b
        return cls.ans2

    @staticmethod  # decorater
    def largest(*args):
        return max(args)


