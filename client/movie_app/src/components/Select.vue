<template>
  <div>
    <div>
        <div> 

          <!-- 왼쪽 : 이야기, 오른쪽 : 추천 영화 포스터 -->
          <div class="row row-no-gutters box" v-if="showStory">
            <div class="col-7 afterChoice" width=800 height=700>
              <section class="section" id="app">
                <article class="article">
                  <p class="p-tag" :data-end="lastLetter">{{ islandStory.substring(0, islandStory.length - 1) }}</p>
                </article>
              </section>
            </div>
            <img @click="goToDetail(movie)" class="col-5" width=530 height=700 src="https://thumbs.gfycat.com/AngryChillyHatchetfish-max-1mb.gif" alt="">
          </div>

          <div class="row row-no-gutters box" v-else>
            <div class="afterChoice">
              <section class="section" id="app">
                <article class="article">
                  <p class="p-tag" :data-end="lastLetter">{{ phrase.substring(0, phrase.length - 1) }}</p>
                </article>
              </section>
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

const myToken = localStorage.getItem('jwt')

export default {
  name:'Select',
  data () {
    return {
      radioGroup: 1,
      picked: '',
      movie: [],
      selected: [],
      story: '당신은 비행기 추락 사고로 파도에 휩쓸리다 무인도에서 깨어났다. 다음 날, 좌절해서 앉아있는 당신에게 정체불명의 사람이 다가온다. 자신을 따라오면 음식과 물을 제공해준다는데...',
      recommendMovieTitle: 'Oka Chinna Viramam',
      recommendedMoviePoster: '',
      showStory: true,
      string: this.recommendMovieTitle,
      explanation: '도전을 받아들일 준비가 되어있는 당신에게 추천하는 영화 <' + this.recommendMovieTitle + '> 영화 포스터를 눌러 리뷰페이지로 이동하세요!',
      index: 0,
    }
  },
  computed: {
    phrase() {
      return ('도전을 받아들일 준비가 되어있는 당신에게 추천하는 영화 <' + this.recommendMovieTitle + '> 영화 포스터를 눌러 리뷰페이지로 이동하세요!').substring(0, this.index);
    },
    islandStory() {
      return this.story.substring(0, this.index);
    },
    lastLetter() {
      return this.phrase[this.phrase.length - 1];
    }
  },
  created() {
    this.showEffect(this.story)
  },
  methods:{
    // getMovie() {
    //   const myToken = localStorage.getItem('jwt')
    //   axios.get(`http://localhost:8000/api/v1/movie_community/recommend/${this.picked}`, {headers: {'Authorization' : 'JWT ' + myToken }})
    //   .then(res=>{
    //    console.log(res.data[0].poster_path)
    //    console.log('movie title : ' , res.data[0].title)
    //    console.log('movie id : ' , res.data[0].id)
    //    this.recommendedMoviePoster = res.data[0].poster_path
    //    this.recommendMovieTitle = res.data[0].title
    //    const wholeSentence = '도전을 받아들일 준비가 되어있는 당신에게 추천하는 영화 <' + res.data[0].title  + '> 영화 포스터를 눌러 리뷰페이지로 이동하세요!'
    //    this.movie = res.data[0]
    //    this.showStory = false
    //    this.showEffect(wholeSentence)
    //   })
    // },

    async getMovie() {
       const res = await axios.get(`http://localhost:8000/api/v1/movie_community/recommend/${this.picked}`, {headers: {'Authorization' : 'JWT ' + myToken }})
       console.log('res : ', res)
       this.recommendedMoviePoster = res.data[0].poster_path
       this.recommendMovieTitle = res.data[0].title
       console.log('recommededMovieTitle : ', this.recommendMovieTitle)
       const wholeSentence = '도전을 받아들일 준비가 되어있는 당신에게 추천하는 영화 영화 포스터를 눌러 리뷰페이지로 이동하세요도전을 받아들일 준비가 되어있는 당신에게 추천하는 영화 영화 포스터를 눌러 리뷰페이지로 이동하세!'
       this.movie = res.data[0]
       this.showStory = false
       this.showEffect(wholeSentence)
       this.index = 0 
      },

    showEffect(sentence) {
      let type = setInterval(() => {
      this.index += 1;
      if (this.index > sentence.length) {
        clearInterval(type);
        console.log('over')
        this.$forceUpdate()
        }
      }, 80);
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
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@300&display=swap');
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
    }


    .section {
      align-items: center;
      display: flex;
      /* justify-content: center; */
    } 

    .article {
      width: 50%;
    }

    /* 스토리 출력되는 부분 */
    .p-tag {
      padding: 16%;
      width: 700px;
      animation: glow 0.5s linear 0s infinite alternate;
      color: black;
      font-size: 2em;
      margin: 0;
      font-family: 'Noto Serif KR', serif;
    }


@media only screen and (max-width: 600px) {
  .article {
    box-sizing: border-box;
    padding: 0 1.3em;
    width: 100%;
  }
}



</style>
