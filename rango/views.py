from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Category, Page
from .forms import CategoryForm, PageForm, UserForm, UserProfileForm


# Create your views here.
def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list,'pages':page_list}
    return render(request,'rango/index.html', context_dict)


def about(request):
    return HttpResponse("URL sites")


def category(request, category_name_slug):
    context_dict = {}
    try:
        cat = Category.objects.get(slug=category_name_slug)
        # cat = get_object_or_404(Category,slug=category_name_slug)
        context_dict['category_name'] = cat.name

        pages = Page.objects.filter(category=cat)

        context_dict['pages'] = pages
        context_dict['category'] = cat
    except (KeyError,Category.DoesNotExist):
        pass

    return render(request,'rango/category.html',context_dict)


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            cat = form.save(commit=True)
            print(cat, cat.slug)
            return index(request)
        else:
            print(form.errors)
    else:
        form = CategoryForm()
    return render(request,'rango/add_category.html',{'form':form})


def add_page(request):

    if request.method == 'POST':
        form = PageForm(request.POST,)

        if form.is_valid():
            page = form.save(commit=True)
            print(page)
            page.save()
            # TODO: use a redirect here
            return index(request)
        else:
            print(form.errors)
    else:
        form = PageForm()
    context_dict = {'form':form}

    return render(request,'rango/add_page.html',context_dict)

#
# def register(request):
#     registered = False
#     if request.method == 'POST':
#         user_form = UserForm(data=request.POST)
#         profile_form = UserProfileForm(data=request.POST)
#
#     if user_form.is_valid() and profile_form.is_valid():
#         user = user_form.save()
#         user.set_password(user.password)
#         user.save()



