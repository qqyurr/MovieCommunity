<template>
  <div>
    <movie-info :movieId="movieId"/>
    <!-- <reviews :movieId="movieId"/> -->
    <write-review :movieId="movieId"/>
  </div>
</template>

<script>
import MovieInfo from '@/components/MovieInfo'
import WriteReview from '@/components/WriteReview'
// import Reviews from '../components/Reviews.vue'


export default {
  name:'MovieDetail',
  data: function() {
    return {
      movieId : this.$route.params.movieId,
      movieData : [],
    }
  },

  mounted() {
    console.log('-----------this.$router')
  },

  components:{
    MovieInfo,
    WriteReview,
    // Reviews,
  },
  created: function() {
      console.log('route params movie id is !!!')
      console.log(this.movieId)
      console.log(this.$route.params.movieId)
  },
}
</script>

<style>

</style>