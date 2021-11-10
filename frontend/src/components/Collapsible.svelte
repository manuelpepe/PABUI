<script>
    export let name;

    let expanded = false;
</script>

<div class="collapsible">
    <h3 style="margin: 0px;">
        <button aria-expanded={expanded} on:click={() => expanded = !expanded}>
            {name}
            <svg viewBox="0 0 20 20" fill="none" >
            <path class="vert" d="M10 1V19" stroke="black" stroke-width="2"/>
            <path d="M1 10L19 10" stroke="black" stroke-width="2"/>
        </button>
    </h3>

    <div class='contents' hidden={!expanded}>
        <slot></slot>
    </div>
</div>

<style>
button {
    display: flex;
    justify-content: space-between;
    width: 100%;
    border: none;
    margin: 0px;
    padding: 1em 0.5em;
}

button[aria-expanded="true"] .vert {
    display: none;
}

button:focus svg{
    outline: 2px solid;
}

svg {
    height: 0.7em;
    width: 0.7em;
}
</style>