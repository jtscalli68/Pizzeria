from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'Pizzas/index.html')

def pizzas(request):
    pizzas = Pizza.objects.order_by('date_added')

    context = {'all_pizzas': pizzas}

    return render(request, 'Pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    p = Pizza.objects.get(id=pizza_id)

    toppings = Topping.objects.filter(pizza=p)

    context = {'pizza': p, 'toppings':toppings}

    return render(request, 'Pizzas/pizza.html', context)


def new_comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    text = Comment.objects.filter(pizza=p)


    if request.method != 'POST':
        form = CommentForm()

    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.pizza = pizza
            new_comment.text = text
            new_comment.save()
            return redirect('Pizzas:pizza', pizza_id=pizza_id)


    context = {'form':form, 'text':text, 'pizza':pizza}
    return render(request, 'Pizzas/new_comment.html', context)

        