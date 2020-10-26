from django.shortcuts import render, redirect
from .forms import EmailForm
from django.core.mail import send_mail
# Create your views here.


def home(request):
    form = EmailForm()
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            name = form['name'].value()
            subject = form['subject'].value()
            email = form['email_address'].value()
            message = form['message'].value()
            form.save()
            body = "Sender name: " + name + "\n" + "\n" + "Email address: " + email + "\n\n\n" + "Email body: " + message
            send_mail(subject=subject, from_email=email, recipient_list=['plabondatta26@gmail.com', ], message=body, fail_silently=False)
            return render(request, 'app/plabon.html', {'form': form})
    return render(request, 'app/plabon.html', {'form': form})

