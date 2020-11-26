<template>
  <div id="inspire" v-if="isLoaded">
    <div class="white bigback">
          <div style="margin: 10%;">
          </div>
          <div class='direction_change' style="height:160px;">
              <span style="width:120px;">
            <strong class='mt-5'>Comedy</strong>
            </span>
            <v-col
              v-for="(movie) in movies.comedy_movies.slice(0,5)"
              :key="movie.id"
              cols="6"
              md="2"
              class='ml-4 mr-0 mt-4 mb-4'
            >
            <v-hover>
              <v-card   height="150" elevation="hover ? 12 : 2" >
                <v-img class='cardhover' :src="movie.poster_path" @click="goToDetail(movie)"></v-img>
              </v-card>
            </v-hover>
            </v-col>
          </div>
            <!--Comedy-->
          <div style="margin: 20%;" >
          </div>
            <!--Action-->
          <div class='direction_change' style="height:160px;">
            <span style="width:120px;">
            <strong class='mt-5'>Action</strong>
            </span>
            <v-col
              v-for="(movie) in movies.action_movies.slice(0,5)"
              :key="movie.id"
              cols="6"
              md="2"
               class='ml-4 mt-4 mb-4'
            >
              <v-card height="150" elevation="2">
                <v-img class='cardhover' :src="movie.poster_path" @click="goToDetail(movie)"></v-img>
              </v-card>
            </v-col>
          </div>
            <!--Action-->
          <div style="margin: 20%;" >
          </div>
            <!--Horror-->
          <div class='direction_change' style="height:160px;">
            <span style="width:120px;">
            <strong  class='mt-5'>Horror</strong>
            </span>
            <v-col
              v-for="(movie) in movies.horror_movies.slice(0,5)"
              :key="movie.id"
              cols="6"
              md="2"
               class='ml-4 mt-4 mb-4'
            >
              <v-card height="150" elevation="2">
                <v-img class='cardhover' :src="movie.poster_path" @click="goToDetail(movie)">
                </v-img>
              </v-card>
            </v-col>
      
          </div>
          <!--Horror -->
          <div style="margin: 20%;">
          </div>
   
            <!--Comedy--> 
        
  
    </div>
  </div>
</template>
 
<script>
const SERVER_URL = 'http://localhost:8000/api/v1/movie_community/movie_list_by_genre/'

import axios from 'axios'
export default {
  name:'MainMovieList',
  data() {
    return {
      movies: [],
      draweer: null,
      isLoaded: false,
    }
  },
  created() {
    this.getMovie()
  },
  methods: {
    getMovie() {
      const myToken = localStorage.getItem('jwt')
      axios.get(SERVER_URL, {headers: {'Authorization' : 'JWT ' + myToken }})
      .then(res=>{
        console.log(res.data.movies_by_genre)
        console.log(res.data.movies_by_genre.action_movies)
        this.movies = res.data.movies_by_genre
        this.isLoaded = true
      })
      .catch(err=>{
        console.log(err)
      })
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
#inspire {
  position: sticky;
  font-family:'Montserrat','Cormorant Garamond','Cormorant Unicase','Coustard' ,'La Belle Aurore','Noto Sans KR','Serif';
  font-size: 20px;
}
.direction_change {
  display: flex;
  padding: 30px;
  background-color: navajowhite;
  box-shadow: 0 0px 0px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
}
.cardhover {

  box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
  transition: all 0.3s cubic-bezier(.25,.8,.25,1);
}
.cardhover:hover {
  box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
}


</style>


