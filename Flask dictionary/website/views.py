from flask import Blueprint, render_template, request, redirect
import openpyxl
workbook = openpyxl.load_workbook('website/static/dictionary.xlsx')
workbook_dictionary=workbook['Sheet1']

views= Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@views.route('/allwords', methods=['GET', 'POST'])
def allwords():
    dict={}
    for row in workbook_dictionary.iter_rows(min_row=4, values_only=True):
        title, meaning= row[0], row[1]
        dict[title]=meaning
        # print(title, meaning)
    return render_template('index.html', words=dict)

    
@views.route('/searchword', methods=['GET', 'POST'])
def searchword():
    if request.method=='POST':
        sub=request.form.get('title')
        print(sub)
        if (sub==""):
            return render_template('index.html', words=None)
        dict={}
        for row in workbook_dictionary.iter_rows(min_row=2, values_only=True):
            title, meaning= row[0], row[1]
            if sub in title or sub in meaning:
                dict[title]=meaning
                print(title, meaning)
        return render_template('index.html', words=dict)
    return render_template('index.html')

@views.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')