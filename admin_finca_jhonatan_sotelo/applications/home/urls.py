from django.contrib import admin
from django.urls import path


from.import views

urlpatterns = [
    path('home/', views.HomeView.as_view()),
    path('crear/', views.CreateView.as_view()),
    path('listar/', views.ListView.as_view()),
    path('actualizar/', views.ActualizarListView.as_view()),
    path('<pk>/actualizarid/', views.UpdateView.as_view()),
    path('eliminar/', views.EliminarListView.as_view()),
    path('<pk>/eliminarid/', views.DeleteView.as_view()),
]
