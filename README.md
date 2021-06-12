# AndaTu

pip install django

pip install djangorestframework

pip install djoser




Endpoints

http://127.0.0.1:8000/auth/token/login/

http://127.0.0.1:8000/auth/token/logout/

User:

  create: http://127.0.0.1:8000/auth/users/

  profile: http://127.0.0.1:8000/auth/users/me/

  destroy: http://127.0.0.1:8000/auth/users/destroy/

Package:

  create: http://127.0.0.1:8000/package/

  detail: http://127.0.0.1:8000/package/{id}/

  destroy: http://127.0.0.1:8000/package/{id}/destroy

Delivery:

  create: http://127.0.0.1:8000/delivery

  detail: http://127.0.0.1:8000/delivery/{id}/

  destroy: http://127.0.0.1:8000/delivery/{id}/destroy
  
Delivery Detail:

  create: http://127.0.0.1:8000/delivery_detail
  
  detail: http://127.0.0.1:8000/delivery_detail/{id}/

  destroy: http://127.0.0.1:8000/delivery_detail{id}/destroy
  
