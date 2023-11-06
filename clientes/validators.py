import re
from validate_docbr import CPF
def cpf_validate(numero_cpf):
    cpf = CPF()
    return cpf.validate(numero_cpf)

def nome_validate(nome):
    return nome.isalpha()

def rg_validate(rg):
    return len(rg) == 9

def celular_validate(celular):
    """Verificar se o celular é válido ((11) 96467-0934)"""
    
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    response = re.findall(modelo, celular)
    return response