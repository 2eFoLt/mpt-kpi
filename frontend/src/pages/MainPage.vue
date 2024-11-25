<script>
export default {
  name: "App",
};
</script>

<template>
  <div class="auth-container">
    <h1>ЦГБ им А.С. Пушкина г. Орёл</h1>
    <div class="popup-wrapper">
      <h2>Вход</h2>
      <form class="auth-form">
        <div class="input-container">
          <input
            type="text"
            class="text-input"
            name="login"
            placeholder="Логин"
          />
          <input
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
	/*font-family: ; */
}

h2 {
	color: #5076b6;
	font-size: 1.6em;
	font-weight: 600;
	line-height: 2em;
	/*font-family: ; */
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
