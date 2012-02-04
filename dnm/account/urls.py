from account.forms import SignupFormExtra
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    (r'^signup', 'userena.views.signup', {'signup_form': SignupFormExtra}),
)