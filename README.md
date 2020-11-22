### client

- vuex
- axios
- router

### server

- django
- djangorestframework
- corsheader

### API 요청 주소

- 홈 화면
  - method : `GET요청`
  - endpoint : /api/v1/movie_community/movies
  - 응답 예시
    ```
    {
    "comedy_movies": [],
    "romance_movies": [],
    "thriller_movies": [],
    "action_movies": [],
    "horror_movies": []
    }
    ```

### Movie Object 예시

```
{
	"id":2,
	"imdb_title_id":"tt10549312",
	"title":"Baba Parasi",
	"year":"2020",
	"genre":"Comedy",
	"duration":"116",
	"country":"Turkey",
	"language":"Turkish, English",
	"director":"Selçuk Aydemir",
	"actors":"Ahmet Kural, Murat Cemcir, Seher Devrim Yakut, Rasim Öztekin, Yagmur Tanrisevsin, Özgür Emre Yildirim, Deniz Barut, Giray Altinok, Ayhan Tas, Osman Alkas, Sabahattin Ozan Aslan, Kenan Dogan Ciniviz, Ferhat Feramuz, Oya Gürel, Onur Cavit Idin",
	"description":"description is so long",
	"avg_vote":"4.6",
	"poster_path":"https://m.media-amazon.com/images/M/MV5BNmI5ZmM2NDgtMmNjNi00ZjY4LWJmZmYtYWVkNjdhODNiZjdiXkEyXkFqcGdeQXVyMTIxODU0NzI5._V1_UX182_CR0,0,182,268_AL_.jpg",
	"avg_star":"3.5"
}
```

- 회원가입

  - method : `POST`
  - endpoint : /api/v1/movie_community/accounts/signup/
  - request body 예시

  ```
  {
  	"username":"gyuyeonKim",
  	"password":"password1234",
  	"passwordConfirmation":"password1234"
  }
  ```

  - 응답 예시

  ```
  {
  	"username":"gyuyeonKim",
  	"today_choice":null
  }
  ```

- 로그인
  - method : `POST`
  - endpoint : /api/v1/movie_community/accounts/api-token-auth/
  - 응답 예시
    ```
    {
    	"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo0LCJ1c2VybmFtZSI6InVzZXI0IiwiZXhwIjoxNjA2MDU2MzIzLCJlbWFpbCI6IiJ9.vYs8-UYpEy1EyUU3OCsJ6kziCS-bp-HnSX4sUmvYTV0"
    }
    ```
