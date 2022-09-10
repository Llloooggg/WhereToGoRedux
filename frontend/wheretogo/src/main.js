import { createApp } from "vue";
import App from "./App.vue";
import axios from "axios";

import "bootstrap/dist/css/bootstrap.min.css";

import NavigationBar from "./components/NavigationBar.vue";

const app = createApp(App);

app.config.globalProperties.axios = axios;

app.component("NavigationBar", NavigationBar);

app.mount("#app");
