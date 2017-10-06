from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.intake_form, name='index'),
    url(r'^pet/new/$', views.pet_new, name='pet_new'),
    url(r'^intake_form/$', views.intake_form, name='intake_form'),
    url(r'^intake_summary/$', views.intake_summary, name='intake_summary'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    # url(r'^admin/', admin.site.urls),
]