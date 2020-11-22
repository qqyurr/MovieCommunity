# Movie Object 예시

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
	"actors":"Ahmet Kural, Murat Cemcir, Onur Cavit Idin",
	"description":"description is so long",
	"avg_vote":"4.6",
	"poster_path":"https://m.media-amazon.com/images/M/MV5BNmI5ZmM2NDgtMmNjNi00ZjY4LWJmZmYtYWVkNjdhODNiZjdiXkEyXkFqcGdeQXVyMTIxODU0NzI5._V1_UX182_CR0,0,182,268_AL_.jpg",
	"avg_star":"3.5"
}
```

# API 요청 주소

### `http://127.0.0.1:8000/swagger/` 에서도 확인 가능

### 특정 영화의 리뷰 창

- method : `GET요청`
- endpoint : /api/v1/movie_community/specific_movies/
- 응답 예시
  ```
  {
      "id": 3,
      "title": "Ask Tesadüfleri Sever 2",
      "year": "2020",
      ... 중략 ...
      "avg_star": "",
      "reviews": [
          {
              "id": 2,
              "content": "해리포터는아즈카반의죄수가최",
              "movie": 3,
              "star": 5,
              "comments": [
                  {
                      "id": 4,
                      "content": "2번리뷰의 1댓글",
                      "created_at": "2020-11-22T20:01:42.690017+09:00",
                      "updated_at": "2020-11-22T20:01:42.690043+09:00",
                      "review": 2
                  },
                  {
                      "id": 5,
                      "content": "2번리뷰의 2댓글",
                      "created_at": "2020-11-22T20:01:45.933366+09:00",
                      "updated_at": "2020-11-22T20:01:45.933472+09:00",
                      "review": 2
                  }
              ]
          },
          {
              "id": 3,
              "content": "영화안본지오래ㄴ",
              "movie": 3,
              "star": 5,
              "comments": []
          }
      ]
  }
  ```

## 홈 화면

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

---

## 회원가입

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

---

## 로그인

- method : `POST`
- endpoint : /api/v1/movie_community/accounts/api-token-auth/
- request body 예시
  ```
  {
    "username":"gyuyeonKim",
    "password":"password1234"
  }
  ```
- 응답 예시
  ```
  {
  	"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo0LCJ1c2VybmFtZSI6InVzZXI0IiwiZXhwIjoxNjA2MDU2MzIzLCJlbWFpbCI6IiJ9.vYs8-UYpEy1EyUU3OCsJ6kziCS-bp-HnSX4sUmvYTV0"
  }
  ```

---

## 리뷰 작성

- method : `POST`
- endpoint : /api/v1/movie_community/reviews/
- request body 예시
  ```
  {
      "content" : "1111",
      "movie" : 3,
      "star" : 5
  }
  ```
- 응답 예시
  ```
  {
      "id": 4,
      "content": "1111",
      "movie": 3,
      "star": 5
  }
  ```

---

## 전체 리뷰 리스트

- method : `GET`
- endpoint : /api/v1/movie_community/reviews/
- 응답 예시
  ```
  [
    {
        "content": "반지의 제왕은 내 두개의 탑이 최고",
        "movie": 2,
        "star": 5
    },
    {
        "content": "해리포터는아즈카반의죄수가최",
        "movie": 3,
        "star": 5
    }
  ]
  ```

---

## 로그인 한 유저가 작성한 리뷰 리스트

- method : `GET`
- endpoint : user_reviews
- request 필요한 값 없고, headers 에 토큰 값만 넣어주면 됨.
- 응답 예시:
  ```
  [
      {
          "id": 1,
          "content": "반지의 제왕은 내 두개의 탑이 최고",
          "movie": 2,
          "star": 5
      },
      {
          "id": 2,
          "content": "해리포터는아즈카반의죄수가최",
          "movie": 3,
          "star": 5
      },
      {
          "id": 3,
          "content": "영화안본지오래ㄴ",
          "movie": 3,
          "star": 5
      }
  ]
  ```

---

## 영화 제목 검색 결과 리스트

- method : `GET`
- endpoint : /api/v1/movie_community/search_movie_title/
- request body 예시
  ```
  {
      "title" : "oh my"
  }
  ```
- 응답 예시
  ```
  [
      {
          "id": 33,
          "imdb_title_id": "tt11143108",
          "title": "Oh My Kadavule",
          "year": "2020",
          "genre": "Comedy",
          "duration": "151",
          "country": "India",
          "language": "Tamil",
          "director": "Ashwath Marimuthu",
          "actors": "Ashok Selvan, Ritika Singh, Vani Bhojan, Vijay Sethupathi, Sha Ra, M.S. Bhaskar, Gajaraj, Ramesh Thilak, Gautham Menon",
          "description": "hahahahahahaha",
          "avg_vote": "8.1",
          "poster_path": "https://m.media-amazon.com/images/M/MV5BNmI5ZmM2NDgtMmNjNi00ZjY4LWJmZmYtYWVkNjdhODNiZjdiXkEyXkFqcGdeQXVyMTIxODU0NzI5._V1_UX182_CR0,0,182,268_AL_.jpg",
          "avg_star": ""
      }
  ]
  ```
