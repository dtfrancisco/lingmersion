<template>
    <div>
        <p>
            Name
        </p>
        <input class="inputbox" type="inputbox" v-model="name" v-on:change="updateList">

        <p>
            Author
        </p>
        <input class="inputbox" type="inputbox" v-model="author" v-on:change="updateList">

        <div class="cards">
            <FlashCards v-bind:listId="this.list.id"/>
        </div>
    </div>
</template>

<script>
import FlashCards from '../components/FlashCards';

export default {
    name: "ListView",
    components: {
        FlashCards
    },
    data() {
        return {
            list: this.$route.params.list,
            name: this.$route.params.list.name,
            author: this.$route.params.list.author
        }
    },
    methods: {
        updateList() {
            const updatedList = {
                id: this.list.id,
                name: this.name,
                author: this.author,
                description: this.list.description,
                created: this.list.created,
                modified: Date.now()
            }
            // Send up to parent
            this.$emit('edit-list', updatedList);
        }
    }
    // created() {
    // },
}
</script>

<style scoped>

</style>