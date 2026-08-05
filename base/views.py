from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .models import ContactMessage

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to database
            contact = form.save()
            
            # Optional: Send email notification
            try:
                send_mail(
                    subject=f"New Contact Message from {contact.fullname}",
                    message=f"""
                    Name: {contact.fullname}
                    Phone: {contact.phone or 'Not provided'}
                    Email: {contact.email or 'Not provided'}
                    Message:
                    {contact.message}
                    
                    Sent at: {contact.created_at}
                    """,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=True,
                )
            except Exception as e:
                print(f"Email error: {e}")
            
            # Add success message
            messages.success(request, 'Your message has been sent successfully!')
            
            # Redirect to prevent form resubmission
            return redirect('home')
        else:
            # Add error messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    
    return render(request, 'index.html', context)

# Optional: Admin view to see all messages
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator

@staff_member_required
def view_messages(request):
    messages_list = ContactMessage.objects.all()
    paginator = Paginator(messages_list, 20)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'admin_messages.html', {'page_obj': page_obj})

@staff_member_required
def mark_as_read(request, message_id):
    try:
        message = ContactMessage.objects.get(id=message_id)
        message.is_read = True
        message.save()
        messages.success(request, 'Message marked as read.')
    except ContactMessage.DoesNotExist:
        messages.error(request, 'Message not found.')
    
    return redirect('view_messages')

# from django.shortcuts import render

def privacy_policy(request):
    return render(request, 'privacy.html')

def terms_of_service(request):
    return render(request, 'terms.html')