"""aqui utilizaremos el modulo Routers para 
   crear las rutas de una manera mas sencilla 
   y no manualmente para eso importamos Router
   quien contiene lo necesario para crearme 
   las rutas 
   """
from rest_framework import routers
from .apy import projectViewSets


"""funcionalidad para crear las rutas la cual se 
   guarda en una variable """
router = routers.DefaultRouter()



"""sacamos uno de sus metodos para crear la ruta  y de ultimo 
   ponemos un enpoint para acceder luego a este
    cual es la magia de esto es que gracias a este 
   proseco aqui se me crearon cuatro rutas una para post put delete
    get  """
router.register('api/project',projectViewSets,'projets')



"""ahora creamos el patters para que lea las rutas creadas """
urlpatterns = router.urls