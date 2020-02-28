<template>
  <div class="addPerson">
    <addPersonForm class="addPersonForm"></addPersonForm>
  </div>
</template>

<style lang="scss" scoped>
  .addPersonForm{
    margin:0 auto;
  }
</style>

<script>
import addPersonForm from '@/components/addPersonForm.vue';
// @ is an alias to /src
export default {
  name: 'addPerson',
  components: {
    addPersonForm,
  },
};

</script>
