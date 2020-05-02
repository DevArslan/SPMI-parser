<template>
<!-- eslint-disable max-len -->
  <div class="wrapper">
    <div class="selectSort" @click="selectSort">
      <button class="selectSort-button" >Сортировать по</button>
        <svg class="selectSort-icon" :class="{ active: isActive }" xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M7.41 8.59L12 13.17l4.59-4.58L18 10l-6 6-6-6 1.41-1.41z"/><path d="M0 0h24v24H0V0z" fill="none"/></svg>
    </div>
    <div class="selectList" v-if="isActive">
      <ul>
        <li class="selectList-item" @click="dateSort">По дате</li>
        <li class="selectList-item" @click="articleNameSort">По названию статьи</li>
        <li class="selectList-item" @click="authorNameSort">По автору</li>
        <li class="selectList-item" @click="creatorNameSort">По главному автору</li>
      </ul>
    </div>

    <div class="exportButtons">
      <button class="exportButtons-excel" @click="exportToExcel">Экспорт в Excel</button>
      <button class="exportButtons-word" @click="exportToDoc">Экспорт в Word</button>
      <button class="exportButtons-pdf" @click="exportToPDF">Экспорт в PDF</button>
    </div>

    <div class="search">
      <ul>
        <li>
          <label for="author">Автор</label>
          <input name="author" class="search-author" type="text" v-model="author" >
        </li>
        <li>
          <label for="articleTitle">Название статьи</label>
          <input name="articleTitle" class="search-articleTitle" type="text" v-model="title" >
        </li>
        <li>
          <label for="journalTitle">Название журнала</label>
          <input name="journalTitle" class="search-journal" type="text" v-model="journal" >
        </li>
      </ul>
    </div>




    <table class="articlesTable" border="1" id="titleTable">
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
                                                            ЗДЕСЬ БЫЛО ЧТО-ТО ВАЖНОЕ, НО Я ЕГО УДАЛИЛ (v-bind:key="item")
      </transition-group> -->
      <articleItem v-for="item of filteredList" v-bind:item="item" v-bind:key="item.id "/>
    </table>
  </div>
</template>
<script>
import articleItem from '@/components/articleItem.vue';
import jsPDF from 'jspdf'
import autoTable from 'jspdf-autotable'

export default {
  props: ['articleData'],
  name: 'articleComponent',
  components: {
    articleItem,
  },
  data() {
    return {
      message: '123456qwertyasdfgh',
      isActive: false,
      author: '',
      journal: '',
      title: '',
    };
  },
  computed: {
    filteredList() {
      const tempAuthor = this.author.charAt(0).toUpperCase() + this.author.slice(1);
      const tempJournal = this.journal.charAt(0).toUpperCase() + this.journal.slice(1);
      const tempTitle = this.title.charAt(0).toUpperCase() + this.title.slice(1);
      try {
        const filteredData = this.articleData.filter(function(articleDataItem){
        if(tempAuthor==='' && tempJournal==='' && tempTitle==='') return true;
        else{
          try {
            return articleDataItem.creator.indexOf(tempAuthor) > -1 && articleDataItem.journal.indexOf(tempJournal) > -1 && articleDataItem.title.indexOf(tempTitle) > -1;
          } catch (error) {
            console.log('Пустое поле')
          }
        }
       })
       console.log(filteredData)
       return(filteredData)
      } catch (err) {
        console.log(err)
        console.log("Данные не получены")
      }
    }
  },
  methods: {
    exportToPDF(){
      const pdf = new jsPDF()
      autoTable(pdf, {
        html: '#titleTable',
        margin: { left:0 },
        columnStyles: {
          0: {cellWidth: 20},
          1: {cellWidth: 20},
          2: {cellWidth: 60},
          3: {cellWidth: 60},
          4: {cellWidth: 20},
          5: {cellWidth: 20},
          6: {cellWidth: 20},
          7: {cellWidth: 20},
          8: {cellWidth: 20},
        }
      })
      pdf.save('table.pdf')
    },
    exportToExcel(){
      let downloadLink = '';
      const dataType = 'application/vnd.ms-excel';
      const tableSelect = document.getElementById('titleTable');
      const tableHTML = tableSelect.outerHTML.replace(/ /g, '%20');

      const filename = 'excelArticles'+'.xls';

      downloadLink = document.createElement("a");

      document.body.appendChild(downloadLink);

      downloadLink.href = 'data:' + dataType + ', ' + tableHTML;

      downloadLink.download = filename;

      downloadLink.click();

      document.body.removeChild(downloadLink);

    },
    exportToDoc(){
      let downloadLink = '';
      const dataType = 'application/msword';
      const tableSelect = document.getElementById('titleTable');
      const tableHTML = tableSelect.outerHTML.replace(/ /g, '%20');

      const filename = 'excelArticles'+'..doc';

      downloadLink = document.createElement("a");

      document.body.appendChild(downloadLink);

      downloadLink.href = 'data:' + dataType + ', ' + tableHTML;

      downloadLink.download = filename;

      downloadLink.click();

      document.body.removeChild(downloadLink);
  },
    selectSort(){
      this.isActive = !this.isActive;
    },
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
      console.log(this.articleData.sort(this.dateSortFunction));
      return this.articleData.sort(this.dateSortFunction);
    },
    articleNameSortFunction(a, b){
      const c = a.title
      const d = b.title
      if (c < d) {
        return -1;
      }
      if (c > d) {
        return 1;
      }
      return 0;
    },
    articleNameSort(){
      return this.articleData.sort(this.articleNameSortFunction);
    },
    authorNameSortFunction(a, b){
      const c = a.author
      const d = b.author
      if (c < d) {
        return -1;
      }
      if (c > d) {
        return 1;
      }
      return 0;
    },
    authorNameSort(){
      return this.articleData.sort(this.authorNameSortFunction);
    },
    creatorNameSortFunction(a, b){
      const c = a.creator
      const d = b.creator
      if (c < d) {
        return -1;
      }
      if (c > d) {
        return 1;
      }
      return 0;
    },
    creatorNameSort(){
      return this.articleData.sort(this.creatorNameSortFunction);
    }

  },
};
</script>
<style lang='scss' scoped>

  .wrapper{
    -webkit-box-shadow: 0px -1px 11px 0px rgba(0,0,0,0.75);
    -moz-box-shadow: 0px -1px 11px 0px rgba(0,0,0,0.75);
    box-shadow: 0px -1px 11px 0px rgba(0,0,0,0.75);
    padding-top:20px;
    .exportButtons{
      margin-left:20px;
      display: flex;
      justify-content: space-between;
      width:30%;
       button{
        margin-top: 10px;
        padding: 5px;
        border-radius: 3px;
        color: #ffffff;
        text-transform: uppercase;
        border:none;
      }
      .exportButtons-word{
        background-color: #2A5594;
      }
      .exportButtons-excel{
        background-color: #016F38;
      }
      .exportButtons-pdf{
        background-color: #EB0C0C;
      }
    }

    .search{
      margin:20px;
      ul {
      margin: 0;
      padding:0;
      width:50%;
      display: flex;
      justify-content: space-between;
      li {
        width: 60%;
        list-style: none;
        margin-bottom: 10px;
        label {
          display: block;
          text-transform: uppercase;
          color: #cccccc;
          font-size: 0.8rem;
        }
        input{
          padding:5px;
          background-color: #2c3e50;
          border:none;
          color:whitesmoke;
          caret-color: whitesmoke;
          margin-bottom: 10px;
          border-bottom:1px solid #ccc;
        }
      }
    }
    }
    .selectSort{
      margin-left: 20px;
      width: 150px;
      padding: 5px;
      border: 1px solid #ccc;
      border-radius: 3px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      .selectSort-icon{
          fill: white;
          transform: rotate(0deg);
          transition: all 0.3s;
      }
      .selectSort-icon.active{
          transform: rotate(-180deg);
          transition: all 0.3s;
      }
    }
    .articlesTable{
      margin-top:20px;
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
    .selectList{
      position: absolute;
      background-color: #2C3E50;
      z-index: 9999;
      margin: 20px;
      width: 150px;
      padding: 5px;
      border: 1px solid #ccc;
      border-radius: 3px;
      ul{
        padding:0px;
        list-style: none;
        .selectList-item{
          cursor: pointer;
          margin:0px 0px 8px 0px;
        }
      }
    }
  }
  // .flip-list-move {
  //   transition: transform 1s;
  // }
</style>
