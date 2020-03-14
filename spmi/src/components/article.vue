<template>
<!-- eslint-disable max-len -->
  <div class="wrapper">
    <button @click="dateSort">Сортировка по дате</button>
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
      <!-- <transition-group name="flip-list" tag="tbody">
          <articleItem v-for="item of articleData" v-bind:item="item" v-bind:key="item" />
      </transition-group> -->
      <articleItem v-for="item of articleData" v-bind:item="item" v-bind:key="item" />
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
  data() {
    return {
      message: '123456qwertyasdfgh',
    };
  },
  methods: {
    dateSortFunction(a, b) {
      const c = Date.parse(a.date);
      const d = Date.parse(b.date);
      if (c < d) {
        return -1;
      }
      if (c > d) {
        return 1;
      }
      return 0;
    },
    dateSort() {
      // `this` указывает на экземпляр vm
      // for(item in this.articleData){
      // }
      console.log(this.articleData.sort(this.dateSortFunction));
      return this.articleData.sort(this.dateSortFunction);
    },
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
  // .flip-list-move {
  //   transition: transform 1s;
  // }
</style>
