from pay.models import *


from .errors import *


class MethodsErrors:
    def DoesNotExist(self, exception_type):
        if exception_type == PaymentReference.DoesNotExist:
            raise PaymentReferenceNotExist
        if exception_type == Payment.DoesNotExist:
            raise PaymentNotExist
    


