<template>
  <v-container>
    포스터 줄거리 별점
    <h3>
      영화 번호 : {{this.movieId}}
      {{ movieinfo.title }}
    </h3>
    <img :src="movieinfo.poster_path" alt="">
    <h3>
      줄거리 : {{ movieinfo.description }}
    </h3>
    <hr>
    <h4 v-for='(review,idx) in movieinfo.reviews' :key='idx'>
      <v-card
          elevation="5"
        >{{ review.content }} {{ review.star }}</v-card>
    
      <h5 v-for='(comment, idx) in review.comments' :key='idx'>
        --- 대댓글: {{ comment.content }}  - {{ comment.created_at }}
      </h5>
    </h4>
    <hr>
    
    <!-- 아래는 리뷰 작성하는 form  -->
    <v-card
    dark>
      <v-textarea
        @keypress.enter="createPost"
        v-model="content"
        name="input"
        filled
        label="Review"
        auto-grow
      ></v-textarea>
      <v-rating
          v-model="star"
          background-color="white"
          color="yellow accent-4"
          dense
          hover
          size="18"
        ></v-rating>
        <v-btn @click="createPost">
          작성하기 
        </v-btn>
    </v-card>


  </v-container>

  
</template>

<script>
import axios from 'axios'

export default {
  name:'MovieInfo',
  computed: {
  },

  data() {
    return {
      movieinfo: [],
      content : '',
      star : 0,
      movie : this.movieId,

      reviewAdded: false,
    }
  },

  props: {
    movieId : [String, Number]
  },

  created() {
    this.getMovieInfo()
  },

  watch: {
    movieId() {
      this.getMovieInfo()
    },

    reviewAdded() {
      this.getMovieInfo()
    },
  },
  methods: {

    // 영화와 댓글과 대댓글들
    getMovieInfo() {
      const myToken = localStorage.getItem('jwt')
      axios.get(`http://localhost:8000/api/v1/movie_community/movies/${this.movieId}/reviews`, {params:{}, headers: {'Authorization' : 'JWT ' + myToken }})
      .then(res=>{
        console.log(res)
        this.movieinfo = res.data
      })
      .catch(err => {
        console.log(err)
      })
    },

    // 리뷰작성 포스트요청
      createPost() {
      const SERVER_URL = `http://localhost:8000/api/v1/movie_community/movies/${this.movieId}/reviews`
      const myToken = localStorage.getItem('jwt')
      const headers = {headers : {'Authorization' : 'JWT ' + myToken }}

      axios.post(SERVER_URL, {content: this.content, star: this.star, movie: this.movieId}, headers)
        .then(res=>{
          console.log(res)
        })
      this.star = 0 
      this.content = ''
      this.reviewAdded = !this.reviewAdded
    },
  },

}
</script>

<style>

</style>