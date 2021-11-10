<script>
    export let taskIndex;
    
    import Collapsible from '../../components/Collapsible.svelte';
    import { tasks } from '../../stores';

</script>

<Collapsible name={$tasks[taskIndex].name}>
    <div class="field">
        <label for="strategy">Strategy: </label>
        <input
            bind:value={$tasks[taskIndex].strategy}
            type="text"
            name="strategy"
        />
    </div>

    {#each Object.entries($tasks[taskIndex].params) as [param, value]}
        <div class="field">
            <label for="param-{param}">{param}: </label>
            <input
                bind:value={$tasks[taskIndex].params[param]}
                type="text"
                name="param-{param}"
            />
        </div>
    {/each}
    
    {#each Object.entries($tasks[taskIndex].repeat_every) as [param, value]}
    <div class="field">
        <label for="repeats_every-{param}">{param}: </label>
        <input
            bind:value={$tasks[taskIndex].repeat_every[param]}
            type="number"
            name="repeats_every-{param}"
        />
    </div>
    {/each}
</Collapsible>

<style>

.field {
    font-size: 1.1em;
    margin: 0.7em 0em;
}
.field label {
    width: 20%;
    display: inline-block;
}

</style>