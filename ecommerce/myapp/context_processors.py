from .models import Order

def global_data(request):
    auth = request.session.get('auth')
    cart = request.session.get('cart', {})

    if not auth:
        return {
            'auth': None,
            'auth_orders': [],
            'cart_count': 0
        }

    auth_orders = []
    if auth.get('role') == 'customer':
        auth_orders = Order.objects.filter(user_id=auth['user_id']).order_by('-created_at')[:5]

    return {
        'auth': auth,
        'auth_orders': auth_orders,
        'cart_count': sum(item['qty'] for item in cart.values())
    }