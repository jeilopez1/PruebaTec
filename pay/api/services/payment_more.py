from pay.models import Payment,PaymentReference
from errors.methods_errors import MethodsErrors
class Paymentmodels():
    def sumar(self, reqest):
        try:
            data=reqest.data["id"]
            payment_reference_instance = PaymentReference.objects.get(id=data)
            pagos_relacionados = Payment.objects.filter(payment_reference_id__invoce_id=data)
            total_paid = sum(pago.paid for pago in pagos_relacionados)
            payment_reference_instance.paid=total_paid
            payment_reference_instance.save()
            return "exito"
        except (Payment.DoesNotExist, PaymentReference.DoesNotExist) as e:
            MethodsErrors.DoesNotExist(self,type(e))

