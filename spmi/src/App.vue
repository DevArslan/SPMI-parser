<template>
  <!-- eslint-disable max-len -->
  <div id="app">
    <div id="nav" class="nav" v-bind:class="{ 'isActive' : active }" @mouseover="mouseOver" @mouseleave="mouseLeave">
      <ul>
        <li class="nav-item">
          <router-link to="/">
            <i class="far fa-address-card fa-2x"></i>
            <p>Данные о преподавателях</p>
          </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/about">
            <i class="fas fa-user-plus fa-2x"></i>
            <p>Опубликованные статьи</p>
          </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/addPerson">
            <i class="fas fa-user-plus fa-2x"></i>
            <p>Добавить</p>
          </router-link>
        </li>

      </ul>
    </div>
    <div class="content">
      <router-view />
    </div>
  </div>
</template>

<style lang="scss">
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #ffffff;
  margin-top: 50px;
}
.nav {
  width: 40px;
  padding: 15px;
  background-color: #41b581;
  border-radius: 5px;
  min-height: 100vh;
  position: fixed;
  z-index: 1;
  transition-property: width;
  transition-duration: 0.45s;
  ul {
    list-style: none;
    padding:0px;
  }
  .nav-item {
    text-transform: uppercase;
    margin-bottom: 15px;
    a {
      display: flex;
      align-items:center;
      font-family: Poppins,sans-serif;
      font-size: .875rem;
      font-weight: 400;
      color: #ccc;
      &.router-link-exact-active {
        color: #ffffff;
      }
      p{
        margin:0;
        opacity: 0;
        transform: translateX(0px);
        transition-property: opacity, transform;
        transition-duration: 0.2s,0.25s;
      }
    }
  }
}
.isActive {
  width: 200px;
  transition-property: width;
  transition-duration: 0.45s;
  .nav-item{
    a{
      p{
        transform: translateX(30px);
        opacity: 1;
        transition-property: opacity, transform;
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
}
</style>

<script>
// @ is an alias to /src
export default {
  data() {
    return {
      items: ['personalData', 'scopus'],
      active: false,
    };
  },
  methods: {
    mouseOver() {
      this.active = true;
    },
    mouseLeave() {
      this.active = false;
    },
  },
};
</script>
