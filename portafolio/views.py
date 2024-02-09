from django.http import JsonResponse
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ContactForm
from django.http import HttpResponse

def index(request):
    proyectos = [
        {
            'nombre': 'Proyecto Uno',
            'tecnologias': ['Django', 'React'],
            'imagen': 'ruta/a/la/imagen/del/proyecto.png',
            'descripcion': 'Descripción breve del proyecto uno...',
            'link': 'http://linkalproyecto1.com'
        },
    ]

    habilidades = [
        {'nombre': 'Python', 'nivel': 'Intermedio', 'icono': 'python-icon.png'},
    ]
    experiencias = [
        {
            'empresa': 'Empresa Uno',
            'titulo': 'Desarrollador Web',
            'inicio': 'Enero 2020',
            'fin': 'Actualidad',
            'descripcion': 'Descripción de las responsabilidades y logros...'
        },
    ]
    context = {
        'proyectos': proyectos,
        'habilidades': habilidades,
        'experiencias': experiencias
    }
    return render(request, 'index.html', context)

def send_contact_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']
            
            subject = f"Nuevo mensaje de contacto de {nombre}"
            message = f"Recibiste un nuevo mensaje de contacto en tu sitio web:\n\n"
            message += f"Nombre: {nombre}\nEmail: {email}\nMensaje:\n{mensaje}"
            
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            
            return JsonResponse({'status': 'success', 'message': 'Correo enviado satisfactoriamente.'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Formulario inválido.'})
        
def health_check(request):
    return HttpResponse("OK", content_type="text/plain")