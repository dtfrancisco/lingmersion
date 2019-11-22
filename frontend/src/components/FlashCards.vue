<template>
    <div>
        <router-link :to="{name: 'add card', params: { id: listId }}" >Create new card </router-link>

        <div class="editable-flash-cards">
            <table>
                <tr>
                    <th>Term</th>
                    <th>Description</th>
                </tr>
                <div v-bind:key="card.id" v-for="card in cardsInList">
                    <tr>
                        <EditableFlashCard v-bind:card="card" v-on:edit-card="updateCard"/>
                    </tr>
                </div>
            </table>
            <p>
                <a href="https://forvo.com/" title="Pronunciations by Forvo"><img src="https://api.forvo.com/byforvoblue.gif" 
                width="120" height="40" alt="Pronunciations by Forvo" style="border:0" /></a>
            </p>
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