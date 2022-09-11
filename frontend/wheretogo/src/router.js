import { createWebHistory, createRouter } from "vue-router";
import MapPage from "./components/MapPage.vue";
import LoginPage from "./components/LoginPage.vue";
const routes = [
    {
        path: "/",
        name: "map",
        component: MapPage,
    },
    {
        path: "/login",
        component: LoginPage,
    },
];
const router = createRouter({
    history: createWebHistory(),
    routes,
});
export default router;