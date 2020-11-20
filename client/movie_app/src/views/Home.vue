<template>
  <div class="home">
    <h2>Movie List</h2>
    <!-- <규연이가 아이패드로 그린 우리의 로고...손그림 그것이 매력포인트여 -->
    <movietest />
  </div>
</template>

<script>
// @ is an alias to /src
import movietest from '@/components/movietest'

export default {
  name: 'Home',
  components: {
    movietest,
  }
}
</script>
