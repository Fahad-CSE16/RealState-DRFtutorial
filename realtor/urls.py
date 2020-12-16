from django.urls import path
from .views import AgentDetailView,AgentListView, TopSellerListView
urlpatterns = [
    path('',AgentListView.as_view(),name='agents' ),
    path('<pk>/',AgentDetailView.as_view(),name='agent-detail' ),
    path('topseller',TopSellerListView.as_view(),name='topseller' ),
    ]