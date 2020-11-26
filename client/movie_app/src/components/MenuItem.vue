<template>
  <div>
      <span v-if="item.showIfLoggined === this.$store.state.login">
        <v-list-item>
        <v-list-item-icon>
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-item-icon>
          <router-link :to="item.url" class='link'> {{item.title}}</router-link>
        </v-list-item>
      </span>
  </div>
</template>

<script>
export default {
  name: 'MenuItem',
  props: {
    item: Object
  },

  methods: {
  },
}
</script>

<style>

</style>