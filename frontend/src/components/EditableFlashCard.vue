<template>
    <div>
        <div>
            <p v-if="this.card.cardId === 1">
                Term
            </p>
            <input class="inputbox" type="inputbox" v-model="term" v-on:change="updateCard">
        </div>
        <div>
            <p v-if="this.card.cardId === 1">
                Description
            </p>
            <input class="inputbox" type="inputbox" v-model="description" v-on:change="updateCard">
        </div>
    </div>

</template>

<script>

export default {
    name: 'EditableFlashCard',
    components: {
    },
    props: ["card"],
    data() {
        return {
            term: this.card.term,
            description: this.card.description,
        }
    },
    methods: {
        updateCard() {
            // console.log(this.term);
            // console.log(this.card.term);
            const updatedCard = {
                listId: this.card.listId,
                cardId: this.card.cardId,
                author: this.card.author,
                term: this.term,
                description: this.description,
                language: this.card.language,
                created: this.card.created,
                modified: Date.now()
            }
            // Send up to parent
            this.$emit('edit-card', updatedCard);

        },
    }
}
</script>

<style scoped>

</style>