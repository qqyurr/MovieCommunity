<template>
  <v-autocomplete
    v-model="newTag"
    :items="entries"
    :search-input.sync="search"
    clearable
    filled
    rounded
    return-object
    @keypress.enter="goToDetail(search)"
  ></v-autocomplete>
</template>

<script>
const BASE_URL = 'http://localhost:8000/api/v1/movie_community/all_movies/'   
import axios from 'axios'

export default {
  name:'Searching',
  data () {
    return {
      newTag: '',
      entries: [],
      queryTerm: ''
    }
  },
  computed: {
    search: {
      get () {
        return this.queryTerm
      },
      set (searchInput) {
        if (this.queryTerm !== searchInput) {
          this.queryTerm = searchInput
          this.loadEntries()
        }
      }
    }
  },
  created () {
    this.loadEntries()
  },
  methods: {
    loadEntries() {
      const myToken = localStorage.getItem('jwt')
      axios.get(BASE_URL, {params:{}, headers: {'Authorization' : 'JWT ' + myToken }})
      .then(res=>{
        console.log(res.data)
        res.data.forEach(element => {
          this.entries.push(element.title)
        });
      })
      .catch(err => {
        console.log(err)
      })
    },
    goToDetail(search) {
      console.log('go to detail clicked')
      const myToken = localStorage.getItem('jwt')
      axios.get(BASE_URL, {params:{}, headers: {'Authorization' : 'JWT ' + myToken }})
      .then(res=>{
        res.data.forEach(element => {
          if (search === element.title){
            this.$router.push('/movies/1/reviews')

            // if (this.$route.path != '/movies/' + element.id + '/reviews') this.$router.push('/movies/' + element.id + '/reviews')
            // this.$router.go(this.$router.currentRoute);
            // return this.$router.push({ name: 'MovieDetail', params: { movieId: element.id }})
            // return this.$router.push('/movies/' + element.id + '/reviews')
          }
        });
      })
    },

  }

}
</script>

<style>

</style>