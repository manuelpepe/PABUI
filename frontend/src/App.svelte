<script>
	import { Router, Route, Link } from "svelte-navigator";
	import TasksView from './views/tasks/TasksView.svelte';
	import ConfigsView from './views/config/ConfigView.svelte';
	import { loadConfig, loadTasks, loadStrategies } from "./rest";
	import StrategiesView from "./views/strategies/StrategiesView.svelte";

	let project;

	loadConfig()
	loadTasks();
	loadStrategies();

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
	<h1>PyAutoBlockchain</h1>
	<p>Project: {project}</p>
</header>

<aside class="sidebar">
	<nav>
		<Link to="/tasks">Tasks</Link>
		<Link to="/config">Config</Link>
		<Link to="/strategies">Strategies</Link>
	</nav>
</aside>


<main>

	
	<Route path="tasks">
		<TasksView />
	</Route>
	<Route path="config">
		<ConfigsView/>
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
</style>