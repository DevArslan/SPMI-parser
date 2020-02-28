<template>
<!-- eslint-disable max-len -->
  <div class="wrapper">
    <table>
      <!-- <caption>A summary of the UK's most famous punk bands</caption> -->
      <thead>
        <tr>
          <th>Автор</th>
          <th>Главный автор</th>
          <th>Название</th>
          <th>Журнал</th>
          <th>Дата публикации</th>
          <th>Том</th>
          <th>Выпуск</th>
          <th>Страницы</th>
          <th>doi</th>
        </tr>
      </thead>
      <tbody>
        <articleItem v-for="item of dateSort(articleData)" v-bind:item="item" v-bind:key="item.id " />
      </tbody>
    </table>
  </div>
</template>
<script>
import articleItem from '@/components/articleItem.vue';

export default {
  props: ['articleData'],
  name: 'articleComponent',
  components: {
    articleItem,
  },
  computed: {
    dateSort: function (dateArray) {
      for (let itemArray of dateArray) {
      itemArray['date'] = 'Complete'
     }
     return dateArray
    }
  }
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
