import numpy as np
#===Characters Set===
lowercase=np.array(list("abcdefghijklmnopqrstuvwxyz"))
uppercase=np.array(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
digits=np.array(list("0123456789"))
symbols=np.array(list("!@#$%^&*()"))
#===User Input===
length=int(input("Enter length of password (min 4): "))
#===Validation===
if length<4:
    print("Password must be at least 4 characters long")
    exit()
#===Guarantee Security===
password_chars=[
    np.random.choice(lowercase),
    np.random.choice(uppercase),
    np.random.choice(digits),
    np.random.choice(symbols),
]
#===All Characters Combine===
all_chars=np.concatenate((lowercase,uppercase,digits,symbols))
#===Remaining Characters Fill===
remaining_length=length-4
if remaining_length>0:
    password_chars+=list(np.random.choice(all_chars,size=remaining_length))
#===Shuffle===
np.random.shuffle(password_chars)
#===Final Password===
password="".join(password_chars)
print(f"Strong password generated : {password}")




