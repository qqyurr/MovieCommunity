<template>
  <div>
    <div>
        <div> 

          <!-- 왼쪽 : 이야기, 오른쪽 : 추천 영화 포스터 -->
          <div class="row row-no-gutters box" v-if="showStory">
            <img class="col-7" width=800 height=700 src="../assets/story_only.png" alt="">
            <img @click="goToDetail(movie)" class="col-5" width=530 height=700 :src="recommendedMoviePoster" alt="">
          </div>

          <div class="row row-no-gutters box" v-else>
            <div class="afterChoice">
                <div class="typing-demo">
                  당신에게 딱 맞는 영화 {{recommendMovieTitle}}
                </div>
            </div>
            <img @click="goToDetail(movie)" class="col-5" width=530 height=700 :src="recommendedMoviePoster" alt="">
          </div>

          <div style="margin-left:5%; margin-top:3%">
            <input type="radio" id="comedy" value="comedy" v-model="picked">
            <label for="comedy" style="margin-left:1%">배고프니까 일단 따라간다. </label>
            <br> 
            <input type="radio" id="romance" value="romance" v-model="picked">
            <label for="romance" style="margin-left:1%">의심스러우니 경계하며 따라간다</label>
            <br>
            <input type="radio" id="thriller" value="thriller" v-model="picked">
            <label for="thriller" style="margin-left:1%">일단 거절한 후 몰래 뒤따라가서 식량을 훔쳐온다.</label>
            <br>
            <input type="radio" id="action" value="action" v-model="picked">
            <label for="action" style="margin-left:1%">생명의 은인이 나타났다. 친절하게 대하자</label>
            <br>
             <v-btn style="margin-top:2%" @click='getMovie()'>pick!</v-btn>
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
      movie: [],
      selected: [],
      recommendMovieTitle: '',
      recommendedMoviePoster: '',
      showStory: true,
    }
  },
  methods:{
    getMovie() {
      const myToken = localStorage.getItem('jwt')
      axios.get(`http://localhost:8000/api/v1/movie_community/recommend/${this.picked}`, {headers: {'Authorization' : 'JWT ' + myToken }})
      .then(res=>{
       console.log(res.data[0].poster_path)
       console.log('movie title : ' , res.data[0].title)
       console.log('movie id : ' , res.data[0].id)
       this.recommendedMoviePoster = res.data[0].poster_path
       this.recommendMovieTitle = res.data[0].title
       this.movie = res.data[0]
       this.showStory = false
      })

    },
    goToDetail(movie) {
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
    .box{
        width: 1300px;     
        height: 700px;   
        /* border: 5px solid grey; */
    }  

    .checkbox {
      display: inline;
    }

    .afterChoice {
      width: 730px;
      height: 690px;
      /*This part is important for centering*/
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .typing-demo {
      width: 22ch;
      animation: typing 2s steps(22), blink .5s step-end infinite alternate;
      white-space: nowrap;
      overflow: hidden;
      border-right: 3px solid;
      font-family: monospace;
      font-size: 2em;
    }

    @keyframes typing {
      from {
        width: 0
      }
    }
        
    @keyframes blink {
      50% {
        border-color: transparent
      }
    }
</style>