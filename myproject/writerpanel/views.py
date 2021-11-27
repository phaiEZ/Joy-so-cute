from django.shortcuts import render
from blogs.models import Blogs
from django.db.models import Sum


def panel(request):
    writer = "pleumssr"
    blogs = Blogs.objects.filter(writer=writer)
    blogCount = blogs.count()
    countView = 0
    for blog in blogs:
        countView += blog.views
    print(countView)
    # countView = Blogs.objects.filter(writer=writer).aggregate(Sum("views"))
    # from krs

    return render(request, "backend/index.html", {"blogs": blogs, "writer": writer, "blogCount": blogCount, "countView": countView})
