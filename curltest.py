'''
curl -X POST -d "username=admin&password=*********" http://127.0.0.1:8000/news/auth/token

"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE0NjgzNDY2MDcsInVzZXJuYW1lIjoiYWRtaW4iLCJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSJ9.P_AzvHqvP20Oe5o_TuBbJhXfHrrVIzsOtlofijf7JfA"

curl -H "Authorization: JWT <your_token>" http://localhost:8000/protected-url/

curl -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE0NjgzNDY2MDcsInVzZXJuYW1lIjoiYWRtaW4iLCJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSJ9.P_AzvHqvP20Oe5o_TuBbJhXfHrrVIzsOtlofijf7JfA" 'http://127.0.0.1:8000/news/'


curl -X POST -d "username=admin&password=*********"

Invoke-WebRequest

Invoke-WebRequest -Headers @{"Authorization" = "JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE0NjgzNDgwNDQsInVzZXJuYW1lIjoiYWRtaW4iLCJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSJ9.FObHu1v8Oaf85Wlml2SGzHxK_IADT8vGo2xp8RvaKo0"} -Uri "http://127.0.0.1:8000/news/"

'''