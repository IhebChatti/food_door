<template>
  <tr>
    <td> {{ item.food.name }} </td>
    <td> {{ item.food.price }}</td>
    <td>{{ item.quantity }}</td>
    <td>${{ getItemTotal(item).toFixed(2) }}</td>
    <td><button class="delete" /></td>
  </tr>
</template>

<script>
</script>

<style lang="scss" scoped>

</style>
