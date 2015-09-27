from django.conf.urls import url

from .views import HomeView

urlpatterns = [
    url(r'^$', HomeView.as_view(template_name="home.html"), name="home"),
    url(r'^faq$', HomeView.as_view(template_name="faq.html"), name="faq"),
    url(r'^shelters-need-help/$', HomeView.as_view(template_name="shelters_need_help.html"), name="home"),
]
