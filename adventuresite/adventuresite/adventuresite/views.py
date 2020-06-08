from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    """docstring for HomePageView."""
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class AboutView(TemplateView):
    """docstring for AboutView."""
    template_name = 'about.html'

class PlacesView(TemplateView):
    """docstring for AboutView."""
    template_name = 'places/places.html'
