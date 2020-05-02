<template>
  <div class="about">
    <articleComponent class="article"
      v-bind:articleData = "articleData"
    />
  </div>
</template>

<script>
import articleComponent from '@/components/article.vue';

export default {
  name: 'about',
  components: {
    articleComponent,
  },
  data() {
    return {
      articleData: null,
    };
  },
  mounted() {
    // const proxy = 'https://cors-anywhere.herokuapp.com/';
    const url = 'http://spmiapi.pythonanywhere.com/api/scopusAPI/';
    const token = localStorage.getItem('auth_token');
    console.log(token)
    fetch(url,{
      headers: {
        Authorization: `Token ${token}`,
      },
    })
      .then(res => res.json())
      .then((data) => {
        console.log(data);
        this.articleData = data;
      });
  },
};

</script>
