from django.db import models


class PlanItem(models.Model):
    name=models.CharField(max_length=255,primary_key=True,blank=False)
    date_created=models.DateTimeField(auto_now_add=True,blank=False)
    date_update=models.DateTimeField()
    effective_start_date=models.DateTimeField(auto_now_add=True,blank=False)
    effective_end_date=models.DateTimeField()
    state=models.BooleanField(blank=False)
    sponsor_id=models.IntegerField(blank=False)
    descripcion=models.CharField(max_length=255)
    type_variable_id=models.IntegerField(blank=False)
    

class ServicePlanning(models.Model):
    date_created=models.DateTimeField(auto_now_add=True,blank=False)
    date_update=models.DateTimeField()
    effective_start_date=models.DateTimeField(auto_now_add=True)
    effective_end_date=models.DateTimeField()
    state=models.BooleanField(blank=False)
    sponsor_id=models.IntegerField(blank=False)
    name=models.CharField(max_length=255)
    strategic_line_id=models.IntegerField()
    service_id=models.IntegerField()

class ServicePlannItem(models.Model):
    date_created=models.DateTimeField(auto_now_add=True,blank=False)
    date_update=models.DateTimeField()
    effective_start_date=models.DateTimeField(auto_now_add=True)
    effective_end_date=models.DateTimeField()
    state=models.BooleanField(blank=False)
    sponsor_id=models.IntegerField(blank=False)
    value=models.IntegerField(blank=False)
    description=models.CharField(max_length=255)
    plan_item_name=models.ForeignKey(PlanItem,on_delete=models.CASCADE, blank=False)
    service_planning_id=models.ForeignKey(ServicePlanning,on_delete=models.CASCADE, blank=False)

class PaymentReference(models.Model):
    date_created=models.DateTimeField(auto_now_add=True,blank=False)
    date_update=models.DateTimeField()
    effective_start_date=models.DateTimeField(auto_now_add=True)
    effective_end_date=models.DateTimeField()
    state=models.BooleanField(blank=False)
    sponsor_id=models.IntegerField(blank=False)
    invoce_id=models.IntegerField()
    state_paid=models.BooleanField(blank=False)
    description=models.CharField(max_length=255)
    paid=models.IntegerField(blank=False)
    value=models.IntegerField(blank=False)
    code_currency_id=models.IntegerField()


class PaymentReferenceDetail(models.Model):
    payment_reference_id=models.ForeignKey(PaymentReference,on_delete=models.CASCADE, blank=False)
    service_planning_id=models.ForeignKey(ServicePlannItem,on_delete=models.CASCADE, blank=False)
    date_created=models.DateTimeField(auto_now_add=True,blank=False)
    date_update=models.DateTimeField()
    effective_start_date=models.DateTimeField(auto_now_add=True)
    effective_end_date=models.DateTimeField()
    user_rol_id=models.IntegerField()
    description=models.CharField(max_length=255)

class Concept(models.Model):
    name=models.CharField(max_length=255,primary_key=True)
    date_created=models.DateTimeField(auto_now_add=True,blank=False)
    date_update=models.DateTimeField()
    effective_start_date=models.DateTimeField(auto_now_add=True)
    effective_end_date=models.DateTimeField()
    state=models.BooleanField(blank=False)
    type_variable_id=models.IntegerField()
    description=models.CharField(max_length=255)

class PaymentFrequency(models.Model):
    date_created=models.DateTimeField(auto_now_add=True,blank=False)
    date_update=models.DateTimeField()
    effective_start_date=models.DateTimeField(auto_now_add=True)
    effective_end_date=models.DateTimeField()
    state=models.BooleanField(blank=False)
    name=models.CharField(max_length=255)
    description=models.CharField(max_length=255)

class PaymentAgreement(models.Model):
    document_type_id=models.IntegerField()
    payment_frencuency_id=models.ForeignKey(PaymentFrequency,on_delete=models.CASCADE, blank=False)
    payment_reference_id=models.ForeignKey(PaymentReference,on_delete=models.CASCADE, blank=False)
    date_created=models.DateTimeField(auto_now_add=True,blank=False)
    date_update=models.DateTimeField()
    effective_start_date=models.DateTimeField(auto_now_add=True)
    effective_end_date=models.DateTimeField()
    state=models.BooleanField(blank=False)
    sponsor_id=models.IntegerField(blank=False)

class PaymentAgreementConcept(models.Model):
    date_created=models.DateTimeField(auto_now_add=True,blank=False)
    date_update=models.DateTimeField()
    effective_start_date=models.DateTimeField(auto_now_add=True)
    effective_end_date=models.DateTimeField()
    state=models.BooleanField(blank=False)
    concept_name=models.ForeignKey(Concept,on_delete=models.CASCADE, blank=False)
    payment_agreement=models.ForeignKey(PaymentAgreement,on_delete=models.CASCADE, blank=False)
    value=models.IntegerField(blank=False)
    description=models.CharField(max_length=255)

class Payment(models.Model):
    date_created=models.DateTimeField(auto_now_add=True,blank=False)
    date_update=models.DateTimeField()
    effective_start_date=models.DateTimeField(auto_now_add=True,blank=False)
    effective_end_date=models.DateTimeField()
    state=models.BooleanField(blank=False)
    code=models.IntegerField(blank=False)
    user_email=models.CharField(blank=False, max_length=500)
    description=models.CharField(blank=False,max_length=500)
    state_transaction=models.BooleanField(blank=False)
    paid=models.IntegerField(blank=False)
    code_currency=models.IntegerField(blank=False)
    sponsor_id=models.IntegerField(blank=False)
    payment_reference_id=models.ForeignKey(PaymentReference,on_delete=models.CASCADE, blank=False)


class PaymentDetail(models.Model):
    Payment_agreement=models.ForeignKey(PaymentAgreement,on_delete=models.CASCADE, blank=False)
    date_created=models.DateTimeField(auto_now_add=True,blank=False)
    date_update=models.DateTimeField()
    effective_start_date=models.DateTimeField(auto_now_add=True,blank=False)
    effective_end_date=models.DateTimeField()
    state=models.BooleanField(blank=False)
    value=models.IntegerField(blank=False)