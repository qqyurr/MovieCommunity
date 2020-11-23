<template>
  <div>
    <movie-info :movieId="movieId"/>
    <reviews :movieId="movieId"/>
    <write-review :movieId="movieId"/>
  </div>
</template>

<script>
import MovieInfo from '@/components/MovieInfo'
import WriteReview from '@/components/WriteReview'
import Reviews from '../components/Reviews.vue'


export default {
  name:'MovieDetail',
  data: function() {
    return {
      movieId : this.$route.params.movieId
    }
  },

  mounted() {
    console.log('-----------this.$router')
    console.log(this.$route)
  },

  components:{
    MovieInfo,
    WriteReview,
    Reviews,
  },

  
    Reviewscreated: function() {
      console.log('route params movie id is !!!')
      console.log(this.movieId)
      console.log(this.$route.params.movieId)
  },
}
</script>

<style>

</style>