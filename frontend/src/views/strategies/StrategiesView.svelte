<script>
    import { strategies } from '../../stores';
    import Strategy from './Strategy.svelte';
</script>

<div>
    {#each Object.entries($strategies) as [name, params]}
        <Strategy {name} params={params} />
    {/each}
</div>
