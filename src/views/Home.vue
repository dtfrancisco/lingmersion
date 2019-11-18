<template>
  <div id="app">
    <Lists v-bind:lists="lists"/>
  </div>
</template>

<script>
import Lists from '../components/Lists';

export default {
  name: "Home",
  components: {
    Lists
  },
  data() {
    return {
      lists: [
        {
          id: 1,
          name: 'List One',
          author: 'Jane Doe',
          description: 'My first list',
          created: 'not yet',
          modified: 'not yet'
        },
        {
          id: 2,
          name: 'List Two',
          author: 'John Smith',
          description: 'Spanish vocabulary',
          created: 'not yet',
          modified: 'not yet'
        }
      ]
    }
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
