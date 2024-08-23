from SUBPROGRAMS.parameters import *
from SUBPROGRAMS.functions import *
from clicknium import locator, ui
from clicknium import clicknium as cc
import time
import subprocess
import pyautogui
from datetime import datetime, timedelta
import re
import pygetwindow as gw
import os
import pyperclip
'''
windows = gw.getWindowsWithTitle(title='TOTVS Linha RM - Construção e Projetos  Alias: CorporeRM | 1-OCEANICA ENGENHARIA E CONSULTORIA S.A.')
print(windows)
if windows:
    window=windows[0]
    window.activate()
    window.maximize()

time.sleep(5)
pyautogui.press('down')
print('PRESS BUTTON DOWN')
time.sleep(2)

time.sleep(5)
pyautogui.hotkey('ctrl', 'enter')
print('PRESS BUTTON DOWN')
time.sleep(2)
'''

'''
click_combo = cc.wait_appear(locator.rm.combobox_lancamento, wait_timeout=15)
click_combo.click()
logging.debug('CLICA PARA APARECER CONTA/CAIXA')

select_conta_caixa = cc.wait_appear(locator.rm.listitem_contacaixa, wait_timeout=15)
select_conta_caixa.click()
logging.debug('CLICA PARA APARECER CONTA/CAIXA')

select_conta_caixa = cc.wait_appear(locator.rm.button_contavalor, wait_timeout=15)
select_conta_caixa.click()
logging.debug('CLICA NO BOTÃO [...]')

select_field_search = cc.wait_appear(locator.rm.edit_tbxsearch, wait_timeout=15)
select_field_search.click()
pyautogui.write('%3212')
logging.debug('CLICA NO CAMPO PESQUISA E DIGITA: %3212')

filter_search = cc.wait_appear(locator.rm.button_btnfilter, wait_timeout=15)
filter_search.click()
logging.debug('CLICA NO BOTÃO DO FILTRO')

btn_ok_contacaixa = cc.wait_appear(locator.rm.button_ok_contacaixa, wait_timeout=15)
btn_ok_contacaixa.click()
logging.debug('CLICA NO BOTÃO OK')

btn_executar = cc.wait_appear(locator.rm.button_executar, wait_timeout=15)
btn_executar.click()
logging.debug('CLICA NO BOTÃO EXECUTAR')


avancar_3 = cc.wait_appear(locator.rm.button_remessas_avancar_3, wait_timeout=15)
avancar_3.click()
logging.debug('CLICA EM AVANCAR PARA CONCLUIR')

execute_processo_pagamento = cc.wait_appear(locator.rm.button_exec_processo_pag, wait_timeout=15)
execute_processo_pagamento.double_click()
logging.debug('CLICA EM AVANCAR PARA CONCLUIR')






exec_success_process = waitForImage(image = exec_sucesso, timeout=600, name = 'PRESS BUTTON OK')
if exec_success_process is not None:
    time.sleep(2)
    logging.debug('O PROCESSAMENTO DE AUTORIZAÇÃO DO BORDERO FOI EXECUTADO COM SUCESSO.')
    time.sleep(2)
    btn_exec_fechar = cc.wait_appear(locator.rm.button_fechar_bordero_autorizacao, wait_timeout=600)
    btn_exec_fechar.click()
    logging.debug('CLICK EM FECHAR.')
    time.sleep(2)


message_erro = cc.wait_appear(locator.rm.edit_textboxlog, wait_timeout=15)
erro_inclusao_bordero = message_erro.get_text()
logging.debug(f'{erro_inclusao_bordero}')
numeros = re.findall(r'1-(\d+)', erro_inclusao_bordero)
ref_lanca = []

for numero in numeros:
    ref_lanca.append(numero)


filter_ref_pag = cc.wait_appear(locator.rm.edit_cod_cliente_fornece, wait_timeout=15)
filter_ref_pag.hover(5)
logging.debug('HOVER FILTER REF PAG')

time.sleep(2)
pyautogui.click(381,308)

time.sleep(2)
pyautogui.press('down')

time.sleep(2)
pyautogui.write('(Personalizar)')

time.sleep(2)
pyautogui.press('enter')

time.sleep(2)
pyautogui.write('Não é igual a')

time.sleep(2)
pyautogui.press('tab')

time.sleep(2)
pyautogui.press('enter')

time.sleep(2)
pyautogui.press('enter')

'''




'''
select_first_row = cc.wait_appear(locator.rm.dataitem_coligada_do_convenio_row0, wait_timeout=15)
if select_first_row is not None:
    select_first_row.click()
    logging.debug('CLICK NA PRIMEIRA LINHA DA TABELA MOVIMENTAÇÃO BANCÁRIA') 

    filter_status_remessa = cc.wait_appear(locator.rm.header_status_da_remessa_pagamento, wait_timeout=15)
    filter_status_remessa.hover(5)
    logging.debug('HOVER FILTER')

    posição = filter_status_remessa.get_position()
    x, y = posição.Right - 5 , posição.Top + 5
    pyautogui.moveTo(x,y)
    pyautogui.click()

    logging.debug('CLICK FILTER')
    time.sleep(2)
    pyautogui.press('down')
    time.sleep(1)
    pyautogui.typewrite('(Personalizar)')
    time.sleep(1)
    pyautogui.press('enter')
    logging.debug('CLICK NO FILTRO  STATUS DA REMESSA')
    time.sleep(2)
    pyautogui.press('tab')
    logging.debug('APERTA TAB PARA ESCREVER O FILTRO')
    time.sleep(2)
    pyautogui.write('Autorizado')
    logging.debug('ESCREVE AUTORIZADO NO FILTRO')
    time.sleep(2)
    pyautogui.press('enter')
    logging.debug('APERTA ENTER PARA SELECIONAR OS AUTORIZADO')
    time.sleep(2)

    select_first_row = cc.wait_appear(locator.rm.dataitem_coligada_do_convenio_row0, wait_timeout=15)
    if select_first_row is not None:

        for i in range(6):
            pyautogui.hotkey('left')
        logging.debug('6 PASSOS PARA ESQUERDA NA TABELA <<')

        check_user_bot()
    else:
        logging.debug('SEM REMESSA DE BORDERO AUTORIZADO')

else:
    select_first_row2 = cc.wait_appear(locator.rm.dataitem_coligada_row0, wait_timeout=15)
    if select_first_row2 is not None:
        select_first_row2.click()

        for i in range(12):
            pyautogui.hotkey('right')
        logging.debug('12 PASSOS PARA ESQUERDA NA TABELA >>')

        filter_status_remessa = cc.wait_appear(locator.rm.header_status_da_remessa_pagamento, wait_timeout=300)
        filter_status_remessa.hover(5)
        logging.debug('HOVER FILTER')

        # BUSCANDO O FILTRO A PARTIR DA POSIÇÃO DO ELEMENTO
        posição = filter_status_remessa.get_position()
        x, y = posição.Right - 5 , posição.Top + 5
        pyautogui.moveTo(x,y)
        pyautogui.click()

        logging.debug('CLICK FILTER')
        time.sleep(2)
        pyautogui.press('down')
        time.sleep(1)
        pyautogui.typewrite('(Personalizar)')
        time.sleep(1)
        pyautogui.press('enter')
        logging.debug('CLICA NO FILTRO  STATUS DA REMESSA')
        time.sleep(2)
        pyautogui.press('tab')
        logging.debug('APERTA TAB PARA ESCREVER O FILTRO')
        time.sleep(2)
        pyautogui.write('Autorizado')
        logging.debug('ESCREVE AUTORIZADO NO FILTRO')
        time.sleep(2)
        pyautogui.press('enter')
        logging.debug('APERTA ENTER PARA SELECIONAR OS AUTORIZADOS')
        time.sleep(5)

        select_first_row = cc.wait_appear(locator.rm.dataitem_coligada_do_convenio_row0, wait_timeout=15)
        if select_first_row is not None:

            for i in range(6):
                pyautogui.hotkey('left')
            logging.debug('6 PASSOS PARA ESQUERDA NA TABELA <<')

            check_user_bot()
        else:
            logging.debug('SEM REMESSA DE BORDERO AUTORIZADO')

    else:
        logging.debug('SEM REMESSA DE BORDERO AUTORIZADO')
        '''


'''
button_prog_exec = cc.wait_appear(locator.rm.button_progresso_da_execução_dos_processos, wait_timeout=360)
button_prog_exec.click()
logging.debug('SELECIONA PROCESSO DA EXECUCAO DOS PROGRESSOS ABA INFERIOR')

get_txt_msg = cc.wait_appear(locator.rm.edit_txmessage_desbloqueio, wait_timeout=60)
txt_msg = get_txt_msg.get_text()
logging.debug(f'MSG AQUI: {txt_msg}')

if txt_msg == '':
    logging.debug('DESBLOQUEIO COM SUCESSO') 
    time.sleep(2)
    click_appear = cc.wait_appear(locator.rm.titlebar_progresso_da_execução_dos_processos, wait_timeout=60)
    click_appear.click()
    logging.debug('SELECIONAR EVIDENCIAR ABA INFERIOR')
    time.sleep(2)
    pyautogui.press('esc')
    logging.debug('FECHANDO ABA INFERIOR')

else:
    logging.debug('DESBLOQUEIO COM ERROR')
    time.sleep(2)
    click_appear = cc.wait_appear(locator.rm.titlebar_progresso_da_execução_dos_processos, wait_timeout=60)
    click_appear.click()
    logging.debug('EVIDENCIAR ABA INFERIOR')
    time.sleep(2)
    pyautogui.press('esc')
    logging.debug('FECHANDO ABA INFERIOR')'''



'''texto = cc.wait_appear(locator.rm.button_116, wait_timeout=15)
txt_extraido = texto.get_text()
logging.debug(f'Texto extraido{txt_extraido}')
resultado = re.search(r"/(\d+)", txt_extraido)
count = int(resultado.group(1))
logging.debug(f'Count {count}')
logging.debug(f'Type {type(count)}')'''


open_RM()
loggin_RM()