from forms import NewsletterForm

def newsletter_form(request):
    form = NewsletterForm()
    return { 'newsletter_form' : form }
