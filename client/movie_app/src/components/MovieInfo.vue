<template>
  <v-container>
    포스터 줄거리 별점
    <h3>
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
const BASE_URL = 'http://localhost:8000/api/v1/movie_community/specific_movie/'

import axios from 'axios'
export default {
  name:'MovieInfo',
  data() {
    return {
      movieinfo: [],
    }
  },
  created() {
    this.getMovieInfo()
  },
  methods: {
    getMovieInfo() {
      axios.post(BASE_URL, { 'movieId': 3})
      .then(res=>{
        console.log(res)
        this.movieinfo = res.data
      })
    }
  },

}
</script>

<style>

</style>