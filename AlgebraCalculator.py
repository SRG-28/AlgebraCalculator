#Primer ejercicio 
#Sofía Rubie García

opcion = ""
while opcion != "4":
   print("Bienvenido Centro Educativo Montessor")
   print("--- Formulas notables ---")
   print("1. Cuadrado de una suma")
   print("2. Cuadrado de una diferencia")
   print("3. Suma por diferencia")
   print("4. Salir")
   opcion=input("Digite la opcion: ")
   match opcion:
      case "1":
        print("***Cuadrado de una suma***")
        a = int(input("Digite el valor de A: "))
        b = int(input("Digite el valor de B: "))
        result = (a ** 2) + (2 * a * b) + (b ** 2)
        print("(", a , "+", b, ")² = ", result)
        input("Presione enter para continuar...")          
      case "2":
        print("***Cuadrado de una diferencia***")
        a = int(input("Digite el valor de A: "))
        b = int(input("Digite el valor de B: "))
        result2 = (a ** 2) - (2 * a * b) + (b ** 2)
        print("(", a , "-", b, ")² = ", result2)
        input("Presione enter para continuar...")          
      case "3":
        print("***Suma por diferencia***")
        a = int(input("Digite el valor de A: "))
        b = int(input("Digite el valor de B: "))
        result3 = (a ** 2) - (b ** 2)
        print("(", a , "+", b, ")(", a , "-", b, ") = ", result3)
        input("Presione enter para continuar...")                
      case "4":
         print("Gracias por usarme")
      case _:
         print("Opción inválida")
