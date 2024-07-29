from django.urls import path
from msgapp import views     #import views as we call at the time of fun creation views.about
from msgapp.views import ContactForm
urlpatterns = [
    #path('urlpatter',views.fun_name)
    path('about',views.about),
   
    #path('urlpatter',className.as_view())
    path('classbase/<eid>',ContactForm.as_view()),
    path('hello',views.hello),
    path('main',views.main),
    path('product',views.product),
    path('cart',views.cart),
    path('form',views.form),
    path('display',views.display),
    path('edit/<eid>',views.edit),
    path('delete/<eid>',views.delete),
]
