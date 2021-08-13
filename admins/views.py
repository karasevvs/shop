from django.shortcuts import render, HttpResponseRedirect
from users.models import User
from products.models import ProductCategory, Product
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm, ProductCategoryAdminProfileForm, \
    ProductAdminProfileForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator


@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {'title': 'Админ-панель'}
    return render(request, 'admins/index.html', context)


class UserListView(ListView):
    model = User
    template_name = 'admins/admin-users-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data(object_list=None, **kwargs)
        context['title'] = 'Админ-панель - Пользователи'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, *args, **kwargs)


class UserCreateView(CreateView):
    model = User
    form_class = UserAdminRegistrationForm
    template_name = 'admins/admin-users-create.html'
    success_url = reverse_lazy('admins:admin_users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserCreateView, self).get_context_data(object_list=None, **kwargs)
        context['title'] = 'Админ-панель - Создание пользователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, *args, **kwargs)


class UserUpdateView(UpdateView):
    model = User
    form_class = UserAdminProfileForm
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserUpdateView, self).get_context_data(object_list=None, **kwargs)
        context['title'] = 'Админ-панель - Редактирование пользователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)


class UserDeleteView(DeleteView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserDeleteView, self).get_context_data(object_list=None, **kwargs)
        context['title'] = 'Админ-панель - Удаление пользователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserDeleteView, self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# Работа с категориями


class CategoryListView(ListView):
    model = ProductCategory
    template_name = 'admins/admin-category-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryListView, self).get_context_data(object_list=None, **kwargs)
        context['title'] = 'Админ-панель - Категории'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryListView, self).dispatch(request, *args, **kwargs)


class CategoryUpdateView(UpdateView):
    model = ProductCategory
    form_class = ProductCategoryAdminProfileForm
    template_name = 'admins/admin-category-update-delete.html'
    success_url = reverse_lazy('admins:admin_category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryUpdateView, self).get_context_data(object_list=None, **kwargs)
        context['title'] = 'Админ-панель - Редактирование категории'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryUpdateView, self).dispatch(request, *args, **kwargs)


class CategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryDeleteView, self).get_context_data(object_list=None, **kwargs)
        context['title'] = 'Админ-панель - Удаление категории'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryDeleteView, self).dispatch(request, *args, **kwargs)


class CategoryCreateView(CreateView):
    model = ProductCategory
    form_class = ProductCategoryAdminProfileForm
    template_name = 'admins/admin-category-create.html'
    success_url = reverse_lazy('admins:admin_category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryCreateView, self).get_context_data(object_list=None, **kwargs)
        context['title'] = 'Админ-панель - Создание категории'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryCreateView, self).dispatch(request, *args, **kwargs)


# Работа с продуктами


class ProductListView(ListView):
    model = Product
    template_name = 'admins/admin-products-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data(object_list=None, **kwargs)
        context['title'] = 'Админ-панель - Продукты'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductListView, self).dispatch(request, *args, **kwargs)


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductAdminProfileForm
    template_name = 'admins/admin-products-create.html'
    success_url = reverse_lazy('admins:admin_product')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductCreateView, self).get_context_data(object_list=None, **kwargs)
        context['title'] = 'Админ-панель - Создание продукта'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductCreateView, self).dispatch(request, *args, **kwargs)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductAdminProfileForm
    template_name = 'admins/admin-products-update-delete.html'
    success_url = reverse_lazy('admins:admin_product')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(object_list=None, **kwargs)
        context['title'] = 'Админ-панель - Редактирование продукта'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductUpdateView, self).dispatch(request, *args, **kwargs)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    success_url = reverse_lazy('admins:admin_product')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductDeleteView, self).get_context_data(object_list=None, **kwargs)
        context['title'] = 'Админ-панель - Удаление продукта'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductDeleteView, self).dispatch(request, *args, **kwargs)

# @user_passes_test(lambda u: u.is_staff)
# def admin_users(request):
#     context = {
#         'title': 'Админ-панель - Пользователи',
#         'users': User.objects.all()}
#     return render(request, 'admins/admin-users-read.html', context)


# @user_passes_test(lambda u: u.is_staff)
# def admin_users_create(request):
#     if request.method == 'POST':
#         form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_users'))
#         else:
#             print(form.errors)
#     else:
#         form = UserAdminRegistrationForm()
#     context = {'title': 'Админ-панель - Создание пользователя',
#                'form': form}
#     return render(request, 'admins/admin-users-create.html', context)


# @user_passes_test(lambda u: u.is_staff)
# def admin_users_update(request, pk):
#     selected_user = User.objects.get(id=pk)
#     if request.method == 'POST':
#         form = UserAdminProfileForm(instance=selected_user, files=request.FILES, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_users'))
#     form = UserAdminProfileForm(instance=selected_user)
#     context = {'title': 'Админ-панель - Редактирование пользователя',
#                'form': form,
#                'selected_user': selected_user,
#                }
#     return render(request, 'admins/admin-users-update-delete.html', context)


# @user_passes_test(lambda u: u.is_staff)
# def admin_users_remove(request, pk):
#     user = User.objects.get(id=pk)
#     # user.delete()
#     user.is_active = False
#     user.save()
#     return HttpResponseRedirect(reverse('admins:admin_users'))


# Категории продуктов


# @user_passes_test(lambda u: u.is_staff)
# def admin_category(request):
#     context = {
#         'title': 'Админ-панель - Категории',
#         'categories': ProductCategory.objects.all()}
#     return render(request, 'admins/admin-category-read.html', context)


# @user_passes_test(lambda u: u.is_staff)
# def admin_category_update(request, pk):
#     selected_category = ProductCategory.objects.get(id=pk)
#     if request.method == 'POST':
#         form = ProductCategoryAdminProfileForm(instance=selected_category, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_category'))
#     form = ProductCategoryAdminProfileForm(instance=selected_category)
#     context = {'title': 'Админ-панель - Редактирование категории',
#                'form': form,
#                'selected_category': selected_category,
#                }
#     return render(request, 'admins/admin-category-update-delete.html', context)


# @user_passes_test(lambda u: u.is_staff)
# def admin_category_remove(request, pk):
#     name = ProductCategory.objects.get(id=pk)
#     name.delete()
#     return HttpResponseRedirect(reverse('admins:admin_category'))


# @user_passes_test(lambda u: u.is_staff)
# def admin_category_create(request):
#     if request.method == 'POST':
#         form = ProductCategoryAdminProfileForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_category'))
#         else:
#             print(form.errors)
#     else:
#         form = ProductCategoryAdminProfileForm()
#     context = {'title': 'Админ-панель - Создание категории',
#                'form': form}
#     return render(request, 'admins/admin-category-create.html', context)


# работа с продуктами


# @user_passes_test(lambda u: u.is_staff)
# def admin_product(request):
#     context = {
#         'title': 'Админ-панель - Продукты',
#         'products': Product.objects.all()}
#     return render(request, 'admins/admin-products-read.html', context)


# @user_passes_test(lambda u: u.is_staff)
# def admin_products_create(request):
#     if request.method == 'POST':
#         form = ProductAdminProfileForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_product'))
#         else:
#             print(form.errors)
#     else:
#         form = ProductAdminProfileForm()
#
#     context = {'title': 'Админ-панель - Создание продукта',
#                'form': form,
#                }
#     return render(request, 'admins/admin-products-create.html', context)


# @user_passes_test(lambda u: u.is_staff)
# def admin_products_update(request, pk):
#     selected_product = Product.objects.get(id=pk)
#     if request.method == 'POST':
#         form = ProductAdminProfileForm(instance=selected_product, files=request.FILES, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_product'))
#     form = ProductAdminProfileForm(instance=selected_product)
#     context = {'title': 'Админ-панель - Редактирование продукта',
#                'form': form,
#                'selected_product': selected_product,
#                }
#     return render(request, 'admins/admin-products-update-delete.html', context)


# @user_passes_test(lambda u: u.is_staff)
# def admin_products_remove(request, pk):
#     product = Product.objects.get(id=pk)
#     product.delete()
#     return HttpResponseRedirect(reverse('admins:admin_product'))

