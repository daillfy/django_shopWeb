from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'order/', include('order.urls', namespace='order')),
    path(r'cart/', include('cart.urls', namespace='cart')), #应该添加在app前面，因为这条路径更加严格
    path(r'app1/',include('app1.urls',namespace='app1')), #为app的一级路由娶一个名字

]


from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)