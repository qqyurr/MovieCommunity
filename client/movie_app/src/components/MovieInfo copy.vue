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
      v-for="(review, idx) in reviews"
      :key="idx"
      :review="review"
    />
    <!-- 댓글리스트 for문 시작 -->
    <h4 v-for='(review,idx) in movieinfo.reviews' :key='idx'>
      <v-card
          class="pa-md-4"
          elevation="2"
        >{{ review.content }} {{ review.star }}

        <!-- 댓글에 달린 대댓 버튼 시작 -->
        <v-icon
          @click="writeComment" 
          large
          color="blue darken-2"
        >
          mdi-message-text
        </v-icon>
        <!-- 댓글에 달린 대댓 버튼 끝-->

        <!-- 댓글에 달린 삭제 버튼 시작-->
        <v-btn
          @click="deleteReview(review.id)"
          icon
          color="pink"
        >
          <v-icon>mdi-heart</v-icon>
        </v-btn>
        <!-- 댓글에 달린 삭제 버튼 끝-->
      </v-card>

        <!-- 대댓 인풋 시작(숨겨놓음) 댓글 마다 다는것임-->
        <span v-if="showComment">
          <v-text-field
          v-model="commentContent"
          @keypress.enter="createComment(review.id)"
          >
          </v-text-field>
        </span>
        <!-- 대댓 인풋 끝-->



      <!-- 리뷰에 달린 대댓글 출력 -->
      <h4 v-for='(comment, idx) in review.comments' :key='idx'>
        <v-card
          class="ml-10 pa-md-4" color="white" 
          elevation="5"
        >{{ comment.content }} {{ comment.created_at}}</v-card>
      </h4>
    </h4>
    <hr>
    
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
      commentContent: '',

      // 내가 작성한 리뷰인지 아닌지
      myReview: false,
      commentCreated: false,
      showComment: false,
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

    commentCreated() {
      this.getMovieInfo()
    }
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

    // 리뷰 삭제
    deleteReview(reviewId) {
      console.log('delete btn clicked')
      const SERVER_URL = `http://localhost:8000/api/v1/movie_community/reviews/${reviewId}/`
      const myToken = localStorage.getItem('jwt')

      axios.delete(SERVER_URL, {params:{}, headers: {'Authorization' : 'JWT ' + myToken }})
        .then(res => {
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
        this.reviewDeleted = !this.reviewDeleted
    },

    // 대댓글 작성
    createComment(reviewId) {
      const SERVER_URL = `http://localhost:8000/api/v1/movie_community/reviews/${reviewId}/comments/`
      const myToken = localStorage.getItem('jwt')
      const headers = {headers : {'Authorization' : 'JWT ' + myToken }}

      console.log(this.commentContent)
      console.log(this.reviewId)
      axios.post(SERVER_URL, {content: this.commentContent, review: reviewId}, headers)
        .then(res=>{
          console.log(' comment created? ')
          console.log(res)
        })
        .catch(err=> {
          console.log(err)
        })
        this.commentCreated = !this.commentCreated
        this.showComment = false

    },

    writeComment() {
      this.showComment = true
    },
  },

}
</script>

<style>

</style>