from django import forms
from django.core.mail import send_mail

class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=75)
    mensagem = forms.CharField(widget=forms.Textarea())

    def enviar_email(self):
        remetente = '%(nome)s <%(email)s>' % self.cleaned_data
        assunto = 'Contato enviado pelo site'
        mensagem = self.cleaned_data['mensagem']
        destinatario = 'francisco.souza@giran.com.br'
        send_mail(assunto, mensagem, remetente, [destinatario,], fail_silently=False)
