<template>
  <v-sheet
    height="400"
    class="overflow-hidden"
    style="position: relative;"
  >
 
  <Home/>
  </v-sheet>
</template>

<script>
import Home from '@/views/Home'
export default {
  name: 'App',

  components: {
    Home,
  },

  data: () => ({
    //
  }),
};
</script>
