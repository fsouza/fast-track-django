# -*- coding: utf-8 -*-
import json
from newsletter.forms import NewsletterForm
from django.http import HttpResponse

def cadastrar_newsletter(request):
    if request.method != 'POST':
        response = HttpResponse("Method not allowed.")
        response.status_code = 405
        return response

    form = NewsletterForm(request.POST)
    if form.is_valid():
        form.save()
        out = { 'status' : u'Ok', 'mensagem' : u'E-mail gravado com sucesso!' }
    else:
        out = { 'status' : u'Erro', 'mensagem' : form.errors['email'][0] }

    json_content = json.dumps(out)
    return HttpResponse(json_content, mimetype='application/json')
