<template>
  <div class="wrapper">
    <table>
      <!-- <caption>A summary of the UK's most famous punk bands</caption> -->
      <thead>
        <tr>
          <th>title</th>
          <th>creator</th>
          <th>publicationName</th>
          <th>volume</th>
          <th>issueIdentifier</th>
          <th>pageRange</th>
          <th>doi</th>
        </tr>
      </thead>
      <tbody>
        <portfolioItem v-for="item of dataOfPerson" v-bind:item="item" v-bind:key="item.id " />
      </tbody>
    </table>
  </div>
</template>
<script>
import portfolioItem from '@/components/portfolioItem.vue';

export default {
  props: ['dataOfPerson'],
  name: 'Portfolio',
  components: {
    portfolioItem,
  },
};
</script>
<style lang='scss' scoped>

  .wrapper{
    table, th, tr{
      border: 1px solid #ccc;
      border-collapse: collapse;
    }
    th{
      padding:10px;
      text-transform: uppercase;
    }
  }

</style>
