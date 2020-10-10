<template>
    <div class="container">

        <table class="table">
            <tr>
                <th>Term</th>
                <th>Description</th>
            </tr>
 

            <div v-bind:key="card.id" v-for="card in cards">
                <tr>
                    <EditableFlashCard v-bind:card="card" v-on:edit-card="editCard"/>
                </tr>
            </div>

        </table>
        <p>
            <a href="https://forvo.com/" title="Pronunciations by Forvo"><img src="https://api.forvo.com/byforvoblue.gif" 
            width="120" height="40" alt="Pronunciations by Forvo" style="border:0" /></a>
        </p>
    </div>
</template>

<script>

import EditableFlashCard from './EditableFlashCard';

export default {
    name: "ListFlashCards",
    components: {
        EditableFlashCard
    },
    props: ["cards"],
    methods: {
        editCard(updatedCard) {
            this.$emit('edit-card', updatedCard);
        }
    }
}
</script>

<style scoped>

</style>