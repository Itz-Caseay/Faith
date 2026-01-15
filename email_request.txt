# views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail 
from django.conf import settings 
from .models import Suggestion
from django.http import JsonResponse 

# --- FONCTION DE GESTION DE FORMULAIRE CENTRALISÉE ---
def handle_form_submission(request, success_redirect_name, is_contact_form=False):
    """ 
    Gère la soumission des formulaires (Suggestion ou Contact). 
    is_contact_form=True indique que c'est le formulaire de la page contact.
    """
    
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'

    # Détermine les noms de champs à utiliser
    if is_contact_form:
        nom_complet = request.POST.get('nom_prenom')
        message_text = request.POST.get('message') 
        # CORRECTION : Sujet admin détaillé
        subject_line = f"Nouveau Message de Contact de {nom_complet} sur votre site."
        success_message = "Merci ! Votre message a été envoyé avec succès et une confirmation vous a été envoyée par e-mail."
        user_subject_line = "Confirmation de réception de votre message | INNOVATECH"
    else:
        nom_complet = request.POST.get('nom')
        message_text = request.POST.get('suggestion')
        # CORRECTION : Sujet admin détaillé
        subject_line = f"Nouvelle Suggestion reçue de {nom_complet} sur votre site."
        success_message = "Merci ! Votre suggestion a été enregistrée et une confirmation vous a été envoyée par e-mail."
        user_subject_line = "Confirmation de votre suggestion | INNOVATECH"


    # Champs communs
    email_utilisateur = request.POST.get('email')
    telephone = request.POST.get('telephone')
    
    # Validation (inchangée)
    if not all([nom_complet, email_utilisateur, telephone, message_text]):
        error_msg = "Veuillez remplir tous les champs obligatoires."
        
        if is_ajax:
            return JsonResponse({'error': error_msg}, status=400) 
        
        messages.error(request, error_msg)
        return redirect(success_redirect_name)

    try:
        # 1. Enregistrement dans la base de données
        message_obj = Suggestion.objects.create(
            nom=nom_complet,
            telephone=telephone,
            email=email_utilisateur,
            suggestion=message_text
        )

        # 2. Envoi de l'e-mail à l'ADMIN/PROPRIÉTAIRE (abdelthesmil@gmail.com)
        recipient_email = 'abdelthesmil@gmail.com' 
        
        # CORRECTION : Corps du message Admin structuré (Message d'abord, puis infos)
        message_body_admin = f"""
Nouveau Message reçue de {nom_complet} sur votre site 
MESSAGE REÇU:
{message_text}

________________________________

INFORMATIONS DE CONTACT:
Nom & Prénom: {nom_complet}
E-mail: {email_utilisateur}
Numéro de téléphone: {telephone}
Date de soumission: {message_obj.date_soumission.strftime('%Y-%m-%d %H:%M:%S')}

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
Bonjour {nom_complet},

Nous vous confirmons la bonne réception de votre message. Notre équipe INNOVATECH va l'examiner et vous reviendra dans les plus brefs délais.

---

Merci de votre intérêt pour nos services !

L'équipe INNOVATECH.
(Ceci est un e-mail automatique, veuillez ne pas y répondre.)
"""
        send_mail(
            user_subject_line,
            user_message_body,
            settings.EMAIL_HOST_USER, 
            [email_utilisateur],       
            fail_silently=False,
        )
        
        # 4. Succès et notification
        if is_ajax:
            return JsonResponse({'success': success_message}) 
            
        messages.success(request, success_message)
        return redirect(success_redirect_name)
        
    except Exception as e:
        print(f"Erreur lors de l'enregistrement ou de l'envoi d'e-mail : {e}")
        error_msg = "Une erreur est survenue lors de l'envoi du message. Veuillez réessayer."
        
        if is_ajax:
            return JsonResponse({'error': error_msg}, status=500)
            
        messages.error(request, error_msg)
        return redirect(success_redirect_name)


# --- VUES EXISTANTES (inchangées) ---
def index(request):
    if request.method == 'POST':
        return handle_form_submission(request, success_redirect_name='index', is_contact_form=False) 
    return render(request, 'index.html')

def apropos(request):
    return render(request, 'apropos.html')

def nos_service(request):
    return render(request, 'nos_service.html')

def contact(request):
    if request.method == 'POST':
        return handle_form_submission(request, success_redirect_name='contact', is_contact_form=True) 
    return render(request, 'contact.html')

# models.py

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    pass

# Nouveau modèle pour enregistrer les suggestions ou retours des utilisateurs
class Suggestion(models.Model):
    # Les champs du formulaire
    nom = models.CharField(max_length=100, verbose_name="Nom")
    telephone = models.CharField(max_length=20, verbose_name="Téléphone")
    email = models.EmailField(verbose_name="Adresse E-mail")
    suggestion = models.TextField(verbose_name="Suggestion/Message")
    
    # Champ de suivi
    date_soumission = models.DateTimeField(default=timezone.now, verbose_name="Date de Soumission")

    class Meta:
        verbose_name = "Suggestion Utilisateur"
        verbose_name_plural = "Suggestions Utilisateurs"
        ordering = ['-date_soumission']

    def __str__(self):
        return f"Suggestion de {self.nom} ({self.email})"

# Settings.py

# ----------------------------------------------------------------------
# Utilisez le backend SMTP pour envoyer des e-mails
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Hôte SMTP (ex: pour Gmail)
EMAIL_HOST = 'smtp.gmail.com'

# Port (587 pour TLS)
EMAIL_PORT = 587

# Utiliser une connexion sécurisée (TLS)
EMAIL_USE_TLS = True

# Votre adresse e-mail d'envoi
EMAIL_HOST_USER = 'abdelthesmil@gmail.com' 

# Votre mot de passe d'application ou mot de passe de compte
# ATTENTION: Pour Gmail, utilisez un "Mot de passe d'application" et NON votre mot de passe habituel.
EMAIL_HOST_PASSWORD = 'znfpaoetsqyaawdz' 

# Adresse e-mail par défaut utilisée si aucune n'est spécifiée (facultatif)
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# ----------------------------------------------------------------------
