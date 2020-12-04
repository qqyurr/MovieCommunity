<template>

  <div>
    <div class="header">
      <h2>LogIn</h2>  
    </div>
    <v-form
      ref="form"
      v-model="valid"
      lazy-validation
    >
      <v-text-field
        v-model="credentials.username"
        :counter="10"
        label="ID"
        required
      ></v-text-field>

      <v-text-field
        v-model="credentials.password"
        :type="show1 ? 'text' : 'password'"
        label="password"
        required
        @keypress.enter="login"
      ></v-text-field>

      <v-btn
        :disabled="!valid"
        class="mr-4"
        @click="login"
      >
      로그인
      </v-btn>
    </v-form>
  </div>
</template>

<script>
import axios from 'axios'
import {mapMutations, mapGetters} from 'vuex'

const SERVER_URL = 'http://127.0.0.1:8000/api/v1/movie_community/accounts/'

  export default {
    name : 'Login',
    data: () => ({
      valid: true,
      show1 : false,
      credentials: {
        username : '',
        password: '',
      },
    }),

    methods: {
      ...mapMutations(['toggleLoginState', 'fetchLoggedInUsername']),
      ...mapGetters(['LoggedInUserData']),

      login() {
        axios.post(SERVER_URL + 'api-token-auth/', this.credentials)
          .then(res => {
            localStorage.setItem('jwt', res.data.token)
            this.$router.push({name: 'Home'})
            this.$store.commit('fetchLoggedInUserData')
          })
          .catch(err => {
            console.log(err)
          })
      },
      validate () {
        this.$refs.form.validate()
      },
    },
  }
</script>