<script>
	import { Router, Route, Link } from "svelte-navigator";
	import TasksView from './views/tasks/TasksView.svelte';
	import ConfigsView from './views/config/ConfigView.svelte';
	import ContractsView from "./views/contracts/ContractsView.svelte";
	import StrategiesView from "./views/strategies/StrategiesView.svelte";
	import { loadConfig, loadTasks, loadStrategies, loadContracts } from "./rest";

	let project;

	loadConfig()
	loadTasks();
	loadStrategies();
	loadContracts();

	fetch("/api/app/get")
	.then(async (res) => {
		if (res.ok) {
			let data = await res.json();
			project = data.directory;
		} else {
			project = "Not loaded";
		}
	});
</script>


<Router>

<header>
	<h2>PyAutoBlockchain</h2>
	<p>Project: {project}</p>
</header>

<aside class="sidebar">
	<nav>
		<Link class="navlink" to="/tasks">Tasks</Link>
		<Link class="navlink" to="/config">Config</Link>
		<Link class="navlink" to="/contracts">Contracts</Link>
		<Link class="navlink" to="/strategies">Strategies</Link>
	</nav>
	<nav>
		<a class="navlink" href="https://github.com/manuelpepe/PyAutoBlockchain" target="_blank" rel="noopener noreferrer">PAB</a>
		<a class="navlink" href="https://github.com/manuelpepe/PABUI" target="_blank" rel="noopener noreferrer">PABUI</a>
	</nav>
</aside>


<main>
	<Route path="tasks">
		<TasksView />
	</Route>
	<Route path="config">
		<ConfigsView/>
	</Route>
	<Route path="contracts">
		<ContractsView/>
	</Route>
	<Route path="strategies">
		<StrategiesView/>
	</Route>
</main>

</Router>


<style>
main {
	width: 70%;
}

header {
	width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

header h2 {
	margin: 0;
}

.sidebar {
	margin-bottom: 1em;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.sidebar nav {
	display: flex;
    flex-direction: row;
    justify-content: space-around;
    width: 15%;
}
</style>