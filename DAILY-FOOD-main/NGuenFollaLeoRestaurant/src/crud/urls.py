from django.urls import path
from . import views
from test2.settings import DEBUG, STATIC_ROOT, MEDIA_ROOT, MEDIA_URL, STATIC_URL
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('upload/', views.upload, name='upload-crud'),
    path('upload2/', views.upload2, name='upload2-crud'),
    path('upload3/', views.upload3, name='upload3-crud'),
    path('cart/', views.cart, name="cart"),
    path('contact/', views.contact, name="contact"),
    path('shop/', views.shop, name="shop"),
    path('single/', views.single, name="single"),
    path('resto/', views.resto, name="resto"),


    path('problem/', views.problem, name='problem'),
    path('<int:id>', views.view_chaussure, name='view_chaussure'),
    path('add', views.add, name='add'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),


    path('upload/<int:crud_id>', views.update_crud),
    path('delete_crud/<int:crud_id>', views.delete_crud),
    path('update_crud/<int:crud_id>', views.update_crud),

    path('upload/<int:crud_id1>', views.update_crud),
    path('delete_crud/<int:crud_id1>', views.delete_crud),
    path('update_crud/<int:crud_id1>', views.update_crud),

    path('upload/<int:crud_id2>', views.update_crud),
    path('crud/<int:id>delete', views.delete_crud, name='delete'),
    path('update_crud/<int:crud_id2>', views.update_crud),


]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
