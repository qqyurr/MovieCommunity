<template>
<div
  class="d-flex flex-row"
    flat
    tile>
  <div>
    <Menu/>
    <Home/>
  </div>
</div>
</template>

<script>
import Menu from '@/views/Menu'
import Home from '@/views/Home'
export default {
  name: 'App',

  components: {
    Home,
    Menu,
  },

  data: () => ({
    //
  }),
};
</script>
