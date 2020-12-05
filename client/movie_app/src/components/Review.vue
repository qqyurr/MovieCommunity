<template>
  <div class="reviewClass">
      <!-- 댓글 시작 -->
      <span v-if="updateNotClicked">
        <li style="list-style: none; padding: 12px !important; border-top:1px solid; border-color: #EEE; ">
          <div class='comment_one'>
          <h4 class='bold'>익명  {{ review.id }}
            <span v-if="this.$store.getters.LoggedInUserData.userId === this.review.user"  class='pointer'>
              <i class="far fa-edit" style="margin-left:1%" @click="showReview()"></i>
              <i class="far fa-trash-alt pointer" style="margin-left:1%" @click="deleteOneReview(review)"></i>
            </span>
            <span>
              <i class="far fa-comment pointer" style="margin-left:1%" @click="showCommentInput"></i>
            </span>
        
          </h4>
          <div class='reviewComment' style="background-color:#FAF8F5; border-radius:10px; margin-top:5px; padding-top:5px; padding-left: 20px; padding-bottom:20px;" >
            <div class='starcolor' style='margin-top:1%; margin-bottom:1%; color:#FFCC80;'>
            <div style="margin-left: -20px;" v-if="review.star === 0">
            <i class='far fa-star'></i>
            <i class='far fa-star'></i>
            <i class='far fa-star'></i>
            <i class='far fa-star'></i>
            <i class='far fa-star'></i>
            </div>
            <div style="margin-left: -20px;" v-if="review.star === 1">
            <i class='fas fa-star'></i>
            <i class='far fa-star'></i>
            <i class='far fa-star'></i>
            <i class='far fa-star'></i>
            <i class='far fa-star'></i>
            </div>
            <div style="margin-left: -20px;" v-if="review.star === 2">
            <i class='fas fa-star'></i>
            <i class='fas fa-star'></i>
            <i class='far fa-star'></i>
            <i class='far fa-star'></i>
            <i class='far fa-star'></i>
            </div>
            <div style="margin-left: -20px;" v-if="review.star === 3">
            <i class='fas fa-star'></i>
            <i class='fas fa-star'></i>
            <i class='fas fa-star'></i>
            <i class='far fa-star'></i>
            <i class='far fa-star'></i>
            </div>
            <div style="margin-left: -20px;" v-if="review.star === 4">
            <i class='fas fa-star'></i>
            <i class='fas fa-star'></i>
            <i class='fas fa-star'></i>
            <i class='fas fa-star'></i>
            <i class='far fa-star'></i>
            </div>
            <div style="margin-left: -20px;" v-if="review.star === 5">
            <i class='fas fa-star'></i>
            <i class='fas fa-star'></i>
            <i class='fas fa-star'></i>
            <i class='fas fa-star'></i>
            <i class='fas fa-star'></i>
            </div>
            </div>
            <h4>{{review.content}}</h4>
          </div>
          </div>
        </li>
      </span>
      <!-- 댓글 끝 -->

      <!-- 수정) 댓글 업데이트 인풋 출력 시작(수정버튼 클릭시에만 보여주기) 원래 댓글을 숨긴다-->
      <!-- v-model 이 양방향바인딩을 해줘서 value 와 충돌이 일어남 -->
      <span v-if="showUpdateInput">
        <v-text-field
          :value="reviewUpdateContent"
          @keypress.enter="updateOneReview(review)"
          v-model="reviewUpdateContent"
        >
        </v-text-field>
      </span>

        <!-- 대댓 인풋 시작(숨겨놓음) 댓글 마다 다는것임-->
        <span v-if="showComment">
          <v-text-field
          placeholder="여기에 대댓글을 작성해주세요"
          v-model="commentContent"
          @keypress.enter="createOneComment(review)"
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

export default {
    name: 'Review',
    props: {
        review: Object,
    },
    data() {
        return {
            originalContent: this.review.content,
            showUpdateInput: false,
            showComment: false, 
            commentContent: '',
            updateNotClicked: true,
            reviewUpdateContent: this.review.content,
        }
    },
    methods: {
      // 리뷰 수정 아이콘 클릭하면 수정창 보이기
      showReview(){
        this.showUpdateInput = true
        this.updateNotClicked = false
      },

      // 대댓글 아이콘 클릭하면 대댓글 입력창 보이기
      showCommentInput() {
          this.showComment = !this.showComment
      },
      
      // 리뷰 삭제 mutation 함수 호출하기
      deleteOneReview(review) {
        this.$store.dispatch('deleteReview', review)
      },

      // 리뷰 업데이트 mutation 함수 호출하기
      updateOneReview(review){
          const reviewUpdateContent = this.reviewUpdateContent
          this.$store.dispatch('updateReview', {review, reviewUpdateContent})
          this.showUpdateInput = false
          this.updateNotClicked = !this.updateNotClicked
      },

      // 대댓글 작성 mutation 함수 호출하기
      createOneComment(review) {
          const commentContent = this.commentContent
          this.$store.dispatch('createReviewComment', {review, commentContent})
          this.commentCreated = !this.commentCreated
          this.showComment = false
          this.commentContent = ''
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
  margin-left: 2%;
  font-size: 6px;
}
.inputStar {
  font-size: 10px;
}
.pointer {
  cursor : pointer;
}

</style>