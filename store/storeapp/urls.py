from django.urls import path
from storeapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('contact',views.contact),
    path('greet',views.greet),
    path('edit/<id>',views.edit),
    path('delete/<id>',views.delete),
    path('Hello',views.Hello),
    path('addproject',views.addproject),
    path('index',views.index),
     path('about',views.about),
    path('cart',views.viewcart),
    path('contact',views.contact),
    path('details/<id>',views.details),
    path('user_login',views.user_login),
    path('order',views.order),
    path('payment',views.payment),
    path('placeorder',views.place_order),
    path('register',views.register),
    path('catfilter/<cv>',views.catfilter),
    path('pricerange',views.pricerange),
    path('sort/<sv>',views.sort),
    path('logout',views.user_logout),
    path('addcart/<rid>',views.addcart),
    path('remove/<rid>',views.removecart),
    path('qty/<sig>/<pid>',views.cartqty),
    path('makepayment',views.makepayment),
    path('sendmail',views.send_mail),
   

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)