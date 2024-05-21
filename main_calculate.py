from Calculator import *

# sečtení z třídy calculate
a = Calculator.add(3,6)
print(a)

b = Calculator.ans_add(10)
c = Calculator.ans_add(4)
print(c)

print()

c = Calculator.clean_ans()
print(c)

print()

g = Calculator.minus(10,4)
print(g)

f = Calculator.ans2_minus(1)
d = Calculator.ans2_minus(2)
print(f"print f: {f}")
print(f"print d: {d}")

q = Calculator.ans2_minus(10)
print(f"print q: {q}")
print()

f = Calculator.largest(1,22,3,4,52)
print(f)

print()
w = Calculator.divide(10,5)
print(f"print w divide: {w}")


from views import *
def run_app():

    while True:
        main_menu_views()
        user_choice = int(input("Zadej volbu: "))

        if user_choice == 1:
            p = Calculator.add(input1_views(),input1_views())
            print(p)

        elif user_choice == 2:
            input1_view()
            input2_views()


        elif user_choice == 0:
            exit()

        else:
            pass#wrong_choice_message()

run_app()