<script>
    import { contracts } from '../../stores';
    import Contract from './Contract.svelte';
</script>


<div>
    {#each Object.entries($contracts) as [name, data]}
        <Contract {name} address={data["address"]} abifile={data["abifile"]} abi={data["abi"]}/>
    {/each}
</div> 
