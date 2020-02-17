<template>
  <div class="about">
    <h1>This is an about page</h1>
  </div>
</template>

<script>


export default {
  mounted() {
    // const proxy = 'https://cors-anywhere.herokuapp.com/';
    const url = 'http://127.0.0.1:8000/api/articleData';
    fetch(url)
      .then(res => res.json())
      .then((data) => {
        console.log(data);
        this.dataOfPerson = data;
      });
  },
};

</script>
