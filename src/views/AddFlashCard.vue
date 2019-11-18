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
export default {
    name: "AddFlashCard",
    components: {

    },
    data() {
        return {
            term: 'Insert text here',
            description: 'Insert description here'
        }
    },
    methods: {
        addCard(e) {
            e.preventDefault(); //don't have form submit to a file
            //TODO- Add card using the database
            console.log(this.$route);
            this.$router.push({name: 'list', params: { id: this.$route.params.id }} );
        }
    }
}
</script>

<style scoped>

</style>