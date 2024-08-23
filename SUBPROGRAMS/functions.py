from SUBPROGRAMS.parameters import *
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
from SUBPROGRAMS.parameters import *


def bot_text_art():
    logging.info("    ____   ")
    logging.info("   [____]    ")
    logging.info(" |=]()()[=|  ")
    logging.info("   _\==/__    _____    ____     _        _____    ___   _  __")
    logging.info(" |__|   |_|  |  _  \  / ___|   | |      |_   _| / ___| | |/ /")
    logging.info(" |_|_/\_|_|  | |  | | | |      | |        | |   | |    | ' / ")
    logging.info(" | | __ | |  | |  | | | |      | |        | |   | |    |  <  ")
    logging.info(" |_|[  ]|_|  | |__| | | |____  | |____   _| |_  | |__  | . \ ")
    logging.info(" \_|_||_|_/  |_____/   \_____| |______| |_____| \ ___| |_|\_\\")
    logging.info("   |_||_|                                                     ")
    logging.info("   | ||_|_   ")
    logging.info(" |___||___|  ")	
    logging.info("             ")

def encerrar_processo_windows(nome_processo):
    try:
        # Executar o comando taskkill para encerrar o processo pelo nome
        subprocess.run(['taskkill', '/f', '/im', nome_processo], check=True)
        print(f'Processo {nome_processo} encerrado forçosamente.')
    except subprocess.CalledProcessError as e:
        print(f'Erro ao encerrar o processo {nome_processo}: {e}')

def show_exception_and_exit(exc_type, exc_value, tb):

    # https:/www.youtube.com/watch?v=8MjfalI4AO8
    # traceback.print_exception(exc_type, exc_value, tb)
    logging.error(exc_value, exc_info=(exc_type, exc_value, tb))

    result = datetime.now().strftime('%Y_%m_%d %H_%M')
    erro_print = f'ERRO {result}'

    screenshot = pyautogui.screenshot()
    screenshot.save(f"{print_path}\\{erro_print}.png")
    logging.debug(f'PRINT SALVO')
    
    #processo_inicio.terminate()
    encerrar_processo_windows(nome_processo)
    logging.debug(f'RM FECHADO')

    with open(f'{email_path}/emailError.html', 'r', encoding='utf-8') as fileError:
        templateError = fileError.read()
        htmlError = templateError.format(mensagem=exc_value)
        
    yag.send(to=email_receivers.split(','), subject=f"ERRO - BOT REMESSAS FÉRIAS / RECISÃO",
    contents=htmlError,
    attachments=[f'{log_path}/{today}/{log_file_name}.log',f'{print_path}/{erro_print}.png'])
    logging.debug(f'EMAIL EXCEÇÃO ENVIADO')

    logging.debug(f'ERRO - {exc_type} / {exc_value}')
    sys.exit(-1)

def open_RM():
    global processo_inicio
    # Substitua 'nome_do_programa' pelo nome ou caminho do programa que você deseja abrir
    programa = 'C:\Totvs\RM.NET\RM.exe'

    # Tente abrir o programa
    try:
        processo_inicio = subprocess.Popen(programa)
        logging.debug('OPEN PROGRAM RM')
    except FileNotFoundError:
        logging.debug('PROGRAM NOT FOUND')
    except Exception as e:
        logging.debug(f'ERROR WHEN OPENING PROGRAM RM {e}')


def loggin_RM():
    cc.wait_appear(locator.rm.pane_picturebox1, wait_timeout=300)

    user_rm = cc.wait_appear(locator.rm.user_field, wait_timeout=15)
    user_rm.double_click()
    time.sleep(2)
    user_rm.send_hotkey(f'{user}')
    logging.debug('ENTRAR USER_NAME')
    pass_rm = cc.wait_appear(locator.rm.pass_field, wait_timeout=15)
    pass_rm.click()
    time.sleep(2)
    pyautogui.typewrite(fr'{password}')
    logging.debug('ENTRAR PASSWORD')
    click_button = cc.wait_appear(locator.rm.button_entrar, wait_timeout=15)
    click_button.click()
    logging.debug('ENTRAR RM')

    flag1 = False
    flag2 = False

    for _ in range(3):
        click_filter = cc.wait_appear(locator.rm.titlebar_titlebar, wait_timeout=30)
        if click_filter is not None:
            click_filter.click()
            time.sleep(2)
            pyautogui.hotkey('esc')
            
            logging.debug('FILTRO ENCONTRADO')

            pyautogui.hotkey('ctrl', 'w')
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'w')
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'w')

            '''flag1 = True
            else:
            logging.debug('FILTRO NÃO ENCONTRADO')'''

            click_filter2 = cc.wait_appear(locator.rm.titlebar_titlebar2, wait_timeout=30)
            if click_filter2 is not None:
                click_filter2.click()
                time.sleep(2)
                pyautogui.hotkey('esc')
                logging.debug('FILTRO ENCONTRADO DE INICIO')

                pyautogui.hotkey('ctrl', 'w')
                time.sleep(2)
                pyautogui.hotkey('ctrl', 'w')
                time.sleep(2)
                pyautogui.hotkey('ctrl', 'w')

                break

            '''flag2 = True

            else:
                logging.debug('FILTRO 2 NÃO ENCONTRADO DE INICIO')

            if flag1 and flag2:
                break'''

        else:
            click_filter = cc.wait_appear(locator.rm.titlebar_titlebar2, wait_timeout=30)
            if click_filter is not None:
                click_filter.click()
                time.sleep(2)
                pyautogui.hotkey('esc')
                
                logging.debug('FILTRO ENCONTRADO')

                pyautogui.hotkey('ctrl', 'w')
                time.sleep(2)
                pyautogui.hotkey('ctrl', 'w')
                time.sleep(2)
                pyautogui.hotkey('ctrl', 'w')

                '''flag1 = True
                else:
                logging.debug('FILTRO NÃO ENCONTRADO')'''

                click_filter2 = cc.wait_appear(locator.rm.titlebar_titlebar, wait_timeout=30)
                if click_filter2 is not None:
                    click_filter2.click()
                    time.sleep(2)
                    pyautogui.hotkey('esc')
                    logging.debug('FILTRO ENCONTRADO DE INICIO')

                    pyautogui.hotkey('ctrl', 'w')
                    time.sleep(2)
                    pyautogui.hotkey('ctrl', 'w')
                    time.sleep(2)
                    pyautogui.hotkey('ctrl', 'w')

                    break
            

    
   


def enter_coligada():

    '''click_context = cc.wait_appear(locator.rm.click_contexto, wait_timeout=300)
    click_context.click()
    logging.debug('CLICK CONTEXTO')'''

    for i in range(7):
        logging.debug(f'AGUARDANDO {i+1}')
        try:
            click_context = cc.wait_appear(locator.rm.click_contexto, wait_timeout=150)
            click_context.click()
            logging.debug('CLICK CONTEXTO')
            break

        except:
            pyautogui.hotkey('up')
            logging.debug('apertou up')
            if i == 7:
                click_context = cc.wait_appear(locator.rm.click_contexto, wait_timeout=150)
                click_context.click()
                logging.debug('CLICK CONTEXTO')

    click_alterar_contexto = cc.wait_appear(locator.rm.menuitem_alterar_contexto_do_módulo, wait_timeout=15)
    click_alterar_contexto.click()
    logging.debug('CLICK ALTERAR MODULO DO CONTEXTO')
    click_colig_cod = cc.wait_appear(locator.rm.edit_coligada_code, wait_timeout=60)
    click_colig_cod.click()
    click_colig_cod.set_text('1')
    logging.debug('INSERE O COLIGADA CODE = 1')
    pyautogui.press('tab')
    logging.debug('APERTA TAB PARA PREENCHER O CAMPO COM A STRING: OCEANICA ENGENHARIA E CONSULTORIA S.A.')
    click_avancar_final = cc.wait_appear(locator.rm.button_bavancar1, wait_timeout=15)
    click_avancar_final.click()
    logging.debug('CLICK AVANÇAR NOVAMENTE')
    click_concluir = cc.wait_appear(locator.rm.button_concluir, wait_timeout=15)
    click_concluir.click()
    logging.debug('CLICK CONCLUIR')

    troca = waitForImage(image = troca_coligada, timeout=20, name = 'TROCA COLIGADA')
    if troca is not None:
        logging.info('TROCA COLIGADA')
        pyautogui.click(troca)
        time.sleep(1)
        pyautogui.hotkey(f'enter')

    click_concluir = cc.wait_disappear(locator.rm.button_concluir, wait_timeout=120)
    logging.debug('POP UP COLIGADA DESAPARECER')


def enter_contas_a_pagar():

    linha_totvs = cc.wait_appear(locator.rm.linha_rm, wait_timeout=120)
    linha_totvs.click()
    logging.debug('CLICK - TOTVS - LINHA RM')
    back_office = cc.wait_appear(locator.rm.back_office, wait_timeout=15)
    back_office.click()
    logging.debug('CLICK - BACK OFFICE')
    gestao_financeira = cc.wait_appear(locator.rm.gestao_financeira, wait_timeout=15)
    gestao_financeira.click()
    logging.debug('CLICK - GESTAO FINANCEIRA')

    contas_pagar = cc.wait_appear(locator.rm.contas_pagar, wait_timeout=60)
    contas_pagar.click()
    logging.debug('CLICK - CONTAS A PAGAR')

    cont = 0
    while cont <= 50:

        select_lancamentos = waitForImage(image = lancamentos, timeout=10, name = 'LANÇAMENTOS')
        if select_lancamentos is not None:
            time.sleep(2)
            pyautogui.click(select_lancamentos)
            logging.debug('CLICA EM LANÇAMENTOS')
            time.sleep(5)

        licencas = waitForImage(image = licencas_excedidas, timeout=10, name = 'LICENCAS EXCEDIDAS')
        if licencas is not None:
            logging.debug('LICENCAS EXCEDIDAS')
            logging.debug(f'TENTANDO NOVAMENTE - {cont+1}')
            pyautogui.hotkey(f'esc')
            if cont == 50:
                logging.debug('ENVIANDO EMAIL DE ERRO')
                email_msg = 'Limite de licenças logadas excedido. Será necessário tentar novamente.'
                logging.debug(email_msg)
                emailErro(email_msg)
                encerra_prog()
            cont += 1
            time.sleep(20)
        
        else:
            break



def obter_intervalo_data():

    # Mude para o diretório especificado
    os.chdir(caminho_da_pasta_data)

    # Nome do arquivo que você deseja ler
    nome_arquivo = 'data.txt'

    # Caminho completo do arquivo
    caminho_arquivo = os.path.join(caminho_da_pasta_data, nome_arquivo)

    hora = datetime.now().time()
    hora_atual = hora.hour
    logging.debug(f'VERIFICANDO A HORA ATUAL {hora_atual}')

    # Verifique se o arquivo existe
    if os.path.exists(caminho_arquivo):
        # Abra o arquivo em modo de leitura
        
        # Padrão regex para encontrar a linha com PIX e a data
        padrao = re.compile(r'FERIAS/RESCISAO:\s*(\d{2}/\d{2}/\d{4}),\s*(\d{2}/\d{2}/\d{4})')

        # Variáveis para armazenar as datas
        data_inicial = None
        data_final = None

        # Ler o conteúdo do arquivo data.txt
        with open('data.txt', 'r') as arquivo:
            for linha in arquivo:
                # Encontrar a correspondência usando o padrão regex
                correspondencia = padrao.search(linha)

                # Verificar se a correspondência foi encontrada
                if correspondencia:
                    # Obter as datas correspondentes
                    data_inicial = correspondencia.group(1)
                    data_final = correspondencia.group(2)

        # Imprimir as datas antes da remoção
        logging.debug(f'Data Inicial FERIAS/RESCISAO antes da remoção: {data_inicial}')
        logging.debug(f'Data Final FERIAS/RESCISAO antes da remoção: {data_final}')

        # Remover as datas do arquivo data.txt
        with open('data.txt', 'r') as arquivo:
            conteudo = arquivo.read()

        conteudo_sem_datas = padrao.sub('FERIAS/RESCISAO:,', conteudo)

        with open('data.txt', 'w') as arquivo:
            arquivo.write(conteudo_sem_datas)

        # Imprimir as datas após a remoção
        logging.debug(f'Data Inicial FERIAS/RESCISAO após a remoção: {data_inicial}')
        logging.debug(f'Data Final FERIAS/RESCISAO após a remoção: {data_final}')

        if data_inicial == None or data_final == None:
            hoje = datetime.now()
            logging.debug(f'hoje -  {hoje}')
            dia_semana_hoje = hoje.weekday()  # Retorna um número entre 0 (segunda) e 6 (domingo)

            if dia_semana_hoje in [2, 3, 4, 5, 6]:  # Quarta, quinta ou sexta
                data_inicio = hoje - timedelta(days=dia_semana_hoje - 2)  # Início da quarta-feira atual
                data_fim = data_inicio + timedelta(days=6)  # Fim da terça-feira da próxima semana
            elif dia_semana_hoje in [0]:  # Segunda
                data_inicio = hoje - timedelta(days=dia_semana_hoje + 5)  # Início da quarta-feira passada
                data_fim = data_inicio + timedelta(days=6)  # Fim da terça-feira desta semana
            elif dia_semana_hoje in [1] and hora_atual < 12:  # Terça antes de meio dia
                data_inicio = hoje - timedelta(days=dia_semana_hoje + 5)  # Início da quarta-feira passada
                data_fim = data_inicio + timedelta(days=6)  # Fim da terça-feira desta semana
            elif dia_semana_hoje in [1] and hora_atual >= 12:  # Terça depois de meio dia
                data_inicio = hoje - timedelta(days=dia_semana_hoje - 2)  # Início da quarta-feira atual
                data_fim = data_inicio + timedelta(days=6)  # Fim da terça-feira da próxima semana
            else:
                # Lidar com outros dias da semana conforme necessário
                data_inicio = data_fim = None

            return data_inicio + timedelta(days=7), data_fim + timedelta(days=7)
        
        else:
            data_inicial_final = datetime.strptime(data_inicial, '%d/%m/%Y')
            data_final_final = datetime.strptime(data_final, '%d/%m/%Y')
            return data_inicial_final, data_final_final
    else:
        hoje = datetime.now()
        logging.debug(f'hoje -  {hoje}')
        dia_semana_hoje = hoje.weekday()  # Retorna um número entre 0 (segunda) e 6 (domingo)

        if dia_semana_hoje in [2, 3, 4, 5, 6]:  # Quarta, quinta ou sexta
            data_inicio = hoje - timedelta(days=dia_semana_hoje - 2)  # Início da quarta-feira atual
            data_fim = data_inicio + timedelta(days=6)  # Fim da terça-feira da próxima semana
        elif dia_semana_hoje in [0]:  # Segunda
            data_inicio = hoje - timedelta(days=dia_semana_hoje + 5)  # Início da quarta-feira passada
            data_fim = data_inicio + timedelta(days=6)  # Fim da terça-feira desta semana
        elif dia_semana_hoje in [1] and hora_atual < 12:  # Terça antes de meio dia
            data_inicio = hoje - timedelta(days=dia_semana_hoje + 5)  # Início da quarta-feira passada
            data_fim = data_inicio + timedelta(days=6)  # Fim da terça-feira desta semana
        elif dia_semana_hoje in [1] and hora_atual >= 12:  # Terça depois de meio dia
            data_inicio = hoje - timedelta(days=dia_semana_hoje - 2)  # Início da quarta-feira atual
            data_fim = data_inicio + timedelta(days=6)  # Fim da terça-feira da próxima semana
        else:
            # Lidar com outros dias da semana conforme necessário
            data_inicio = data_fim = None

        return data_inicio + timedelta(days=7), data_fim + timedelta(days=7)
    

def data_filter():

    '''global inicio, fim

    inicio, fim = obter_intervalo_data()

    if inicio and fim:
        logging.debug(f"DATA INICIO {inicio.strftime('%d-%m-%Y')}")
        logging.debug(f"DATA FIM {fim.strftime('%d-%m-%Y')}")
    else:
        texto_msg = 'NÃO FOI PROGRAMADO PARA RODAR NO FINAL DE SEMANA'
        logging.debug(texto_msg)
        emailFinalizado(texto_msg)
        encerra_prog()'''


    dt_inicial_format = inicio.strftime("%d-%m-%Y")
    dt_final_format = fim.strftime("%d-%m-%Y")
    logging.debug('CLICK - SELECIONA A DATA DE QUARTA FEIRA E DA PROXIMA TERÇA')
    logging.debug(f'QUARTA-FEIRA: {dt_inicial_format}')
    logging.debug(f'TERCA-FEIRA: {dt_final_format}')

    #selecionando o filtro
    
    #try:
    select_filter = cc.wait_appear(locator.rm.select_filter, wait_timeout=60)
    select_filter.click()
    time.sleep(2)
    filter_global = cc.wait_appear(locator.rm.group_filtros_globais, wait_timeout=60)
    filter_global.click()
    time.sleep(5)
    #filter_global.set_text('REMESSA FERIAS/RESCISAO')
    #pyautogui.write('REMESSA FERIAS/RESCISAO', interval=0.5)
    keyboard.write('REMESSA FERIAS/RESCISAO', delay=0.5)
    logging.debug('FILTRO - REMESSA FERIAS/RESCISAO')

    execute = cc.wait_appear(locator.rm.button_exec_filtro, wait_timeout=15)
    execute.click()
    logging.debug('CLICK - BUTÃO DE SELECAO DE FILTRO')

    start_dt = cc.wait_appear(locator.rm.dt_inicial_filtro, wait_timeout=15)
    start_dt.double_click()
    time.sleep(2)
    start_dt.send_hotkey(f'{dt_inicial_format}')
    logging.debug(f'INSERE - DATA DE QUARTA-FEIRA: {dt_inicial_format}')

    end_dt = cc.wait_appear(locator.rm.dt_final_filtro, wait_timeout=15)
    end_dt.double_click()
    time.sleep(2)
    end_dt.send_hotkey(f'{dt_final_format}')
    logging.debug(f'INSERE - DATA DA PROX TERCA-FEIRA: {dt_final_format}')

    select_filter = cc.wait_appear(locator.rm.button_ok_filtro, wait_timeout=15)
    select_filter.click()
    logging.debug('CLICK - BUTÃO DE EXECUTAR O FILTRO')
    time.sleep(5)

def filter_clean():
    for i in range(3):
        try:
            clear_filter_x = waitForImage(image = filter_clear, timeout=15, name = 'FILTER CLEAN')
            if clear_filter_x is not None:
                time.sleep(2)
                pyautogui.click(clear_filter_x)
                logging.debug('CLICK NO BOTÃO X DO LIMPA FILTRO')
        except:
            pass 

def desmark_filter():

    '''check_lancamentos_receber = cc.wait_appear(locator.rm.checkbox_lançamentos_a_receber, wait_timeout=1000)
    check_lancamentos_receber.click()
    logging.debug('CLICK CHECKBOX LANÇAMENTOS A RECEBER')'''

    for i in range(7):
        logging.debug(f'AGUARDANDO {i+1}')
        try:
            check_lancamentos_receber = cc.wait_appear(locator.rm.checkbox_lançamentos_a_receber, wait_timeout=150)
            check_lancamentos_receber.click()
            logging.debug('CLICK CHECKBOX LANÇAMENTOS A RECEBER')
            break

        except:
            pyautogui.hotkey('up')
            logging.debug('apertou up')
            if i == 7:
                check_lancamentos_receber = cc.wait_appear(locator.rm.checkbox_lançamentos_a_receber, wait_timeout=150)
                check_lancamentos_receber.click()
                logging.debug('CLICK CHECKBOX LANÇAMENTOS A RECEBER')


    check_lancamentos_baixados = cc.wait_appear(locator.rm.checkbox_lançamentos_baixados, wait_timeout=15)
    check_lancamentos_baixados.click()
    logging.debug('CLICK CHECKBOX LANÇAMENTOS BAIXADOS')

    check_lancamentos_cancelados = cc.wait_appear(locator.rm.checkbox_lançamentos_cancelados, wait_timeout=15)
    check_lancamentos_cancelados.click()
    logging.debug('CLICK CHECKBOX LANÇAMENTOS CANCELADOS')

    check_lancamentos_faturados = cc.wait_appear(locator.rm.checkbox_lançamentos_faturados, wait_timeout=15)
    check_lancamentos_faturados.click()
    logging.debug('CLICK CHECKBOX LANÇAMENTOS FATURADOS')

    filter_refresh = cc.wait_appear(locator.rm.button_atualiza_filtro, wait_timeout=15)
    filter_refresh.click()
    logging.debug('ATUALIZA O FILTRO')

def encerra_prog():
    
    #processo_inicio.terminate()
    encerrar_processo_windows(nome_processo)
    logging.debug('RM ENCERRADO')

    sys.exit()

def tabela_vazia():

    filter_clean()

    texto = cc.wait_appear(locator.rm.button_116, wait_timeout=15)
    txt_extraido = texto.get_text()
    logging.debug(f'Texto extraido{txt_extraido}')
    resultado = re.search(r"/(\d+)", txt_extraido)
    count = int(resultado.group(1))
    logging.debug(f'Count {count}')
    logging.debug(f'Type {type(count)}')
    number_rows = count

    if number_rows == 0:
        time.sleep(2)
        logging.debug('SEM REMESSA DE FÉRIAS/RESCISÃO')   
        time.sleep(2)
        return True
    
    else:
        logging.debug('TABELA CONTÉM REGISTROS')
        return False

    '''logging.debug('VERIFICANDO SE A TABELA ESTÁ VAZIA')

    time.sleep(10)
    pyautogui.hotkey('Ctrl', 'g')
    time.sleep(2)

    numero_registros = cc.wait_appear(locator.rm.text_remessa_ferias_rescisao_registros, wait_timeout=15)
    number_rows = numero_registros.get_text()
    logging.debug(number_rows)
    time.sleep(2)
    pyautogui.hotkey('Enter')

    if number_rows == 'Para este processo é necessário que existam registros na visão.':
        time.sleep(2)
        logging.debug('SEM REMESSA DE FÉRIAS/RESCISÃO')   
        time.sleep(2)
        return True
    
    else:
        logging.debug('TABELA CONTÉM REGISTROS')
        return False'''

def desbloqueio():

    click_all = cc.wait_appear(locator.rm.header_x, wait_timeout=120)
    click_all.click()
    logging.debug('SELECIONA TODAS AS TUPLAS')

    time.sleep(5)

    pyautogui.hotkey('Ctrl', 'p')
    logging.debug('CONTROL P PARA SELECIONAR PROCESSO')
    time.sleep(1)

    for i in range(7):
        time.sleep(0.5)
        pyautogui.press('down')
    logging.debug('7 SETAS PARA BAIXO - MANUTENÇÃO DE LANÇAMENTO')
    time.sleep(2)

    pyautogui.press('right')
    logging.debug('SETA PARA DIREITA')
    time.sleep(2)

    for i in range(8):
        time.sleep(0.5)
        pyautogui.press('down')
    logging.debug('8 SETAS PARA BAIXO')
    time.sleep(2)

    pyautogui.press('enter')
    logging.debug('ENTER PARA SELECIONAR DESBLOQUEIO ALTERAÇÃO')

    for i in range(3):
        time.sleep(20)
        pyautogui.press('esc')

    '''button_prog_exec = cc.wait_appear(locator.rm.button_progresso_da_execução_dos_processos, wait_timeout=360)
    button_prog_exec.click()
    logging.debug('SELECIONA PROCESSO DA EXECUCAO DOS PROGRESSOS ABA INFERIOR')

    get_txt_msg = cc.wait_appear(locator.rm.edit_txmessage_desbloqueio, wait_timeout=60)
    txt_msg = get_txt_msg.get_text()
    logging.debug(f'MSG AQUI: {txt_msg}')'''

    '''if txt_msg == '':
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

    '''time.sleep(2)
    click_appear = cc.wait_appear(locator.rm.titlebar_progresso_da_execução_dos_processos, wait_timeout=60)
    if click_appear is not None:
        click_appear.click()
    logging.debug('EVIDENCIAR ABA INFERIOR')'''
    '''time.sleep(5)
    pyautogui.press('esc')
    logging.debug('FECHANDO ABA INFERIOR')'''


def exec_lancamentos():
    
    time.sleep(2)
    pyautogui.hotkey('Ctrl', 'g')
    logging.debug('CONTROL G')

    click_combo = cc.wait_appear(locator.rm.combobox_lancamento, wait_timeout=15)
    click_combo.click()
    logging.debug('CLICK PARA APARECER CONTA/CAIXA')

    select_conta_caixa = cc.wait_appear(locator.rm.listitem_contacaixa, wait_timeout=15)
    select_conta_caixa.click()
    logging.debug('SELECIONA CONTA/CAIXA')
    
    select_conta_caixa = cc.wait_appear(locator.rm.button_contavalor, wait_timeout=15)
    select_conta_caixa.click()
    logging.debug('CLICK NO BOTÃO [...]')

    select_field_search = cc.wait_appear(locator.rm.edit_tbxsearch, wait_timeout=15)
    select_field_search.click()
    pyautogui.write('%3212')
    logging.debug('CLICK NO CAMPO PESQUISA E DIGITA: %3212')

    filter_search = cc.wait_appear(locator.rm.button_btnfilter, wait_timeout=15)
    filter_search.click()
    logging.debug('CLICK NO BOTÃO DO FILTRO')

    btn_ok_contacaixa = cc.wait_appear(locator.rm.button_ok_contacaixa, wait_timeout=15)
    btn_ok_contacaixa.click()
    logging.debug('CLICK NO BOTÃO OK')

    btn_executar = cc.wait_appear(locator.rm.button_executar, wait_timeout=15)
    btn_executar.click()
    logging.debug('CLICK NO BOTÃO EXECUTAR')

def process_lancamentos():

    exec_lancamentos()

    #cc.wait_appear(locator.rm.button_btncancel, wait_timeout=1000)

    for i in range(7):
        logging.debug(f'AGUARDANDO {i+1}')
        try:
            cc.wait_appear(locator.rm.button_btncancel, wait_timeout=150)
            break

        except:
            pyautogui.hotkey('up')
            logging.debug('apertou up')
            if i == 7:
                cc.wait_appear(locator.rm.button_btncancel, wait_timeout=150)
                


    exec_success_process = waitForImage(image = exec_sucesso, timeout=15, name = 'PRESS BUTTON OK')
    if exec_success_process is not None:
        #time.sleep(2)
        logging.debug('O PROCESSAMENTO DE LANÇAMENTO FOI EXECUTADO COM SUCESSO.')
        time.sleep(1)
        txt_log = cc.wait_appear(locator.rm.edit_textboxlog_2, wait_timeout=15)
        txt_log.click()
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1)
        txt_log = pyperclip.paste()
        logging.debug(f'{txt_log}')
        button_close = cc.wait_appear(locator.rm.button_btncancel, wait_timeout=15)
        button_close.click()
        proccess_bordero()

    else:
        time.sleep(2)
        logging.debug('O PROCESSAMENTO DE LANÇAMENTO COM ERRO.')
        time.sleep(2)
        txt_log = cc.wait_appear(locator.rm.edit_textboxlog2, wait_timeout=15)
        txt_log.click()
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(2)
        txt_log = pyperclip.paste()
        logging.debug(f'{txt_log}')
        button_close = cc.wait_appear(locator.rm.button_btncancel, wait_timeout=15)
        button_close.click()

        
    
def proccess_bordero():

    cc.wait_appear(locator.rm.checkbox_lançamentos_a_receber, wait_timeout=1000)

    time.sleep(2)
    pyautogui.hotkey('Ctrl', 'p')
    time.sleep(1)
    pyautogui.press('down')
    time.sleep(1)
    pyautogui.press('down')
    time.sleep(1)
    pyautogui.press('right')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    logging.debug('SELECIONAR INCLUSÃO DE BORDERO')

    #TRATATIVA PARA ERRO DE EXCEÇÃO AO INCLUIR AS AMOSTRAS NO BORDERO

    atualizacao_bordero = waitForImage(image = atualizacao_bordero_excecao, timeout=20, name = 'PRESS BUTON SIM')
    if atualizacao_bordero is not None:
        pyautogui.click(atualizacao_bordero)
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)

    menuitem_inclusao_bordero = cc.wait_appear(locator.rm.button_bordero_inclusao_trespontos, wait_timeout=60)
    menuitem_inclusao_bordero.click()
    logging.debug('CLICK EM CONVÊNIO TRÊS PONTINHOS')

    combo_sispag = cc.wait_appear(locator.rm.combobox_sispag, wait_timeout=15)
    combo_sispag.click()
    logging.debug('CLICK EM COMBOBOX PARA SELECIONAR O ID DO CONVÊNIO')

    select_convenio = cc.wait_appear(locator.rm.listitem_id_convenio, wait_timeout=15)
    select_convenio.click()
    logging.debug('CLICK EM ID DO CONVÊNIO')

    time.sleep(2)
    pyautogui.press('tab')
    logging.debug('APERTA TAB PARA ESCREVER O ID')

    time.sleep(2)
    pyautogui.write('9')
    logging.debug('ESCREVE O ID 9 - FERIAS/RESCISÃO')

    time.sleep(2)
    pyautogui.press('enter')
    logging.debug('APERTA ENTER PARA SELECIONAR O ID 9 - FERIAS/RESCISÃO')

    time.sleep(2)
    pyautogui.press('enter')
    logging.debug('APERTA ENTER PARA ESCOLHER O ID 9 - FERIAS/RESCISÃO')
    time.sleep(2)

    exec_bordero = cc.wait_appear(locator.rm.button_exec_bordero, wait_timeout=60)
    exec_bordero.click()
    logging.debug('CLICK EM EXECUTAR NA INCLUSÃO DO BORDÊRO')

    time.sleep(2)

    exec_success_process = waitForImage(image = exec_sucesso, timeout=600, name = 'PRESS BUTTON OK')
    if exec_success_process is not None:
        time.sleep(2)
        logging.debug('O PROCESSAMENTO DO BORDERO FOI EXECUTADO COM SUCESSO.')
        time.sleep(2)
        
    else:
        time.sleep(2)
        logging.debug('ERRO NA INCLUSÃO DO BORDERÔ')

    btn_exec_fechar = cc.wait_appear(locator.rm.button_bordero_fechar, wait_timeout=15)
    btn_exec_fechar.click()
    logging.debug('CLICK EM FECHAR.')
    time.sleep(2)

def movimentacao_bancaria():

    '''movi_bancaria = cc.wait_appear(locator.rm.tabitem_movimentacoes_bancarias, wait_timeout=1000)
    movi_bancaria.click()
    logging.debug('CLICK NA ABA MOVIMENTAÇÃO BANCARIA')'''

    for i in range(7):
        logging.debug(f'AGUARDANDO {i+1}')
        try:
            movi_bancaria = cc.wait_appear(locator.rm.tabitem_movimentacoes_bancarias, wait_timeout=150)
            movi_bancaria.click()
            logging.debug('CLICK NA ABA MOVIMENTAÇÃO BANCARIA')
            break

        except:
            pyautogui.hotkey('up')
            logging.debug('apertou up')
            if i == 7:
                movi_bancaria = cc.wait_appear(locator.rm.tabitem_movimentacoes_bancarias, wait_timeout=150)
                movi_bancaria.click()
                logging.debug('CLICK NA ABA MOVIMENTAÇÃO BANCARIA')

    time.sleep(2)

    cont = 0
    
    for i in range (3):

        while cont <= 50:

            bordero_click = waitForImage(image = bordero, timeout=60, name = 'IMAGEM BORDERO')
            if bordero_click is not None:
                time.sleep(2)
                pyautogui.click(bordero_click)
                logging.debug('IMAGEM BORDERO CLICADA.')

            licencas = waitForImage(image = licencas_excedidas, timeout=10, name = 'LICENCAS EXCEDIDAS')
            if licencas is not None:
                logging.debug('LICENCAS EXCEDIDAS')
                logging.debug(f'TENTANDO NOVAMENTE - {cont+1}')
                time.sleep(1)
                pyautogui.hotkey(f'esc')
                if cont == 50:
                    logging.debug('ENVIANDO EMAIL DE ERRO')
                    texto_msg = 'LICENCAS EXCEDIDAS, FAVOR REINICIAR O BOT'
                    emailErro(texto_msg)
                    encerra_prog()          
                cont += 1
                time.sleep(10)
            
            else:
                break

            '''licencas2 = waitForImage(image = licencas_2, timeout=2, name = 'LICENCE SERVER')
            if licencas2 is not None:
                time.sleep(2)
                for i in range(5):
                    pyautogui.press('tab')
                    time.sleep(1)
                    
                pyautogui.press('enter')'''
            
            

        filtro_movimentacao = cc.wait_appear(locator.rm.titlebar_titlebar, wait_timeout=180)
        if filtro_movimentacao is not None:
            logging.debug('ENCONTROU O FILTRO DA MOVIMENTAÇÃO BANCÁRIA')
            break

    filtro_movimentacao.click()
    logging.debug('CLICA NA ABA SUPERIOR DO FILTRO')


    time.sleep(2)
    pyautogui.write('hoje')
    #pyautogui.write('últimos 7 dias')
    #pyautogui.write('Esta semana')
    
    time.sleep(2)
    pyautogui.press('enter')
    logging.debug('SELECIONA O FILTRO HOJE')

    filter_clean()

    time.sleep(2)

    select_first_row = cc.wait_appear(locator.rm.dataitem_coligada_row0, wait_timeout=15)
    if select_first_row is not None:
        select_first_row.click()
        logging.debug('CLICK NA PRIMEIRA LINHA DA TABELA MOVIMENTAÇÃO BANCÁRIA')    

        for i in range(12):
            pyautogui.hotkey('right')
        logging.debug('12 PASSOS PARA DIREITA NA TABELA >>')

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
        pyautogui.write('Pendente')
        logging.debug('ESCREVE PENDENTE NO FILTRO')
        time.sleep(2)
        pyautogui.press('enter')
        logging.debug('APERTA ENTER PARA SELECIONAR OS PENDENTES')
        time.sleep(2)

        select_first_row = cc.wait_appear(locator.rm.dataitem_coligada_do_convenio_row0, wait_timeout=15)
        if select_first_row is not None:
            select_first_row.click()

            select_all = cc.wait_appear(locator.rm.header_x1, wait_timeout=120)
            select_all.click()
            logging.debug('SELECIONA TODAS AS TUPLAS COM STATUS PENDENTE')

            time.sleep(2)
            pyautogui.hotkey('Ctrl', 'p')
            logging.debug('CLICK EM PROCESSOS')
            time.sleep(2)
            pyautogui.hotkey('down')
            logging.debug('APERTA PARA BAIXO')
            time.sleep(2)
            pyautogui.hotkey('ENTER')
            logging.debug('APERTA ENTER')
            time.sleep(2)

            exec_bordero_autorizacao = cc.wait_appear(locator.rm.button_exec_autorizacao, wait_timeout=15)
            exec_bordero_autorizacao.click()
            logging.debug('CLICK EM EXECUTAR BORDERO DE PAGAMENTO')
            
            #cc.wait_appear(locator.rm.button_fechar_bordero, wait_timeout=1000)

            for i in range(7):
                logging.debug(f'AGUARDANDO {i+1}')
                try:
                    cc.wait_appear(locator.rm.button_fechar_bordero, wait_timeout=150)
                    break

                except:
                    pyautogui.hotkey('up')
                    logging.debug('apertou up')
                    if i == 7:
                        cc.wait_appear(locator.rm.button_fechar_bordero, wait_timeout=150)

            exec_success_process = waitForImage(image = exec_sucesso, timeout=15, name = 'PRESS BUTTON OK')
            if exec_success_process is not None:
                logging.debug('O PROCESSAMENTO DE AUTORIZAÇÃO DO BORDERO FOI EXECUTADO COM SUCESSO.')

            else:
                logging.debug('O PROCESSAMENTO DE AUTORIZAÇÃO DO BORDERO FOI EXECUTADO COM ERRO FAVOR VERIFICAR.')
            
            btn_exec_fechar = cc.wait_appear(locator.rm.button_fechar_bordero, wait_timeout=60)
            btn_exec_fechar.click()
            logging.debug('CLICK EM FECHAR.')

        else:
            logging.debug('SEM PROCESSAMENTO DE BORDERO PENDENTE.')

    else:
        logging.debug('SEM PROCESSAMENTO DE BORDERO')


def remessa_pagamento():

    time.sleep(5)

    filter_clean()

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
        

def check_user_bot():

    texto = cc.wait_appear(locator.rm.button_99, wait_timeout=15)
    txt_extraido = texto.get_text()
    logging.debug(f'Texto extraido{txt_extraido}')
    resultado = re.search(r"/(\d+)", txt_extraido)
    count = int(resultado.group(1))
    logging.debug(f'Count {count}')
    logging.debug(f'Type {type(count)}')

    for processo in range(count):

        time.sleep(2)
        pyautogui.hotkey('ctrl', 'c')
        logging.debug('CHECK USER BOT 1')

        time.sleep(2)
        usuario = pyperclip.paste()
        logging.debug(f'{usuario}')

        #if usuario == 'integracao':
        if usuario == 'dclick':

            time.sleep(2)

            for i in range(7):
                pyautogui.hotkey('right')
            logging.debug('7 PASSOS PARA DIREITA NA TABELA >>')

            time.sleep(2)
            pyautogui.hotkey('ctrl', 'c')

            time.sleep(2)
            bot = pyperclip.paste()
            logging.debug(f'{bot}')

            # Usando expressão regular para encontrar o nome PIX
            padrao = r'\bFERIAS\b'
            match = re.search(padrao, bot)

            if match:
                logging.debug("NOME FERIAS/RECISAO ENCONTRADO")
                pyautogui.hotkey('ctrl', 'space')
                time.sleep(2)
                pyautogui.hotkey('Ctrl', 'p')
                logging.debug('CLICK EM PROCESSOS')
                time.sleep(2)

                for i in range(3):
                    pyautogui.press('down')
                    logging.debug(f'APERTA PARA BAIXO {i}')
                    time.sleep(2)

                pyautogui.press('ENTER')
                logging.debug('APERTA ENTER')
                time.sleep(2)

                remessas_avancar = cc.wait_appear(locator.rm.button_processo_avancar, wait_timeout=15)
                remessas_avancar.click()
                logging.debug('CLICK EM REMESSAS DE PAGAMENTO')

                for i in range(3):
                    time.sleep(1)
                    pyautogui.press('tab')
                    logging.debug(f'APERTA TAB {i}')

                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(2)
                pyautogui.write('341')
                time.sleep(2)
                pyautogui.press('enter')
                time.sleep(2)
                pyautogui.press('enter')
                time.sleep(2)

                remessas_avancar2 = cc.wait_appear(locator.rm.button_remssas_avancar_2, wait_timeout=15)
                remessas_avancar2.click()
                logging.debug('CLICK EM AVANÇAR')

                dt_inicial_format = inicio.strftime("%d-%m-%Y")
                dt_final_format = fim.strftime("%d-%m-%Y")
                logging.debug('CLICK - SELECIONA A DATA DE QUARTA FEIRA E DA PROXIMA TERÇA')
                logging.debug(f'QUARTA-FEIRA: {dt_inicial_format}')
                logging.debug(f'TERCA-FEIRA: {dt_final_format}')

                data_inicial_param = inicio.strftime("%d")
                data_final_param = fim.strftime("%d")
                data_ano_param = fim.strftime("%Y")
                dois_digitos_ano = str(data_ano_param)[-2:]

                time.sleep(2)
                pyautogui.press('tab')
                time.sleep(2)


                desmark_salvar_arq = cc.wait_appear(locator.rm.checkbox_desmarcar, wait_timeout=15)
                desmark_salvar_arq.click()
                logging.debug('DESMARCA CHECKBOX PARA SALVAR ARQUIVO DE REMESSA')

                dot_three = cc.wait_appear(locator.rm.button_btnselecaodiretorio, wait_timeout=15)
                dot_three.click()
                logging.debug('CLICK NOS ... PARA SELECIONAR O DIRETÓRIO E NOME DO ARQUIVO.')

                click_dir = cc.wait_appear(locator.rm.toolbar_endereço, wait_timeout=15)
                click_dir.double_click()
                logging.debug('DUPLO CLICK NO DIRETORIO')

                time.sleep(0.5)

                global novo_nome

                pyautogui.write(f'{caminho_pasta}')
                time.sleep(0.5)

                pyautogui.press('enter')
                time.sleep(0.5)

                for i in range(6):
                    time.sleep(0.5)
                    pyautogui.press('tab')
                    logging.debug(f'APERTA TAB {i}')

                # Caminho para a pasta
                #caminho_pasta = r'X:\\'

                # Tente mudar para o diretório
                '''try:
                    os.chdir(caminho_pasta)
                except Exception as e:
                    logging.debug(f'Erro ao tentar acessar o diretório: {e}')
                    exit()
'''
                # Liste todos os arquivos na pasta
                arquivos = os.listdir(caminho_pasta)

                # Encontre a última letra usada
                arquivos_com_padrao = [arquivo[-5] for arquivo in arquivos if arquivo.startswith(f'F{data_inicial_param}{data_final_param}{dois_digitos_ano}') and arquivo.endswith('.txt')]

                if arquivos_com_padrao:
                    ultima_letra_usada = max(arquivos_com_padrao)
                    logging.debug(f'A ULTIMA LETRA USADA: {ultima_letra_usada}')
                    # Determine a próxima letra
                    proxima_letra = chr(ord(ultima_letra_usada) + 1)
                    logging.debug(f'A LETRA SERA: {proxima_letra}')
                    
                else:
                    proxima_letra = 'A'
                    logging.debug(f'LETRA "A" SERÁ UTILIZADA')
                    
                if proxima_letra == 'Q':
                    texto_msg = 'FAVOR VERIFICAR OS NOMES DOS ARQUIVOS DE REMESSA DE RESCISÃO/FERIAS NA PASTA X:\\ PARA NÃO SOBREPOR'
                    logging.debug(texto_msg)
                    emailErro(texto_msg)
                
                
                novo_nome = f'F{data_inicial_param}{data_final_param}{dois_digitos_ano}{proxima_letra}.txt'

                pyautogui.write(novo_nome)
                logging.debug(novo_nome)
  
                click_save = cc.wait_appear(locator.rm.button_salvar, wait_timeout=15)
                click_save.double_click()
                logging.debug('CLICK NO BUTÃO SALVAR')

                avancar_3 = cc.wait_appear(locator.rm.button_remessas_avancar_3, wait_timeout=15)
                avancar_3.click()
                logging.debug('CLICK EM AVANCAR PARA CONCLUIR')

                execute_processo_pagamento = cc.wait_appear(locator.rm.button_exec_processo_pag, wait_timeout=15)
                execute_processo_pagamento.double_click()
                logging.debug('CLICK EM EXECUTAR')

                cc.wait_appear(locator.rm.button_btnfechar, wait_timeout=1000)

                exec_success_process = waitForImage(image = exec_sucesso, timeout=15, name = 'PRESS BUTTON OK')
                if exec_success_process is not None:
                    time.sleep(2)
                    logging.debug('O PROCESSAMENTO DE AUTORIZAÇÃO DO BORDERO FOI EXECUTADO COM SUCESSO.')
                    time.sleep(2)
                    txt_log = cc.wait_appear(locator.rm.edit_textboxlog1, wait_timeout=15)
                    txt_log.click()
                    time.sleep(2)
                    pyautogui.hotkey('ctrl', 'a')
                    time.sleep(2)
                    pyautogui.hotkey('ctrl', 'c')
                    time.sleep(2)
                    txt_log = pyperclip.paste()
                    logging.debug(f'{txt_log}')
                    emailSuccess()

                    
                else:
                    time.sleep(2)
                    texto_msg = 'O PROCESSAMENTO DE AUTORIZAÇÃO DO BORDERO FOI EXECUTADO COM ERRO.'
                    logging.debug(texto_msg)
                    time.sleep(2)
                    txt_log = cc.wait_appear(locator.rm.edit_textboxlog1, wait_timeout=15)
                    txt_log.click()
                    time.sleep(2)
                    pyautogui.hotkey('ctrl', 'a')
                    time.sleep(2)
                    pyautogui.hotkey('ctrl', 'c')
                    time.sleep(2)
                    txt_log = pyperclip.paste()
                    logging.debug(f'{txt_log}')
                    emailErro(texto_msg)

                click_close = cc.wait_appear(locator.rm.button_btnfechar, wait_timeout=15)
                click_close.click()

                break

            else:
                logging.debug("NOME FERIAS NAO ENCONTRADO.")
                for i in range(7):
                    pyautogui.hotkey('left')
                logging.debug('7 PASSOS PARA ESQUERDA NA TABELA <<')
                pyautogui.press('down')
                logging.debug(f'COUNT1: {processo}')

        else:
            logging.debug('O USUÁRIO NÃO É INTEGRAÇÃO PARA ESSA REMESSA PARA PARA DE BAIXO')
            pyautogui.press('down')
            logging.debug(f'COUNT1: {processo}')

        if processo+1 == count:
            logging.debug('NÃO FOI ENCONTRADO O USUÁRIO INTEGRAÇÃO E O NOME DO ARQUIVO SISPAG')


# wait for image with pyautogui
def waitForImage(image, timeout, name):
    inicialTime = time.time()

    while True:
        # try to find image on screen
        location = pyautogui.locateOnScreen(image=image, confidence=0.9)

        if location is not None:
            # Image found
            logging.info(f'{name} image found.')
            return location

        # checking if timeout is over
        currentTime = time.time()
        if currentTime - inicialTime >= timeout:
            # timeout is over and the image was not found.
            logging.info(f'{name} image not found.')
            return None

        # waiting for searching again
        time.sleep(0.5)

def emailSuccess():
    with open(f'{email_path}/emailSuccess.html', 'r', encoding='utf=8') as fileSuccess:
        templateSuccess = fileSuccess.read()
        htmlSuccess = templateSuccess
    yag.send(to=str(email_receivers).split(','), subject=f"SUCESSO - BOT REMESSAS FÉRIAS/RESCISÃO",
    contents=htmlSuccess,
    attachments=[f'{log_path}/{today}/{log_file_name}.log', f'{caminho_pasta}\{novo_nome}'])
    logging.info('Success e-mail sent.')

def emailErro(texto_msg):
    with open(f'{email_path}/emailError.html', 'r', encoding='utf=8') as fileSuccess:
        templateSuccess = fileSuccess.read()
        htmlSuccess = templateSuccess.format(mensagem = texto_msg)
    yag.send(to=str(email_receivers).split(','), subject=f"ERRO - BOT REMESSAS FÉRIAS/RESCISÃO",
    contents=htmlSuccess,
    attachments=f'{log_path}/{today}/{log_file_name}.log')
    logging.info('Success e-mail sent.')



def emailFinalizado(texto_msg):
    with open(f'{email_path}/emailFinalizado.html', 'r', encoding='utf=8') as fileSuccess:
        templateSuccess = fileSuccess.read()
        htmlSuccess = templateSuccess.format(mensagem = texto_msg)
    yag.send(to=str(email_receivers).split(','), subject=f"FINALIZADO SEM PROCESSAMENTO - BOT REMESSAS FÉRIAS/RESCISÃO",
    contents=htmlSuccess,
    attachments=f'{log_path}/{today}/{log_file_name}.log')
    logging.info('Finalizado e-mail sent.')


###########
def check_movimentacao_bancaria():
    global inicio, fim
    
    linha_totvs = cc.wait_appear(locator.rm.linha_rm, wait_timeout=120)
    linha_totvs.click()
    logging.debug('CLICK - TOTVS - LINHA RM')
    back_office = cc.wait_appear(locator.rm.back_office, wait_timeout=15)
    back_office.click()
    logging.debug('CLICK - BACK OFFICE')
    gestao_financeira = cc.wait_appear(locator.rm.gestao_financeira, wait_timeout=15)
    gestao_financeira.click()
    logging.debug('CLICK - GESTAO FINANCEIRA')


    inicio, fim = obter_intervalo_data()

    if inicio and fim:
        logging.debug(f"DATA INICIO {inicio.strftime('%d-%m-%Y')}")
        logging.debug(f"DATA FIM {fim.strftime('%d-%m-%Y')}")
    else:
        texto_msg = 'NÃO FOI PROGRAMADO PARA RODAR NO FINAL DE SEMANA'
        logging.debug(texto_msg)
        emailFinalizado(texto_msg)
        encerra_prog()

    movimentacao_bancaria()
    remessa_pagamento()