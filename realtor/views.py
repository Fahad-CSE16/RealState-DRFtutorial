from rest_framework import permissions
from rest_framework.generics import ListAPIView,ListCreateAPIView, RetrieveAPIView,RetrieveDestroyAPIView, RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .models import Agent
from .serializers import AgentSerializer
class AgentListView(ListAPIView):
    permission_classes=(permissions.AllowAny,)
    queryset=Agent.objects.all()
    serializer_class=AgentSerializer
    pagination_class=None
class AgentDetailView(RetrieveAPIView):
    queryset=Agent.objects.all()
    serializer_class=AgentSerializer
class TopSellerListView(ListAPIView):
    permission_classes=(permissions.AllowAny,)
    queryset=Agent.objects.filter(top_seller=True)
    serializer_class=AgentSerializer
    pagination_class=None
