<template>
  <tr>
    <td>{{item['surname']}}</td>
    <td>{{item['name']}}</td>
    <td>{{item['academicDegree']}}</td>
    <td>{{item['position']}}</td>
    <td>{{item['department']}}</td>
    <td>{{item['link']}}</td>
  </tr>
</template>
<script>

export default {
  props: {
    item: {
      type: Object,
      required: true,
    },
  },
};
</script>
<style lang="scss" scoped>
  td{
    text-align: justify ;
    padding:10px;
    border-right: 0.5px solid #cccccc;
    }
  a{
    text-align: justify ;
    padding:10px;
  }
</style>
