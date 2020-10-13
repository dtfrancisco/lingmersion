<template>
    <div>
        <form @submit="addCard">
            <div>
                <div class="alert alert-warning" role="alert">
                    Term must be in {{this.language}}!
                </div>
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
            language: this.$route.params.language
        }
    },
    methods: {
        addCard(e) {
            e.preventDefault(); //don't have form submit to a file

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

</style>