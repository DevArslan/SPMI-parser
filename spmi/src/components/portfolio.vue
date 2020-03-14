<template>
  <div class="wrapper">
    <input type="text" v-model="surname" placeholder="Введите фамилию сотрудника">
    <p>{{surname}}</p>
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
        <portfolioItem v-for="item of filteredList()" v-bind:item="item" v-bind:key="item.id " />
      </tbody>
    </table>
  </div>
</template>
<script>
import portfolioItem from '@/components/portfolioItem.vue';

export default {
  props: {
    dataOfPerson: {
      type: Array,
      required: true,
    }
  },
  name: 'Portfolio',
  components: {
    portfolioItem,
  },
  data() {
    return {
      surname: '',
      dataOfPersonData: this.dataOfPerson,
    };
  },
  methods: {
    filteredList() {
      const tempSurname = this.surname;
      console.log(this.dataOfPerson)
      const FiltrDATA = this.dataOfPerson.filter(function(dataOfPersonItem){
        if(tempSurname==='') return true;
        else return dataOfPersonItem['surname'].indexOf(tempSurname) > -1;
       })
      console.log(FiltrDATA)//
      return(FiltrDATA)//
    }
  }
  // mounted() {
  //   this.dataOfPersonData = this.filteredList();
  //   console.log(dataOfPersonData)
  // },
  //  computed: {
  //    filteredList(callback) {
  //     // this.dataOfPersonData = [{}];
  //     // dataOfPersonData = this.dataOfPerson;
  //     const tempSurname = this.surname;
  //       // return this.dataOfPersonData.filter(function(dataOfPersonItem){
  //       //   if(tempSurname==='') return true;
  //       //   else return dataOfPersonItem['name'].indexOf(tempSurname) > -1;
  //       // })
  //       console.log(this.dataOfPerson)
  //     return callback(this.dataOfPerson);
  //    },
  //  },
};
</script>
<style lang='scss' scoped>

  .wrapper{
    .buttonClass{
      margin-left: 50%;
    }
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
