<template>
    <div>
        <td>
            <input class="inputbox" type="inputbox" v-model="term" v-on:change="updateCard">
            <div v-if="audio">
                <audio
                    controls
                    src: ="audio">
                    Play audio
                </audio>
            </div>

        </td>
        <td>
            <input class="inputbox" type="inputbox" v-model="description" v-on:change="updateCard">
        </td>
    </div>

</template>

<script>
import axios from 'axios';

export default {
    name: 'EditableFlashCard',
    components: {
    },
    props: ["card"],
    data() {
        return {
            term: this.card.term,
            description: this.card.description,
            audio: ''
        }
    },
    methods: {
        updateCard() {
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
        fetchAudio() {
            if (this.audio) { // Don't fetch audio again if there's already an audio path
                return;
            }
            const payload = {
                word: this.term,
                language: this.card.language
            }

            const path = `http://localhost:5000/getaudio/${payload.word}/${payload.language}`;

            axios.get(path)
              .then((res) => {
                 this.audio = res.data;
                 console.log(this.audio);
              })
            .catch((error) => {
              console.error(error);
            });
        }
    },
    created() {
        this.fetchAudio();
    }
}
</script>

<style scoped>

</style>