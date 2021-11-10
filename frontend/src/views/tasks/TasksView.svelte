<script>
    import { tasks } from '../../stores';
	import { saveTasks } from '../../rest';
	import { deepEqual } from '../../utils';
    import Task from './Task.svelte';
	import { get } from "svelte/store";

    let dirty = false;
    let message = null;


    function updateDirty() {
        dirty = get(tasks.checkpoint).length > 0 && !deepEqual(get(tasks.checkpoint), get(tasks))
    }

    function saveTasksAndUpdateMessage() {
        saveTasks().then((saved) => {
            if (saved) {
                message = "Changes saved"
                tasks.updateCheckpoint()
                updateDirty()
            } else {
                message = "Error saving changes"
            }
        })
    }

    tasks.subscribe(() => updateDirty());
    updateDirty()
</script>

<div style="color: {dirty ? 'red' : 'green'}; display: block">
    {dirty ? 'Changes found' : 'No changes'}
</div>

<button on:click="{saveTasksAndUpdateMessage}">Save</button>

{#if message}
    {message}
{/if}

<div>
    {#if tasks}
        {#each [...Array($tasks.length).keys()] as taskIx}
            <Task taskIndex={taskIx}/>
        {/each }
    {:else}
        Error loading tasks
    {/if}
</div>

