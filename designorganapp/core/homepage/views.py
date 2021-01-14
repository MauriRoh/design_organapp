from django.views.generic import TemplateView

# Renderiza los Template.
class IndexView(TemplateView):
    template_name = 'index.html'
