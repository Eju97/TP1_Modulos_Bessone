
def  calcular_IMC(peso: float, altura: float):
    try:
        imc = peso/(altura**2)
        return round(imc, 2)
    except ZeroDivisionError:
        print ("Error")
    except Exception as e:
        print(e)


def calcular_porcentaje_grasa(peso: float, altura: float, edad: int, valorGenero: float):
    try:
        imc = calcular_IMC(peso, altura)
        if imc is None:
            print("error")
        porcentajeGrasa = 1.2 * imc + 0.23 * edad - 5.4 - valorGenero
        return porcentajeGrasa
    except Exception:
        print("error")


def calcular_calorias_en_reposo(peso: float, altura: float, edad: int, valorGenero: float):
    try:
        alturaCentimetros = altura * 100
        tmb = (10*peso) + (6.25*alturaCentimetros) - (5*edad) + valorGenero
        return round(tmb, 2)
    except Exception as e:
        print(f"Error en el c'alculo decalorias en reposo: {e}")
        return None


def calcular_calorias_en_actividad(peso: float, altura: float, edad: int, valorGenero: float, valorActividad: float):
    try:
        tmb = calcular_calorias_en_reposo(peso, altura, edad, valorGenero)
        if tmb is None:
            return None
        tmbActividad = tmb*valorActividad
        return round(tmbActividad, 2)
    except Exception as e:
        print(f"Error en el calculo de calorias con actividad: {e}")
        return None


def consumo_calorias_recomendado_para_adelgazar(peso: float, altura: float, edad: int, valorGenero: float):
    try:
        tmb = calcular_calorias_en_reposo(peso, altura, edad, valorGenero)
        if tmb is None:
            return "No se pudo calcular el rango de calorias"
        valorMinimo = round(tmb*0.80, 0)
        valorMaximo = round(tmb*0.85, 0)

        mensaje = f"Para adelgazar es recomendado que consumas entre: {int(valorMinimo)} y {int(valorMaximo)} calorias al dia"
        return mensaje
    except Exception as e:
        print(f"Error en el calculo de calorias para adelgazar: {e}")
        return "Error en el calculo"