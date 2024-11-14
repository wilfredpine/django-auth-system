from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy

from django.core.exceptions import PermissionDenied

# Create your views here.

@login_required
def index(request):
    
    # user role validation
    if not request.user.is_staff:
        return render(request, 'index.html')
    else:
        raise PermissionDenied  # Deny access for non-staff users
    
class change_password(LoginRequiredMixin, PasswordChangeView):
    template_name = 'change_password.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['validlink'] = True
        context['page_name'] = 'account'
        return context