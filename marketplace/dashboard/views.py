from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from item.models import Item
from .forms import EditItem


@login_required
def listItems(request):
    item = Item.objects.filter(created_by=request.user)
    print(item)
    return render(request, "dashboard/dashboard.html", {"item": item})


@login_required
def editItems(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == "POST":
        form = EditItem(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("item:detail", pk=item.id)
    else:
        form = EditItem()

    return render(request, "dashboard/edit_item.html", {"form": form})


@login_required
def deleteItem(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect("item:dashboard:listItems")
