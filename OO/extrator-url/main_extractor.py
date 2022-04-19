from URL_extractor import URLExtractor


def main():
    url_extractor = URLExtractor("https://bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")
    #url_extractor = URLExtractor(input("Digite uma URL:"))
    value_quantity = url_extractor.get_value_parameter("quantidade")
    #value_quantity = url_extractor.get_value_parameter(input("Digite o parametro: "))
    print(value_quantity)


if __name__ == "__main__":
    main()
