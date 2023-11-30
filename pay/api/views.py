from rest_framework.views import APIView
from rest_framework.response import Response
from .services.payment_more import Paymentmodels
from .documentacion import payment


class ApiViewRequest(APIView):
    @payment()
    def post(self,request):
        instance=Paymentmodels.sumar(self,request)
        return Response(instance)
        
    
        
