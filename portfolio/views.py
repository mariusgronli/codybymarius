from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomepageView(TemplateView):
    template_name="portfolio/index.html"

class CvpageView(TemplateView):
    template_name="portfolio/cv.html"
