<template>
  <div>
      <!-- 댓글 시작 -->
      <v-card
          class="pa-md-4"
          elevation="2"
        >{{ review.content }} {{ review.star }}

        <!-- 댓글에 달린 대댓 버튼 시작 -->
        <v-icon @click="showCommentInput"
        large 
        color="blue darken-2">
        mdi-message-text
        </v-icon>
        <!-- 댓글에 달린 대댓 버튼 끝-->

        <!-- 댓글에 달린 삭제 버튼 시작-->

        <v-btn
            @click="deleteReview(review.id)"
            class="ma-2"
            text
            icon
            color="red lighten-2"
        >
        <v-icon>mdi-thumb-down</v-icon>
          </v-btn>

        <!-- 댓글에 달린 삭제 버튼 끝-->
      </v-card>
      <!-- 댓글 끝 -->

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
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Review',
    props: {
        review: Object,
    },
    data() {
        return {
            commentCreated: false,
            showComment: false,
            commentContent: '',
        }
    },
    watch: {
    },
    methods: {
    
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
        this.$emit('review-deleted')
    },

    showCommentInput() {
        this.showComment = true
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
            this.commentContent = ''
            this.$emit('comment-created')
        },
    },
}
</script>

<style>

</style>