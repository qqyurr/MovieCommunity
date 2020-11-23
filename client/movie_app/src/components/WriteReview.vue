<template>
  <v-container>
    <v-card
    dark>
      <v-textarea
        name="input"
        filled
        label="Review"
        auto-grow
      ></v-textarea>
      <v-rating
          v-model="rating"
          background-color="white"
          color="yellow accent-4"
          dense
          hover
          size="18"
        ></v-rating>
        <v-btn>
          이 버튼을 누르면 리뷰 저장 + 별점 저장 
        </v-btn>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name:'WriteReview',
}
</script>

<style>

</style>