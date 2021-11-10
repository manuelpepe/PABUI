<script>
    export let name;
    export let params;

    import Collapsible from '../../components/Collapsible.svelte';

</script>



<Collapsible {name}>
    {#each params as param}
        <div class="params">
            {#if param["name"]}
                <span class="param">Name: {param["name"]}</span>
            {/if}
            {#if param["type"]}
                <span class="param">Type: {param["type"]}</span>
            {/if}
            {#if param["default"]}
                <span class="param">Default: {param["default"]}</span>
            {/if}
        </div>
    {/each}
</Collapsible>

<style>
    .params {
        margin: 1em 0em;
    }
    .param {
        display: block;
    }
</style>