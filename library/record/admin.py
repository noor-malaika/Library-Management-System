from django.contrib import admin
from .models import TblLibraryBranch,TblBook,TblBookAuthors,TblBookCopies,TblBookLoans,TblBorrower,TblPublisher

# Register your models here.


admin.site.register(TblBook)
admin.site.register(TblBookAuthors)
admin.site.register(TblBookCopies)
admin.site.register(TblBookLoans)
admin.site.register(TblBorrower)
admin.site.register(TblLibraryBranch)
admin.site.register(TblPublisher)

