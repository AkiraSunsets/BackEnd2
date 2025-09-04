from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import * # Importa todas as views do módulo

urlpatterns = [ #paleta de endpoints
    #GET / POST
    path('authors', visualizacao_autor),
    path('autores', AutoresView.as_view()),
    path('books', BooksView.as_view()),
    path('publishers', PublisherView.as_view()),
    path('buscar/', AutoresView.as_view()),
    
    #UPDATE/DELETE
    path('autor/<int:pk>', AutoresDetailView.as_view()),
    path('books/<int:pk>', BooksDetailView.as_view()),
    path('publisher/<int:pk>', PublisherDetailView.as_view()),

    #TOKEN 
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name="token_refresh"),
]