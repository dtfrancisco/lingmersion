<template>
    <div>
        <form @submit="addList">
            <div>
                <p>Name</p>
                <input class="inputbox" type="inputbox" v-model="name" placeholder="Insert name of list here">
            </div>
            <div>
                <p>Author</p>
                <input class="inputbox" type="inputbox" v-model="author" placeholder="Insert author here">
            </div>
            <div>
                <p>Description</p>
                <input class="inputbox" type="inputbox" v-model="description" placeholder="Insert description here">
            </div>
            <input type="submit" value="Submit" class="btn">
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
            };

            axios.post(path, payload)
            .then(() => {
            })
            .catch((error) => {
                console.error(error);
            });

            console.log("Route ", this.$route);
            this.$router.push({name: 'home'} );
        }
    }
}
</script>

<style scoped>

</style>