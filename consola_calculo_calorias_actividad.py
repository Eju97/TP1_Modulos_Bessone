import calculadora_indices as calculadora

def consola_calculo_tmb():
    print("======== CALCULADORA DE CALORÍAS SEGÚN ACTIVIDAD FÍSICA ========")
    print("Calcula las calorías que quemas considerando tu actividad física")
    print("================================================================\n")

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
            valorGenero = 5
        elif genero.upper() == 'F':
            valorGenero = -161

        print("\nSelecciona la opción acorde a tu actividad física por semana:")
        print("(1) Poco o ningún ejercicio")
        print("(2) Ejercicio ligero (1 a 3 días a la semana)")
        print("(3) Ejercicio moderado (3 a 5 días a la semana)")
        print("(4) Deportista (6 a 7 días a la semana)")
        print("(5) Atleta (entrenamientos mañana y tarde)")
        opcion_actividad = int(input("Selecciona una opción (1-5): "))
        if opcion_actividad not in [1, 2, 3, 4, 5]:
            print("Error: Debes seleccionar una opción entre 1 y 5")
        elif opcion_actividad == 1:
            valorActividad = 1.2
        elif opcion_actividad == 2:
            valorActividad = 1.375
        elif opcion_actividad == 3:
            valorActividad = 1.55
        elif opcion_actividad == 4:
            valorActividad = 1.72
        elif opcion_actividad == 5:
            valorActividad = 1.9
            return

        if valorGenero is None or valorActividad is None:
            print("Error al procesar los datos")
            return

        calorias_actividad = calculadora.calcular_calorias_en_actividad(peso, altura, edad, valorGenero, valorActividad)
        tmb = calculadora.calcular_calorias_en_reposo(peso, altura, edad, valorGenero)

        if calorias_actividad is not None and tmb is not None:
            print("\n=== RESULTADO ===")
            print(f"Calorías totales con actividad física: {calorias_actividad} calorías por día")
            print("===================")
        else:
            print("No se pudieron calcular las calorías debido a un error en los datos")

    except ValueError:
        print("Error: Por favor ingresa valores numéricos válidos")
    except Exception as e:
        print(f"Error inesperado: {e}")

consola_calculo_tmb()