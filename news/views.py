from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Post
from .filters import PostFilter
from .forms import NewsForm, ArticlesForm


class PostList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post
    # Поле, которое будет использоваться для сортировки объектов
    ordering = '-date_creation'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'flatpages/posts.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'posts'
    # Указываем кол-во записей на странице
    paginate_by = 10


class PostSearchList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post
    # Поле, которое будет использоваться для сортировки объектов
    ordering = '-date_creation'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'flatpages/posts_search.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'posts'
    # Указываем кол-во записей на странице
    paginate_by = 10

    # Переопределяем функцию получения списка товаров
    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Post
    # Используем другой шаблон — product.html
    template_name = 'flatpages/post.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'post'


# Добавляем новые представления для создания постов.
class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('simpleapp.add_post',)
    # Указываем нашу разработанную форму
    form_class = NewsForm
    # модель постов
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'flatpages/post_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author_id = 1  # Временное поле
        post.category_type = 'NW'
        return super().form_valid(form)


class ArticlesCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('simpleapp.add_post',)
    # Указываем нашу разработанную форму
    form_class = ArticlesForm
    # модель постов
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'flatpages/post_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author_id = 1  # Временное поле
        post.category_type = 'AR'
        return super().form_valid(form)


# Добавляем новые представления для создания постов.
class NewsUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('simpleapp.change_post',)
    # Указываем нашу разработанную форму
    form_class = NewsForm
    # модель постов
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'flatpages/post_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.category_type = 'NW'
        return super().form_valid(form)


class ArticlesUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('simpleapp.change_post',)
    # Указываем нашу разработанную форму
    form_class = ArticlesForm
    # модель постов
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'flatpages/post_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.category_type = 'AR'
        return super().form_valid(form)


# Представление удаляющее пост.
class NewsDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('simpleapp.delete_post',)
    model = Post
    template_name = 'flatpages/post_delete.html'
    success_url = reverse_lazy('post_list')


class ArticlesDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('simpleapp.delete_post',)
    model = Post
    template_name = 'flatpages/post_delete.html'
    success_url = reverse_lazy('post_list')

