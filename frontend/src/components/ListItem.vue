<template>
    <div>
        <p>
            {{list.name}}
            by {{list.author}}
        </p>
        <p>
            {{list.description}}
        </p>
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