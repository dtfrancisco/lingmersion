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

export default {
    name: "FlashCards",
    components: {
        EditableFlashCard
    },
    props: ["listId"],
    data() {
        return {
            cards: [
            {
                listId: 1,
                cardId: 1,
                author: 'Jane Doe',
                term: 'coisa',
                description: 'algo que existe',
                language: 'portuguese',
                created: Date('1995-12-17T03:24:00'),
                modified: Date('1995-12-17T03:24:00')
            },
            {
                listId: 2,
                cardId: 3,
                author: 'John Smith',
                term: 'entender',
                description: 'saber algo',
                language: 'spanish',
                created: Date('1995-12-17T03:24:00'),
                modified: Date('1995-12-17T03:24:00')
            },
            {
                listId: 1,
                cardId: 2,
                author: 'Jane Doe',
                term: 'cachorro',
                description: 'animal fofinho e o melhor amigo do homem',
                language: 'portuguese',
                created: Date('1995-12-17T03:24:00'),
                modified: Date('1995-12-17T03:24:00')
            },
            ]
        }
    },
    computed: {
        cardsInList() {
            return this.cards.filter(card => card.listId === this.listId);
        }
    },
    methods: {
        updateCard(updatedCard) {
            this.updatedCards = this.cards.filter(card => updatedCard.cardId !== card.cardId);
            this.updatedCards.push(updatedCard);
            this.cards = this.updatedCards;
        }
    }
}
</script>

<style scoped>

</style>