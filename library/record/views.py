from django.shortcuts import render
from django.db import connection
from .models import TblBook,TblBookAuthors,TblBookCopies,TblBookLoans,TblBorrower,TblLibraryBranch,TblPublisher

# Create your views here.

def bookcopiesatallbranches_procedure(request):
    if request.method == 'POST':
        book_name = request.POST.get('book_name')
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM bookcopiesatallbranches(%s)", [book_name])
            result = cursor.fetchall()

        context = {"result": result}
        return render(request, 'record/result.html', context)
    else:
        return render(request, 'record/bookcopiesatallbranches.html')


def book_list(request):
    books = TblBook.objects.all()
    return render(request, 'record/book_list.html', {'books': books})

def authors_list(request):
    authors = TblBookAuthors.objects.all()
    return render(request, 'record/author_list.html', {'authors': authors})

def copies_list(request):
    copies = TblBookCopies.objects.all()
    return render(request, 'record/copies_list.html', {'copies': copies})

def loans_list(request):
    loans = TblBookLoans.objects.all()
    return render(request, 'record/loan_list.html', {'loans': loans})

def borrower_list(request):
    borrowers = TblBorrower.objects.all()
    return render(request, 'record/borrower_list.html', {'borrowers': borrowers})

def branch_list(request):
    branches = TblLibraryBranch.objects.all()
    return render(request, 'record/branch_list.html', {'branches': branches})

def publisher_list(request):
    publishers = TblPublisher.objects.all()
    return render(request, 'record/publisher_list.html', {'publishers': publishers})