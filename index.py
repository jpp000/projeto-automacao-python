import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press('win')

pyautogui.write("chrome")

pyautogui.press('enter')
 

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(link)
pyautogui.press('enter')

time.sleep(3)

pyautogui.click(x=741, y=380)

pyautogui.write("email")
pyautogui.press('tab')

pyautogui.write('senha')   
pyautogui.press('tab')

pyautogui.press('enter')

time.sleep(2)
pyautogui.press('enter')

import pandas

tabela = pandas.read_csv('produtos.csv')

pyautogui.click(x=688, y=257)

for linha in tabela.index:

   pyautogui.write(tabela.loc[linha, 'codigo'])
   pyautogui.press('tab')

   pyautogui.write(tabela.loc[linha,'marca'])
   pyautogui.press('tab')

   pyautogui.write(tabela.loc[linha, 'tipo'])
   pyautogui.press('tab')

   pyautogui.write(str(tabela.loc[linha, 'categoria']))
   pyautogui.press('tab')

   pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
   pyautogui.press('tab')

   pyautogui.write(str(tabela.loc[linha, 'custo']))
   pyautogui.press('tab')

   # se ele nao tiver nenhuma obs deve continuar o codigo
   obs = tabela.loc[linha, 'obs']
   
   if not pandas.isna(obs):
      pyautogui.write(str(obs))
      pyautogui.press('tab')
      pyautogui.press('enter')

   pyautogui.press('tab')
   pyautogui.press('enter')   

   pyautogui.scroll(5000)

   pyautogui.click(x=688, y=257)




