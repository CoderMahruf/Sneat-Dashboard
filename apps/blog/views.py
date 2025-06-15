
from django.views.generic import ListView,CreateView
from web_project import TemplateLayout
from .models import Blog


class BasedView(ListView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))
        return context

class BlogView(BasedView):
    template_name = "blogs.html"
    model = Blog
    context_object_name = "blogs"
    paginate_by  = 5
