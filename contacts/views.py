from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from contacts.models import Contact
from django.contrib import messages
from contacts.forms import ContactForm


class ContactList(ListView):
    model = Contact
    context_object_name = 'contacts'
    template_name = 'contacts/all_contacts.html'


class ContactDetail(DetailView):
    model = Contact
    context_object_name = 'contact'
    template_name = 'contacts/contact_detail.html'


class ContactCreate(CreateView):
    model = Contact
    fields = '__all__'
    template_name = 'contacts/contact_form.html'


def ContactEdit(request, pk):
    form = ContactForm(request.POST or None, instance=Contact.objects.get(pk=pk))
    if form.is_valid():
        contact = form.save()
        messages.success(request, 'success')
        return redirect('contact_edit', pk=contact.pk)
    return render(request, 'contacts/contact_form.html', {'form': form})
