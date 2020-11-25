<template>
  <div class="reviewClass">
      <!-- 댓글 시작 -->
      <span v-if="updateNotClicked">
        <li style="list-style: none; padding: 12px !important; border-top:1px solid; border-color: #EEE; ">
          <span class="comment" style="font-size:13px;">{{ review.content }}</span>
            <span>{{review.star}}</span>
            <i class="far fa-comment" style="margin-left:1%" @click="showCommentInput"></i>

            <!-- 로그인 유저와 리뷰 작성자가 일치할 때만 수정/삭제 버튼 보여주기 시작-->
            <span v-if="writer">
              <i class="far fa-edit" style="margin-left:1%" @click="showReview(review.id)"></i>
              <i class="far fa-trash-alt" style="margin-left:1%" @click="deleteReview(review.id)"></i>
            </span>
            <!-- 로그인 유저와 리뷰 작성자가 일치할 때만 수정/삭제 버튼 보여주기 끝-->

        </li>
      </span>
      <!-- 댓글 끝 -->

      <!-- 수정) 댓글 업데이트 인풋 출력 시작(수정버튼 클릭시에만 보여주기) 원래 댓글을 숨긴다-->
      <!-- v-model 이 양방향바인딩을 해줘서 value 와 충돌이 일어남 -->
      <span v-if="showUpdateInput">
        <v-text-field
          :value="reviewUpdateContent"
          @keypress.enter="updateReview(review.id)"
          v-model="reviewUpdateContent"
        >
        </v-text-field>

        
      </span>

        <!-- 대댓 인풋 시작(숨겨놓음) 댓글 마다 다는것임-->
        <span v-if="showComment">
          <v-text-field
          placeholder="여기에 대댓글을 작성해주세요"
          v-model="commentContent"
          @keypress.enter="createComment(review.id)"
          >
          </v-text-field>
        </span>
        <!-- 대댓 인풋 끝-->

      <!-- 리뷰에 달린 대댓글 출력 -->
      <div v-for="(comment, idx) in review.comments" :key='idx'>
        <li style="margin-left:2%; list-style: none;padding: 12px !important; border-top:1px solid; border-color: #EEE; ">
        <i class="fa fa-share fa-flip-vertical re" style=color:#ccc;></i>
        <span class="comment" style="font-size:13px; margin-left:1%">{{ comment.content }}</span>
          <span>{{comment.createdTime}}</span>
        </li>
      </div>
      <!-- 리뷰에 달린 대댓글 출력 끝 -->
  </div>
</template>

<script>
import axios from 'axios'

const myToken = localStorage.getItem('jwt')

export default {
    name: 'Review',
    props: {
        review: Object,
    },
    data() {
        return {
            writer: false,
            commentCreated: false,

            originalContent: this.review.content,

            //showUpdateInput
            showUpdateInput: false,

            showComment: false, 
            commentContent: '',

            updateNotClicked: true,

            // 유저가 수정한 리뷰 내용
            reviewUpdateContent: this.review.content,
        }
    },
    watch: {
        writer() {
            this.$emit('review-deleted')
        },
    },
    // 로그인한 유저가 댓글의 작성자와 같은지 확인
    created: function() {
        const reviewId = this.review.id
        const SERVER_URL = `http://localhost:8000/api/v1/movie_community/reviews/${reviewId}/writer/`
        axios.get(SERVER_URL, {params:{reviewId:reviewId}, headers: {'Authorization' : 'JWT ' + myToken }})
        .then(res => {
            this.writer= res.data.isWriter
        })
        .catch(err=>{
            console.log(err)
        })
    },
    methods: {

    // 리뷰 수정창 보이기
    showReview(reviewId){
      console.log('review update clicked')
      console.log(reviewId)
      this.showUpdateInput = true
      console.log("showupdateInput : ", this.showUpdateInput)
      this.updateNotClicked = false
      console.log("updateNotClicked: ", this.updateNotClicked)
      console.log(this.review.content)
     
    },

    // 리뷰 업데이트 하기
    updateReview(reviewId){
      const SERVER_URL = `http://localhost:8000/api/v1/movie_community/reviews/${reviewId}/`
      const headers = {headers : {'Authorization' : 'JWT ' + myToken }}
      axios.put(SERVER_URL, {content: this.reviewUpdateContent}, headers)
        .then(res => {
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
        this.showUpdateInput = false
        this.updateNotClicked = !this.updateNotClicked
        this.$emit('comment-created')
    },
    
    // 리뷰 삭제
    deleteReview(reviewId) {
      console.log('delete btn clicked')
      const SERVER_URL = `http://localhost:8000/api/v1/movie_community/reviews/${reviewId}/`

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
        this.showComment = !this.showComment
        },
    // 대댓글 작성
    createComment(reviewId) {
        const SERVER_URL = `http://localhost:8000/api/v1/movie_community/reviews/${reviewId}/comments/`
        const headers = {headers : {'Authorization' : 'JWT ' + myToken }}

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

<style scoped>
.reviewClass {
    font-family: 'Nanum Gothic Coding', monospace;
}
</style>