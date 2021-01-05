segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))
dias = int(segundos/60/60//24)
horas = int((segundos/60//60) - (dias * 24))
minutos = int((segundos//60) - (horas * 60) - (dias * 24 * 60))
segundos = int(segundos - (minutos * 60) - (horas * 60 * 60) - (dias * 24 * 60 * 60))
print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos.")

