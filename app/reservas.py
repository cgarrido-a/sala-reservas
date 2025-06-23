def reservar(nueva):
    if verificar_disponibilidad(reservas, nueva):
        reservas.append(nueva)
        return {"mensaje": "Reserva creada"}, 200
    else:
        return {"error": "Sala ya reservada a esa hora"}, 409
