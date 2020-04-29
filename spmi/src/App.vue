<template>
  <!-- eslint-disable max-len -->
  <div id="app">
    <navigation v-if="isAuthenticated"></navigation>

    <div class="content">
      <router-view />
    </div>
  </div>
</template>

<style lang="scss" >
#app {
  font-family: "Circe", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #ffffff;
  margin-top: 50px;
}
.isActive {
  width: 200px;
  transition-property: width;
  transition-duration: 0.45s;
  .nav-item{
    a{
      p{
        transform: translateX(30px);
        visibility: visible;
        opacity: 1;
        transition-property: opacity, transform, visibility;
        transition-duration: 0.5s,0.5s;
      }
    }
  }
}
.content {
  padding-left: 100px;
}
body{
  background-color: #2c3e50;
  input:focus,
  select:focus,
  textarea:focus,
  button:focus {
    outline: none;
}
}
button {
  padding: 0;
  border: none;
  font: inherit;
  color: inherit;
  background-color: transparent;
  cursor: pointer;
}
</style>

<script>
// @ is an alias to /src
import navigation from '@/components/navigation.vue';
export default {
  components: {
    navigation,
  },
  data() {
    return {
      items: ['personalData', 'scopus'],
      isAuthenticated: localStorage.getItem('auth_token'),
    };
  },
  beforeUpdate(){
    this.isAuthenticated = localStorage.getItem('auth_token')
  }

};
</script>
