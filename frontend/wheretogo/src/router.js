import { createWebHistory, createRouter } from "vue-router";
import MapPage from "./components/MapPage.vue";
import LoginPage from "./components/LoginPage.vue";
import RegistrationPage from "./components/RegistrationPage.vue";
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
    {
        path: "/register",
        component: RegistrationPage,
    },
];
const router = createRouter({
    history: createWebHistory(),
    routes,
});
export default router;