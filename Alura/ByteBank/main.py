from cpf_cnpj import Document
from phones_br import PhonesBr
from dates_br import Datesbr
from acess_cep import SearchAdress


one_cpf = "42465260880"
one_cnpj = "33372251000156"

document_cpf = Document.create_document(one_cpf)
document_cnpj = Document.create_document(one_cnpj)

print(document_cpf)
print(document_cnpj)

phone_number = "+5511940246209"

phone_object = PhonesBr(phone_number)
print(phone_object)

registration = Datesbr()
print(registration.format_date())
print(registration.registration_time())

cep = "06826530"
object_cep = SearchAdress(cep)

district, locality, state = object_cep.acess_cep()

print(f"{district} - {locality} - {state} - {object_cep}")

