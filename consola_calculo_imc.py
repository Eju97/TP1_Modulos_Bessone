import calculadora_indices  as calculadora

def consola_calculo_imc():
    print("===========================================================")
    print("=== CALCULADORA DE ÍNDICE DE MASA CORPORAL (IMC) ===")
    print("===========================================================\n")

    try:
        print("Por favor, ingresa los siguientes datos a continuacion:")
        peso = float(input("Ingresar PESO en kilogramos: "))
        if peso <= 0:
            print("Error: El peso debe ser un valor positivo y mayor a 0")
            return
        altura = float(input("Ingresar ALTURA en metros: "))
        if altura <= 0:
            print("Error: La altura debe ser un valor positivo y mayor a 0")
            return
        print(f"Los datos ingresados son Peso: {peso}, Altura: {altura}")


        imc = calculadora.calcular_IMC(peso, altura)
        if imc is not None:
            print("\n=== RESULTADO ===")
            print(f"Tu IMC es: {imc}")
            print("===================")

    except ValueError:
        print("Error: Por favor ingresa valores numéricos válidos")
    except Exception as e:
        print(f"Error inesperado: {e}")

consola_calculo_imc()