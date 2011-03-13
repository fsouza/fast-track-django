# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from contato.forms import ContatoForm

def contato(request):
    template_name = "contato_form.html"
    form = ContatoForm()
    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.enviar_email()
            messages.success(request, "Contato enviado com sucesso!")
            return HttpResponseRedirect(reverse("contato"))
    return render_to_response(template_name, {
            'form' : form
        }, context_instance=RequestContext(request)
    )
