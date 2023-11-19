from django.urls    import path
from .              import views

urlpatterns = [
    path('grandeurs/<int:id>/', views.detail, name='detail'),
    path('grandeurs', views.grandeur_list, name="grandeurs"),
    path('new', views.new, name = 'new') 
]
