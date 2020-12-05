<template>
  <div class='nomargin'>
      <h1>my page</h1>
      <hr>
      <h2>내가 작성한 리뷰</h2>
      <br>

      <h3>내가 리뷰 쓴 영화 페이지로 이동하기</h3>
        
    <div  v-for="(review, idx) in myReviews" :key="idx" class='myreview'>
        <div class='reviewcolor'>
            <div> {{ review.content }}</div>
            <div class='starcolor'>
                <span v-for="index in (5-review.star)" :key="index">
                    <i class='far fa-star'></i>
                </span>
                <span v-for="index in review.star" :key="index">
                    <i class='fas fa-star'></i>
                </span>
            </div>
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
.reviewcolor {
    margin: 2%;
    padding: 4%;
    background-color :#f7f7f7;
    border-radius: 10px;
    display: flex;
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