<template>
  <div>
    <div>
      <p>당신은 길을 잃었습니다. 이후 벌어질 일은?</p>
        <div>
          
      
          <input type="radio" id="comedy" value="comedy" v-model="picked">
          <label for="comedy">comedy</label>
          <br>
          <input type="radio" id="romance" value="romance" v-model="picked">
          <label for="romance">romance</label>
          <br>
          <input type="radio" id="thriller" value="thriller" v-model="picked">
          <label for="thriller">thriller</label>
          <br>
          <input type="radio" id="action" value="action" v-model="picked">
          <label for="action">action</label>
          <br>
          <span>Picked: {{ picked }}</span>
          <br>
          <v-btn @click='getMovie()'>pick!</v-btn>
          <div v-for='(movie,idx) in movies' :key=idx >
            {{ movie.title }}
            <img :src="movie.poster_path" alt="poster" @click="goToDetail(movie)">
          </div>
     
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name:'Select',
  data () {
    return {
      radioGroup: 1,
      picked: '',
      movies:[],
    }
  },
  methods:{
    getMovie() {
      const myToken = localStorage.getItem('jwt')
      axios.get(`http://localhost:8000/api/v1/movie_community/recommend/${this.picked}`, {headers: {'Authorization' : 'JWT ' + myToken }})
      .then(res=>{
        this.movies = res.data
      })
      // 'recommend/<str:genre>/'
    },
    goToDetail(movie) {
    console.log('goToDetail clicked! ')
    this.$store.state.selectedMovie = movie.id
    console.log(this.$store.state.selectedMovie)
    this.$router.push('/movies/' + movie.id + '/reviews/')
    }

  },
}
</script>

<style>

</style>