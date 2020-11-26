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
    watch: {
    '$store.state.login': function() {
      console.log('I am Login.vue watch : loggined status changed : ', this.$store.state.login)
    }
  },

    methods: {
      login() {
        axios.post(SERVER_URL + 'api-token-auth/', this.credentials)
          .then(res => {
            console.log(res.data.token)
            localStorage.setItem('jwt', res.data.token)
            this.$router.push({name: 'Home'})
            this.$store.state.login = true
            this.$store.state.loginUserName = res.data.token
            console.log('this.$store.state.login', this.$store.state.login)
            this.$forceUpdate()
            const token = res.data.token
            var base64Url = token.split('.')[1];
            var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
            var jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
                return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
            }).join(''));

            console.log(jsonPayload)
            const userInfo = JSON.parse(jsonPayload)
            console.log(userInfo)
            console.log(userInfo.user_id)
            this.$store.state.loggedInUserData = userInfo.user_id

            console.log('logged in user id : ' , this.$store.getters.getLoggedInUserData)
            

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