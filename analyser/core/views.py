# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import Document
from .forms import DocumentForm
from analyser.utils import get_delimiter

import pandas as pd

# Create your views here.
def index(request):
    docs = Document.objects.all()
    return render(
        request,
        'core/index.html',
        {'documents': docs}
    )

def detail(request, id):
    doc = get_object_or_404(Document, pk=id)
    delimiter = get_delimiter(doc.docfile.path)
    data = pd.read_csv(doc.docfile.path, sep=delimiter, header=0)
    head = data.head()
    shape = data.shape
    shape = {
        'l': shape[0],
        'c': shape[1]
    }

    return render(
        request,
        'core/detail.html', {
        'document': doc,
        'head': head,
        'shape': shape
    })

def create(request):
    form = DocumentForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/core/')

    return render(
        request,
        'core/create.html',
        {'form': form}
    )

def groupby(request, id, col):
    doc = get_object_or_404(Document, pk=id)
    delimiter = get_delimiter(doc.docfile.path)
    data = pd.read_csv(doc.docfile.path, sep=delimiter, header=0)
    clean = data[col].fillna('Missing Data')
    clean[clean == ''] = 'Unknown Data'
    data[col] = clean
    grouped = data.groupby([col]).count()
    grouped = grouped.reset_index()
    return render(
        request,
        'core/groupby.html', {
        'grouped': grouped,
        'document': doc,
        'column': col
    })

def numstats(request, id):
    doc = get_object_or_404(Document, pk=id)
    delimiter = get_delimiter(doc.docfile.path)
    data = pd.read_csv(doc.docfile.path, sep=delimiter, header=0)
    data = data._get_numeric_data()
    base = {
        'Soma': data.sum(),
        'Média': data.mean(),
        'Mínimo': data.min(),
        'Máximo': data.max(),
    }
    data = pd.DataFrame(base)
    return render(
        request,
        'core/numstats.html', {
        'data': data,
        'doc': doc
    })