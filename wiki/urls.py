from django.urls import path
from wiki.views import PageListView, PageDetailView, CreatePageView



urlpatterns = [
    path('', PageListView.as_view(), name='wiki-list-page'),
    path('new/', CreatePageView.as_view(), name='new_page'),
    # this path must always go last because it's not exact and can take any input with its slug
    path('<str:slug>/', PageDetailView.as_view(), name='wiki-details-page'),
]
