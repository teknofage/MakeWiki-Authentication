from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

from wiki.models import Page
from api.serializers import PageSerializer
from api.serializers import ChoiceSerializer

class PageList(ListCreateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class PageDetail(RetrieveDestroyAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer