<template>
    <div class="container col-xl-10 col-xxl-8 px-4 py-5">
        <div class="row align-items-center g-lg-5 py-5">
            <div class="col-md-10 mx-auto col-lg-5">
                <div class="card card-container">
                    <Form @submit="handleLogin" :validation-schema="schema"
                        class="p-4 p-md-5 border rounded-3 bg-light">
                        <h5 class="card-title">Login</h5>
                        <div class="form-group">
                            <label for="username">Username</label>
                            <Field name="username" type="text" class="form-control" />
                            <ErrorMessage name="username" class="error-feedback" />
                        </div>
                        <div class="form-group">
                            <label for="password">Password</label>
                            <Field name="password" type="password" class="form-control" />
                            <ErrorMessage name="password" class="error-feedback" />
                        </div>
                        <br>
                        <div class="form-group">
                            <button class="btn btn-primary btn-block" :disabled="loading">
                                <span v-show="loading" class="spinner-border spinner-border-sm"></span>
                                <span>Login</span>
                            </button>
                        </div>
                        <div class="form-group">
                            <div v-if="message" class="alert alert-danger" role="alert">
                                {{ message }}
                            </div>
                        </div>
                    </Form>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import { Form, Field, ErrorMessage } from "vee-validate";
import * as yup from "yup";
export default {
    name: "LoginPage",
    components: {
        Form,
        Field,
        ErrorMessage,
    },
    data() {
        const schema = yup.object().shape({
            username: yup.string().required("Username is required!"),
            password: yup.string().required("Password is required!"),
        });
        return {
            loading: false,
            message: "",
            schema,
        };
    },
    computed: {
        loggedIn() {
            return this.$store.state.auth.status.loggedIn;
        },
    },
    created() {
        if (this.loggedIn) {
            this.$router.push("/");
        }
    },
    methods: {
        handleLogin(user) {
            this.loading = true;
            this.$store.dispatch("auth/login", user).then(
                () => {
                    this.$router.push("/");
                },
                (error) => {
                    this.loading = false;
                    this.message =
                        (error.response &&
                            error.response.data &&
                            error.response.data.message) ||
                        error.message ||
                        error.toString();
                }
            );
        },
    },
};
</script>