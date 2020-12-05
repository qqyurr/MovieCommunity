import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const Authentication = {

  fetchUserData() {
    const token = localStorage.getItem('jwt')
    if (token != null) {
      var base64Url = token.split('.')[1];
      var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
      var jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
          return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
      }).join(''));
      const userInfo = JSON.parse(jsonPayload)
      return {
        isLoggedIn: true,
        userId: userInfo.user_id,
        username: userInfo.username
      }
    } else {
      return {
        isLoggedIn: false,
        userId: '',
        username: ''
      }
    }
  }
}

export default new Vuex.Store({
  state: {
    movieDetail: {movieInfo: {}, actors: [], length_of_reviews: 0, reviews: []},
    selectedMovie: 2,
    drawerState: false,
    loggedInUserData: Authentication.fetchUserData(),
  },
  getters : {
    drawerState: (state) => state.drawerState,

    FetchedMovieDetail(state) {
      return state.movieDetail
    },

    LoggedInUserData(state) {
      return state.loggedInUserData
    }
  },
  mutations: {


// 비동기 api 로직은 모두 actions 에 정의하자 영화 디테일 페이지 불러오는것부터 다시하자~ actions까지 해놓음!

    fetchLoggedInUserData(state) {
      state.loggedInUserData = Authentication.fetchUserData()
    },

    toggleDrawerState (state, data) {
      state.drawerState = data
    },

    fetchMovieDetail(state, movieId) {
      const myToken = localStorage.getItem('jwt')
      axios.get(`http://localhost:8000/api/v1/movie_community/movies/${movieId}/reviews`, {params:{}, headers: {'Authorization' : 'JWT ' + myToken }})
      .then(res=>{
        console.log('review 가 바로 반영되서 날라왔읕텐데? : ', res.data.reviews)
        const acts = res.data.actors.split(',')
        state.movieDetail.reviews = res.data.reviews
        state.movieDetail.movieInfo = res.data
        state.movieDetail.actors = acts.slice(0,5)
        state.movieDetail.length_of_reviews = res.data.reviews.length
      })
      .catch(err => {
        console.log(err)
      })
    },
  },
  actions: {
    // 리뷰작성 포스트요청
    createReview(context, review) {
      console.log('post : ' , review)
      const SERVER_URL = `http://localhost:8000/api/v1/movie_community/movies/${review.movieId}/reviews/`
      const myToken = localStorage.getItem('jwt')
      const headers = {headers : {'Authorization' : 'JWT ' + myToken }}
  
      axios.post(SERVER_URL, {content: review.content, star: review.star, movie: review.movieId}, headers)
        .then(res=> {
          console.log(res)
        })
        .catch(err=> {
          console.log(err)
        })
        .finally(()=> {
          console.log('finally')
          context.commit('fetchMovieDetail', review.movieId)
        })
      
    },

    // 리뷰 업데이트
    updateReview(context, payload) {
      const SERVER_URL = `http://localhost:8000/api/v1/movie_community/reviews/${payload.review.id}/`
      const myToken = localStorage.getItem('jwt')
      const headers = {headers : {'Authorization' : 'JWT ' + myToken }}
      axios.put(SERVER_URL, {content: payload.reviewUpdateContent}, headers)
        .then(res => {
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
        .finally(() => {
          context.commit('fetchMovieDetail', payload.review.movie)
        })
    },

    // 리뷰 삭제
    deleteReview(context, review) {
      console.log('clicked!')
      const myToken = localStorage.getItem('jwt')
      const SERVER_URL = `http://localhost:8000/api/v1/movie_community/reviews/${review.id}/`
  
      axios.delete(SERVER_URL, {params:{}, headers: {'Authorization' : 'JWT ' + myToken }})
        .then(res => {
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
        .finally(() => {
          context.commit('fetchMovieDetail', review.movie)
        }) 
      
    },

    // 대댓글 달기
    createReviewComment(context, payload) {
      const myToken = localStorage.getItem('jwt')
      const SERVER_URL = `http://localhost:8000/api/v1/movie_community/reviews/${payload.review.id}/comments/`
      const headers = {headers : {'Authorization' : 'JWT ' + myToken }}

      axios.post(SERVER_URL, {content: payload.commentContent, review: payload.review.id}, headers)
          .then(res=>{
            console.log(res)
          })
          .catch(err=> {
            console.log(err)
          })
          .finally(() => {
            context.commit('fetchMovieDetail', payload.review.movie)
          }) 
    },
  },


  modules: {
  }
})
