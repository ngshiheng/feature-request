from .models import Request
from .forms import RequestForm
from django.views.generic import ListView, CreateView


# class RequestListView(ListView):
#     model = Request
#     template_name = 'feature_request/index.html'
#     context_object_name = 'requests'
#     ordering = ['-target_date']


class RequestCreateView(CreateView):
    model = Request
    template_name = 'feature_request/index.html'
    form_class = RequestForm

    def form_valid(self, form):
        form.instance.submitter = self.request.user
        return super().form_valid(form)
