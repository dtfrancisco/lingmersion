<template>
    <div class="container">
        <router-link class="btn btn-primary mt-3 mb-3" :to="{name: 'add list'}" >Create new list </router-link>
        <div class="row">
            <div class="col-md-4 col-sm-4">
                <h5>Your Lists</h5>
            </div>
             <div class="col-md-4 col-sm-4">
                <h5>Most Liked/Viewed Lists</h5>
            </div>
            <div class="col-md-4 col-sm-4">
                <h5>Recently Created Lists</h5>
                <div v-bind:key="list.id" v-for="list in lists">
                    <ListItem v-bind:list="list"/>
                </div>
            </div>
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