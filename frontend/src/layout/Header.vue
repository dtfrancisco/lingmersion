<template>
    <header class="header">
        <h1 class="mt-2">Lingmersion</h1>
        <div class="mb-2" id="nav">
            <router-link to="/">Home</router-link> |
            <router-link to="/about">About</router-link>
        </div>
    </header>
</template>

<script>
export default {
    name: "Header"
}
</script>

<style scoped>
    .header {
        background: #63b7af;
        color: #d4f3ef;
        padding: 5px;
    }

    .header a {
        color: #333;
        padding-right: 5px;
    }
</style>