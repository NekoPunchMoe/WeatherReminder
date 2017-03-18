from django.conf.urls import url
from django.contrib import admin
import reminder.views as reminder_views

urlpatterns = [
   url(r'^$', reminder_views.manage),
   url(r'^admin/', admin.site.urls),
   url(r'^del_reminder/', reminder_views.del_reminder),
]