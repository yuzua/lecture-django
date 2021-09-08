from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.views import generic
from django.urls import reverse_lazy
from .forms import InquiryForm
import logging

logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
    template_name="diary/index.html"

class InquiryView(generic.FormView):
    template_name="diary/inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('diary:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request,'メッセージを送信しました。')
        logger.info('Inquiry set by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)