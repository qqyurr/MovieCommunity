const Authentication = {

  fetchUserData() {
    const token = localStorage.getItem('jwt')
    if (token != null) {
      var base64Url = token.split('.')[1];
      var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
      var jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
          return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
      }).join(''));
      const userInfo = JSON.parse(jsonPayload)
      return {
        isLoggedIn: true,
        userId: userInfo.user_id,
        username: userInfo.username
      }
    } else {
      return {
        isLoggedIn: false,
        userId: '',
        username: ''
      }
    }
  }
}


const state = {
  movieDetail: {movieInfo: {}, actors: [], length_of_reviews: 0, reviews: []},
  selectedMovie: 2,
  drawerState: false,
  loggedInUserData: Authentication.fetchUserData(),

  fetchUserData() {
    const token = localStorage.getItem('jwt')
    if (token != null) {
      var base64Url = token.split('.')[1];
      var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
      var jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
          return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
      }).join(''));
      const userInfo = JSON.parse(jsonPayload)
      return {
        isLoggedIn: true,
        userId: userInfo.user_id,
        username: userInfo.username
      }
    } else {
      return {
        isLoggedIn: false,
        userId: '',
        username: ''
      }
    }
  }
}

export {Authentication}
export default state