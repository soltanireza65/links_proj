from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from common.decorators import ajax_required
from links.forms import LinkCreateForm, LinkUpdateForm
from links.models import Link
from stats.models import Click


@login_required
def link_list(request):
    # links = Link.objects.filter(user=request.user, is_active=True)
    links = Link.objects.filter(user=request.user)
    # profile_link = User.objects.filter()
    profile_link = request.user.username
    context = {
        'section': 'links',
        'links': links,
        'profile_link': f'https://many.link/{profile_link}'
    }
    return render(request, 'links/links.html', context)


@ajax_required
def link_clicked(request):
    link_id = request.POST.get('id')
    link = Link.objects.filter(id=link_id).get()
    click = Click.objects.create(link=link)
    click.save()
    link.num_clicks += 1
    link.save()
    print('++========================++')
    print(link, 'Clicked: ', link.num_clicks, ' Times')
    print('++========================++')
    if request.is_ajax():
        return JsonResponse({
            'section': 'links',
            'status': 'ok',
            'num_clicks': link.num_clicks
        })


@login_required
def link_create(request):
    if request.method == "POST":
        form = LinkCreateForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            new_link = form.save(commit=False)
            new_link.user = request.user
            new_link.save()

            messages.success(request, 'Link Added Successfully')
            return redirect('link_list')
    else:
        form = LinkCreateForm(data=request.GET)

    context = {
        'form': form,
        'section': 'links',
    }
    return render(request, 'links/link_create.html', context)


def link_edit(request, link_id):
    link = Link.objects.get(id=link_id)
    form = LinkUpdateForm(instance=link)

    if request.method == "POST":
        form = LinkUpdateForm(request.POST, instance=link)
        if form.is_valid():
            # cd = form.cleaned_data
            form.save()
            messages.success(request, 'Link Updated')
            return redirect('link_list')
    context = {
        'form': form,
        'section': 'links',
    }

    return render(request, 'links/link_edit.html', context)


@login_required
def appearance(request):
    if request.method == "POST":
        # TODO GET Current User
        # TODO SET User Profile Style to given POST param
        # TODO SAVE User
        # TODO IN Template Stuffs ==> Update UI profile style
        pass
    else:
        pass
        # TODO GET profile_style val
        # TODO Set Current Style

    #
    context = {
        'section': 'appearance',
        'style_classes': 'style_classes'
    }
    return render(request, 'links/appearance.html', context)


@login_required
def stats(request):
    clicks = Click.objects.filter(link__user=request.user)

    context = {
        'section': 'stats',
        'clicks': clicks
    }
    # return render(request, 'links/stats.html', context)
    return JsonResponse(context)


@login_required
def settings(request):
    context = {
        'section': 'settings',
        # 'links': links
    }
    return render(request, 'links/settings.html', context)
