<v-card
          class="pa-md-4"
          elevation="2"
        >{{ review.content }} {{ review.star }}

        <!-- 댓글에 달린 대댓 버튼 시작 -->
        <v-icon @click="showCommentInput"
        large 
        color="blue darken-2">
        mdi-message-text
        </v-icon>
        <!-- 댓글에 달린 대댓 버튼 끝-->

        <!-- 댓글에 달린 수정 버튼 시작 -->
        <v-icon @click="updateReview(review.id)">mdi-pencil</v-icon>

        <!-- 댓글에 달린 삭제 버튼 시작-->
        <span v-if="writer">
        <v-btn
            @click="deleteReview(review.id)"
            class="ma-2"
            text
            icon
            color="red lighten-2"
        >
        <v-icon>mdi-thumb-down</v-icon>
          </v-btn>
        </span>
        <!-- 댓글에 달린 삭제 버튼 끝-->
      </v-card>