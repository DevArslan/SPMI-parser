<template>
  <div class="wrapper">
    <div class="search">
      <input class="surnameSearch" type="text" v-model="surname" placeholder="Введите фамилию сотрудника">
    </div>
    <div class="dataTable">
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
          <portfolioItem v-for="item of filteredList" v-bind:item="item" v-bind:key="item.id " />
        </tbody>
      </table>
    </div>
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
  computed: {
    filteredList() {
      const tempSurname = this.surname;
      try {
        const FiltrDATA = this.dataOfPerson.filter(function(dataOfPersonItem){
        if(tempSurname==='') return true;
        else return dataOfPersonItem['surname'].indexOf(tempSurname) > -1;
       })
       return(FiltrDATA)
      } catch (err) {
        console.log("Данные не получены")//
      }

    }
  }
};
</script>
<style lang='scss' scoped>

  .wrapper{
    .search{
      -webkit-box-shadow: 0px -1px 11px 0px rgba(0,0,0,0.75);
      -moz-box-shadow: 0px -1px 11px 0px rgba(0,0,0,0.75);
      box-shadow: 0px -1px 11px 0px rgba(0,0,0,0.75);
      .surnameSearch{
      margin:20px;
      width:20%;
      padding:5px;
      }
    }
    .dataTable{
      margin-top: 20px;
      -webkit-box-shadow: 0px -1px 11px 0px rgba(0,0,0,0.75);
      -moz-box-shadow: 0px -1px 11px 0px rgba(0,0,0,0.75);
      box-shadow: 0px -1px 11px 0px rgba(0,0,0,0.75);
      table{
        table-layout: auto;
        width: 100%;
      }
      table, th, tr{
        border-bottom: 1px solid #ccc;
        border-collapse: collapse;
        border-right: 0.5px solid #cccccc;
      }
      th{
        padding:10px;
        text-transform: uppercase;
      }
    }
  }


</style>
