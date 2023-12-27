from django.shortcuts import render

def index(request):
    # Aquí puedes definir tus datos codificados, como ejemplos de proyectos, habilidades, etc.
    proyectos = [
        {
            'nombre': 'Proyecto Uno',
            'tecnologias': ['Django', 'React'],
            'imagen': 'ruta/a/la/imagen/del/proyecto.png',
            'descripcion': 'Descripción breve del proyecto uno...',
            'link': 'http://linkalproyecto1.com'
        },
        # ... más proyectos
    ]

    habilidades = [
        {'nombre': 'Python', 'nivel': 'Intermedio', 'icono': 'python-icon.png'},
        # ... más habilidades
    ]

    experiencias = [
        {
            'empresa': 'Empresa Uno',
            'titulo': 'Desarrollador Web',
            'inicio': 'Enero 2020',
            'fin': 'Actualidad',
            'descripcion': 'Descripción de las responsabilidades y logros...'
        },
        # ... más experiencias
    ]

    # Cualquier otro dato que quieras pasar a la plantilla
    context = {
        'proyectos': proyectos,
        'habilidades': habilidades,
        'experiencias': experiencias
    }

    # Renderizas la plantilla HTML con tu contexto
    return render(request, 'index.html', context)