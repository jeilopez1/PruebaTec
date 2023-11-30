from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


def payment(Campos=True):  # Cambia el valor predeterminado a False
    request_body_schema = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "id": openapi.Schema(
                type=openapi.TYPE_NUMBER,
                description="id de pago.",
            
            ),
        },
        required=(
            [
                "id",
            ]
            if Campos
            else []
        ),
    )

    response_schema = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "id": openapi.Schema(type=openapi.TYPE_STRING),
        },
    )

    return swagger_auto_schema(
        request_body=request_body_schema,
        responses={
            201: openapi.Response(
                description="Respuesta exitosa", schema=response_schema
            )
        },
    )

