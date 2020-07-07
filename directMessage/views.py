from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import directMessage
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# Create your views here.
class MessageCreateView(LoginRequiredMixin, CreateView):
    model = directMessage
    fields = ['text']

    template_name = 'directMessage/create_message.html'

    def form_valid(self, form):
        form.instance.message_from = self.request.user
        name =  self.kwargs['name']
        userObject = User.objects.get(username=name)
        form.instance.message_to = userObject
        return super().form_valid(form)

def MessageListView(request):

    userAccessingWeb = request.user
    userMessages = directMessage.objects.filter(message_to=userAccessingWeb)
    

    return render(request, 'directMessage/messages.html', {'messages_inbox': userMessages})

