<template>
    <div class="container">
        <textarea class="inputbox" type="inputbox" rows="4" cols="50" readonly="readonly" v-on:click="switchSide" v-model="data_shown">
        </textarea>
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
    props: ["card"],
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
        }
    },
    created() {
        this.fetchAudio();
    }
}
</script>

<style scoped>
    textarea {
        cursor: pointer;
        text-align-last: center;
    }
</style>