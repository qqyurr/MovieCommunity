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
    <h2>자유롭게 리뷰를 남겨보세요</h2>
    <h4 v-for='(review,idx) in movieinfo.reviews' :key='idx'>
      {{ review.content }}
      별점: {{ review.star }}
      <h5 v-for='(comment, idx) in review.comments' :key='idx'>
        --- 대댓글: {{ comment.content }}  - {{ comment.created_at }}
      </h5>
    </h4>
    <hr>
  </v-container>
</template>

<script>
// const BASE_URL = 'http://localhost:8000/api/v1/movie_community/movies/' + this.$store.state.selectedMovie + '/reviews/'
// const BASE_URL = 'http://localhost:8000/api/v1/movie_community/movies/' + props.movieId + '/reviews/'
// const BASE_URL = 'http://localhost:8000/api/v1/movie_community/movies/' + 3 + '/reviews/'


import axios from 'axios'


export default {
  name:'MovieInfo',
  computed: {
  },

  data() {
    return {
      movieinfo: [],
    }
  },

  props: {
    movieId : String,
  },

  created() {
    console.log('------------------ movie id is : ')
    console.log(this.movieId)
    this.getMovieInfo()
  },
  methods: {

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
    }
  },

}
</script>

<style>

</style>