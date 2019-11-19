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
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

.btn {
  display: inline-block;
  border: none;
  background: #555;
  color: #fff;
  padding: 7px 20px;
  cursor: pointer;
}
</style>
