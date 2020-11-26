<template>
  <div class="reviewClass">
      <!-- 댓글 시작 -->
      <span v-if="updateNotClicked">
        <li style="list-style: none; padding: 12px !important; border-top:1px solid; border-color: #EEE; ">
          <div class='comment_one'>

          <h4 class='bold'>익명  {{ review.id }}
        

            <span v-if="writer"  class='pointer'>
              <i class="far fa-edit" style="margin-left:1%" @click="showReview()"></i>
            </span>
            <span>
              <i class="far fa-comment pointer" style="margin-left:1%" @click="showCommentInput"></i>
            </span>
            <span v-if="writer">
              <i class="far fa-trash-alt pointer" style="margin-left:1%" @click="deleteReview(review.id)"></i>
            </span>
         
        
          </h4>
          <div class='reviewComment' style="background-color:#FAF8F5; border-radius:10px; margin-top:5px; padding-top:5px; padding-left: 20px; padding-bottom:20px;" >
            <div class='starcolor' style='margin-top:1%; margin-bottom:1%; color:#FFCC80;'>
            <div v-if="review.star === 0">
            <i class='far fa-star'></i>
            <i class='far fa-star'></i>
            <i class='far fa-star'></i>
            <i class='far fa-star'></i>
            <i class='far fa-star'></i>
            </div>
            <div v-if="review.star === 1">
            <i class='fas fa-star'></i>
            <i class='far fa-star'></i>
            <i class='far fa-star'></i>
            <i class='far fa-star'></i>
            <i class='far fa-star'></i>
            </div>
            <div v-if="review.star === 2">
            <i class='fas fa-star'></i>
            <i class='fas fa-star'></i>
            <i class='far fa-star'></i>
            <i class='far fa-star'></i>
            <i class='far fa-star'></i>
            </div>
            <div v-if="review.star === 3">
            <i class='fas fa-star'></i>
            <i class='fas fa-star'></i>
            <i class='fas fa-star'></i>
            <i class='far fa-star'></i>
            <i class='far fa-star'></i>
            </div>
            <div v-if="review.star === 4">
            <i class='fas fa-star'></i>
            <i class='fas fa-star'></i>
            <i class='fas fa-star'></i>
            <i class='fas fa-star'></i>
            <i class='far fa-star'></i>
            </div>
            <div v-if="review.star === 5">
            <i class='fas fa-star'></i>
            <i class='fas fa-star'></i>
            <i class='fas fa-star'></i>
            <i class='fas fa-star'></i>
            <i class='fas fa-star'></i>
            </div>
            </div>
            <h4>{{review.content}}</h4>
          </div>


          <!-- 로그인 유저와 리뷰 작성자가 일치할 때만 수정/삭제 버튼 보여주기 시작-->
          <!-- 로그인 유저와 리뷰 작성자가 일치할 때만 수정/삭제 버튼 보여주기 끝-->
          </div>

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
        <li class='inputStar' style="margin-left:1%; list-style: none;padding: 12px !important; border-top:1px solid; border-radius:10px; border-color: #EEE; ">

        <span class="comment" style="font-size:20px; font-color:black; margin-left:1%">
          <i class="fa fa-share fa-flip-vertical re" style=color:#ccc;></i>
          {{ comment.content }}</span>
          <span>{{comment.created_at}}</span>
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
    showReview(){
      this.showUpdateInput = true
      this.updateNotClicked = false
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
.comment_one {
  display:flex;
  flex-direction: column;
}
.starcolor {
  font-size: 6px;
}
.inputStar {
  font-size: 10px;
}
.pointer {
  cursor : pointer;
}

</style>