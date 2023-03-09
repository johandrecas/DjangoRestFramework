"""importamos views sets 
    
    para que nos sirve view_sets:
        para decile que tipo de consultas podemos hacer 
        y esto lo hacemos nombrando el objeto del modelo
        que importamos

    para que sirve permissions []:
        nos sirve para decirle que tipo de permisos va tener
         mi modelo para esto se creara una lista con el nombre
        permissions_clases donde en una lista le diremos los 
         permisos que tendra mi clase  """

from .models import Project
from rest_framework import viewsets,permissions
from .serializer import ProjectSerializer



class projectViewSets(viewsets.ModelViewSet):

    """Traemos todos los modelos de models y lo guardamos en esta variable
       con este nombre """
    queryset = Project.objects.all()

    """ahora le damos los permisos para esta clase 
       y se los pasamos en una lista con la palabra
       permisions y punto podremos ver todos sus permisos
        """
    permission_classes = [permissions.AllowAny]

    """luego le decimos como serialize el modelo
       y este serializado lo traemos de la clase 
       que ya creamos serializer"""
    serializer_class = ProjectSerializer
    

"""de aqui nos vamos a crer archivo para las rutas"""

