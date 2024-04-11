from django.shortcuts import render, redirect

from contacts.models import Contact
from contacts.forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('main-page')
        
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})