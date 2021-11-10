<script>
import Collapsible from "../../components/Collapsible.svelte";

    export let name;
    export let address;
    export let abifile;
    export let abi;

    let showingABI = false;

    function showABI() {
        showingABI = !showingABI
    }
</script>


<div class="modal" hidden={!showingABI}>
    <pre>
        <textarea name="abi" id="" cols="30" rows="10">{JSON.stringify(JSON.parse(abi), null, 4)}</textarea>
    </pre>
    <button on:click="{showABI}">Close</button>
</div>

<Collapsible {name}>
    <div class="container">
        <div class="field"><span class="label">Address: </span><span>{address}</span></div>
        <div class="field"><span class="label">ABI File: </span><span>{abifile}</span></div>
        <button on:click="{showABI}">Show ABI</button>
    </div>
</Collapsible>

<style>
    .container {
        display: flex;
        flex-direction: column;
    }

    .field {
        margin: 0.3em 0.3em;
    }

    button {
        height: 3em;
        width: 25%;
        align-self: center;
        margin-bottom: 1em;
    }

    .modal {
        position: fixed;
        top: 0;
        left: 25vw;
    }

    textarea {
        width: 50vw;
        height: 80vh;
    }
</style>