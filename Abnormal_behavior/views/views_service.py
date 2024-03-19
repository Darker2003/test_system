from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import Quotes

# def quotes(request):
#     if request.method == 'POST':
#         qname = request.POST.get('username')
#         qmail = request.POST.get('email')
#         qphone = request.POST.get('phone')
#         qadvise = request.POST.get('selected_service')
#         qmessage = request.POST.get('message')

#         if qname and qmail and qphone and qadvise and qmessage:
#             # Check if a quote with the given email already exists
#             existing_quote = Quotes.objects.filter(qmail=qmail).first()
#             if existing_quote:
#                 messages.error(request, "A quote with this email already exists")
#                 return redirect('home')

#             # Create a new object of the Quotes model and save it to the datbase
#             new_quote = Quotes(
#                 qmail=qmail,
#                 qname=qname,
#                 qphone=qphone,
#                 qadvise=qadvise,
#                 qmessage=qmessage
#             )
#             new_quote.save()
#             messages.success(request, "Your information has been saved successfully")
#             return redirect('home')  # Redirect to the home page after saving
#         else:
#             messages.error(request, "Please fill in all required fields")
#     else:
#         messages.error(request, "Invalid request")

#     return render(request, "index.html")


from django.http import HttpRequest

from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import Quotes  # Assuming you have a Quotes model

def quotes(request):
    if request.method == 'POST':
        referring_page = request.POST.get('referring_page')

        qname = request.POST.get('username')
        qmail = request.POST.get('email')
        qphone = request.POST.get('phone')
        qadvise = request.POST.get('selected_service')
        qmessage = request.POST.get('message')

        if referring_page == 'index':
            template = 'index.html'
        elif referring_page == 'contact':
            template = 'contact.html'
        else:
            template = 'index.html'

        if qname and qmail and qphone and qadvise and qmessage:
            existing_quote = Quotes.objects.filter(qmail=qmail).first()
            if existing_quote:
                messages.error(request, "A quote with this email already exists")
            else:
                new_quote = Quotes(qmail=qmail, qname=qname, qphone=qphone, qadvise=qadvise, qmessage=qmessage)
                new_quote.save()
                messages.success(request, "Your information has been saved successfully")
                return redirect('home')  # Assuming 'home' is the name of the index page URL pattern
        else:
            messages.error(request, "Please fill in all required fields")

    else:
        template = 'index.html'  # Default template

    return render(request, template)

