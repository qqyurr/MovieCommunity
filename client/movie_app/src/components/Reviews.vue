<template>
  <div>
    <h4 v-for='(review,idx) in movieinfo.reviews' :key='idx'>
      {{ review.content }}
      별점: {{ review.star }}
      <h5 v-for='(comment, idx) in review.comments' :key='idx'>
        --- 대댓글: {{ comment.content }}  - {{ comment.created_at }}
      </h5>
    </h4>
  </div>
</template>

<script>
export default {
  name: 'Reviews',
  props: {
    movieId : String,
  },
}
</script>

<style>

</style>