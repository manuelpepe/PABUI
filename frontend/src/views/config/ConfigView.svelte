<script>
    import { config } from '../../stores';
	import { saveConfig } from '../../rest';
	import { deepEqual, recursiveDictFlatten } from '../../utils';
    import { onMount } from 'svelte';
	import { get } from "svelte/store";
import InputField from '../../components/InputField.svelte';

    let dirty = false;
    let message = null;
    let mapping = {}

    onMount(() => {
    });

    function updateDirty() {
        dirty = Object.keys(get(config.checkpoint)).length > 0 && !deepEqual(get(config.checkpoint), get(config))
    }

    function saveConfigAndUpdateMessage() {
        saveConfig().then((saved) => {
            if (saved) {
                message = "Changes saved"
                config.updateCheckpoint()
                updateDirty()
            } else {
                message = "Error saving changes"
            }
        })
    }

    function updateConfigMap() {
        mapping = recursiveDictFlatten(get(config))
    }

    function updaterFor(path) {
        let parts = path.split(".");
        let final = parts.at(-1);
        return (event) => {
            config.update((curval) =>{
                let val = curval;
                parts.slice(0, -1).forEach(key => {
                    val = val[key]
                });
                val[final] = event.detail.value 
                return curval
            });
        }
    }

    function typeFor(path) {
        let value = mapping[path];
        if (typeof value === "number") {
            return "number"
        }
        return "text"
    }
    
    config.subscribe(() => updateDirty());
    config.subscribe(() => updateConfigMap())
    updateDirty()
</script>

<div class="controls">
    <div class="row">
        <button on:click="{saveConfigAndUpdateMessage}" disabled={!dirty}>Save into config.json</button>
        <span style="color: {dirty ? 'red' : 'green'}">
            {dirty ? 'Changes found' : 'No changes'}
        </span>
    </div>

    <div class="row">
        {#if message}
            {message}
        {/if}
    </div>
</div>


<div>
    {#if config}
        {#each Object.keys(mapping) as path}
            <InputField label={path} name={path} type="{typeFor(path)}" bind:value={mapping[path]} on:input="{updaterFor(path)}"/>
        {/each }
    {:else}
        Error loading config
    {/if}
</div>