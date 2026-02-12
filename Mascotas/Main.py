# ===============================
# ASISTENTE INTELIGENTE DE MASCOTAS
# Nivel: Medio
# ===============================

BASE_CONOCIMIENTO = {
    "perro": {
        "no come": {
            "consejo": [
                "Verifica si cambiaste recientemente el alimento.",
                "Evita darle restos de comida humana.",
                "Asegúrate de que tenga agua fresca siempre.",
                "Revisa si hay vómitos o diarrea.",
                "Mantén horarios fijos de comida."
            ],
            "grave": "Si no come por más de 24 horas o está decaído, acude al veterinario."
        },
        "se rasca": {
            "consejo": [
                "Revisa pulgas, garrapatas o enrojecimiento.",
                "Lava su cama y mantas semanalmente.",
                "Evita bañarlo en exceso.",
                "Cambia el champú por uno hipoalergénico.",
                "Aspira la casa con frecuencia."
            ],
            "grave": "Si hay heridas, sangrado o pérdida de pelo, consulta al veterinario."
        },
        "triste": {
            "consejo": [
                "Aumenta el tiempo de paseo diario.",
                "Estimúlalo con juegos mentales.",
                "Evita dejarlo solo por largos períodos.",
                "Mantén una rutina estable.",
                "Observa si duerme más de lo normal."
            ],
            "grave": "Si dura más de 48 horas, podría indicar enfermedad."
        },
        "ladra mucho": {
            "consejo": [
                "Identifica si ladra por aburrimiento o miedo.",
                "Proporciónale ejercicio diario.",
                "Evita gritarle cuando ladra.",
                "Refuerza el silencio con premios.",
                "Bloquea estímulos externos si es necesario."
            ],
            "grave": "Ladridos excesivos repentinos pueden indicar estrés o dolor."
        },
        "hace necesidades en casa": {
            "consejo": [
                "Saca a tu perro a la misma hora todos los días.",
                "Limpia bien el área para eliminar olores.",
                "Refuerza con premios cuando lo haga bien.",
                "Evita castigos físicos.",
                "Reduce el acceso a zonas problemáticas."
            ],
            "grave": "Si ya estaba entrenado y cambió de repente, consulta al veterinario."
        },

        # ✅ PROBLEMA NUEVO
        "vomita": {
            "consejo": [
                "Retira la comida por 8–12 horas (no el agua).",
                "Evita que coma basura o restos.",
                "Dale pequeñas cantidades de agua.",
                "Observa si el vómito tiene espuma, sangre o color amarillo.",
                "Reintroduce comida blanda poco a poco (arroz y pollo sin sal)."
            ],
            "grave": "Si vomita varias veces, hay sangre o está decaído, acude al veterinario."
        }
    },

    "gato": {
        "no come": {
            "consejo": [
                "Mantén el plato limpio y lejos del arenero.",
                "Evita cambios bruscos de alimento.",
                "Sirve la comida a temperatura ambiente.",
                "Reduce ruidos durante la comida.",
                "Observa si hay bolas de pelo."
            ],
            "grave": "Un gato sin comer más de 24h es una urgencia veterinaria."
        },
        "se rasca": {
            "consejo": [
                "Revisa pulgas o irritaciones.",
                "Cambia la arena si es perfumada.",
                "Cepíllalo regularmente.",
                "Lava mantas y camas.",
                "Evita productos fuertes de limpieza."
            ],
            "grave": "Si hay costras, heridas o caída de pelo, ve al veterinario."
        },
        "agresivo": {
            "consejo": [
                "Respeta su espacio personal.",
                "Evita tocarlo cuando está alterado.",
                "Usa juguetes para liberar energía.",
                "Mantén rutinas estables.",
                "Proporciónale escondites seguros."
            ],
            "grave": "Agresividad repentina puede indicar dolor o enfermedad."
        },
        "maulla mucho": {
            "consejo": [
                "Revisa si tiene hambre o sed.",
                "Asegúrate de que el arenero esté limpio.",
                "Juega con él antes de dormir.",
                "No refuerces el maullido con atención inmediata.",
                "Verifica si busca aparearse."
            ],
            "grave": "Maullidos excesivos y repentinos pueden indicar malestar."
        },

        # ✅ PROBLEMA NUEVO
        "orina fuera del arenero": {
            "consejo": [
                "Limpia el arenero todos los días.",
                "Coloca el arenero en un lugar tranquilo.",
                "Evita arenas perfumadas.",
                "Ten un arenero por gato + uno extra.",
                "Reduce el estrés (cambios, visitas, ruidos)."
            ],
            "grave": "Si orina poco, con dolor o hay cambios repentinos, puede ser una urgencia urinaria."
        }
    }
}


def mostrar_problemas(mascota):
    print("\nProblemas disponibles:")
    for problema in BASE_CONOCIMIENTO[mascota]:
        print(f"- {problema}")


def obtener_recomendacion(mascota, problema):
    datos = BASE_CONOCIMIENTO[mascota][problema]

    print("\n📌 Recomendaciones:")
    for consejo in datos["consejo"]:
        print(f"✔ {consejo}")

    print("\n⚠ Advertencia:")
    print(datos["grave"])


def asistente_mascotas():
    print("🐾 ASISTENTE INTELIGENTE PARA MASCOTAS 🐾\n")

    mascota = input("¿Qué mascota tienes? (perro/gato): ").lower()

    if mascota not in BASE_CONOCIMIENTO:
        print("❌ Mascota no soportada.")
        return

    mostrar_problemas(mascota)

    problema = input("\nEscribe el problema exactamente como aparece arriba: ").lower()

    if problema not in BASE_CONOCIMIENTO[mascota]:
        print("❌ Problema no registrado.")
        return

    obtener_recomendacion(mascota, problema)

    print("\n❤️ Gracias por cuidar de tu mascota.")


# Ejecutar
asistente_mascotas()
