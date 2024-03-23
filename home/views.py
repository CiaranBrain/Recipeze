from django.shortcuts import render
from django.views.generic import TemplateView


class Index(TemplateView):
    """Renders the main index page of the application."""

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class About(TemplateView):
    """Renders the "About Us" page of the application."""
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
