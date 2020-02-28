<template>
  <tr>
    <td>{{item['author']}}</td>
    <td>{{item['creator']}}</td>
    <td>{{item['title']}}</td>
    <td>{{item['journal']}}</td>
    <td>{{item['date']}}</td>
    <td>{{item['volume']}}</td>
    <td>{{item['issue']}}</td>
    <td>{{item['pages']}}</td>
    <td>{{item['doi']}}</td>
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
    border: 1px solid #ccc;
    }
  a{
    text-align: justify ;
    padding:10px;
  }
</style>
