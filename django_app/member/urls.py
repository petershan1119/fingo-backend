from django.conf.urls import url
from member import views


urlpatterns = [
    url(r'^login/$', views.UserLogin.as_view()),
    url(r'^logout/$', views.UserLogout.as_view()),
    url(r'^signup/$', views.UserSignUp.as_view()),
    url(r'^activate/(?P<hash>.*)/$', views.UserActivate.as_view()),
    url(r'^upload_profile/$', views.UserProfileImgUpload.as_view()),
    url(r'^fb_login/$', views.UserFacebookLogin.as_view()),
    url(r'^fb_user_img/$', views.FacebookUserImageUpload.as_view()),
]