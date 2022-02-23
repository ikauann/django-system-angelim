import requests
import json
from bling.models import BlingEstoque
import telegram

def salvar_db(data):
    for d in data:
        data_produto = d.get('produto')
        sku = data_produto.get('codigo')
        preco = data_produto.get('preco')
        BlingEstoque.objects.update_or_create(
            sku=sku,
            defaults={
                'status': 'update',
                'preco': preco,
        })



def exec():

    #telegram:
    token = '1974108710:AAEbiqss0ASLoSp8Qe2coKbTnn8YC5PrA78'
    bot = telegram.Bot(token=token)

    chat_id = '1402282485'
    kwargs = {
        'chat_id': chat_id,
        'msg': 'Job iniciado'
    }
    bot.sendMessage(kwargs['chat_id'], kwargs['msg'])

    #bling:
    api_key = 'd4a1fc2cdb7bc18dbb931e87801b8baa9d3fd41eecfd896a8699e18f861ccffd00ec7709'
    payload = {'apikey': api_key}

    print('Pagina 1')
    response = requests.get('https://bling.com.br/Api/v2/produtos/json', params=payload)
    data = response.json().get('retorno').get('produtos')
    salvar_db(data)

    aux_paginacao = 0
    count_paginacao = 2
    while aux_paginacao == 0:
        print('PAGINA ', str(count_paginacao))
        response = requests.get(
            'https://bling.com.br/Api/v2/produtos/page={}/json'.format(str(count_paginacao)),
            params=payload
        )
        data = response.json().get('retorno').get('produtos')
        if data == None:
            print('ACABOU')
            aux_paginacao = 1
        else:
            salvar_db(data)
            count_paginacao += 1

    #telegram:
    kwargs = {
    'chat_id': chat_id,
    'msg': 'Job finalizado'
    }
    bot.sendMessage(kwargs['chat_id'], kwargs['msg'])
