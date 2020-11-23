<template>
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
    ></v-text-field>

    <v-btn
      :disabled="!valid"
      class="mr-4"
      @click="login"
    >
      로그인
    </v-btn>


  </v-form>
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

    methods: {
      login() {
        axios.post(SERVER_URL + 'api-token-auth/', this.credentials)
          .then(res => {
            console.log(res.data.token)
            localStorage.setItem('jwt', res.data.token)
            this.$router.push({name: 'Home'})

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