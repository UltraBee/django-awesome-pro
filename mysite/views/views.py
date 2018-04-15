from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from views.models import *

class AboutView(TemplateView):
    template_name = "views/templateview.html"

class PublishersView(ListView):
    model = Publisher
    context_object_name="publisher_list"

class ShowPublisher(DetailView):
    model = Publisher
    context_object_name = "publisher"
    # template_name = "views/templateview.html"
