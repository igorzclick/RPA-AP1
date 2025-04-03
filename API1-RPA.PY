import time
import pandas as pd
import pyautogui as p

def abrir_navegador():
    p.press('win')
    time.sleep(2)
    p.write('opera')
    time.sleep(5)
    p.press('enter')
    time.sleep(5)

def abrir_site():
    p.write('https://www.impacta.edu.br')
    time.sleep(2)
    p.press('enter')
    time.sleep(5)

def login():
    # Mouse position: (1647, 137)--> posição do mouse no botão de login da home da faculdade
    p.click(x=1647, y=137)  # Clique no campo de login
    time.sleep(2)
    # Mouse position: (956, 447)--> posição do mouse no campo de inserir o RA
    p.click(x=956, y=447) 
    p.write('2303701') #RA
    time.sleep(2)
    p.press('tab')
    time.sleep(2)
    p.write(df.at[17,3])  #SENHA
    time.sleep(2)
    p.press('tab')
    time.sleep(2)
    p.press('tab',presses=5)
    p.press('enter')
    time.sleep(5)  

def logout():
# Mouse position: (1868, 219)--> posição do mouse no botão de logout
    p.click(x=1868, y=219) # Clique no botão de logout
    time.sleep(2)
   
       
# abrir_navegador()
# abrir_site()
# login()       

# arquivo='Tarefas.xslsx'
# if os.path.exists(arquivo):
#     p.alert("arquivo encontrado")
# else:
#     p.alert("arquivo não encontrado")
#     p.alert("crie o arquivo tarefas.csv com as colunas: tarefa, data, hora, status")


df = pd.read_excel('Tarefas.xlsx', engine='openpyxl')
for index, row in df.iterrows():
    if row["Status"] == "Abrir navegador":
        abrir_navegador()
        time.sleep(2)
        index+1
    elif row["Digitar site"] == "Abrir site": 
        abrir_site()
        time.sleep(2)
        index+1
    elif row["Digitar login"] == "Login":
        login()
        time.sleep(2)
        index+1
    elif row["Logout"] == "Logout":
        logout()
        time.sleep(2)
        index+1
    elif pd.isna(index) or index=="":
        p.alert("acabaram as tarefas")
        time.sleep(2)
        break



    

        






