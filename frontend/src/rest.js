import { get } from 'svelte/store';
import { tasks, config, strategies } from './stores';


export async function loadTasks() {
    return fetch("/api/tasks/get")
    .then(async res => {
        if (res.ok) {
            console.log("Setting tasks")
            let data = await res.json();
            tasks.set(data, true);
        } else {
            console.log(res);
        }
    });
}


export async function saveTasks() {
    return fetch("/api/tasks/save", {
        method: "POST",
        headers: { 
            "Content-Type": "application/json"
        },
        body: JSON.stringify(get(tasks))
    }).then(async res => {
        if (res.ok) {
            return new Promise(async (resolve, reject) =>{
                let data = await res.json()
                resolve(data["saved"]);
            })
        } else {
            console.log("Error updating tasks", res);
        }
    });
}


export async function loadConfig() {
    return fetch("/api/config/current")
    .then(async res => {
        if (res.ok) {
            let data = await res.json();
            config.set(data, true);
        } else {
            console.log(res);
        }
    });
}

export async function saveConfig() {}


export async function loadStrategies() {
    return fetch("/api/strategies/get")
    .then(async res => {
        if (res.ok) {
            let data = await res.json();
            strategies.set(data, true);
        } else {
            console.log(res);
        }
    });
}
