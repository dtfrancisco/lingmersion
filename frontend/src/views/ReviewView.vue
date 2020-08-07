<template>
    <div class="container">
        <h3 class="mt-3 mb-5">
            {{name}} by {{author}}
        </h3>

        <div v-if="currentCardLoaded" class="current_card">
            <ReviewFlashCard v-bind:validNextCards="this.validNextCards" v-bind:card="currentCard" v-on:fetch-new-review-flashcard="fetchNewCard"/>
        </div>
        <div class="cards">
            <ListFlashCards v-bind:cards="cards" v-bind:listId="this.list.id" v-on:edit-card="updateCard"/>
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
            cards: [],
            currentCard: '', //Filled in by loadCurrentCardFromId method
            currentCardLoaded: false,
            cardId: 1,
            id: this.$route.params.id,
            list: '',
            name: '',
            validNextCards: [false, false],
            author: ''
        }
    },
    methods: {
        getCards() {
            const path = `http://localhost:5000/cards/list/${this.id}`;
            axios.get(path)
            .then((res) => {
                this.cards = res.data;

                this.updateValidNextCards();

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
        fetchNewCard(newCardId) {
            this.currentCardLoaded = false;
            this.cardId = newCardId;
            this.updateValidNextCards();
            this.loadCurrentCardFromId();
        },
        updateValidNextCards() {
            if (this.cardId == 1) {
                this.validNextCards[0] = false;
            }
            else if (this.cardId > 1) {
                this.validNextCards[0] = true;
            }

            if (this.cardId == this.cards.length) {
                this.validNextCards[1] = false;
            }
            else {
                this.validNextCards[1] = true;
            }
        },
        updateCard(updatedCard) {
            this.oldCard = this.cards.filter(card => updatedCard.cardId == card.cardId);
            this.cards.pop(this.oldCard);
            this.cards.push(updatedCard);

            // const path = `http://localhost:5000/cards/${this.id}/`;

            // axios.get(path)
            // .then((res) => {
            //     this.list = res.data;
            //     this.name = this.list.name;
            //     this.author = this.list.author;
            // })
            // .catch((error) => {
            //     console.error(error);
            // });
        }
    },
    created() {
        this.getList();
        this.getCards();
        this.loadCurrentCardFromId();
    }
}

</script>

<style scoped>

</style>