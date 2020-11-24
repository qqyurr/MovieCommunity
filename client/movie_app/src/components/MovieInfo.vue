<template>
  <v-container>
    <!-- 영화 정보 출력  -->
    <h3>
      영화 번호 : {{this.movieId}}
      {{ movieinfo.title }}
    </h3>
    <img :src="movieinfo.poster_path" alt="">
    <h3>
      <v-card
        elevation="2"
      > {{ movieinfo.description }} 
      </v-card>
      줄거리 : {{ movieinfo.description }}
    </h3>
    <hr>
    <v-card
      class="d-inline"
      elevation="2"
    >이미지옆에 설명</v-card>

    

    <!-- 리뷰창 시작 : 리뷰 컴포넌트 불러오기 -->
    <Review
      v-for="(review, idx) in movieinfo.reviews"
      :key="idx"
      :review="review"
      @comment-created="onCommentCreated"
      @review-deleted="onReviewDeleted"
    />

    
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
        console.log(res)
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

</style>