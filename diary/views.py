from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import InquiryForm
import logging

logger = logging.getLogger(__name__)

# Create your views here.
# def index(request):
#     return render(request, 'diary/index.html')

class IndexView(generic.TemplateView):
    template_name="diary/index.html"

class InquiryView(generic.FormView):
    template_name="diary/inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('diary:inquiry')

    def form_valid(self, form):
        form.send_email()
        logger.info('Inquiry set by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)