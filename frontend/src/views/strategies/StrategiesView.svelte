<script>
    import { strategies } from '../../stores';
	import { get } from "svelte/store";
import Strategy from './Strategy.svelte';

    let parsedStrategies = {};

    /*
        The PARSER_REGEX is used to match the following strings into three groups:
            *args
            **kwargs
            myVar
            myVar: myType
            myVar = 'my value'
            myVar: myType = 'my value'
    */
    let PARSER_REGEX = /(\*?\*?[a-zA-Z1-9_-]*):?(?: ?([a-zA-Z1-9_-]*))?(?: ?= ?(.*))?/;


    function parseParamString(paramDef) {
        let match = paramDef.match(PARSER_REGEX);
        return {
            name: match[1],
            type: match[2] !== '' ? match[2] : undefined,
            default: match[3]
        }
    }

    function parseParams(params) {
        return params.map(param => parseParamString(param));
    }

</script>


<div>
    {#each Object.entries($strategies) as [name, params]}
        <Strategy {name} params={parseParams(params)} />
    {/each }
</div>
