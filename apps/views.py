from audioop import reverse

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm, BlogForm
from .models import Category, Product, Blog_category, Blog, Blog_comment
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect

from .models import Product, ProductCategory


def post_list(request):
    posts = Post.objects.all().order_by('-created_date')
    return render(request, 'post_list.html', {'posts': posts})


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog-list-left-sidebar.html', {'form': form})


def a_blog(request):
    context = {
        'categories': Blog_category.objects.all()
    }
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Blog')
    return render(request, 'apps/add_blog.html', context)


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, '',
                  {'category': category, 'categories': categories, 'products': products})


def w_comment_blog(request, pk):
    if request.method == 'POST':
        blog = Blog.objects.get(pk=pk)
        Blog_comment.objects.create(body=request.POST['body'], blog=blog)
    return redirect(reverse('one_blog', kwargs={'pk': pk}))


def blog(request):
    category_id = request.GET.get('category', 0)
    if category_id:
        blogss = Blog.objects.filter(category_id=category_id)
    else:
        blogss = Blog.objects.all()
    context = {
        'blogs': blogss,
        'categories': Blog_category.objects.all()
    }
    return render(request, 'apps/blog_list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'blog-list-left-sidebar.html', {'product': product})


def one_blog(request, pk):
    blog = Blog.objects.get(id=pk)
    comments = Blog_comment.objects.filter(blog=blog)
    context = {
        'blog': blog,
        'comments': comments
    }
    return render(request, 'apps/blog_detail.html', context)


def product_list(request, category_slug=None):
    category = None
    categories = ProductCategory.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(ProductCategory, slug=category_slug)
        products = products.filter(category=category)
    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    context = {'product': product}
    return render(request, 'shop/product/detail.html', context)
