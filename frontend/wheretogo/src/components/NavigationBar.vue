<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
      <a class="navbar-brand" href="/">WhereToGo</a>
      <div class="collapse navbar-collapse" id="navbarNavDropdown">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link" href="">Map</a>
          </li>
        </ul>
        <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
          <li class="nav-item dropdown">
            <a
              class="nav-link dropdown-toggle"
              href="#"
              id="navbarDropdownMenuLink"
              role="button"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              Username
            </a>
            <ul
              class="dropdown-menu dropdown-menu-end"
              aria-labelledby="navbarDropdownMenuLink"
            >
              <li>
                <a class="dropdown-item" href="">Admin page</a>
              </li>
              <li>
                <a class="dropdown-item" href="">Change E-Mail</a>
              </li>
              <li>
                <a class="dropdown-item" href="">Sign Out</a>
              </li>
            </ul>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="">Sign In</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="">Sign Up</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavigationBar",
};
</script>
