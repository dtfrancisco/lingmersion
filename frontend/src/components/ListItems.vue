<template>
    <div>
        <router-link :to="{name: 'list', params: { id: list.id, list: list }}" >
            <ListItem v-bind:list="list"/>
        </router-link>
    </div>
</template>

<script>
import ListItem from './ListItem';

export default {
    name: "ListItems",
    components: {
        ListItem
    },
    props: ["list"]
    
}
</script>

<style scoped>

</style>