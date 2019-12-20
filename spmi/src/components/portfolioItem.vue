<template>
  <tr>
    <td>{{item['dc:title']}}</td>
    <td>{{item['dc:creator']}}</td>
    <td>{{item['prism:publicationName']}}</td>
    <td>{{item['prism:volume']}}</td>
    <td>{{item['prism:issueIdentifier']}}</td>
    <td>{{item['prism:pageRange']}}</td>
    <td>https://doi.org/{{item['prism:doi']}}</td>
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
