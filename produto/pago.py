import mercadopago

sdk = mercadopago.SDK("TEST-1363675576556254-021312-efbb0c786d4754ab6cebacb5aeb42be4-1218814315")

payment_data = {
    "items": [
        {"id": "1", "title": "Camisa", "quantity": 1, "currency_id": "BRL", "unit_price": 259.99}
    ],
    "back_urls": {
        "success": "http://127.0.0.1:5000/compracerta",
        "failure": "http://127.0.0.1:5000/compraerrada",
        "pending": "http://127.0.0.1:5000/compraerrada"
    }
}

result = sdk.preference().create(payment_data)
payment = result["response"]
print(payment)







# import mercadopago

# sdk = mercadopago.SDK("TEST-1363675576556254-021312-efbb0c786d4754ab6cebacb5aeb42be4-1218814315")

# request_options = mercadopago.config.RequestOptions()
# request_options.custom_headers = {
#     'x-idempotency-key': '<SOME_UNIQUE_VALUE>'
# }

# payment_data = {
#     "transaction_amount": 100,
#     "token": "CARD_TOKEN",
#     "description": "Payment description",
#     "payment_method_id": 'visa',
#     "installments": 1,
#     "payer": {
#         "email": 'test_user_123456@testuser.com'
#     }
# }
# result = sdk.payment().create(payment_data, request_options)
# payment = result["response"]

# print(payment)