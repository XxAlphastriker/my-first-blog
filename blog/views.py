from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from django.views.generic import CreateView, TemplateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from .models import Perfil

from .forms import SignUpForm

class SignUpView(CreateView):
    model = Perfil
    form_class = SignUpForm

    def form_valid(self, form):
        '''
        Comprobamos si el formulario es valido y lo guardamos, para que luego el usuario incie sesion y lo redirigamos al IndexError
        '''

        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/')

class BienvenidaView(TemplateView):
    template_name = 'blog/bienvenida.html'

class SignInView(LoginView):
    template_name = 'blog/iniciar_sesion.html'

class SignOutView(LogoutView):
    pass

def UploadCurse(request):
    return render(request, 'blog/curso.html')

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html',{'post': post})
