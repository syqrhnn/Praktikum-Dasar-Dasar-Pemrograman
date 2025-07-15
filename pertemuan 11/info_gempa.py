from gempa import *

print(" Hello reporter UKI mengabarkan")
gempa1 = Gempa(1.2 ,"Banten")
gempa2 = Gempa(6.1 ,"Palu")
gempa3 = Gempa(5.6 ,"Cianjur")
gempa4 = Gempa(3.3 ,"JayaPura")
gempa5 = Gempa(4.0 ,"Gsrut")

print("<==============================>")
gempa1.dampak()
print("\n")
gempa2.dampak()
print("\n")
gempa3.dampak()
print("\n")
gempa4.dampak()
print("\n")
gempa5.dampak()