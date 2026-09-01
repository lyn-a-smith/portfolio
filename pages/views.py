from django.shortcuts import redirect, render

from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.
def about_me_view(request):
    return render(request, 'pages/about_me.html')

def experience_view(request):
    return render(request, 'pages/experience.html')

def contact_view(request):
    # Post: the visitor has submitted the form
    if request.method == 'POST':
        form = ContactForm(request.POST) # bind submitted data to the form
        if form.is_valid(): # Django validates the form data

            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Build the email body
            message_body =( 
                f"New message from your Portfolio\n"
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Message: {message}\n"
            )

            try:
                # Send the email
                send_mail(
                    'New message from your Portfolio',
                    message_body,
                    email,
                    ['lynsmith5770@gmail.com']
                )
                # Successs: reset the form and display a success message
                form = ContactForm() # reset the form
                return redirect('thank_you')

            except Exception as e:
                # Error: display an error message
                return render(request, 'pages/contact.html', {'form': form, 'error':str(e)})

        else:
            # Form is not valid: display the form with errors
            return render(request, 'pages/contact.html', {'form': form})

    # Get: the visitor is accessing the page for the first time
    else:
        form = ContactForm()
        return render(request, 'pages/contact.html', {'form': form})

def thank_you_view(request):
    return render(request, 'pages/thank_you.html')

