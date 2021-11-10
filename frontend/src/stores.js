import { get, writable } from "svelte/store";

function createCheckpointStore(value) {
        const { subscribe, set, update } = writable({});
        let original_set = set;

        class Store {
            constructor(value) {
                this.checkpoint = writable(value);
                this.set(value)
            }

            set(value, is_checkpoint=false) {
                original_set(value);
                if (is_checkpoint) {
                    this.updateCheckpoint(value)
                }
            }

            updateCheckpoint(value = null) {
                if (value !== null) {
                    this.checkpoint.set(JSON.parse(JSON.stringify(value)));
                } else {
                    this.checkpoint.set(JSON.parse(JSON.stringify(get(this))));
                }
            }
					
            subscribe = subscribe;
            update = update;
        }

        let store = new Store(value);
        return store;
}

export const tasks = createCheckpointStore([]);
export const config = createCheckpointStore({});
export const contracts = writable([]);
export const strategies = writable([]);