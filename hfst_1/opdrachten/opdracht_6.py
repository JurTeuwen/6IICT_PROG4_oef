# Open lied.txt in Python
lied = open("lied.txt", "r")
# Vorm lied om naar lijst, vervang witregels '\n' door spaties ' ' 
lied = lied.read().replace('\n', ' ') 
# Test inhoud van lied
print(lied)

""" Begin eigen code hier """