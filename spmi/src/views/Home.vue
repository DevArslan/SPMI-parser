<template>
  <div class="home">

    <Portfolio class="portfolio"
      v-bind:dataOfPerson = "dataOfPerson"
    />
  </div>
</template>

<style lang = "scss" scoped>

</style>

<script>
// @ is an alias to /src

import Portfolio from '@/components/portfolio.vue';

export default {
  name: 'home',
  components: {
    Portfolio,
  },
  data() {
    return {
      dataOfPerson: null,
    };
  },
  mounted() {
    // const proxy = 'https://cors-anywhere.herokuapp.com/';
    const url = 'http://127.0.0.1:8000/api/personalData';
    const token = localStorage.getItem('auth_token');
    fetch(url,{
      headers: {
        Authorization: `Token ${token}`,
      },
    })
      .then(res => res.json())
      .then((data) => {
        // console.log(data);
        this.dataOfPerson = data;
      });
  },
};

</script>
