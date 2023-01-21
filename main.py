#Генератор пароля

import random
lower_case = "abcdefghijklmnopqrtuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRTUVWXYZ"
num = "1234567890"
symbol = "{} [] () @ # _ - &"

ans = lower_case + num + symbol + upper_case

lenght = 20
password = "".join(random.sample(ans,lenght))
print("Сгенерированый пароль, это - ",password)
