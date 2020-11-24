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
    }
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