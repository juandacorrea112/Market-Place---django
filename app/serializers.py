from .models import Marca, Producto #Marca
from rest_framework import serializers

# class MarcaSerializer(serializers.ModelSerializer):
    
#     class meta:
#         model = Marca
#         fields = '__all__'



class ProductoSerializer(serializers.ModelSerializer):
    nombre_marca = serializers.CharField(read_only=True, source="marca.nomrbe")
    # marca = MarcaSerializer(read_only=True)
    marca_id = serializers.PrimaryKeyRelatedField(queryset=Marca.objects.all(), source="marca")
    nombre = serializers.CharField(required = True, min_length=3)

    def validate_nomrbe(self, value):
        existe = Producto.objects.filter(nombre__iexact = value).exists()

        if existe:
            raise serializers.ValidationError("Este producto ya existe")
        return value

    class Meta:
        model = Producto
        fields = '__all__'

