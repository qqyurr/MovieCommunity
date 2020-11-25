<template>
  <div>
    <div>
        <div> 
          <!-- <img src="../assets/story_white.png" style="width: 1200px;" alt=""> -->
          <!-- <img src="../assets/story_white.png" style="width: 720; " alt=""> -->

         <div class="row row-no-gutters box">
            <img class="col-7" width=800 height=700 src="../assets/story_only.png" alt="">
            <img class="col-5" width=530 height=700 src="https://contentserver.com.au/assets/600828_p13153578_p_v8_ab.jpg" alt="">
          </div>



          <div class="form-check">
            <input class="form-check-input" type="checkbox" value="" id="defaultCheck1">
            <label class="form-check-label" for="defaultCheck1"> 배고프니까 일단 따라간다. </label>
            <br>
            <input class="form-check-input" type="checkbox" value="" id="defaultCheck1">
            <label class="form-check-label" for="defaultCheck1"> 의심스러우니 경계하며 따라간다. </label>
            <br>
            <input class="form-check-input" type="checkbox" value="" id="defaultCheck1">
            <label class="form-check-label" for="defaultCheck1"> 일단 거절한 후 몰래 뒤따라가서 식량을 훔쳐온다. </label>
            <br>
            <input class="form-check-input" type="checkbox" value="" id="defaultCheck1">
            <label class="form-check-label" for="defaultCheck1"> 생명의 은인이 나타났다. 친절하게 대하자.</label>
          </div>

                <span>Picked: {{ picked }}</span>
      
          <!-- <input type="radio" id="comedy" value="comedy" v-model="picked">
          <label for="comedy">34132432</label>
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
          <br> -->


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
      selected: [],
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
    .img {
      /* <img src="paris.jpg" alt="Paris" width="400" height="300"> */
        max-width: 100%;
        max-height: 100%;
    }
    .left{
        max-width: 100%;
        max-height: 100%;
        display: block; /* remove extra space below image */
    }
    .right{
        max-width: 100%;
        max-height: 100%;
        display: block; /* remove extra space below image */
    }
    .box{
        width: 1300px;     
        height: 700px;   
        /* border: 5px solid grey; */
    }  

    .checkbox {
      display: inline;
    }
</style>