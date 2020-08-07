<template>
    <div class="container">
        <textarea class="inputbox" type="inputbox" rows="4" cols="50" readonly="readonly" v-on:click="switchSide" v-model="data_shown">
        </textarea>
        <div>
            <span v-show="this.validNextCards[1]" v-on:click="getNextFlashCard('next')" class="image-container">
                <img src="https://cdns.iconmonstr.com/wp-content/assets/preview/2018/240/iconmonstr-arrow-right-thin.png" width="50" height="50"/>
            </span>
            <span v-show="this.validNextCards[0]" v-on:click="getNextFlashCard('prev')" class="image-container">
                <img src="https://cdns.iconmonstr.com/wp-content/assets/preview/2018/240/iconmonstr-arrow-right-thin.png" style="transform:rotate(180deg)" width="50" height="50"/>
            </span>
        </div>
        <div>
            <audio controls v-on:mouseover="loadAudioTrack" ref="audio">
                <source v-bind:src ="audio" type="audio/mp3"/>
                Play audio
            </audio>
        </div>
    </div>

</template>

<script>
import axios from 'axios';

export default {
    name: 'ReviewFlashCard',
    components: {
    },
    props: ["card", "validNextCards"],
    data() {
        return {
            side: 'front',
            data_shown: this.card.term,
            term: this.card.term,
            description: this.card.description,
            audio: '',
            audio_loaded: false,
        }
    },
    methods: {
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
        },
        loadAudioTrack() {
            if (!this.audio_loaded) {
                console.log('Loading audio track');
                this.$refs.audio.pause();
                this.$refs.audio.load();
                this.audio_loaded = true;
            }
        },
        switchSide() {
            if (this.side == 'front') {
                this.data_shown = this.description;
                this.side = 'back';
            }
            else {
                this.data_shown = this.term;
                this.side = 'front';
            }
        },
        getNextFlashCard(direction) {
            console.log('hi', direction);
            if (direction == 'prev') {
                this.$emit('fetch-new-review-flashcard', this.card.cardId - 1);
            }
            else {
                this.$emit('fetch-new-review-flashcard', this.card.cardId + 1);
            }
        }
    },
    created() {
        this.fetchAudio();
    }
}
</script>

<style scoped>
    .image-container{
        cursor: pointer;
        margin-left: -100px;
        margin-right: -100px;
    }
    textarea {
        cursor: pointer;
        text-align-last: center;
    }
</style>