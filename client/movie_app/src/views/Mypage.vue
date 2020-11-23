<template>
  <div>
      <h1>my page</h1>
      <hr>
      <h2>내가 작성한 리뷰</h2>

      <p>반지의제왕 ⭑⭑⭑⭑⭑ go </p>
      <p>해리포뤄 ⭑⭑⭑⭑⭑ go </p>
      <p>호빗 ⭑⭑⭑⭑⭑ go </p>

      
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = ''

export default {
    name: 'Mypage',
    data: function() {
        return {
            myReviews: []
        }
    },
    methods: {
        getMyReviews(){
            axios.get(SERVER_URL)
                .then(res => {
                    console.log(res)
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