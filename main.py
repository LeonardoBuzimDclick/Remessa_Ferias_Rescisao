from clicknium import locator, ui
from clicknium import clicknium as cc
#from SUBPROGRAMS.functions import bot_text_art, show_exception_and_exit, open_RM, loggin_RM, enter_coligada, enter_contas_a_pagar, data_filter, desmark_filter, desbloqueio, filter_clean, process_lancamentos, proccess_bordero, movimentacao_bancaria, remessa_pagamento, tabela_vazia, emailSuccess, emailErro, encerra_prog
from SUBPROGRAMS.functions import *
from SUBPROGRAMS.parameters import *


if __name__ == '__main__':

    sys.excepthook = show_exception_and_exit
    encerrar_processo_windows(nome_processo)
    bot_text_art()
    open_RM()
    loggin_RM()
    enter_coligada()
    check_movimentacao_bancaria() ###
    enter_contas_a_pagar()
    data_filter()
    desmark_filter()
    result = tabela_vazia()
    if result == True:
        texto_msg = 'SEM REMESSA DE FÉRIAS/RESCISÃO'
        logging.debug(texto_msg)
        emailFinalizado(texto_msg)
        encerra_prog()
        
    else:
        desbloqueio()
        process_lancamentos()
        movimentacao_bancaria()
        remessa_pagamento()
        texto_msg = 'BOT FÉRIAS/RESCISÃO FINALIZADO'
        logging.debug(texto_msg)
        emailFinalizado(texto_msg)
        encerra_prog()