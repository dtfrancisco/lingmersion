<template>
    <div>
        <router-link :to="{name: 'add card', params: { id: listId }}" >Create new card </router-link>

        <div class="editable-flash-card">
            <div v-bind:key="card.id" v-for="card in cardsInList">
                <EditableFlashCard v-bind:card="card" v-on:edit-card="updateCard"/>
            </div>
        </div>
    </div>
</template>

<script>

import EditableFlashCard from './EditableFlashCard';
import axios from 'axios';

export default {
    name: "FlashCards",
    components: {
        EditableFlashCard
    },
    props: ["listId"],
    data() {
        return {
            cards: []
        }
    },
    computed: {
        cardsInList() {
            return this.cards.filter(card => card.listId === this.listId);
        }
    },
    methods: {
        getCards() {
            const path = 'http://localhost:5000/cards/';
            axios.get(path)
            .then((res) => {
                this.cards = res.data;
            })
            .catch((error) => {
                console.error(error);
            });
        },
        updateCard(updatedCard) {
            this.updatedCards = this.cards.filter(card => updatedCard.cardId !== card.cardId);
            this.updatedCards.push(updatedCard);
            this.cards = this.updatedCards;
        }
    },
    created() {
        this.getCards();
    }
}
</script>

<style scoped>

</style>