import yfinance as yf
import pyautogui
import pyperclip
import webbrowser
import time

ticker = input('Digite o código da ação: ')
dt_inicio = input('Digite a data de início (aaaa-mm-dd): ')
dt_fim = input('Digite a data de fim (aaaa-mm-dd): ')

dados = yf.Ticker(ticker)
tabela = dados.history(start=dt_inicio, end=dt_fim)
fechamento = tabela.Close
maxima = round(fechamento.max(), 2)
minimo = round(fechamento.min(), 2)
media = round(fechamento.mean(), 2)
atual = round(fechamento[-1], 2)

destinatario = "felipecsantos.pt@gmail.com"
assunto = "Análise diária"

mensagem = f"""
Bom dia,

Segue abaixo as análises da ação {ticker} do período de {dt_inicio} a {dt_fim}:

Cotação máxima: R${maxima}
Cotação mínima: R${minimo}
Cotação atual: R${atual}
Valor médio: R${media}

Qualquer dúvida estou à disposição.

Atenciosamente.
"""

# abrir o navegador e acessar o site do gmail
webbrowser.open("https://www.gmail.com/")
time.sleep(3)

# configurando uma pause de 3 segundos
pyautogui.PAUSE = 3

#click no botão de escrever
pyautogui.click(x=83, y=160)

# digitar o email do destinatário e teclar tab
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")


# digitar o assunto do email e teclar tab
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# digitar a mensagem do email
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

# clicar no botão de enviar
pyautogui.click(x=2826, y=1356)

# Fechar a aba do navegador
pyautogui.hotkey("ctrl", "f4")

print('E-mail enviado com sucesso!')