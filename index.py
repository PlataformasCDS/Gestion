import os
print("Content-Type: text/plain\n")
print("WSGI_HANDLER =", os.getenv("WSGI_HANDLER"))
print("DJANGO_SETTINGS_MODULE =", os.getenv("DJANGO_SETTINGS_MODULE"))
