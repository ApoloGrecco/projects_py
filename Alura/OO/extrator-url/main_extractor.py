from URL_extractor import URLExtractor


def main():
    url_extractor = URLExtractor("https://bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")
    #url_extractor = URLExtractor(input("Digite uma URL:"))
    #value_quantity = url_extractor.get_value_parameter("quantidade")
    #value_quantity = url_extractor.get_value_parameter(input("Digite o parametro: "))
    #print(value_quantity)

    VALOR_DOLAR = 4.65
    moeda_origem = url_extractor.get_value_parameter("moedaOrigem")
    moeda_destino = url_extractor.get_value_parameter("moedaDestino")
    quantidade = url_extractor.get_value_parameter("quantidade")

    url_extractor.currency_conversion(moeda_origem, moeda_destino, quantidade, VALOR_DOLAR)


if __name__ == "__main__":
    main()
