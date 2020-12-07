<template>
  <div class='nomargin'>
      <h1>my page</h1>
      <hr>
      <h2>내가 작성한 리뷰</h2>
      <br>

      <h3>내가 쓴 리뷰 페이지로 이동할 수 있습니다.</h3>
        
    <div  v-for="(review, idx) in myReviews" :key="idx" class='myreview'>
        <div class='myMovie'>
            <div> {{ review.movie[0][0].title }}</div>
            <div> 내가 쓴 댓글 수 : {{ review.my_review_count }}</div>
            <div> 내가 준 평균 평점 : 추가하기 </div>
            <div> 내 댓글에 달린 대댓글 수 : 추가하기</div>
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = 'http://127.0.0.1:8000/api/v1/movie_community/user_reviews/'

export default {
    name: 'Mypage',
    data: function() {
        return {
            myReviews: []
        }
    },
    methods: {
        getMyReviews(){
            console.log('getMyReviews called')
            const myToken = localStorage.getItem('jwt')
            axios.get(SERVER_URL, {params:{}, headers: {'Authorization' : 'JWT ' + myToken }})
                .then(res => {
                    console.log(res.data)
                    this.myReviews = res.data
                    console.log(res.data[1].movie[0][0])
                    this.myReviews = res.data
                })
                .catch(err => {
                    console.log(err)
                })
        },
    },
    created: function() {
        this.getMyReviews()
    },
}
</script>

<style>
.nomargin {
    padding: 0px !important;
    margin: 0px !important;
    width: 800px;
    display: flex;
    flex-direction: column;
}
.myreview {
    border-bottom: 0.5px solid #d8d8d8;
}
.myMovie {
    margin: 2%;
    padding: 4%;
    background-color :#f7f7f7;
    border-radius: 10px;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    font-family: 'Noto Serif Kr';
}
.starcolor {
  font-size: 13px;
  margin-top:1%; 
  margin-bottom:1%; 
  margin-left:1px; 
  color: goldenrod;
}

</style>