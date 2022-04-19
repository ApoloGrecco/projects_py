import re

class URLExtractor:
    def __init__(self, url):
        self.url = self.sanitize_url(url)
        self.valid_url()

    def sanitize_url(self, url):
        if type(url) == str:
            return url.strip().replace(" ", "")
        else:
            return ""

    def valid_url(self):
        if not self.url:
            raise ValueError('A URL está vázia ou é inválida')

        url_pattern = re.compile("(http(s)?://)?(www.)?[a-zA-Z0-9]+.com(.br)?/[a-zA-Z0-9]+")
        match = url_pattern.match(self.url)
        if not match:
            raise ValueError("A URL não é válida")

    def get_url_base(self):
        index_question = self.url.find('?')
        url_base = self.url[:index_question]
        return url_base

    def get_url_parameters(self):
        index_question = self.url.find('?')
        url_parameters = self.url[index_question + 1:]
        return url_parameters

    def get_value_parameter(self, search_parameter):
        index_parameter = self.get_url_parameters().find(search_parameter)
        index_value = (index_parameter + len(search_parameter)) + 1
        index_commercial = self.get_url_parameters().find('&', index_value)
        if index_commercial == -1:
            value = self.get_url_parameters()[index_value:]
        else:
            value = self.get_url_parameters()[index_value:index_commercial]
        return value

    # def __len__(self):
    #     return len(self.url)
    #
    # def __str__(self):
    #     return self.url + "\n" + "Parâmetros: " + self.get_url_parameters() + "\n" + "URL Base: " + self.get_url_base()
    #
    # def __eq__(self, other):
    #     return self.url == other.url
