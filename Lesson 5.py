name = "Sergiy"
print(name.upper())

print("Hello " + name)
print(name*5)

for s in name.upper():
    print(s, end=' - ')
print()

age = 20
print(f"{name:.<20s}", "Hello")
print(f"{age:^20d}", "Hello")

students = {"Anna":20, "Alexander":19, "Sergiy":21}

w = 0
for n, a in students.items():
    if len(n) > w:
        w = len(n)

print("_"*(w+10))
for n, a in students.items():
    print(f"|{n:{w+2}} | {a:^3}|")
    print("-"*(w+10))


pi = 3.141592456456456
print(f"{pi:#^10.4f}", "Hello")

d = 0.053548
print(f"{d:3.3%}")

print(f"Hello {name}, you age {age}")
print("Hello {n:s}, you age {a:d}".format(n=name, a=age))
print("Hello %s, you age %d" % (name, age))
print("{:-^30}".format("Hello"))

print("1.Save\n2.Open\n3.Print\n4.Exit")
print("Hello\rPython")
print("Hello\bPython")
print("\a")

import time
for _ in range(20):
    for s in name:
        print(s, end='')
        time.sleep(0.3)
    for i in range(len(name)):
        print("\b", end='')
        time.sleep(0.3)


