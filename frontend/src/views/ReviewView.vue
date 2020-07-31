<template>
    <div class="container">
        <h3 class="mt-3 mb-5">
            {{name}} by {{author}}
        </h3>

        <div v-if="currentCardLoaded" class="current_card">
            <ReviewFlashCard v-bind:listId="this.list.id" v-bind:card="currentCard"/>
        </div>
        <div class="cards">
            <ListFlashCards v-bind:listId="this.list.id"/>
        </div>
    </div>
</template>

<script>
import ReviewFlashCard from '../components/ReviewFlashCard';
import ListFlashCards from '../components/ListFlashCards';
import axios from 'axios';

export default {
    name: "ReviewView",
    components: {
        ReviewFlashCard,
        ListFlashCards
    },
    data() {
        return {
            currentCard: '', //Filled in by loadCurrentCardFromId method
            currentCardLoaded: false,
            cardId: 1,
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
        },
        loadCurrentCardFromId() {
            const path = `http://localhost:5000/list/${this.id}/card/${this.cardId}`;

            axios.get(path)
            .then((res) => {
                this.currentCard = res.data;
                this.currentCardLoaded = true;
            })
            .catch((error) => {
                console.error(error);
            });
        },
    },
    created() {
        this.getList();
        this.loadCurrentCardFromId();
    }
}

</script>

<style scoped>

</style>