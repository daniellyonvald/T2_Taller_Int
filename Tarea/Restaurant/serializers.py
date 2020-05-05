from rest_framework import serializers
from .models import Ingrediente, Hamburgesa

class HamburgesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hamburgesa
        fields = ['id','nombre', 'precio', 'descripcion', 'imagen', 'ingredientes']

    def create(self, validated_data):
        return Hamburgesa.objects.create(**validated_data)

    def update(self, instance, validated_data): #Revisar
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.precio = validated_data.get('precio', instance.precio)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        instance.imagen = validated_data.get('imagen', instance.imagen)
        instance.ingredientes = validated_data.get('ingredientes', instance.ingredientes)
        instance.save()
        return instance

class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ['id','nombre', 'descripcion']

    def create(self, validated_data):
        return Ingrediente.objects.create(**validated_data)
