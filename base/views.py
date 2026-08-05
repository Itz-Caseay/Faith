from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .forms import ContactForm
from .models import ContactMessage

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to database
            contact = form.save()
            
            # ===== SEND BEAUTIFUL EMAIL =====
            try:
                # Prepare email context
                email_context = {
                    'fullname': contact.fullname,
                    'phone': contact.phone or 'Not provided',
                    'email': contact.email or 'Not provided',
                    'message': contact.message,
                    'created_at': contact.created_at.strftime('%B %d, %Y at %I:%M %p'),
                    'message_id': str(contact.id).zfill(4),
                    'admin_url': request.build_absolute_uri('/admin/base/contactmessage/' + str(contact.id) + '/change/'),
                }
                
                # Render HTML email template
                html_message = render_to_string('email_notification.html', email_context)
                plain_message = strip_tags(html_message)
                
                # Send email
                send_mail(
                    subject=f"🔔 New Contact Message from {contact.fullname}",
                    message=plain_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    html_message=html_message,
                    fail_silently=False,
                )
                print("✅ Email sent successfully!")
            except Exception as e:
                print(f"❌ Email error: {e}")
            
            # Add success message
            messages.success(request, '✅ Your message has been sent successfully!')
            return redirect('home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = ContactForm()
    
    context = {'form': form}
    return render(request, 'index.html', context)

# ===== PRIVACY POLICY VIEW =====
def privacy_policy(request):
    """Display the privacy policy page"""
    return render(request, 'privacy.html')

# ===== TERMS OF SERVICE VIEW =====
def terms_of_service(request):
    """Display the terms of service page"""
    return render(request, 'terms.html')

# ===== ADMIN MESSAGES VIEW =====
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator

@staff_member_required
def view_messages(request):
    """Admin view to see all contact messages"""
    messages_list = ContactMessage.objects.all()
    paginator = Paginator(messages_list, 20)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'admin_messages.html', {'page_obj': page_obj})

@staff_member_required
def mark_as_read(request, message_id):
    """Mark a message as read"""
    try:
        message = ContactMessage.objects.get(id=message_id)
        message.is_read = True
        message.save()
        messages.success(request, '✅ Message marked as read.')
    except ContactMessage.DoesNotExist:
        messages.error(request, '❌ Message not found.')
    
    return redirect('view_messages')