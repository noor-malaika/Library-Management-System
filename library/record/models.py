# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class RecordBook(models.Model):
    id = models.BigAutoField(primary_key=True)
    book_title = models.CharField(max_length=100)
    book_publishername = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'record_book'


class TblBook(models.Model):
    book_bookid = models.AutoField(primary_key=True)
    book_title = models.CharField(max_length=100)
    book_publishername = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'tbl_book'


class TblBookAuthors(models.Model):
    book_authors_authorid = models.AutoField(primary_key=True)
    book_authors_bookid = models.CharField(max_length=100)
    book_authors_authorname = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tbl_book_authors'


class TblBookCopies(models.Model):
    book_copies_copiesid = models.AutoField(primary_key=True)
    book_copies_bookid = models.CharField(max_length=100)
    book_copies_branchid = models.CharField(max_length=100)
    book_copies_no_of_copies = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbl_book_copies'


class TblBookLoans(models.Model):
    book_loans_loansid = models.AutoField(primary_key=True)
    book_loans_bookid = models.CharField(max_length=100)
    book_loans_branchid = models.CharField(max_length=100)
    book_loans_cardno = models.CharField(max_length=100)
    book_loans_dateout = models.CharField(max_length=50)
    book_loans_duedate = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tbl_book_loans'


class TblBorrower(models.Model):
    borrower_cardno = models.AutoField(primary_key=True)
    borrower_borrowername = models.CharField(max_length=100)
    borrower_borroweraddress = models.CharField(max_length=200)
    borrower_borrowerphone = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tbl_borrower'


class TblLibraryBranch(models.Model):
    library_branch_branchid = models.AutoField(primary_key=True)
    library_branch_branchname = models.CharField(max_length=100)
    library_branch_branchaddress = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'tbl_library_branch'


class TblPublisher(models.Model):
    publisher_publishername = models.CharField(primary_key=True, max_length=100)
    publisher_publisheraddress = models.CharField(max_length=200)
    publisher_publisherphone = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tbl_publisher'
