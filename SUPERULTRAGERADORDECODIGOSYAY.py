
import random

keyRNG = ['+','!','@','#','%','A','T','G']

code = ""

for i in range(1,8):    
    code = code+str(random.randint(0,9))

for i in range(1,8):
    split = random.randint(0,len(code))
    key = random.choice(keyRNG)
    code = code[:split]+key+code[split:]

print(code)
