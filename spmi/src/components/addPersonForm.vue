<template>
  <div class="addPerson">
    <form action method="post" class="addPersonForm">
      <ul>
        <li>
          <label for="surname">Фамилия</label>
          <input type="text" v-model="surname" name="surname" />
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
        <button @click.prevent="setValue">Отправить</button>
      </ul>
    </form>
  </div>
</template>

<style lang="scss">
.addPerson {
  .addPersonForm {
    ul {
      li {
        list-style: none;
        label {
          display: block;
        }
      }
    }
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
    setValue() {
      const url = 'http://127.0.0.1:8000/api/personalData/';
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
        },
        body: JSON.stringify(data),
      });
    },
  },
};

</script>
