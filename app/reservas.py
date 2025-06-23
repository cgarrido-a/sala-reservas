reservas = []

def verificar_disponibilidad(reservas, nueva):
    for r in reservas:
        if r["sala"] == nueva["sala"] and r["hora"] == nueva["hora"]:
            return False
    return True

def reservar(nueva):
    if verificar_disponibilidad(reservas, nueva):
        reservas.append(nueva)
        return {"mensaje": "Reserva creada"}, 200
    else:
        return {"error": "Sala ya reservada a esa hora"}, 409
