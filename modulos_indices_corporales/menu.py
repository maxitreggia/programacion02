from consola_calculo_imc import calculo_imc
from consola_calculo_porcentaje_grasa import calculo_porcentaje_grasa
from consola_calculo_calorias_reposo import calculo_calorias_en_reposo
from consola_calculo_calorias_actividad import calculo_calorias_en_actividad
from consola_calculo_adelgazar import calculo_consumo_recomendado_para_adelgazar


def main():
    while True:
        try:
            menu = int(input(f"Que desea calcular:"
                             "\n1. Calcular IMC"
                             "\n2. Calcular Porcentaje de grasa corporal"
                             "\n3. Calcular Calorias en reposo"
                             "\n4. Calcular Calorias en actividad"
                             "\n5. Calcular consumo recomendado para adelgazar"
                             "\n6. Salir"
                             "\nIngrese una opcion:"))
            match menu:
                case 1:
                    calculo_imc()
                case 2:
                    calculo_porcentaje_grasa()
                case 3:
                    calculo_calorias_en_reposo()
                case 4:
                    calculo_calorias_en_actividad()
                case 5:
                    calculo_consumo_recomendado_para_adelgazar()
                case 6:
                    print("Saliendo...")
                    break
                case _:
                    print("Opción no válida. Por favor, ingrese una opción del 1 al 6.")
        except ValueError:
            print("Error: Ingrese un número válido para la opción.")


if __name__ == '__main__':
    main()
