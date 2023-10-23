import os
import random
import sys

if len(sys.argv) != 2:
    print("Usage: python3 bot.py [1-6]")
    sys.exit(1)

input_arg = sys.argv[1]

try:
    input_arg = int(input_arg)
    if input_arg < 1 or input_arg > 6:
        print("Error: solo se puede establecer de 1 a 6 horas, aplicando cambios automáticos...")
        print("Inicie de nuevo el código")
        sys.exit(1)
except ValueError:
    print("Error: Ingrese un número válido del 1 al 6")
    sys.exit(1)

horas = [60, 120, 180, 240, 300, 360]
hora = horas[input_arg - 1]

with open('.github/workflows/MirrorSC.yml', 'r') as file:
    file_data = file.read()

file_data = file_data.replace('hori', str(hora))
file_data = file_data.replace('horo', str(input_arg))

with open('.github/workflows/MirrorSC.yml', 'w') as file:
    file.write(file_data)

os.system('git add -f .')
commit_message = f"Activando: {input_arg} horas, número de activación: {random.randint(1, 1000)}"
os.system(f'git commit -m "{commit_message}"')
os.system('git push')

os.remove('.github/workflows/MirrorSC.yml')
os.system('cp .github/MirrorSCb.yml .github/workflows/MirrorSC.yml')
