from django.shortcuts import render, redirect
from .models import Request, ProductArea, Client


def index(request):
    requests = Request.objects.all().order_by('priority')
    clients = Client.objects.all()
    product_areas = ProductArea.objects.all()

    # Submit request
    if request.method == "POST":
        if "taskAdd" in request.POST:
            title = request.POST["title"]
            description = request.POST["description"]
            client = request.POST["client_select"]
            priority = request.POST["priority"]
            date = str(request.POST["date"])
            product_area = request.POST["product_area_select"]

            request_object = Request(title=title,
                                     description=description,
                                     client=Client.objects.get(client=client),
                                     priority=priority,
                                     target_date=date,
                                     product_area=ProductArea.objects.get(product_area=product_area)
                                     )
            request_object.save()

            return redirect("/")

        # Delete a single request at a time
        if "taskDelete" in request.POST:
            try:
                selected_request_id = request.POST["checkedbox"]
                req = Request.objects.get(id=selected_request_id)
                req.delete()

            # do nothing if no checked box:
            except:
                pass

    return render(request, "feature_request/index.html",
                  {"requests": requests, "clients": clients, "product_areas": product_areas, })
