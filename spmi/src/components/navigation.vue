<template>
<div id="nav" class="nav" v-bind:class="{ 'isActive' : active }" @mouseover="mouseOver" @mouseleave="mouseLeave">
      <ul>
        <li class="nav-item">
          <router-link to="/">
            <!--<i class="far fa-address-card fa-2x"></i>-->
            <span><svg xmlns="http://www.w3.org/2000/svg" fill="#ffffff" enable-background="new 0 0 24 24" height="36" viewBox="0 0 24 24" width="36"><g><rect fill="none" height="24" width="24"/></g><g><g/><g><g><path d="M16.67,13.13C18.04,14.06,19,15.32,19,17v3h4v-3 C23,14.82,19.43,13.53,16.67,13.13z" fill-rule="evenodd"/></g><g><circle cx="9" cy="8" fill-rule="evenodd" r="4"/></g><g><path d="M15,12c2.21,0,4-1.79,4-4c0-2.21-1.79-4-4-4c-0.47,0-0.91,0.1-1.33,0.24 C14.5,5.27,15,6.58,15,8s-0.5,2.73-1.33,3.76C14.09,11.9,14.53,12,15,12z" fill-rule="evenodd"/></g><g><path d="M9,13c-2.67,0-8,1.34-8,4v3h16v-3C17,14.34,11.67,13,9,13z" fill-rule="evenodd"/></g></g></g></svg></span>
            <p>Данные о преподавателях</p>
          </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/about">
            <span><svg xmlns="http://www.w3.org/2000/svg" fill="#ffffff" height="36" viewBox="0 0 24 24" width="36"><path d="M19 5v14H5V5h14m1.1-2H3.9c-.5 0-.9.4-.9.9v16.2c0 .4.4.9.9.9h16.2c.4 0 .9-.5.9-.9V3.9c0-.5-.5-.9-.9-.9zM11 7h6v2h-6V7zm0 4h6v2h-6v-2zm0 4h6v2h-6zM7 7h2v2H7zm0 4h2v2H7zm0 4h2v2H7z"/><path d="M0 0h24v24H0z" fill="none"/></svg></span>
            <p>Опубликованные статьи</p>
          </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/addPerson">
          <span>
            <svg xmlns="http://www.w3.org/2000/svg" fill="#ffffff" height="36" viewBox="0 0 24 24" width="36"><path d="M0 0h24v24H0z" fill="none"/><path d="M15 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm-9-2V7H4v3H1v2h3v3h2v-3h3v-2H6zm9 4c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg>
          </span>
            <!-- <i class="fas fa-user-plus fa-2x"></i> -->
            <p>Добавить</p>
          </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/login">
          <span>
            <svg xmlns="http://www.w3.org/2000/svg" fill="#ffffff" height="36" viewBox="0 0 24 24" width="36"><path d="M0 0h24v24H0z" fill="none"/><path d="M15 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm-9-2V7H4v3H1v2h3v3h2v-3h3v-2H6zm9 4c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg>
          </span>
            <!-- <i class="fas fa-user-plus fa-2x"></i> -->
            <p>Login</p>
          </router-link>
        </li>
      </ul>
      <!-- НАДО ПЕРЕДЕЛАТЬ МЕНЮ В ЦИКЛ (ЕСЛИ ПРИДУМАТЬ ЧТО-ТО С ИКОНКАМИ) -->
</div>
</template>

<style lang="scss" >

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
        svg{
          fill: #67DFD4;
        }
      }
      p{
        margin:0;
        opacity: 0;
        transform: translateX(0px);
        transition-property: opacity, transform, visibility;
        transition-duration: 0.2s,0.25s;
        visibility: hidden;
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
        visibility: visible;
        opacity: 1;
        transition-property: opacity, transform, visibility;
        transition-duration: 0.5s,0.5s;
      }
    }
  }
}

</style>


<script>

export default {
  name: 'navigation',
  data() {
    return {
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

