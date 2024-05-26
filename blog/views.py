from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, LoginForm, CommentForm, PostForm
from .models import Post, Comment
from django.contrib.auth.mixins import UserPassesTestMixin


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "home.html"
    paginate_by = 6


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=request.user.id).exists():
            liked = True

        show_map = post.latitude is not None and post.longitude is not None

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
                "show_map": show_map
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False

        if post.likes.filter(id=request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, 'Your comment was submitted successfully!')
            return redirect('post_detail', slug=post.slug)
        else:
            messages.error(request, 'There was an error with your comment.')

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked,
                "show_map": post.latitude is not None and post.longitude is not None
            },
        )


class PostLike(View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            messages.success(request, 'You unliked the post.')
        else:
            post.likes.add(request.user)
            messages.success(request, 'You liked the post.')

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'edit_post.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def get_success_url(self):
        messages.success(self.request, 'Post updated successfully.')
        return reverse_lazy('post_detail', kwargs={'slug': self.object.slug})


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'
    context_object_name = 'post'
    success_url = reverse_lazy('home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Post deleted successfully.')
        return super().delete(request, *args, **kwargs)


class SignUpView(View):
    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully.')
            return redirect('home')
        return render(request, 'registration/signup.html', {'form': form})


class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.warning(request, 'You are already logged in.')
            return redirect('home')
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.warning(request, 'You are already logged in.')
            return redirect('home')

        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
        return render(request, 'registration/login.html', {'form': form})


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'Logout successful.')
        return redirect('home')


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'registration/profile.html', {'user': request.user})


@method_decorator(login_required, name='dispatch')
class EditProfileView(View):
    def get(self, request, *args, **kwargs):
        form = EditProfileForm(instance=request.user)
        return render(request, 'registration/edit_profile.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('account_profile')
        return render(request, 'registration/edit_profile.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class DeleteAccountView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'registration/delete_account.html')

    def post(self, request, *args, **kwargs):
        user = request.user
        logout(request)
        user.delete()
        messages.success(request, 'Account deleted successfully.')
        return redirect('home')


class PostCreateView(LoginRequiredMixin, View):
    form_class = PostForm
    template_name = 'post_create.html'
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.status = 1
            new_post.save()
            messages.success(request, 'Blog post created successfully!')
            return redirect('home')
        return render(request, self.template_name, {'form': form})


class PostListView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    paginate_by = 6


class MapView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.exclude(latitude__isnull=True).exclude(longitude__isnull=True)
        return render(request, 'map.html', {'posts': posts})


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ['body']
    template_name = 'edit_comment.html'
    context_object_name = 'comment'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def get_success_url(self):
        messages.success(self.request, 'Comment updated successfully.')
        return reverse_lazy('post_detail', kwargs={'slug': self.object.post.slug})


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'delete_comment.html'
    context_object_name = 'comment'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def get_success_url(self):
        messages.success(self.request, 'Comment deleted successfully.')
        return reverse_lazy('post_detail', kwargs={'slug': self.object.post.slug})