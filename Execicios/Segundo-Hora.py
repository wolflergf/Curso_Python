print('****************************')
print('Transformar Segundos em Hora')
print('****************************')
segundos_digitados = float(input('Digite os segundo para transformar em horas: '))
hora = segundos_digitados / 3600
minutos = (segundos_digitados % 3600) / 60
segundos = (segundos_digitados % 3600) % 60

print('Os {} digitados equivalem a {:.0f}h, {:.0f}min, e {:.0f}'.format(segundos_digitados, hora, minutos, segundos))
