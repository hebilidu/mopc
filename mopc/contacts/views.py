from django.shortcuts import render, redirect
from .models import Contact

# Create your views here.
def index(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/index.html', { 'contacts': contacts })

def addContact(request):
    if request.method == 'POST':
        new_contact = Contact(
            full_name = request.POST['fullname'],
            relationship = request.POST['relationship'],
            email = request.POST['email'],
            phone_number = request.POST['phone-number'],
            address = request.POST['address']
        )
        new_contact.save()
        return redirect('index')
    return render(request, 'contacts/new.html')

def details(request, pk):
    contact = Contact.objects.get(id=pk)
    return render(request, 'contacts/details.html', { 'contact': contact })