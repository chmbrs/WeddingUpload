from django.views.generic import TemplateView

class TestPage(TemplateView):
    """docstring forTestPage."""
    template_name = 'test.html'

class ThanksPage(TemplateView):
    """docstring for ThanksPage."""
    template_name = 'thanks.html'


class HomePage(TemplateView):
    template_name = 'index.html'
