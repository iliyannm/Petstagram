from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from petstagram_app.accounts.views import UserLoginView, ProfileDetailsView, UserRegisterView, ChangeUserPasswordView, \
    UserLogoutView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login user'),
    path('profile/<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('profile/create/', UserRegisterView.as_view(), name='create profile'),
    path('edit-password/', ChangeUserPasswordView.as_view(), name='change password'),
    path('password_change_done/', RedirectView.as_view(url=reverse_lazy('dashboard')), name='password_change_done'),
    path('logout/', UserLogoutView.as_view(next_page=reverse_lazy('index')), name='logout user'),
    # path('profile/edit/', edit_profile, name='edit profile'),
    # path('profile/delete/', delete_profile, name='delete profile'),
)
