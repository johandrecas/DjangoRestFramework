from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):

    #aqui creamos los campos que queremos que se consulten
    class Meta:

        #Debo especificar el modelo al que me refiero el que esta en models
        # la clase Project
        model = Project
        
        #Creo la tupla de los datos que quiero que me consulte
        #que coinciden con los que tengo en mi modelo
        fields = ('id','title','description','tecnology','created_at')

        #luego le definimos los campos que seran de solo lectura
        # osea esto lo hago para que no puedan ser modificados 
        read_only_fields=('created_at',)