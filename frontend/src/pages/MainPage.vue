<template>
  <h1>Здесь когда-то будет frontend.</h1>
  <p>
    А пока ты можешь проверить как круто проксируется
    <a href="/api">backend</a>
    !
  </p>
  <p>
    А ещё можешь посмотреть как работает роутинг
    <RouterLink to="/">Go to Home</RouterLink>
    !
  </p>
  <p><strong>Current route path:</strong> {{ $route.fullPath }}</p>
</template>

<script>
export default {
  name: "App",
};
</script>
