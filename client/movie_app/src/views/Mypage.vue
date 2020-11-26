<template>
  <div>
      <h1>my page</h1>
      <hr>
      <h2>내가 작성한 리뷰</h2>
      <br>
        <ul>
            <li v-for="(review, idx) in myReviews" :key="idx">
                <p> {{ review.content }} |
                    내가 준 별점 : {{ review.star }}</p>
            </li>
        </ul>
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

</style>