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
