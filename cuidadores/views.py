from django.shortcuts import render, redirect
from django.db.models import Count
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from .models import Cuidador
from openpyxl import Workbook

# Funções de Permissão
def e_admin(user): return user.is_superuser
def e_staff(user): return user.is_staff

@login_required
@user_passes_test(e_staff)
def dashboard(request):
    total = Cuidador.objects.count()
    if total == 0:
        return render(request, 'cuidadores/dashboard.html', {'total': 0, 'lista_negra': 0})
    
    por_status = Cuidador.objects.values('status').annotate(qtd=Count('status'))
    por_cidade = Cuidador.objects.values('cidade').annotate(qtd=Count('cidade')).order_by('-qtd')[:5]
    lista_negra = Cuidador.objects.filter(lista_negra=True).count()

    context = {
        'total': total,
        'por_status': por_status,
        'por_cidade': por_cidade,
        'lista_negra': lista_negra,
    }
    return render(request, 'cuidadores/dashboard.html', context)

def cadastro(request):
    if request.method == "POST":
        whatsapp = request.POST.get('whatsapp')
        if Cuidador.objects.filter(whatsapp=whatsapp).exists():
            return render(request, 'cuidadores/formulario.html', {'erro': 'Este WhatsApp já está cadastrado!'})

        Cuidador.objects.create(
            nome=request.POST.get('nome'),
            whatsapp=whatsapp,
            email=request.POST.get('email'),
            estado=request.POST.get('estado'),
            cidade=request.POST.get('cidade'),
            bairro=request.POST.get('bairro'),
            formacao=request.POST.get('formacao'),
            capacitacoes=", ".join(request.POST.getlist('capacitacoes')),
            curriculo=request.FILES.get('curriculo')
        )
        return render(request, 'cuidadores/sucesso.html')
    return render(request, 'cuidadores/formulario.html')

@login_required
@user_passes_test(e_admin)
def lista_cuidadores(request):
    cuidadores = Cuidador.objects.all().order_by('-data_cadastro')
    return render(request, 'cuidadores/lista.html', {'cuidadores': cuidadores})

@login_required
@user_passes_test(e_admin)
def exportar_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="cuidadores.xlsx"'
    wb = Workbook()
    ws = wb.active
    ws.append(['Nome', 'WhatsApp', 'Cidade', 'Status'])
    for c in Cuidador.objects.all():
        ws.append([c.nome, c.whatsapp, c.cidade, c.get_status_display()])
    wb.save(response)
    return response