<template>
  <div class="login">
    <loginForm ></loginForm>
  </div>
</template>

<style lang="scss" scoped>
  .login{
    display: flex;
    justify-content: center;
  }
</style>

<script>
import loginForm from '@/components/loginForm.vue';
// @ is an alias to /src
export default {
  name: 'login',
  components: {
    loginForm,
  },
};

</script>
