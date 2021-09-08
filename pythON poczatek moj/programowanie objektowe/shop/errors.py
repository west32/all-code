# Zadanie nr 1
# Zastąp wyjątek rzucany w klasie Order własną klasą wyjątku.
#
#
# Zadanie nr 2
# Rozbuduj własną klasę wyjątku dodając do niej domyślną wiadomość i pole allowed_limit.

class LimitError(Exception):
    def __init__(self,allowed_limit,message=None,*args):
        self.allowed_limit = allowed_limit
        if message is None:
            message = f"przekroczono limit elementów zamówienia, który wynosi {allowed_limit}"
        super().__init__(message,*args)