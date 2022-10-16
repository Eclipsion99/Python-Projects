from random import choice, shuffle

final = []
Num, Alpha, alpha, Spl = "", "", "", "$@!_%&"

for i in range(48, 58): Num += chr(i)
for i in range(65, 91): Alpha += chr(i)
for i in range(97, 123): alpha += chr(i)

for i in range(4):
    final += choice(Alpha) + choice(alpha)
for i in range(2):
    final += choice(Num) + choice(Spl)

shuffle(final)
print("".join(final))
