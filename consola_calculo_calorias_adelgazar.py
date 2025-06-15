import calculadora_indices  as calculadora

def consola_calculo_calorias_adelgazar():
    print("=== CALCULADORA DE CALORÍAS PARA ADELGAZAR ===")
    print("Calcula el rango de calorías recomendado para perder peso")
    print("======================================================\n")

    try:
        print("Por favor, ingresa los siguientes datosa a continuacion:")
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

        if valorGenero is None:
            print("Error al procesar el género")
            return

        recomendacion = calculadora.consumo_calorias_recomendado_para_adelgazar(
            peso, altura, edad, valorGenero
        )

        tmb = calculadora.calcular_calorias_en_reposo(peso, altura, edad, valorGenero)

        if tmb is not None and "Error" not in recomendacion:
            print(recomendacion)

        else:
            print("No se pudo calcular la recomendación debido a un error en los datos")

    except ValueError:
        print("Error: Por favor ingresa valores numéricos válidos")
    except Exception as e:
        print(f"Error inesperado: {e}")

consola_calculo_calorias_adelgazar()