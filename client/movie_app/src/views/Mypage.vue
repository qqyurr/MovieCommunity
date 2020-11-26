<template>
  <div class='nomargin'>
      <h1>my page</h1>
      <hr>
      <h2>내가 작성한 리뷰</h2>
      <br>
        

    <div  v-for="(review, idx) in myReviews" :key="idx" class='myreview'>
      

        <div class='reviewcolor'>
                <div > {{ review.content }}</div>
                 <div class='starcolor' style='color:#FFCC80;'>
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
    font-size: 20%;
    margin-left: 3%;
}

</style>