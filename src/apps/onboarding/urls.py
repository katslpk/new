from django.urls import path


from apps.onboarding.views.index import IndexView
from apps.onboarding.apps import OnboardingConfig
from apps.onboarding.views.sign_in import SignInView
from apps.onboarding.views.sign_in_verified import SignInVerifiedView
from apps.onboarding.views.sign_up_confirmed import SignUpConfirmedView
from apps.onboarding.views.sign_up import SignUpView
from apps.onboarding.views.main import ProfileView
from apps.onboarding.views.main_edit import ProfileEditView



app_name = OnboardingConfig.label

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("sign_in/", SignInView.as_view(), name="sign_in",),
    path("sign_in/<str:code>/", SignInVerifiedView.as_view(), name="sign_in_verified",),
    path("sign_up/", SignUpView.as_view(), name="sign_up"),
    path("sign_up/confirmed/", SignUpConfirmedView.as_view(), name="sign_up_confirmed"),
    path("main/", ProfileView.as_view(), name="main"),
    path("main/edit/", ProfileEditView.as_view(), name="main_edit"),
]
