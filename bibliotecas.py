def tratamento_qj(item):
    item = eval(item['data'][0])
    sku = item['retorno']['estoques'][0]['estoque']['codigo']
    estoque = item['retorno']['estoques'][0]['estoque']['estoqueAtual']
    dicionario = {
        'sku':sku,
        'estoque': estoque
    }
    return dicionario