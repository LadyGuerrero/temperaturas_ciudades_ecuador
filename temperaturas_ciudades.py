# Definición de la estructura de datos 3D: [ciudades][semanas][días]
temperaturas = [
    # Ciudad 1 - Guayaquil
    [
        # Semana 1
        [
            {"day": "Lunes", "temp": 88},
            {"day": "Martes", "temp": 90},
            {"day": "Miércoles", "temp": 91},
            {"day": "Jueves", "temp": 89},
            {"day": "Viernes", "temp": 92},
            {"day": "Sábado", "temp": 93},
            {"day": "Domingo", "temp": 91}
        ],
        # Semana 2
        [
            {"day": "Lunes", "temp": 89},
            {"day": "Martes", "temp": 91},
            {"day": "Miércoles", "temp": 92},
            {"day": "Jueves", "temp": 90},
            {"day": "Viernes", "temp": 93},
            {"day": "Sábado", "temp": 94},
            {"day": "Domingo", "temp": 92}
        ],
        # Semana 3
        [
            {"day": "Lunes", "temp": 87},
            {"day": "Martes", "temp": 89},
            {"day": "Miércoles", "temp": 91},
            {"day": "Jueves", "temp": 92},
            {"day": "Viernes", "temp": 94},
            {"day": "Sábado", "temp": 93},
            {"day": "Domingo", "temp": 91}
        ],
        # Semana 4
        [
            {"day": "Lunes", "temp": 88},
            {"day": "Martes", "temp": 90},
            {"day": "Miércoles", "temp": 92},
            {"day": "Jueves", "temp": 91},
            {"day": "Viernes", "temp": 93},
            {"day": "Sábado", "temp": 92},
            {"day": "Domingo", "temp": 90}
        ]
    ],
    # Ciudad 2 - Quito
    [
        # Semana 1
        [
            {"day": "Lunes", "temp": 65},
            {"day": "Martes", "temp": 68},
            {"day": "Miércoles", "temp": 67},
            {"day": "Jueves", "temp": 66},
            {"day": "Viernes", "temp": 70},
            {"day": "Sábado", "temp": 69},
            {"day": "Domingo", "temp": 67}
        ],
        # Semana 2
        [
            {"day": "Lunes", "temp": 64},
            {"day": "Martes", "temp": 66},
            {"day": "Miércoles", "temp": 68},
            {"day": "Jueves", "temp": 67},
            {"day": "Viernes", "temp": 69},
            {"day": "Sábado", "temp": 70},
            {"day": "Domingo", "temp": 68}
        ],
        # Semana 3
        [
            {"day": "Lunes", "temp": 66},
            {"day": "Martes", "temp": 68},
            {"day": "Miércoles", "temp": 70},
            {"day": "Jueves", "temp": 69},
            {"day": "Viernes", "temp": 71},
            {"day": "Sábado", "temp": 70},
            {"day": "Domingo", "temp": 67}
        ],
        # Semana 4
        [
            {"day": "Lunes", "temp": 65},
            {"day": "Martes", "temp": 67},
            {"day": "Miércoles", "temp": 68},
            {"day": "Jueves", "temp": 66},
            {"day": "Viernes", "temp": 69},
            {"day": "Sábado", "temp": 68},
            {"day": "Domingo", "temp": 66}
        ]
    ],
    # Ciudad 3 - Cuenca
    [
        # Semana 1
        [
            {"day": "Lunes", "temp": 67},
            {"day": "Martes", "temp": 69},
            {"day": "Miércoles", "temp": 71},
            {"day": "Jueves", "temp": 70},
            {"day": "Viernes", "temp": 72},
            {"day": "Sábado", "temp": 71},
            {"day": "Domingo", "temp": 68}
        ],
        # Semana 2
        [
            {"day": "Lunes", "temp": 68},
            {"day": "Martes", "temp": 70},
            {"day": "Miércoles", "temp": 72},
            {"day": "Jueves", "temp": 71},
            {"day": "Viernes", "temp": 73},
            {"day": "Sábado", "temp": 72},
            {"day": "Domingo", "temp": 69}
        ],
        # Semana 3
        [
            {"day": "Lunes", "temp": 65},
            {"day": "Martes", "temp": 67},
            {"day": "Miércoles", "temp": 69},
            {"day": "Jueves", "temp": 68},
            {"day": "Viernes", "temp": 70},
            {"day": "Sábado", "temp": 69},
            {"day": "Domingo", "temp": 66}
        ],
        # Semana 4
        [
            {"day": "Lunes", "temp": 66},
            {"day": "Martes", "temp": 68},
            {"day": "Miércoles", "temp": 70},
            {"day": "Jueves", "temp": 69},
            {"day": "Viernes", "temp": 71},
            {"day": "Sábado", "temp": 70},
            {"day": "Domingo", "temp": 67}
        ]
    ]
]

# Nombres de las ciudades
ciudades = ["Guayaquil", "Quito", "Cuenca"]

# Iteración con bucles anidados para calcular promedios
print("ANÁLISIS DE TEMPERATURAS POR CIUDAD Y SEMANA")
print("============================================")

for ciudad_idx, ciudad_data in enumerate(temperaturas):
    print(f"\nCIUDAD: {ciudades[ciudad_idx]}")
    print("-" * 40)

    # Para almacenar todos los promedios de esta ciudad
    promedios_ciudad = []

    for semana_idx, semana_data in enumerate(ciudad_data):
        # Extraer solo las temperaturas de cada diccionario en la semana
        temperaturas_semana = [dia["temp"] for dia in semana_data]
        suma_temperaturas = sum(temperaturas_semana)
        promedio = suma_temperaturas / len(semana_data)
        promedios_ciudad.append(promedio)

        # Imprimir el promedio semanal redondeado a 1 decimal
        print(f"Semana {semana_idx + 1}: Promedio = {promedio:.1f}°F")

        # Imprimir detalles de cada día
        for dia in semana_data:
            print(f"  - {dia['day']}: {dia['temp']}°F")

    # Calcular y mostrar el promedio general de la ciudad
    promedio_ciudad = sum(promedios_ciudad) / len(promedios_ciudad)
    print(f"\nPromedio general de {ciudades[ciudad_idx]}: {promedio_ciudad:.1f}°F")

print("\nANÁLISIS COMPLETADO")

