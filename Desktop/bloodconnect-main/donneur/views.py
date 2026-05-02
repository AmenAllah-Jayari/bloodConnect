from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import DonneurProfileForm

@login_required
def donneur_dashboard(request):
    donneur = request.user.donneur
    
    if request.method == 'POST':
        # request.FILES lezemha tkoun mawjouda 3la khatre el tssawer[cite: 1]
        form = DonneurProfileForm(request.POST, request.FILES, instance=donneur)
        if form.is_valid():
            form.save()
            return redirect('donneur:dashboard')
    else:
        form = DonneurProfileForm(instance=donneur)

    return render(request, 'donneur/donneur_dashboard.html', {
        'form': form,
        'donneur': donneur
    })