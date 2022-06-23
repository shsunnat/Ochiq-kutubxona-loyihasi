from django.urls import path
from .views import SignUpView

# ====THIS IS OUR SIGNUP URL LINK FOR ENTER WEBSITE=======

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]

