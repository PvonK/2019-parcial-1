from hexad import hexad

def interfaz (x):

    if not x:
        return 'ingrese un numero'


    try:

        int(x)

        if 4095 < int(x):
            return 'Ingrese un numero menor a 4095'
        else:
            if int(x)<0:
                return 'ingrese un  numero positivo'
            else:
                return hexad(x)

    except:

        return 'ingrese un numero'




        

    

