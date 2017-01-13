from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^api/jos-v1.5/', include('onlineshop.urls')),
    url(r'^api/jos-v1.5/admin/', admin.site.urls),
]