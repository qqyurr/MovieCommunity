<template>
  <div>
    <movie-info/>
    <write-review/>
  </div>
</template>

<script>
import MovieInfo from '@/components/MovieInfo'
import WriteReview from '@/components/WriteReview'
export default {
  name:'MovieDetail',
  components:{
    MovieInfo,
    WriteReview,
  },
}
</script>

<style>

</style>