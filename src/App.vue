<template>
  <nav>
    <router-link to="/">Inicio</router-link> |
    <router-link to="/usuario">usuario</router-link> |
    <router-link to="/medico">medico</router-link> |
    <router-link to="/paciente">paciente</router-link> |
    <router-link to="/familiar">familiar</router-link> |
    <router-link to="/auxiliar">auxiliar</router-link>
  </nav>
  <router-view/>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #3c11e9;
}

nav a.router-link-exact-active {
  color: #424ab9;
}
</style>
