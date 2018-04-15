from django.urls import path

from views.views import AboutView, PublishersView, ShowPublisher

urlpatterns = [
    path('templateview/', AboutView.as_view()),
    path('listview/', PublishersView.as_view()),
    path(r'listview/(?P<pk>[0-9]+)/$', ShowPublisher.as_view(), name = 'show_publisher'),
]