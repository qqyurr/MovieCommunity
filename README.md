### client

- vuex
- axios
- router

### server

- django
- djangorestframework
- corsheader

### API 요청 주소

GET요청) 홈 화면 : /api/v1/movie_community/
응답 예시 :

```
{
"comedy_movies": [],
"romance_movies": [],
"thriller_movies": [],
"action_movies": [],
"horror_movies": []
}

movie Object 하나 예시 :
```

{
"id": 2,
"imdb*title_id": "tt10549312",
"title": "Baba Parasi",
"year": "2020",
"genre": "Comedy",
"duration": "116",
"country": "Turkey",
"language": "Turkish, English",
"director": "Selçuk Aydemir",
"actors": "Ahmet Kural, Murat Cemcir, Seher Devrim Yakut, Rasim Öztekin, Yagmur Tanrisevsin, Özgür Emre Yildirim, Deniz Barut, Giray Altinok, Ayhan Tas, Osman Alkas, Sabahattin Ozan Aslan, Kenan Dogan Ciniviz, Ferhat Feramuz, Oya Gürel, Onur Cavit Idin",
"description": "A group of siblings that share nothing but a father come together after the patriarch's death to compete for his fortune. He left a save for his children, but took the password to the grave with him.",
"avg_vote": "4.6",
"poster_path": "https://m.media-amazon.com/images/M/MV5BNmI5ZmM2NDgtMmNjNi00ZjY4LWJmZmYtYWVkNjdhODNiZjdiXkEyXkFqcGdeQXVyMTIxODU0NzI5._V1_UX182_CR0,0,182,268_AL*.jpg",
"avg_star": ""
},

```

```
