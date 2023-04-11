from django.urls import path
from .import views
# from test2.settings import DEBUG, STATIC_ROOT, MEDIA_ROOT, MEDIA_URL, STATIC_URL
# from django.conf.urls.static import static

urlpatterns = [
    path('', views.Accueil, name="index"),
#     path('upload/', views.upload, name='upload-crud'),
#     path('upload2/', views.upload2, name='upload2-crud'),
    path('administration/', views.Administration, name='admin'),
#     path('upload/', views.upload, name='upload-Restaurant'),
#     path('update/<int:Admin_id>', views.update_Restaurant),
#     path('delete/<int:Admin_id>', views.delete_Restaurant),
    path('restau/', views.restau, name='restau'),
    path('cart/', views.cart, name="cart"),
#     path('contact/', views.contact, name="contact"),
    path('shop/', views.shop, name="shop"),
#     path('single/', views.single, name="single"),


    path('problem/', views.problem, name='problem'),
#     path('<int:id>', views.view_chaussure, name='view_chaussure'),
    path('add/', views.CommentaireClient, name='add'),
    path('restaurant/<int:id>/edit', views.edit_Restaurant, name='edit'),
    path('restaurant/<int:id>/delete', views.delete_Restaurant, name='delete'),


#     path('signup', views.signup, name='signup'),
#     path('signin', views.signin, name='signin'),
#     path('signout', views.signout, name='signout'),
#     path('activate/<uidb64>/<token>', views.activate, name='activate'),

#     path('upload/<int:crud_id>', views.update_crud),
#     path('delete_crud/<int:crud_id>', views.delete_crud),
#     path('update_crud/<int:crud_id>', views.update_crud),

#     path('upload/<int:crud_id1>', views.update_crud),
#     path('delete_crud/<int:crud_id1>', views.delete_crud),
#     path('update_crud/<int:crud_id1>', views.update_crud),
]

# if DEBUG:
#     urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
#     urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
