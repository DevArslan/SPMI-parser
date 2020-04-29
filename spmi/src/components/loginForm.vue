<template>
  <div class="loginWrapper">
    <form action method="post" class="loginForm">
      <ul>
        <li>
          <label for="login">Login</label>
          <input type="text" placeholder="" v-model="login" name="login" />
        </li>
        <li>
          <label for="password">Password</label>
          <input type="password" v-model="password" name="password" />
        </li>
        <li>
          <button class="loginForm-Button" @click.prevent="tokenAuth">Sign in</button>
        </li>
      </ul>
    </form>
  </div>
</template>

<script>
  export default {
    name: 'loginForm',
    data() {
      return {
        login: '',
        password: '',
      };
    },
    methods: {
      async tokenAuth() {
        const url = 'http://127.0.0.1:8000/api-token-auth/'
        const data = {
            username: this.login,
            password: this.password,
        }
        await fetch(url, {
          method: 'POST',
          headers: {
          'Content-Type': 'application/json',
          },

          body: JSON.stringify(data),
        })
          .then(res => res.json())
          .then(data => localStorage.setItem('auth_token',data.token))
          if(localStorage.getItem('auth_token')){
            this.$router.push('/')
          }

      }
    }
  }
</script>>

<style lang='scss' scoped>


</style>

