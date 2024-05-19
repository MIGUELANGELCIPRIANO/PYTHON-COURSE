# CLASS NEW EXCEPTION


class NewException(Exception):
    def __init__(self, error):
        print(f"ERROR: {error}")


raise NewException("error management test")
