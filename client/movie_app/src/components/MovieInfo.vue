<template>
  <v-container>
    <!-- 영화 정보 출력  -->
    

    <div class="movieInfo col" style="margin-bottom: 5%; border-style:solid; border-width:0.5px; border-radius: 5px;">
      
      <div class="poster col-3" style="display:inline">
        <img class="imgTag" width=240 height=360 :src="movieinfo.poster_path" alt="">
      </div>

      <div class="col-8 description" style="margin-left:4%;">
        <h1>{{ movieinfo.title }}</h1>
        <br>
        <h3>Director : {{ movieinfo.director}}</h3>
        <br>
        <h3>Actors</h3>
        <div v-for="(actor,idx) in actors" :key='idx'>
          {{ actor }}
        </div>
        
        <br>
        <h3>Synopsis</h3>
        <p>{{ movieinfo.description }}</p>
      </div>
    </div>
    

    <!-- 리뷰창 시작 : 리뷰 컴포넌트 불러오기 -->
    <div>
    <h3 style="margin-left:1%; margin-bottom:2%">댓글 목록 ({{movieinfo.reviews.length}}개의 댓글)</h3>
    <Review
      v-for="(review, idx) in movieinfo.reviews"
      :key="idx"
      :review="review"
      @comment-created="onCommentCreated"
      @review-deleted="onReviewDeleted"
    />
    </div>

    
    <!-- 아래는 리뷰 작성하는 form  -->
      <!-- 별점 -->
      <v-rating
        v-model="star"
        background-color="orange lighten-3"
        color="orange"
        large
      ></v-rating>
      <!-- 내용 -->
      <v-textarea
        @keypress.enter="createPost"
        v-model="content"
        outlined
        name="input-7-4"
        label="코멘트를 작성해주세요"
        value="The Woodman set to work at once, and so sharp was his axe that the tree was soon chopped nearly through."
      ></v-textarea>
  </v-container>
</template>


<script>
import axios from 'axios'
import Review from './Review.vue'


export default {
  components: { Review },
  name:'MovieInfo',
  computed: {
  },

  data() {
    return {
      // 별점 기본 값
      rating: 0,
      // 별점 선택 값
      star : 0,
      movieinfo: [],
      content : '',
      movie : this.movieId,
      reviewAdded: false,
      reviewDeleted: false,
      actors: [],
    }
  },

  props: {
    movieId : [String, Number]
  },

  created() {
    this.getMovieInfo()
  },

  watch: {
    movieId() {
      this.getMovieInfo()
    },

    reviewAdded() {
      this.getMovieInfo()
    },

    reviewDeleted() {
      this.getMovieInfo()
    },
  },
  methods: {

    // 영화와 댓글과 대댓글 반환
    getMovieInfo() {
      const myToken = localStorage.getItem('jwt')
      axios.get(`http://localhost:8000/api/v1/movie_community/movies/${this.movieId}/reviews`, {params:{}, headers: {'Authorization' : 'JWT ' + myToken }})
      .then(res=>{
        console.log('my data', res.data.reviews.length)
        const acts = res.data.actors.split(',')
        this.actors = acts.slice(0,5)
        this.movieinfo = res.data
      })
      .catch(err => {
        console.log(err)
      })
    },

    // 리뷰작성 포스트요청
      createPost() {
      const SERVER_URL = `http://localhost:8000/api/v1/movie_community/movies/${this.movieId}/reviews/`
      const myToken = localStorage.getItem('jwt')
      const headers = {headers : {'Authorization' : 'JWT ' + myToken }}

      axios.post(SERVER_URL, {content: this.content, star: this.star, movie: this.movieId}, headers)
        .then(res=> {
          console.log(res)
        })
        .catch(err=> {
          console.log(err)
        })
      this.star = 0 
      this.content = ''
      this.reviewAdded = !this.reviewAdded
    },

    onCommentCreated() {
      console.log(' comment created : movieInfo')
      this.reviewAdded = !this.reviewAdded
    },

    onReviewDeleted() {
      this.reviewDeleted = !this.reviewDeleted
    },
  },

}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Source+Sans+Pro:wght@300&display=swap');

.img {
  /* <img src="paris.jpg" alt="Paris" width="400" height="300"> */
    max-width: 100%;
    max-height: 100%;
    margin-bottom: 2px;
}

v-container {
  font:Source Sans Pro;
}
.movieInfo {
  width: 1100px;
  height: 430px;
  display:flex;
  flex-direction: row;
  position: relative;
}
.poster{
  position: relative;

}
.imgTag {
  position: absolute;
  /* margin: auto; */
  top: 5%;
  /* left: 20%;  */
}
.description{
  
}
</style>