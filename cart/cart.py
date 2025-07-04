from panther_store.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session

        # Get current cart from session, or create one
        cart = self.session.get('session_key')

        if not cart:
            cart = self.session['session_key'] = {}

        self.cart = cart

    def add(self, product, quantity=1):
        product_id = str(product.id)

        if product_id in self.cart:
            self.cart[product_id]['quantity'] += quantity
        else:
            self.cart[product_id] = {
                'price': str(product.price),
                'quantity': quantity,
                'name': product.name
            }

        self.save()

    def remove(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def update(self, product_id, quantity):
        product_id = str(product_id)
        if product_id in self.cart:
            self.cart[product_id]['quantity'] = quantity
            self.save()

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_prods(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        # Annotate product objects with cart data (quantity, subtotal, etc.)
        for product in products:
            pid = str(product.id)
            product.cart_quantity = self.cart[pid]['quantity']
            product.cart_price = float(self.cart[pid]['price'])
            product.cart_total = round(product.cart_price * product.cart_quantity, 2)

        return products

    def save(self):
        self.session.modified = True
