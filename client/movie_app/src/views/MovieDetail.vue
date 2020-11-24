<template>
  <div v-if="movieId">
    <movie-info :movieId="movieId"/>
  </div>
</template>

<script>
import MovieInfo from '@/components/MovieInfo'


export default {
  name:'MovieDetail',
  data: function() {
    return {
      movieId : '',
    }
  },

  mounted() {
    this.movieId = `${this.$route.params.movieId}`
  },

  watch: {
    $route(){
      this.movieId = `${this.$route.params.movieId}`
    }
  },

  components:{
    MovieInfo,
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