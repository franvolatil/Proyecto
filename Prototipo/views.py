
import json

from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from Prototipo.forms import PostForm
from Prototipo.forms import SismoForm
from .models import Post
from .models import Sismo
from obspy.core import read
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from django.core import serializers



def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'Prototipo/post_list.html', {'posts': posts})

def post_detail(request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'Prototipo/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
          post = form.save(commit=False)
          post.author = request.user
          post.published_date = timezone.now()
          post.save()
          return redirect('Prototipo.views.post_detail', pk=post.pk)

    else:
         form = PostForm()
    return render(request, 'prototipo/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('Prototipo.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'prototipo/post_edit.html', {'form': form})

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('Prototipo.views.post_list')


def sismos_list(request):
    sismos = Sismo.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'Prototipo/sismos_list.html', {'sismos': sismos})

def sismo_detail(request, pk):
        sismo = get_object_or_404(Sismo, pk=pk)
        return render(request, 'Prototipo/sismos_list.html', {'sismo': sismo})

def sismo_new(request):
    if request.method == "POST":
        form = SismoForm(request.POST, request.FILES)
        if form.is_valid():
          sismo = form.save(commit=False)
          sismo.author = request.user
          sismo.published_date = timezone.now()
          sismo.text = 'myfolder'
          sismo.save()
          header(sismo)
          sismo.save()
          return redirect('Prototipo.views.sismos_list')

    else:
         form = SismoForm()
    return render(request, 'prototipo/sismo_edit.html', {'form': form})


def sismo_edit(request, pk):
    sismo = get_object_or_404(Sismo, pk=pk)
    if request.method == "POST":
        form = SismoForm(request.POST, instance=sismo)
        if form.is_valid():
            sismo = form.save(commit=False)
            sismo.author = request.user
            sismo.save()
            return redirect('Prototipo.views.sismos_list')
    else:
        form = SismoForm(instance=sismo)
    return render(request, 'prototipo/sismo_edit.html', {'form': form})

def sismo_remove(request, pk):
    sismo = get_object_or_404(Sismo, pk=pk)
    sismo.delete()
    return redirect('Prototipo.views.sismos_list')

def sismo_detail(request, pk):
    sismo = get_object_or_404(Sismo, pk=pk)
    return render(request, 'prototipo/sismos_detail.html', {'sismo': sismo})

def header(sismo):

    st = read(sismo.eje_x)
    tr = st[0]

    sismo.network =  tr.stats.network

    sismo.station = tr.stats.station

    sismo.location = tr.stats.location

    sismo.channel = tr.stats.channel

    sismo.starttime = tr.stats.starttime

    sismo.endtime = tr.stats.endtime

    sismo.sampling_rate = tr.stats.sampling_rate

    sismo.delta = tr.stats.delta

    sismo.npts = tr.stats.npts

    sismo.calib = tr.stats.calib

    sismo.format = tr.stats._format

    return sismo

def grafico():

    st = read('myfolder/C.GO01..BHE.M__at__2014-04-04T09.56.55.000Z.SAC')
    xx = st[0]
    cx = np.array(xx.data)
    ntx = signal.detrend(cx)
    ax1.plot(ntx)

    XY = []
    for lines in plt.gca().get_lines():
        for x, y in lines.get_xydata():
            XY.append([x,y])

   # return HttpResponse(simplejson.dumps(XY), mimetype='application/json')


    return json.dumps(["string", 1, 2.5, None])


def tasks_json(request):
    tasks = Task.objects.all()
    data = serializers.serialize("json", tasks)
    return HttpResponse(data, content_type='application/json')


def chart_data_json(request):
    data = {}
    params = request.GET

    days = params.get('days', 0)
    name = params.get('name', '')
    if name == 'avg_by_day':
        data['chart_data'] = ChartData.get_avg_by_day(
            user=request.user, days=int(days))

    return HttpResponse(json.dumps(data), content_type='application/json')


def get_avg_by_day():

    datos = [1,2,3,4,5,6]



    data = {'dates': [], 'values': []}
    for a in datos:
        data['dates'].append(a['record_date'].strftime('%m/%d'))
        data['values'].append(core.utils.round_value(a['avg_value']))

    return data