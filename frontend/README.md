# Frontend

Frontend source code using SvelteJS

## Development

Install the dependencies...

```bash
cd frontend/
npm install
```

...then start [Rollup](https://rollupjs.org) which will autobuild as you edit and save your files:

```bash
npm run dev
```

Rollup will also start a development server in the 5777 port. **Do not try to use the UI through that endpoint**, you should
start the flask development server and access the application through it to have the API respond correctly.


## Building

To create an optimised version of the app:

```bash
npm run build
```