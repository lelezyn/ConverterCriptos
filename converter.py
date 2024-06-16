import requests

def get_crypto_price(crypto):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data[crypto]['usd']
    else:
        raise ValueError(f'Erro ao obter o preço para {crypto}.')

def convert_tokens(amount_tokens, from_crypto, to_crypto):
    from_price = get_crypto_price(from_crypto)
    to_price = get_crypto_price(to_crypto)
    amount_usd = amount_tokens * from_price
    to_crypto_amount = amount_usd / to_price
    return to_crypto_amount

if __name__ == '__main__':
    try:
        amount_tokens = float(input('Digite a quantidade de tokens da criptomoeda de origem: '))
        from_crypto = input('Digite a criptomoeda de origem (em minúsculas, ex: bitcoin): ')
        to_crypto = input('Digite a criptomoeda de destino (em minúsculas, ex: ethereum): ')
        result = convert_tokens(amount_tokens, from_crypto, to_crypto)
        print(f'Com {amount_tokens} {from_crypto}, você pode obter {result:.6f} {to_crypto}.')
    except ValueError as e:
        print(e)
