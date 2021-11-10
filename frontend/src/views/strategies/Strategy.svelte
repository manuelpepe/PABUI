<script>
    export let name;
    export let params;
    export let doc;

    import Collapsible from '../../components/Collapsible.svelte';

</script>



<Collapsible {name}>
    <div class="data">
        {#if doc}
            <h4>Description</h4>
            <p>{doc}</p>
        {/if}
        <h4>Params</h4>
        {#each params as param}
            <div class="params">
                <span class="param">{param}</span>
            </div>
        {/each}
    </div>
</Collapsible>

<style>
    .data h4,p {
        margin: 0.5em 0.3em;
    }

    .params {
        margin: 0.5em 0em;
    }
    .param {
        display: block;
    }
</style>