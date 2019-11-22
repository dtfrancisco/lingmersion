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
import axios from 'axios';

export default {
    name: "ListView",
    components: {
        FlashCards
    },
    data() {
        return {
            id: this.$route.params.id,
            list: '',
            name: '',
            author: ''
        }
    },
    methods: {
        getList() {
            this.id = this.$route.params.id;

            const path = `http://localhost:5000/list/${this.id}`;

            axios.get(path)
            .then((res) => {
                this.list = res.data;
                this.name = this.list.name;
                this.author = this.list.author;
            })
            .catch((error) => {
                console.error(error);
            });
        },
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
    },
    created() {
        this.getList();
    }
}
</script>

<style scoped>

</style>