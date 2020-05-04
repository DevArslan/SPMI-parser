<template>
  <div class="addPerson">
    <form action method="post" class="addPersonForm">
      <ul>
        <li>
          <label for="surname">Фамилия</label>
          <input type="text" placeholder="" v-model="surname" name="surname" />
        </li>
        <li>
          <label for="name">Имя, отчество</label>
          <input type="text" v-model="name" name="name" />
        </li>
        <li>
          <label for="link">Ссылка на профиль</label>
          <input type="text" v-model="link" name="link" />
        </li>
        <li>
          <label for="degree">Ученая степень</label>
          <input type="text" v-model="degree" name="degree" />
        </li>
        <li>
          <label for="position">Должность</label>
          <input type="text" v-model="position" name="position" />
        </li>
        <li>
          <label for="department">Кафедра</label>
          <input type="text" v-model="department" name="department" />
        </li>
        <button class="addPersonForm-Button" @click.prevent="setValue">Добавить</button>
      </ul>
    </form>
    <p class="orText">ИЛИ</p>
    <form action method="post" class="addPersonForm">
      <ul>
        <li>
          <label class="fileDownloadLabel" for="fileDownload">Выберите xls файл</label>
          <input name = "fileDownload" id="fileDownload" class="fileDownloadInput" type="file" placeholder="Выбрать" />
        </li>
        <button class="addPersonForm-Button" @click.prevent="downloadExcelFile">Добавить</button>
      </ul>
    </form>
  </div>
</template>

<style lang="scss" scoped>
.addPerson {
  -webkit-box-shadow: 0px -1px 11px 0px rgba(0,0,0,0.75);
  -moz-box-shadow: 0px -1px 11px 0px rgba(0,0,0,0.75);
  box-shadow: 0px -1px 11px 0px rgba(0,0,0,0.75);
  width: 300px;
  margin:0 auto;
  border-radius: 3px;
  .addPerson-nav{
    margin-left: 40px;
    margin-top: 30px;
    width:50%;
    display: flex;
    justify-content:space-between;
    button{
      padding-bottom: 1px;
    }
    .byHandActive{
      border-bottom: 1px solid #67DFD4;
      padding-bottom: 0px;
    }
    .excelActive{
      border-bottom: 1px solid #67DFD4;
      padding-bottom: 0px;
    }
  }
  .addPersonForm {
    ul {
      margin: 0;
      padding:15px;
      li {
        list-style: none;
        margin-bottom: 10px;
        label {
          display: block;
          text-transform: uppercase;
          color: #cccccc;
          font-size: 0.8rem;
        }
        .fileDownloadLabel{
          border:1px solid #ccc;
          text-align: center;
          padding:5px 5px;
        }
        .fileDownloadLabel:hover{
          cursor: pointer;
        }
        .fileDownloadInput{
          width: 0.1px;
          height: 0.1px;
          opacity: 0;
          overflow: hidden;
          position: absolute;
          z-index: -1;
        }
        input{
          background-color: #2c3e50;
          border:none;
          color:whitesmoke;
          caret-color: whitesmoke;
          margin-bottom: 10px;
          border-bottom:1px solid #ccc;
          padding:5px 5px;
          width: 97%;
        }
      }
    }
    .addPersonForm-Button{
      margin-top: 10px;
      padding: 10px 90px 10px 90px;
      border-radius: 3px;
      background-color: #67DFD4;
      color: #ffffff;
      text-transform: uppercase;
      border:none;
    }
  }
  .orText{
    text-align: center;
  }
}
</style>

<script>
// @ is an alias to /src
export default {
  name: 'addPersonForm',
  data() {
    return {
      surname: '',
      name: '',
      link: '',
      degree: '',
      position: '',
      department: '',
    };
  },
  methods: {
    downloadExcelFile(){
      const token = localStorage.getItem('auth_token');
      const formData = new FormData();
      const file = document.querySelector('#fileDownload').files[0]
      const url = 'http://127.0.0.1:8000/api/personalData/upload/data'
      fetch(url, {
        method: 'POST',
        headers: {
          Authorization: `Token ${token}`,
        },
        body: file,
      });
      // const url = http://127.0.0.1:8000/
    },
    setValue() {
      const url = 'http://127.0.0.1:8000/api/personalData/';
      const token = localStorage.getItem('auth_token');
      const data = {
        surname: this.surname,
        name: this.name,
        link: this.link,
        academicDegree: this.degree,
        position: this.position,
        department: this.department,
      };
      fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Token ${token}`,
        },
        body: JSON.stringify(data),
      });
    },
  },
};

</script>
