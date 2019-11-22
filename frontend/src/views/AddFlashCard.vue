<template>
    <div>
        <form @submit="addCard">
            <div>
                <p>Term</p>
                <input class="inputbox" type="inputbox" v-model="term">
            </div>
            <div>
                <p>Description</p>
                <input class="inputbox" type="inputbox" v-model="description">
            </div>
            <input type="submit" value="Submit" class="btn">
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
            term: 'hello',
            description: 'Insert description here'
        }
    },
    methods: {
        addCard(e) {
            e.preventDefault(); //don't have form submit to a file

            const path = 'http://localhost:5000/addcard/';

            const payload = {
                id: this.$route.params.id,
                author: 'sample',
                term: this.term,
                description: this.description,
                language: 'portuguese'
            };

            axios.post(path, payload)
            .then(() => {
            })
            .catch((error) => {
                console.error(error);
            });

            console.log("Route ", this.$route);
            // this.$router.push({name: 'list', params: { id: this.$route.params.id }} );
        }
    }
}
</script>

<style scoped>

</style>