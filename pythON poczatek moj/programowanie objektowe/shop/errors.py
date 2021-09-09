# Zadanie nr 1
# Zastąp wyjątek rzucany w klasie Order własną klasą wyjątku.
#
#
# Zadanie nr 2
# # Rozbuduj własną klasę wyjątku dodając do niej domyślną wiadomość i pole allowed_limit.
#
# Rozbuduj poprzednie rozwiązanie o wypisanie informacji zawartych w obiekcie wyjątku.

class LimitError(Exception):
    def __init__(self,allowed_limit,message=None,*args):
        self.allowed_limit = allowed_limit
        if message is None:
            message = f"przekroczono limit elementów zamówienia, który wynosi {allowed_limit}"
        super().__init__(message,*args)

class NotValidInput(Exception):
    pass



class ProductNotAvailable(Exception):
    def __init__(self,product_name,*args):
        self.product_name = product_name
        super().__init__(*args)

class TemporaryOutOfStock(ProductNotAvailable):
    def __init__(self, product_name, available_quantity, *args):
        self.product_name = product_name
        self.available_quantity = available_quantity

        super().__init__(product_name,*args)