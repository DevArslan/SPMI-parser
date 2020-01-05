<template>
  <div class="home">

    <Portfolio
      v-bind:dataOfPerson = "dataOfPerson"
    />
  </div>
</template>

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
    const proxy = 'https://cors-anywhere.herokuapp.com/';
    const url = `${proxy}https://api.elsevier.com/content/search/scopus?query=au-id(23099248900)&apiKey=287f28aed3a978f68bfa3ef6991edc94`;
    fetch(url)
      .then(res => res.json())
      .then((data) => {
        this.dataOfPerson = data['search-results'].entry;
      });
  },
};

</script>
