import asyncio
import re

import openpyxl
from django.shortcuts import render, redirect

from .details_parsing import get_product_info
from .forms import ProductForm


def product_info(request):
    if request.method == 'POST':
        wild_pars = ProductForm(request.POST)
        article = wild_pars.data.get('article')
        index_list = []
        if not article.isdigit() and re.findall(r'(.xlsx)$', article):
            try:
                loc = article
                print(loc)
                my_wb = openpyxl.load_workbook(loc)
                sheets = my_wb.active
                print(sheets)
                for sheet in sheets['A']:
                    print('sheet', sheet.value)
                    index_list.append(sheet.value)
            except Exception as ex:
                print(f'Some {ex} here.')
                return redirect('error')
        elif article.isdigit():
            index_list.append(article)
        else:
            return redirect('error')
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(get_product_info(index_list))
        loop.close()

    context = {
        'form': ProductForm(),
    }
    return render(request, 'base.html', context)


def error(request):
    context = {
    }
    return render(request, 'error.html', context)
