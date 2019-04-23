num = int(input("Ingrese un numero de base decimal: "))
if num<10 and num>=0:
    print(f"Su numero en hexadecimal es: {num}")
if num>=10 and num <=15:
    if num == 10: 
        print("Su numero es A")
    if num == 11:
        print("Su numero es B")
    if num == 12:
        print("Su numero es C")
    if num == 13:
        print("Su numero es D")
    if num == 14:
        print("Su numero es E")
    if num == 15:
        print("Su numero es F")
if 256>num>=16:
    pd = int(num / 16)
    if pd == 10:
        pd = str("A")
    if pd == 11:
        pd = str("B")
    if pd == 12:
        pd = str("C")
    if pd == 13:
        pd = str("D")
    if pd == 14:
        pd = str("E")
    if pd == 15:
        pd = str("F")
    sd = int (num % 16)
    if sd == 10:
        sd = str("A")
    if sd == 11:
        sd = str("B")
    if sd == 12:
        sd = str("C")
    if sd == 13:
        sd = str("D")
    if sd == 14:
        sd = str("E")
    if sd == 15:
        sd = str("F")
    print(f"Su numero es {pd}{sd}")
if 4095>num>=256:
    pd = int((num / 16) / 16)
    if pd == 10:
        pd = str("A")
    if pd == 11:
        pd = str("B")
    if pd == 12:
        pd = str("C")
    if pd == 13:
        pd = str("D")
    if pd == 14:
        pd = str("E")
    if pd == 15:
        pd = str("F")
    sd = int ((num / 16) % 16)
    if sd == 10:
        sd = str("A")
    if sd == 11:
        sd = str("B")
    if sd == 12:
        sd = str("C")
    if sd == 13:
        sd = str("D")
    if sd == 14:
        sd = str("E")
    if sd == 15:
        sd = str("F")
    td = int (num % 16)
    if td == 10:
        td = str("A")
    if td == 11:
        td = str("B")
    if td == 12:
        td = str("C")
    if td == 13:
        td = str("D")
    if td == 14:
        td = str("E")
    if td == 15:
        td = str("F")
print(f"Su numero es {pd}{sd}{td}")
    




    







    

