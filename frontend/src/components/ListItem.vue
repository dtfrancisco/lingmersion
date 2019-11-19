<template>
    <div>
        <router-link :to="{name: 'list', params: { id: list.id, list: list }}" >
            <p>
                {{list.name}}
                by {{list.author}}
            </p>
            <p>
                {{list.description}}
            </p>
        </router-link>
    </div>
</template>

<script>

export default {
    name: "ListItem",
    components: {
    },
    props: ["list"]
    
}
</script>

<style scoped>

</style>