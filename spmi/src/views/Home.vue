<template>
  <div class="home">

    <Portfolio class="portfolio"
      v-bind:dataOfPerson = "dataOfPerson"
    />
  </div>
</template>

<style lang = "scss" scoped>
  .portfolio{
    -webkit-box-shadow: 0px -1px 11px 0px rgba(0,0,0,0.75);
    -moz-box-shadow: 0px -1px 11px 0px rgba(0,0,0,0.75);
    box-shadow: 0px -1px 11px 0px rgba(0,0,0,0.75);
  }
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
    fetch(url)
      .then(res => res.json())
      .then((data) => {
        console.log(data);
        this.dataOfPerson = data;
      });
  },
};

</script>
