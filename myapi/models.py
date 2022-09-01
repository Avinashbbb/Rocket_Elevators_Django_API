# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Efmigrationshistory(models.Model):
    migrationid = models.CharField(db_column='MigrationId', primary_key=True, max_length=150)  # Field name made lowercase.
    productversion = models.CharField(db_column='ProductVersion', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '__EFMigrationsHistory'


class Addresses(models.Model):
    id = models.BigAutoField(primary_key=True)
    address_type = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    entity = models.CharField(max_length=255)
    numberandstreet = models.CharField(db_column='numberAndStreet', max_length=255)  # Field name made lowercase.
    suiteorapartment = models.CharField(db_column='suiteOrApartment', max_length=255)  # Field name made lowercase.
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    customer_id = models.BigIntegerField(blank=True, null=True)
    building_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'addresses'


class ArInternalMetadata(models.Model):
    key = models.CharField(primary_key=True, max_length=255)
    value = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ar_internal_metadata'


class Batteries(models.Model):
    id = models.BigAutoField(primary_key=True)
    types = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    employeeid = models.IntegerField(db_column='EmployeeId')  # Field name made lowercase.
    date_commissioning = models.DateTimeField()
    date_last_inspection = models.DateTimeField()
    certificate_of_operations = models.CharField(max_length=255)
    information = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    building = models.ForeignKey('Buildings', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    employee_id = models.IntegerField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'batteries'


class BuildingDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    informationkey = models.CharField(db_column='InformationKey', max_length=255, blank=True, null=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    building_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'building_details'


class BuildingTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    number_apartments = models.IntegerField(blank=True, null=True)
    number_floors = models.IntegerField(blank=True, null=True)
    number_elevators = models.IntegerField(blank=True, null=True)
    number_occupants = models.IntegerField(blank=True, null=True)
    companyname = models.CharField(db_column='companyName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'building_types'


class Buildings(models.Model):
    id = models.BigAutoField(primary_key=True)
    addressofbuilding = models.CharField(db_column='addressOfBuilding', max_length=255, blank=True, null=True)  # Field name made lowercase.
    full_name_building_admin = models.CharField(max_length=255)
    email_building_admin = models.CharField(max_length=255)
    phone_building_admin = models.CharField(max_length=255)
    full_name_technical_authority = models.CharField(max_length=255)
    email_technical_authority = models.CharField(max_length=255)
    phone_technical_authority = models.CharField(max_length=255)
    interventiondatestart = models.CharField(db_column='interventionDateStart', max_length=255, blank=True, null=True)  # Field name made lowercase.
    interventiondateend = models.CharField(db_column='interventionDateEnd', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customer = models.ForeignKey('Customers', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    address_of_building = models.CharField(max_length=255, blank=True, null=True)
    full_name_building_adm = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'buildings'


class CacheMemories(models.Model):
    id = models.BigAutoField(primary_key=True)
    selectedcustomer = models.CharField(db_column='selectedCustomer', max_length=255, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cache_memories'


class Columns(models.Model):
    id = models.BigAutoField(primary_key=True)
    types = models.CharField(max_length=255)
    model = models.CharField(max_length=255, blank=True, null=True)
    numberfloorserved = models.CharField(db_column='numberFloorServed', max_length=255)  # Field name made lowercase.
    status = models.CharField(max_length=255)
    information = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    batterie = models.ForeignKey(Batteries, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    number_floor_served = models.CharField(max_length=255, blank=True, null=True)
    typs = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'columns'


class Customers(models.Model):
    id = models.BigAutoField(primary_key=True)
    datecreation = models.DateTimeField(db_column='dateCreation', blank=True, null=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='companyName', max_length=255)  # Field name made lowercase.
    fullname = models.CharField(db_column='fullName', max_length=255)  # Field name made lowercase.
    contactphone = models.CharField(db_column='contactPhone', max_length=255)  # Field name made lowercase.
    email = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    companyhqaddresse = models.CharField(db_column='companyHqAddresse', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fullnametechnicalauthority = models.CharField(db_column='fullNameTechnicalAuthority', max_length=255, blank=True, null=True)  # Field name made lowercase.
    technicalauthorityphone = models.CharField(db_column='technicalAuthorityPhone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    technicalauthorityemail = models.CharField(db_column='technicalAuthorityEmail', max_length=255, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    companey_name = models.CharField(max_length=255, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    full_name_technical_authority = models.CharField(max_length=255, blank=True, null=True)
    technical_authority_email = models.CharField(max_length=255, blank=True, null=True)
    usr_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'


class Elevator(models.Model):
    certificate_operations = models.CharField(max_length=255, blank=True, null=True)
    column_id = models.CharField(max_length=255, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    information = models.CharField(max_length=255, blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    serial_number = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    types = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elevator'


class Elevators(models.Model):
    id = models.BigAutoField(primary_key=True)
    serial_number = models.CharField(max_length=255)
    companyname = models.CharField(db_column='companyName', max_length=255)  # Field name made lowercase.
    model = models.CharField(max_length=255)
    fullname = models.CharField(db_column='fullName', max_length=255)  # Field name made lowercase.
    email = models.CharField(max_length=255)
    types = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    datecommissioning = models.DateTimeField(db_column='dateCommissioning')  # Field name made lowercase.
    datelastinspection = models.DateTimeField(db_column='dateLastInspection')  # Field name made lowercase.
    certificateoperations = models.CharField(db_column='certificateOperations', max_length=255)  # Field name made lowercase.
    information = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    column = models.ForeignKey(Columns, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    certificate_operations = models.CharField(max_length=255, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elevators'


class Employees(models.Model):
    id = models.BigAutoField(primary_key=True)
    firstnname = models.CharField(db_column='firstNname', max_length=255)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=255)  # Field name made lowercase.
    title = models.CharField(max_length=255)
    user_id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    facial_keypoints = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'


class GoogleMapsCustomersLocations(models.Model):
    id = models.BigAutoField(primary_key=True)
    location_building = models.CharField(max_length=255, blank=True, null=True)
    building_floors = models.IntegerField(blank=True, null=True)
    client_name = models.CharField(max_length=255, blank=True, null=True)
    nb_battries = models.IntegerField(blank=True, null=True)
    nb_columns = models.IntegerField(blank=True, null=True)
    nb_elevators = models.IntegerField(blank=True, null=True)
    tech_contact = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'google_maps_customers_locations'


class Interventions(models.Model):
    id = models.BigAutoField(primary_key=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    interventiondatestart = models.CharField(db_column='interventionDateStart', max_length=255, blank=True, null=True)  # Field name made lowercase.
    interventiondateend = models.CharField(db_column='interventionDateEnd', max_length=255, blank=True, null=True)  # Field name made lowercase.
    result = models.CharField(max_length=255, blank=True, null=True)
    report = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    customer_id = models.BigIntegerField(blank=True, null=True)
    employee_id = models.BigIntegerField(blank=True, null=True)
    building_id = models.BigIntegerField(blank=True, null=True)
    batterie_id = models.BigIntegerField(blank=True, null=True)
    column_id = models.BigIntegerField(blank=True, null=True)
    elevator_id = models.BigIntegerField(blank=True, null=True)
    intervention_date_end = models.CharField(max_length=255, blank=True, null=True)
    intervention_date_start = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'interventions'


class Leads(models.Model):
    id = models.BigAutoField(primary_key=True)
    fullnamecontact = models.CharField(db_column='fullNameContact', max_length=255, blank=True, null=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='companyName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=255, blank=True, null=True)
    phonenumber = models.CharField(db_column='phoneNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nameproject = models.CharField(db_column='nameProject', max_length=255, blank=True, null=True)  # Field name made lowercase.
    descriptionproject = models.CharField(db_column='descriptionProject', max_length=255, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(max_length=255, blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    file = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    customer_id = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'leads'


class Products(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'products'


class Quotes(models.Model):
    type_building = models.CharField(max_length=255)
    numapartment = models.IntegerField(db_column='numApartment', blank=True, null=True)  # Field name made lowercase.
    numfloor = models.IntegerField(db_column='numFloor', blank=True, null=True)  # Field name made lowercase.
    numelevator = models.IntegerField(db_column='numElevator', blank=True, null=True)  # Field name made lowercase.
    numoccupant = models.IntegerField(db_column='numOccupant', blank=True, null=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='companyName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quotes'


class SchemaMigrations(models.Model):
    version = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'schema_migrations'


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=255)
    encrypted_password = models.CharField(max_length=255)
    emp = models.IntegerField(blank=True, null=True)
    reset_password_token = models.CharField(unique=True, max_length=255, blank=True, null=True)
    reset_password_sent_at = models.DateTimeField(blank=True, null=True)
    remember_created_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    admin = models.TextField(blank=True, null=True)  # This field type is a guess.
    user_id = models.IntegerField(blank=True, null=True)
    usr_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
