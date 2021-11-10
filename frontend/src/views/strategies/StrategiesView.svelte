<script>
    import { strategies } from '../../stores';
    import Strategy from './Strategy.svelte';
</script>

<div>
    {#each Object.entries($strategies) as [name, data]}
        <Strategy {name} params={data["params"]} doc={data["doc"]} />
    {/each}
</div>
