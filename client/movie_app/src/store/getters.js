const getters = {
  drawerState: (state) => state.drawerState,

  FetchedMovieDetail(state) {
    console.log(state.movieDetail)
    return state.movieDetail
  },

  LoggedInUserData(state) {
    return state.loggedInUserData
  }
}

export default getters