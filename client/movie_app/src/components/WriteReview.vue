<template>
  <v-container>
    <v-card
    dark>
      <v-textarea
        @keypress.enter="createPost"
        v-model="review.content"
        name="input"
        filled
        label="Review"
        auto-grow
      ></v-textarea>
      <v-rating
          v-model="review.star"
          background-color="white"
          color="yellow accent-4"
          dense
          hover
          size="18"
        ></v-rating>
        <v-btn @click="createPost">
          이 버튼을 누르면 리뷰 저장 + 별점 저장 
        </v-btn>
    </v-card>
  </v-container>
</template>

<script>
import axios from 'axios'

export default {
  name:'WriteReview',
  data() {
    return {
      review : {
        content : '',
        star : '',
        movie : this.$store.state.selectedMovie,
      }
    }
  },
  props: {
    movieId : String
  },
  methods: {
    createPost() {
      const myToken = localStorage.getItem('jwt')
      const headers = {headers : {'Authorization' : 'JWT ' + myToken }}
      axios.post(`http://localhost:8000/api/v1/movie_community/movies/${this.movieId}/reviews`, this.review, headers)
      this.review.star = ''
      this.review.content = ''
      this.$router.push(`/movies/${this.movieId}/reviews`)
    },
  },
}
</script>

<style>

</style>