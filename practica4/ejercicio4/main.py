from persona import Persona, Sexo


def main():
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    sexo_input = input("Ingrese el sexo (Mujer/Hombre): ").capitalize()
    sexo = Sexo.MUJER if sexo_input == "Mujer" else Sexo.HOMBRE
    peso = float(input("Ingrese el peso (kg): "))
    altura = float(input("Ingrese la altura (m): "))

    persona1 = Persona(nombre, edad, sexo, peso, altura)
    persona2 = Persona(nombre, edad, sexo)
    persona3 = Persona()

    persona3.set_nombre("Por Defecto")
    persona3.set_edad(30)
    persona3.set_sexo(Sexo.HOMBRE)
    persona3.set_peso(70)
    persona3.set_altura(1.75)

    personas = [persona1, persona2, persona3]

    for i, persona in enumerate(personas, start=1):
        imc_resultado = persona.valorarPesoCorporal()
        estado_peso = "por debajo del peso ideal" if imc_resultado == -1 else (
            "en el peso ideal" if imc_resultado == 0 else "con sobrepeso")
        mayor_edad = "es mayor de edad" if persona.esMayorDeEdad() else "no es mayor de edad"

        print(f"\nInformación de Persona {i}:")
        print(persona)
        print(f"Estado de peso: {estado_peso}")
        print(f"Mayoría de edad: {mayor_edad}")


if __name__ == "__main__":
    main()
