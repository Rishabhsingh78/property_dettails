from django.urls import path
from .views import ParsePDFView

urlpatterns = [
    path('parse-pdf/', ParsePDFView.as_view(), name='parse_pdf')
]
