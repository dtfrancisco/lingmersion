<template>
    <div>
        <!-- <h3>Your Lists</h3>
        <h3>Recently Created Lists</h3>
        <h3>Most Liked/Viewed Lists</h3> -->
        <div v-bind:key="list.id" v-for="list in lists">
            <ListItem v-bind:list="list"/>
        </div>
    </div>
</template>

<script>
import ListItem from './ListItem';

export default {
    name: "Lists",
    components: {
        ListItem
    },
    props: ["lists"]
    
}
</script>

<style scoped>

</style>