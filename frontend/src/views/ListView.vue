<template>
    <div class="container">
        <div class="mt-1 mb-1">
            Name
        </div>
        <input class="inputbox" type="inputbox" v-model="name" v-on:change="updateList">

        <div class="mt-1 mb-1">
            Author
        </div>
        <input class="inputbox" type="inputbox" v-model="author" v-on:change="updateList" readonly>

        <div class="mt-1 mb-1">
            Description
        </div>
        <input class="inputbox" type="inputbox" v-model="description" v-on:change="updateList">

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
import Vue from 'vue';

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
            description: '',
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
                this.list = res.data[0];
                this.name = this.list.name;
                this.author = this.list.author;
                this.description = this.list.description,
                this.language = this.list.language
            })
            .catch((error) => {
                console.error(error);
            });
        },
        updateList() {
            const path = `http://localhost:5000/list/${this.id}/`;

            const payload = {
                id: this.list.id,
                name: this.name,
                author: this.author,
                description: this.description,
                language: this.list.language,
                created: this.list.created,
                modified: Date.now()
            }

            axios.put(path, payload)
            .then((res) => {
                this.list = res.data;
            })
            .catch((error) => {
                console.error(error);
            });
        },
        updateCard(updatedCard) {
            var objIndex = this.cards.findIndex((card => card.id == updatedCard.cardId));
            this.showCards = false;
            //Update object's name property.
            let newCard = this.cards[objIndex];
            newCard["term"] = updatedCard["term"];
            newCard["description"] = updatedCard["description"];
            newCard["last_modified"] = updatedCard["last_modified"];

            Vue.set(this.cards, objIndex, newCard);
            this.showCards = true;
            // Can use either the updatedCard or oldCard's id since they have the same id
            const path = `http://localhost:5000/list/${this.id}/card/${updatedCard.cardId}/`;

            const payload = {
                author: this.cards[objIndex].author,
                term: this.cards[objIndex].term,
                description: this.cards[objIndex].description,
                language: this.cards[objIndex].language,
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
input:read-only {
  background-color: #DCDCDC;
  cursor: not-allowed;
}
</style>