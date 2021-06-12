# AndaTu

pip install django
pip install djangorestframework
pip install djoser


Endpoints

http://127.0.0.1:8000/auth/token/login/
http://127.0.0.1:8000/auth/token/logout/

create user(POST):
http://127.0.0.1:8000/auth/users/
profile:
http://127.0.0.1:8000/auth/users/me
delete user:
http://127.0.0.1:8000/auth/users/destroy

create package(POST):
http://127.0.0.1:8000/package/
package (GET):
http://127.0.0.1:8000/package/{id}
delete package:
http://127.0.0.1:8000/package/{id}/destroy

create delivery(POST):
http://127.0.0.1:8000/delivery
delivery(GET):
http://127.0.0.1:8000/delivery/{id}
delevte delivery:
http://127.0.0.1:8000/delivery/destroy

create delivery detail(POST):
http://127.0.0.1:8000/delivery_detail
delivery detail(GET):
http://127.0.0.1:8000/delivery_detail/{id}
delete delivery detail:
http://127.0.0.1:8000/delivery_detail/{id}/destroy







