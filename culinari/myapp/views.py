from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, get_object_or_404, redirect
from PIL import Image

from .forms import RecipeForm, UserCreationForm
from .models import Category, Recipe, User


def home(request):
    list_categories = Category.objects.all()
    recipes = Recipe.objects.all().order_by('-id')[:5]
    return render(request, 'myapp/home.html', {'list_categories': list_categories, 'recipes': recipes})


def all_recipe(request):
    recipes_order = Recipe.objects.all()
    return render(request, 'myapp/recipes.html', {'recipes_order': recipes_order})


def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_recipe')
    else:
        form = RecipeForm()
    return render(request, 'myapp/add_recipes.html', {'form': form})


def recipe_full(request, category_id):
    list_recipe_cagory = get_object_or_404(Category.objects, id=category_id)
    lisrt_recipe = Recipe.objects.filter(category_recipe=list_recipe_cagory)
    return render(request, 'myapp/recipe_full.html',
                  {'list_recipe_cagory': list_recipe_cagory, 'lisrt_recipe': lisrt_recipe})


def user_logout(request):
    logout(request)
    return redirect('home')


def recept_text(request, id_recipe):
    recipes_order = Recipe.objects.filter(pk=id_recipe)
    return render(request, 'myapp/manual.html', {'recipes_order': recipes_order})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


def user_login(request, author_id):
    list_recipes = Recipe.objects.filter(author_id=author_id)

    return render(request, 'myapp/user.html', {"list_recipes": list_recipes})


def create_recipe(request, id_recipe):
    recipe = get_object_or_404(Recipe, id=id_recipe)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recept_text', id_recipe)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'myapp/create_recipe.html', {'form': form})


def delete_recipe(request, id_recipe):
    recipe = get_object_or_404(Recipe, id=id_recipe)
    if recipe is not None:
        recipe.delete()
    return redirect('home')


def delete_user(request, id_user):
    user = get_object_or_404(User, id=id_user)
    if user is not None:
        user.delete()
    return redirect('home')

# Create your views here.
