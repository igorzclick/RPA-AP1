import time
import pandas as pd
import pyautogui as p
import openpyxl
import re

# Funções auxiliares
def esperar(valor):
    print(f"Aguardando {valor} segundos...")
    time.sleep(int(valor))

def pressionar_tecla(tecla):
    if "tab" in tecla.lower():
        match = re.search(r"(\d+)", tecla)
        if match:
            vezes = int(match.group(1))
            print(f"Pressionando TAB {vezes} vezes")
            p.press('tab', presses=vezes,interval=0.56)
    else:
        print(f"Pressionando tecla: {tecla}")
        p.press(tecla)
        time.sleep(2)

def digitar_texto(texto):
    print(f"Digitando: {texto}")
    p.write(str(texto))
    time.sleep(1)

# Lê a planilha
arquivo = r'C:\Users\Igor\Desktop\RPA\RPA-AP1\Tarefas.xlsx'
df = pd.read_excel(arquivo, engine='openpyxl')

# Itera pelas tarefas
for _, row in df.iterrows():                        

    tarefa = str(row["Tarefa"]).strip().lower()
    tipo = str(row["Tipo"]).strip()
    data = str(row["Dado"]).strip()
    
    print(f"Executando tarefa: {tarefa}")

    if tipo.lower() == "espera":
        esperar(data)
        
    elif tipo.lower() == "tecla":
        pressionar_tecla(data)

    elif tipo.lower() == "texto":
        digitar_texto(data)

p.alert("Automação finalizada.")