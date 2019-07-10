from django.shortcuts import render, redirect
from .models import Request, ProductArea


def index(request):
    requests = Request.objects.all()
    product_areas = ProductArea.objects.all()

    if request.method == "POST":
        if "taskAdd" in request.POST:
            title = request.POST["title"]
            description = request.POST["description"]
            client = request.POST["client_select"]
            priority = request.POST["priority"]
            date = str(request.POST["date"])
            product_area = request.POST["product_area_select"]

            Todo = Request(title=title,
                           description=description,
                           client=client,
                           priority=priority,
                           target_date=date,
                           product_area=ProductArea.objects.get(product_area=product_area)
                           )
            Todo.save()
            return redirect("/")

        if "taskDelete" in request.POST:
            checkedlist = request.POST["checkedbox"]

            for todo_id in checkedlist:
                todo = Request.objects.get(id=int(todo_id))
                todo.delete()

    return render(request, "feature_request/index.html", {"requests": requests, "product_areas": product_areas})
