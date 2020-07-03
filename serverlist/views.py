from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, DeleteView
from serverlist.forms import *
from serverlist.models import Server, ServerIP


class ServerList(ListView):
    template_name = 'index.html'
    model = Server
    context_object_name = 'servers'


class ServerInfo(DetailView):
    model = Server
    template_name = 'server_info.html'

    def get_context_data(self, **kwargs):
        context = super(ServerInfo, self).get_context_data(**kwargs)
        server = Server.objects.get(pk=self.kwargs['pk'])
        if not server.parent:
            context['list'] = Server.objects.filter(parent=self.kwargs['pk'])
        context['ip_list'] = ServerIP.objects.filter(server=self.kwargs['pk'])
        return context


class CreateServer(TemplateView):
    template_name = 'add_server.html'
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        kwargs['form'] = ServerCreationForm()
        kwargs['ip_form'] = ServerIpFormSet()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = ServerCreationForm(request.POST)
        if form.is_valid():
            new_server = form.save(commit=False)
            if 'pk' in self.kwargs:
                server = Server.objects.get(pk=self.kwargs['pk'])
                new_server.parent = server
            ip_form = ServerIpFormSet(request.POST, instance=new_server)
            if ip_form.is_valid():
                new_server.save()
                ip_form.save()
        else:
            print(form.errors)
        return HttpResponseRedirect(self.success_url)


class UpdateServer(TemplateView):
    template_name = 'add_server.html'
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        server = get_object_or_404(Server, pk=self.kwargs['pk'])
        kwargs['form'] = ServerCreationForm(instance=server)
        kwargs['ip_form'] = ServerIpFormSet(instance=server)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        server = get_object_or_404(Server, pk=self.kwargs['pk'])
        update_form = ServerCreationForm(request.POST, instance=server)
        ip_form = ServerIpFormSet(request.POST, instance=server)
        if update_form.is_valid() and ip_form.is_valid():
            update_form.save()
            ip_form.save()
        else:
            print(ip_form.errors)
        return HttpResponseRedirect(self.success_url)


class DeleteServer(DeleteView):
    model = Server
    success_url = reverse_lazy('home')
    template_name = 'delete_confirm.html'
