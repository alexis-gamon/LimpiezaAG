from django.urls import path, include

from .views import LimpiezaListView, LimpiezaTemplateView, LimpiezaPageDetail, LimpiezaPagesCreate, LimpiezaPageUpdate, LimpiezaPageDelete, ComentariosCreateView

urlpatterns = [

    path('Limpieza/',LimpiezaTemplateView.as_view(), name='Limpieza'),
    path('', LimpiezaListView.as_view(), name='lista_tec'),
### Detalle
    path('<int:pk>/', LimpiezaPageDetail.as_view(), name='limpieza_detalle'),
### Crear
    path('nuevo/', LimpiezaPagesCreate.as_view(), name="limpieza_nuevo"),
### Modificar
    path('<int:pk>/editar/', LimpiezaPageUpdate.as_view(), name="limpieza_editar"),
### Borrar 
    path('<int:pk>/eliminar/', LimpiezaPageDelete.as_view(), name="limpieza_eliminar"),

    path('<int:pk>/Comentario/',ComentariosCreateView.as_view(), name='Comentario'),


]