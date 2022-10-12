from django.urls import path
from Modelos.views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("noroeste/", noroeste),
    path("noroeste/salta/", blogssalta),
    path("noroeste/salta/agregarblogSalta/", agregarblogSalta),
    path('noroeste/salta/editarblogSalta/<blogsalta_id>', editarblogSalta),
    path("noroeste/salta/borrarblogSalta/<blogsalta_id>", borrarblogSalta),
    path("noroeste/salta/leerblogSalta/<blogsalta_id>", leerblogSalta),
    path("patagonia/", patagonia),
    path("patagonia/rionegro/", blogsrionegro),
    path("patagonia/rionegro/agregarblogRioNegro/", agregarblogRioNegro),
    path('patagonia/rionegro/editarblogRioNegro/<blogrionegro_id>', editarblogRioNegro),
    path("patagonia/rionegro/borrarblogRioNegro/<blogrionegro_id>", borrarblogRioNegro),
    path("patagonia/rionegro/leerblogRioNegro/<blogrionegro_id>", leerblogRioNegro)


]