from django.shortcuts import render

productos = [
    {"nombre": "Fertilizante NPK 15-15-15", "categoria": "Fertilizantes", "precio": 18990, "stock": 120},
    {"nombre": "Semilla de Maíz Híbrido", "categoria": "Semillas", "precio": 5990, "stock": 340},
    {"nombre": "Herbicida Glifosato 20L", "categoria": "Agroquímicos", "precio": 45990, "stock": 25},
]

def index(request):
    data = {"productos": productos}
    return render(request, "index.html", data)
