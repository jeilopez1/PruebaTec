from rest_framework.exceptions import ValidationError

class PaymentReferenceNotExist(ValidationError):
    status_code = 404
    default_detail = {"error": "no existe referencia de pago"}


class PaymentNotExist(ValidationError):
    status_code = 404
    default_detail = {"error": "no hay pago"}




