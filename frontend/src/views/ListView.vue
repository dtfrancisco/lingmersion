<template>
    <div class="container">
        <div class="mt-1 mb-1">
            Name
        </div>
        <input class="inputbox" type="inputbox" v-model="name" v-on:change="updateList">

        <div class="mt-1 mb-1">
            Author
        </div>
        <input class="inputbox" type="inputbox" v-model="author" v-on:change="updateList">

        <div>
            <router-link class="btn btn-primary mt-3 mb-3 mr-3" :to="{name: 'add card', params: { id: id, author: author, language: language }}" >Create new card </router-link>
            <router-link class="btn btn-primary mt-3 mb-3" :to="{name: 'review cards', params: { id: id, cards: cards}}" >Review cards</router-link>
        </div>

        <div v-if="showCards" class="cards">
            <ListFlashCards v-bind:cards="cards" v-on:edit-card="updateCard"/>
        </div>
    </div>
</template>

<script>
import ListFlashCards from '../components/ListFlashCards';
import axios from 'axios';

export default {
    name: "ListView",
    components: {
        ListFlashCards
    },
    data() {
        return {
            cards: [],
            id: this.$route.params.id,
            list: '',
            name: '',
            author: '',
            language: '',
            showCards: false
        }
    },
    methods: {
        getCards() {
            const path = `http://localhost:5000/cards/list/${this.id}`;
            axios.get(path)
            .then((res) => {
                this.cards = res.data;
                this.showCards = true;
            })
            .catch((error) => {
                console.error(error);
            });
        },
        getList() {
            this.id = this.$route.params.id;

            const path = `http://localhost:5000/list/${this.id}`;

            axios.get(path)
            .then((res) => {
                this.list = res.data;
                this.name = this.list.name;
                this.author = this.list.author;
                this.language = this.list.language
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
                language: this.list.language,
                created: this.list.created,
                modified: Date.now()
            }
            // Send up to parent
            this.$emit('edit-list', updatedList);
        },
        updateCard(updatedCard) {
            var objIndex = this.cards.findIndex((card => card.cardId == updatedCard.cardId));
            this.showCards = false;
            //Update object's name property.
            this.cards[objIndex] = updatedCard;
            this.showCards = true;
            // Can use either the updatedCard or oldCard's id since they have the same id
            const path = `http://localhost:5000/list/${this.id}/card/${updatedCard.cardId}/`;

            const payload = {
                listId: this.cards[objIndex].listId,
                cardId: this.cards[objIndex].cardId,
                author: this.cards[objIndex].author,
                term: this.cards[objIndex].term,
                description: this.cards[objIndex].description,
                language: this.cards[objIndex].language,
                created: this.cards[objIndex].created,
                modified: this.cards[objIndex].modified
            };

            axios.put(path, payload)
            .then((res) => {
                this.list = res.data;
            })
            .catch((error) => {
                console.error(error);
            });
        }
    },
    created() {
        this.getList();
        this.getCards();
    }
}
</script>

<style scoped>

</style>