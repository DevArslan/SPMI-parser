<template>
  <div class="wrapper">
    <table>
      <!-- <caption>A summary of the UK's most famous punk bands</caption> -->
      <thead>
        <tr>
          <th>Фамилия</th>
          <th>Имя, Отчество</th>
          <th>Ученое звание</th>
          <th>Должность</th>
          <th>Кафедра</th>
          <th>Ссылка</th>
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

    table{
      table-layout: auto;
      width: 100%;
    }
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
