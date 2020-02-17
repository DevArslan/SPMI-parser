<template>
  <div class="addPerson">
    <addPersonForm></addPersonForm>
  </div>
</template>

<style lang="scss">

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
