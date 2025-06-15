import calculadora_indices as calculadora

def consola_porcentaje_grasa():
    print("===================================================")
    print("=== CALCULADORA DE PORCENTAJE DE GRASA CORPORAL ===")
    print("===================================================\n")

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
        edad = int(input("Ingresar Edad (años): "))
        if edad <= 0:
            print("Error: La edad debe ser un valor positivo y mayor a 0")
            return

        print("\nSelecciona tu género:")
        print("M - Masculino")
        print("F - Femenino")
        genero = input("Género (M/F): ").strip().upper()
        if genero not in ['M', 'F']:
            print("Error: Debes seleccionar M (para masculino) o F (para femenino)")
        elif genero.upper() == 'M':
            valorGenero = 10.8
        elif genero.upper() == 'F':
            valorGenero = 0
        if valorGenero is None:
            print("Error al procesar el género")
            return

        porcentaje_grasa = calculadora.calcular_porcentaje_grasa(peso, altura, edad, valorGenero)
        if porcentaje_grasa is not None:
            print("\n=== RESULTADO ===")
            print(f"Tu porcentaje de grasa corporal es: {porcentaje_grasa}%")
            print("===================")
        else:
            print("No se pudo calcular el porcentaje de grasa debido a un error en los datos")

    except ValueError:
        print("Error: Por favor ingresa valores numéricos válidos")
    except Exception as e:
        print(f"Error inesperado: {e}")

consola_porcentaje_grasa()