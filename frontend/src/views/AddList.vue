<template>
    <div>
        <form @submit="addList">
            <p class="errors" v-if="errors.length">
                <b>Please correct the following error(s):</b>
                <ul>
                    <li v-bind:key="error" v-for="error in errors">{{ error }}</li>
                </ul>
            </p>

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
                <select id="selectNumber" @change="changeLanguage($event)">
                    <option value="" selected disabled>Choose a language</option>
                    <option v-for="language in languages" v-bind:value="language.id" v-bind:key="language.id">{{ language.name }}</option>
                </select>
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
            language: '',
            errors: [],
            languages: []
        }
    },
    methods: {
        addList(e) {
            e.preventDefault(); //don't have form submit to a file

            if (!this.name || !this.author || !this.description || !this.language) {
                this.errors = [];

                if (!this.name) {
                    this.errors.push('Name required.');
                }
                if (!this.author) {
                    this.errors.push('Author required.');
                }
                if (!this.description) {
                    this.errors.push('Description required.');
                }
                if (!this.language) {
                    this.errors.push('Language required.');
                }
                return false;
            }

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
        },
        getLanguages() {
            const path = `http://localhost:5000/languages`;

            axios.get(path)
            .then((res) => {
                this.languages = res.data;
                console.log(this.languages);
            })
            .catch((error) => {
                console.error(error);
            });

        },
        changeLanguage(e) {
            this.language = e.target.options[e.target.options.selectedIndex].text
        }
    },
    created() {
        this.getLanguages();
    }
}
</script>

<style scoped>
.errors {
    color: red;
}
</style>