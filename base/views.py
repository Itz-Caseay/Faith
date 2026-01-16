from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail 
from django.conf import settings 
from .models import Review
from django.http import JsonResponse 

# Create your views here.

# --- FONCTION DE GESTION DE FORMULAIRE CENTRALISÉE ---
def handle_form_submission(request, success_redirect_name, is_contact_form=False):
    """ 
    Gère la soumission des formulaires (Suggestion ou Contact). 
    is_contact_form=True indique que c'est le formulaire de la page contact.
    """
    
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'

    # Détermine les noms de champs à utiliser
    if is_contact_form:
        fullname = request.POST.get('fullname')
        review_text = request.POST.get('review') 
        # CORRECTION : Sujet admin détaillé
        subject_line = f"New Message recieved ffrom {fullname} through your website."
        success_message = "Thanks ! Your message was successfully sent and a confirmation message was sent to you via your email."
        user_subject_line = "Confirmation Of a new message | PRINCE"
    else:
        fullname = request.POST.get('fullname')
        review_text = request.POST.get('review') 
        # CORRECTION : Sujet admin détaillé
        subject_line = f"New Message recieved ffrom {fullname} through your website."
        success_message = "Thanks ! Your message was successfully sent and a confirmation message was sent to you via your email."
        user_subject_line = "Confirmation Of a new message | PRINCE"


    # Champs communs
    user_email = request.POST.get('email')
    phone = request.POST.get('phone')
    
    # Validation (inchangée)
    if not all([fullname, user_email, phone, review_text]):
        error_msg = "Veuillez remplir tous les champs obligatoires."
        
        if is_ajax:
            return JsonResponse({'error': error_msg}, status=400) 
        
        messages.error(request, error_msg)
        return redirect(success_redirect_name)

    try:
        # 1. Enregistrement dans la base de données
        message_obj = Review.objects.create(
            fullname=fullname,
            phone=phone,
            email=user_email,
            review=review_text
        )

        # 2. Envoi de l'e-mail à l'ADMIN/PROPRIÉTAIRE (abdelthesmil@gmail.com)
        recipient_email = 'faithprince32@gmail.com' 
        
        # CORRECTION : Corps du message Admin structuré (Message d'abord, puis infos)
        message_body_admin = f"""
New Message from {fullname} through your website.
MESSAGE RECIEVED:
{review_text}

________________________________

CONTACT INFORMATION:
Name & Surname: {fullname}
Email: {user_email}
Phone Number: {phone}
Date Recieved: {message_obj.datesubmitted.strftime('%Y-%m-%d %H:%M:%S')}

--------------------------------
"""
        send_mail(
            subject_line,
            message_body_admin,
            settings.EMAIL_HOST_USER, 
            [recipient_email], 
            fail_silently=False,
        )
        
        # 3. NOUVEAU: Envoi de l'e-mail de confirmation à l'UTILISATEUR
        # CORRECTION : Le propre message de l'utilisateur a été retiré de ce corps.
        user_message_body = f"""
Hello {fullname},

We've recieved your mail {fullname}, Now we are taking notice of it. We shall get back to you as soon as possible (ASAP).

---

Thanks for your interest in our services !

Team Prince.
(This is an automatic mail, Don't bother responding.)
"""
        send_mail(
            user_subject_line,
            user_message_body,
            settings.EMAIL_HOST_USER, 
            [user_email],       
            fail_silently=False,
        )
        
        # 4. Succès et notification
        if is_ajax:
            return JsonResponse({'success': success_message}) 
            
        messages.success(request, success_message)
        return redirect(success_redirect_name)
        
    except Exception as e:
        print(f"Error occured while trying to send the email : {e}")
        error_msg = "An error occurred while trying to send your message. Please retry."
        
        if is_ajax:
            return JsonResponse({'error': error_msg}, status=500)
            
        messages.error(request, error_msg)
        return redirect(success_redirect_name)


# --- VUES EXISTANTES (inchangées) ---
def index(request):
    if request.method == 'POST':
        return handle_form_submission(request, success_redirect_name='index', is_contact_form=False) 
    return render(request, 'contact.html')

def apropos(request):
    return render(request, 'apropos.html')

def nos_service(request):
    return render(request, 'nos_service.html')

def contact(request):
    if request.method == 'POST':
        return handle_form_submission(request, success_redirect_name='contact', is_contact_form=True) 
    return render(request, 'index.html')
