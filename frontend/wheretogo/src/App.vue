<template>

  <body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark" style="height: 7vh">
      <div class="container-fluid">
        <a class="navbar-brand" href="/">WhereToGo</a>
        <div class="collapse navbar-collapse" id="navbarNavDropdown">
          <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
            <div v-if="!currentUser" class="navbar-nav ml-auto">
              <li class="nav-item">
                <router-link to="/register" class="nav-link">
                  Sign Up
                </router-link>
              </li>
              <li class="nav-item">
                <router-link to="/login" class="nav-link">
                  Login
                </router-link>
              </li>
            </div>
            <div v-if="currentUser" class="navbar-nav ml-auto">
              <li class="nav-item">
                <router-link to="/profile" class="nav-link">
                  {{ currentUser.username }}
                </router-link>
              </li>
              <li class="nav-item">
                <a class="nav-link" @click.prevent="logOut">
                  LogOut
                </a>
              </li>
            </div>
          </ul>
        </div>
      </div>
    </nav>


    <div class="container-fluid m-0 p-0" style="height: 93vh">
      <router-view />
    </div>
  </body>
</template>

<script>
export default {
  name: "App",
  computed: {
    currentUser() {
      return this.$store.state.auth.user;
    },
    showAdminBoard() {
      if (this.currentUser && this.currentUser["roles"]) {
        return this.currentUser["roles"].includes("ROLE_ADMIN");
      }
      return false;
    },
    showModeratorBoard() {
      if (this.currentUser && this.currentUser["roles"]) {
        return this.currentUser["roles"].includes("ROLE_MODERATOR");
      }
      return false;
    },
  },
  methods: {
    logOut() {
      this.$store.dispatch("auth/logout");
      this.$router.push("/login");
    },
  },
};
</script>
