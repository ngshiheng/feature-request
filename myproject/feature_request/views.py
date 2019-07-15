from django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect
from .forms import RequestForm
from .models import Request


def index(request):
    form = RequestForm(request.POST)
    request_list = Request.objects.all()

    # If this is a POST request then process the Form data
    if request.method == "POST":

        # When 'Add Request' is clicked:
        if "taskAdd" in request.POST:
            if form.is_valid():
                form.save()

                # Reorder all the features' priority after adding a new request
                request_list = Request.objects.order_by('priority', '-id')
                for i, req in enumerate(request_list, 1):
                    Request.objects.filter(id=req.id).update(priority=i)

                return HttpResponseRedirect(reverse('index'))

        # When 'Delete Request' is clicked:
        if "taskDelete" in request.POST:
            try:
                selected_request_id = request.POST["checkedbox"]
                req = Request.objects.get(id=selected_request_id)
                req.delete()

                # Reorder all the features' priority after removing a request
                request_list = Request.objects.all()
                for i, req in enumerate(request_list, 1):
                    Request.objects.filter(id=req.id).update(priority=i)

                return HttpResponseRedirect(reverse('index'))

            # Do nothing if no requests are selected
            except:
                pass

    # If this is a GET (or any other method) create the default form.
    else:
        form = RequestForm()
        request_list = Request.objects.all()

    context = {
        'form': form,
        'request_list': request_list,
    }

    return render(request, 'feature_request/index.html', context)
