from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validate(self, data):
        if not cpf_validate(data['cpf']):
            raise serializers.ValidationError({"cpf":"CPF inválido!"})

        if not nome_validate(data['nome']):
            raise serializers.ValidationError({"nome":"Não inclua números neste campo."})
        
        if not rg_validate(data['rg']):
            raise serializers.ValidationError({"rg":"O RG deve ter 9 dígitos"})
        
        if not celular_validate(data['celular']):
            raise serializers.ValidationError({"celular":"O celular deve seguir este modelo (XX) XXXXX-XXXX"})
        
        return data
            