import razorpay
from django.http import HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from authentication.models import UserProfile
from config import settings
from payment.models import Contribution
from user_dashboard.models import Project

client = razorpay.Client(auth=(settings.RAZORPAY_ID, settings.RAZORPAY_SECRET_KEY))


def create_order(request):
    amount = int(request.POST['amount'])*100
    currency = request.POST['currency']
    project = request.POST['project_id']
    user_profile = UserProfile.objects.get(user=request.user)
    contact = user_profile.contact
    address = user_profile.location
    name = user_profile.user.first_name
    order = client.order.create(data=dict(amount=amount, currency=currency, payment_capture='0'))
    order_id = order['id']
    callback_url = 'pay_handle/ '
    contribution = Contribution(
                                user=user_profile,
                                project=Project.objects.get(pk=project),
                                amount=amount,
                                currency=currency,
                                order_id=order_id,
                                )
    contribution.save()
    context = {
        'order_id': order_id,
        'merchant_key': settings.RAZORPAY_ID,
        'amount': amount,
        'currency': currency,
        'callback_url': callback_url,
        'contact': contact,
        'address': address,
        'name': name
    }
    return render(request, 'payment/payment.html', context=context)


@csrf_exempt
def payment_handler(request):
    if request.method == 'POST':
        try:
            payment_id = request.POST['razorpay_payment_id']
            order_id = request.POST['razorpay_order_id']
            signature = request.POST['razorpay_signature']
            details = {
                'razorpay_order_id': order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
            print(details)
            contribution = Contribution.objects.get(order_id=order_id)
            amount = contribution.amount
            contribution.payment_id = payment_id
            contribution.verification_signature = signature
            result = client.utility.verify_payment_signature(details)
            if result is not None:
                try:
                    client.payment.capture(payment_id, amount)
                    contribution.verification_status = True
                    contribution.save()
                    return render(request, 'payment/success.html')
                except:
                    contribution.delete()
                    return render(request, 'payment/failure.html')
            else:
                contribution.delete()
                return render(request, 'payment/failure.html')
        except:
            return HttpResponseBadRequest()
    else:
        return HttpResponseBadRequest()
