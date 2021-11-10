<script>
    export let name;
    export let params;

    import Collapsible from '../../components/Collapsible.svelte';

</script>



<Collapsible {name}>
    {#each params as param}
        <div class="params">
            <span class="param">{param}</span>
        </div>
    {/each}
</Collapsible>

<style>
    .params {
        margin: 0.5em 0em;
    }
    .param {
        display: block;
    }
</style>