<script>
    import { createEventDispatcher } from "svelte";

    export let placeholder = "";
    export let name = "";
    export let label = "";
    export let value = "";
    export let type = "text";
  
    const dispatch = createEventDispatcher();

    function handleInput(e) {
        value = type.match(/^(number|range)$/)
            ? +e.target.value
            : e.target.value;
        dispatch('input', {value: value});
    };
  </script>
  
  <div class="container">
      <label for="{name}">{label}</label>
      <input {name} {type} {value} {placeholder} on:input={handleInput} />
  </div>

  <style>
    .container {
        font-size: 1.1em;
        margin: 0.7em 0em;
    }
    label {
        width: 20%;
        display: inline-block;
    }
  </style>