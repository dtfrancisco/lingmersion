<template>
    <div>
        <form @submit="processForm">
            <div>
                <div class="alert alert-warning" role="alert">
                    Term must be in {{this.language}}!
                </div>
                <p class="errors" v-if="errors.length">
                    <b>Please correct the following error(s):</b>
                    <ul>
                        <li v-bind:key="error" v-for="error in errors">{{ error }}</li>
                    </ul>
                </p>
                <div class="mt-1 mb-1">
                    Term
                </div>
                <input class="inputbox" type="inputbox" v-model="term" placeholder="Add term here">
            </div>
            <div>
                <div class="mt-1 mb-1">
                    Description
                </div>
                <input class="inputbox" type="inputbox" v-model="description" placeholder="Insert description here">
            </div>
            <input type="submit" value="Submit" class="btn btn-primary mt-3">
        </form>
    </div>   
</template>

<script>
import axios from 'axios';

export default {
    name: "AddFlashCard",
    components: {

    },
    data() {
        return {
            term: '',
            description: '',
            id: this.$route.params.id,
            language: this.$route.params.language,
            errors: []
        }
    },
    methods: {
        processForm(e) {
            e.preventDefault(); //don't have form submit to a file

            this.errors = [];

            if (!this.term || !this.description) {

                if (!this.term) {
                    this.errors.push('Term required.');
                }
                if (!this.description) {
                    this.errors.push('Description required.');
                }
                return false;
            }

            this.validateTerm();
        },
        validateTerm() {
            const payload = {
                word: this.term,
                language: this.language
            }

            const path = `http://localhost:5000/getaudio/${payload.word}/${payload.language}`;

            axios.get(path)
              .then(() => {
                  this.addCard();
              })
              .catch((error) => {
                console.error("No word found at ", error);
                this.errors.push('Term is not valid. Please enter a valid term.');
                return false;
              });

            return true;
        },
        addCard() {
            const path = `http://localhost:5000/list/${this.id}/addcard/`;

            const payload = {
                id: this.id,
                author: this.$route.params.author,
                term: this.term,
                description: this.description,
                language: this.language,
            };

            axios.post(path, payload)
            .then(() => {
            })
            .catch((error) => {
                console.error(error);
            });

            this.$router.push({name: 'list', params: { id: this.$route.params.id }} );

        }
    }
}
</script>

<style scoped>
.errors {
    color: red;
}
</style>