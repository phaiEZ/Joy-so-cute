from django.contrib.auth import login
from django.shortcuts import render
from blogs.models import Blogs
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth


@login_required(login_url="member")
def panel(request):
    writer = auth.get_user(request)
    blogs = Blogs.objects.filter(writer=writer)
    blogCount = blogs.count()
    countView = 0
    for blog in blogs:
        countView += blog.views
    print(countView)
    # countView = Blogs.objects.filter(writer=writer).aggregate(Sum("views"))
    # from krs ^

    return render(request, "backend/index.html", {"blogs": blogs, "writer": writer, "blogCount": blogCount, "countView": countView})


def displayForm(request):
    writer = auth.get_user(request)
    blogs = Blogs.objects.filter(writer=writer)
    blogCount = blogs.count()
    countView = 0
    for blog in blogs:
        countView += blog.views
    print(countView)
    # countView = Blogs.objects.filter(writer=writer).aggregate(Sum("views"))
    # from krs ^

    return render(request, "backend/blogForm.html", {"blogs": blogs, "writer": writer, "blogCount": blogCount, "countView": countView})
