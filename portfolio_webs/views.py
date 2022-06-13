from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from decouple import config

from . forms import ContactForm

# Create your views here.
def index(request):
    """Creating a homepage view"""
    return render(request, 'portfolio_webs/index.html')

""" def skills(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'portfolio_webs/skills.html') """

def about(request):
    """Creating a contact page"""
    return render(request, 'portfolio_webs/about.html')

def contact(request):
    """Gathering user data and sending email"""
    if request.method == 'POST':
        # POST data submitted; process data
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = [config('EMAIL_RECIPIENT')]
            if cc_myself:
                recipients.append(sender)
            try:
                send_mail(subject, message, sender, recipients, fail_silently=True)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect(reverse('portfolio_webs:thank_you'))
    else:
        # No data submitted; create a blank form
        form = ContactForm()

    context = {'form': form}
    return render(request, 'portfolio_webs/contact.html', context)
                
def polite(request):
    """Being polite to users entry"""
    return render(request, 'portfolio_webs/thank_you.html')
        
                
            
    
