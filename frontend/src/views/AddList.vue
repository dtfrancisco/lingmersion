<template>
    <div>
        <form @submit="addList">
            <div>
                <div class="mt-1 mb-1">
                    Name
                </div>
                <input class="inputbox" type="inputbox" v-model="name" placeholder="Insert name of list here">
            </div>
            <div>
                <div class="mt-1 mb-1">
                    Author
                </div>
                <input class="inputbox" type="inputbox" v-model="author" placeholder="Insert author here">
            </div>
            <div>
                <div class="mt-1 mb-1">
                    Description
                </div>
                <input class="inputbox" type="inputbox" v-model="description" placeholder="Insert description here">
            </div>
            <div>
                <div class="mt-1 mb-1">
                    Language
                </div>
                <input class="inputbox" type="inputbox" v-model="language" placeholder="Insert language here">
            </div>

            <input type="submit" value="Submit" class="btn btn-primary mt-3">
        </form>
    </div>   
</template>

<script>
import axios from 'axios';

export default {
    name: "AddList",
    components: {

    },
    data() {
        return {
            name: '',
            author: '',
            description: '',
            language: ''
        }
    },
    methods: {
        addList(e) {
            e.preventDefault(); //don't have form submit to a file

            const path = 'http://localhost:5000/addlist/';

            const payload = {
                name: this.name,
                author: this.author,
                description: this.description,
                language: this.language
            };

            axios.post(path, payload)
            .then(() => {
            })
            .catch((error) => {
                console.error(error);
            });

            this.$router.push({name: 'home'} );
        }
    }
}
</script>

<style scoped>

</style>