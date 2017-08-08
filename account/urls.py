from django.conf.urls import url

from account.views import RegisterUserView

urlpatterns = [
    # /account/register
    url(r'^register/$', view=RegisterUserView.as_view(), name='register'),
]