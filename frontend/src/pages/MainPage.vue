<script>
export default {
  name: "App",
};
</script>

<template>
  <div id="page">
    <h1>ЦГБ им А.С. Пушкина г. Орёл</h1>
    <div id="authorize">
      <h2>Вход</h2>
      <form>
        <input type="text" class="text-input" name="login" placeholder="Логин">
        <input type="password" class="text-input" name="password" placeholder="Пароль">
        <input type="submit" class="submit-input" name="signin" value="Войти">
      </form>
    </div>
  </div>
</template>

<style>
  #authorize {
    width: 22rem;
    height: 18rem;
    background-color: white;
    border-radius: 0.6em;
  }

  #page {
    background-color: #5076B6;
  }

  form {
    justify-content: space-between;
  }

  #page, #authorize, form {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  h1 {
    color: white;
    font-size: 1.6em;
    font-weight: 600;
    line-height: 2em;
    /*font-family: ; */
  }

  h2 {
    color: #5076B6;
    font-size: 1.4em;
    font-weight: 600;
    line-height: 2em;
    /*font-family: ; */
  }

  .text-input {
    width: 19em;
    /*font-family: ; */
    font-size: 1em;
    font-weight: 500;
    line-height: 2em;
    padding-left: 1.2em;
    text-align: left;
    background-color: #CCDEF1;
    border-radius: 0.5em;
    border-style: hidden;
    background-clip: padding-box;
    outline: none;
  }

  .submit-input {
    color: white;
    width: 8em;
    height: 2.2em;
    background-color: #5076B6;
    border-radius: 0.4em;
    border-style: hidden;
  }
</style>
