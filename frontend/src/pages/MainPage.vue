<template>
  <div class="auth-container">
    <h1>ЦГБ им А.С. Пушкина г. Орёл</h1>
    <div class="popup-wrapper">
      <h2 class="auth-title">Вход</h2>
      <form class="auth-form" @submit.prevent="sendLoginRequest">
        <div class="input-container">
          <input
            v-model="email"
            type="text"
            class="text-input"
            name="login"
            placeholder="Логин"
          />
          <input
            v-model="password"
            type="password"
            class="text-input"
            name="password"
            placeholder="Пароль"
          />
        </div>
        <input type="submit" class="submit-input" name="signin" value="Войти" />
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      email: "",
      password: "",
    };
  },

  computed: {
    formValid() {
      return this.emailValid && this.password != "";
    },

    emailValid() {
      return String(this.email)
        .toLowerCase()
        .match(
          /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
        );
    },
  },
  methods: {
    sendLoginRequest() {
      if (!this.formValid) return;
      return axios.post("api/auth/login/", {
        email: this.email,
        password: this.password,
      });
    },
  },
};
</script>

<style lang="sass" scoped>
.popup-wrapper {
    width: 100%;
	max-width: 26em;
    padding: 3.75em 2em;
    text-align: center;

	background-color: white;
	border-radius: 0.6em;
}

.auth-form {
    width: 100%;
    padding-top: 4em;
}

.auth-container {
	height: 100vh;
	background-color: #5076b6;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 2em;
    padding-bottom: 4em;
    overflow: hidden;
}

form {
	justify-content: space-between;
}

.input-container {
    width: 100%;
    gap: 1em;
    padding-bottom: 6em;
}

.popup-wrapper,
.auth-container,
.input-container,
form {
	display: flex;
	flex-direction: column;
	align-items: center;
}

h1 {
	color: white;
	font-size: 1.6em;
	font-weight: 600;
	color: white;
	line-height: 2em;
    font-variation-settings: "wght" 600;
	font-weight: 600;

}

h2 {
	color: #5076b6;
	font-size: 1.6em;
	line-height: 2em;
    font-variation-settings: "wght" 600;
	font-weight: 600;
}

.text-input {
	width: 100%;
	/*font-family: ; */
	font-size: 1em;
	font-weight: 500;
	line-height: 2.5em;
	padding-left: 1.2em;
	text-align: left;
	background-color: #ccdef1;
	border-radius: 0.5em;
	border-style: hidden;
	background-clip: padding-box;
	outline: none;
}

.submit-input {
	color: white;
	width: 10em;
	height: 3em;
	font-size: 1em;
	font-weight: 600;
	background-color: #5076b6;
	border-radius: 0.4em;
	border-style: hidden;
}
</style>
