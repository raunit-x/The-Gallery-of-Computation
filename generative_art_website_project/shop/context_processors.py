from .forms import NewsletterForm


def newsletter_form(request):
    return {'newsletter_form': NewsletterForm()}
