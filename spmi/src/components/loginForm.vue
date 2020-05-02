<template>
  <div class="loginWrapper">
    <div class="loginNav">
      <button class="loginNav-signIn"  @click.prevent="logInUpChange" v-bind:class="{ 'signInButtonActive' : !active }">Sign In</button>
      <button class="loginNav-signUp" @click.prevent="logInUpChange" v-bind:class="{ 'signUpButtonActive' : active }">Sign Up</button>
    </div>
    <div class="loginForms">
      <form class="loginForms-signIn" action method="post" v-bind:class="{ 'signInInactive' : active }">
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
      <form class="loginForms-signUp" action method="post" v-bind:class="{ 'signUpActive' : active }">
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
            <label for="password">Confirm Password</label>
            <input type="password" v-model="password" name="password" />
          </li>
          <li>
            <button class="loginForm-Button" @click.prevent="tokenAuth">Sign Up</button>
          </li>
        </ul>
      </form>
    </div>
  </div>
</template>

<style lang='scss' scoped>
  .loginWrapper{
    -webkit-box-shadow: 0px -1px 11px 0px rgba(0,0,0,0.75);
    -moz-box-shadow: 0px -1px 11px 0px rgba(0,0,0,0.75);
    box-shadow: 0px -1px 11px 0px rgba(0,0,0,0.75);
    width: 300px;
    margin:0 auto;
    border-radius: 3px;
    .loginNav{
      margin-left: 40px;
      margin-top: 30px;
      width:50%;
      display: flex;
      justify-content:space-between;
      button{
        padding-bottom: 1px;
      }
      .signInButtonActive{
        border-bottom: 1px solid #67DFD4;
        padding-bottom: 0px;
      }
      .signUpButtonActive{
        border-bottom: 1px solid #67DFD4;
        padding-bottom: 0px;
      }
    }
    .loginForms{
      box-sizing: border-box;
      margin-top: 35px;
      .loginForms-signUp{
        opacity: 0;
        position: relative;
        left:300px;
        top:-170px;
        transition: opacity .5s ease, transform .5s ease;
      }
      .loginForms-signIn{
        transition: opacity .5s ease, transform .5s ease;
      }
      .signInInactive{
        transform: translateX(-300px);
        opacity: 0;
      }
      .signUpActive{
        transform: translateX(-300px);
        opacity: 1;
      }
    }
    li{
      list-style: none;
        label{
          display: block;
          text-transform: uppercase;
          color: #cccccc;
          font-size: 0.8rem;
        }
        input{
          background-color: #2c3e50;
          border:none;
          color:whitesmoke;
          caret-color: whitesmoke;
          margin-bottom: 10px;
          border-bottom:1px solid #ccc;
          padding:5px 5px;

        }
        button{
          margin-top: 10px;
          padding: 5px;
          border-radius: 3px;
          background-color: #67DFD4;
          color: #ffffff;
          text-transform: uppercase;
          border:none;
        }
      }
  }


</style>

<script>
  export default {
    name: 'loginForm',
    data() {
      return {
        login: '',
        password: '',
        active: '',
      };
    },
    methods: {
      async tokenAuth() {
        const url = 'https://spmiapi.pythonanywhere.com/api-token-auth/'
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
      },
      logInUpChange(){
        this.active = !this.active;
        console.log(this.active);
      }

    }
  }
</script>>



