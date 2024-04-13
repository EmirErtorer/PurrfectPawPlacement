from django.urls import path
from .views import GeneralUserSignUpView, ShelterSignUpView, CustomLoginView

urlpatterns = [
    path('signup/general/', GeneralUserSignUpView.as_view(), name='general_signup'),
    path('signup/shelter/', ShelterSignUpView.as_view(), name='shelter_signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
]