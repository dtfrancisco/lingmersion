<template>
  <div id="app">
    <Lists v-bind:lists="lists"/>
  </div>
</template>

<script>

import Lists from '../components/Lists';
import axios from 'axios';

export default {
  name: "Home",
  components: {
    Lists
  },
  data() {
    return {
      lists: []
    }
  },
  methods: {
    getLists() {
      const path = 'http://localhost:5000/lists/';
      axios.get(path)
        .then((res) => {
          this.lists = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    }
  },
  created() {
    this.getLists();
  }
}
</script>

<style>
</style>
