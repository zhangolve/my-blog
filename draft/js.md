https://nodejs.org/en/blog/release/v15.0.0/


Node.js 15 comes with a new major release of npm, npm 7. npm 7 comes with many new features - including npm workspaces and a new package-lock.json format. npm 7 also includes yarn.lock file support. One of the big changes in npm 7 is that peer dependencies are now installed by default.

nodejs 14 可以，但是15不可以。

In this setup, index.js explicitly requires lodash to be present, and binds it as _ (no global scope pollution). By stating what dependencies a module needs, webpack can use this information to build a dependency graph. It then uses the graph to generate an optimized bundle where scripts will be executed in the correct order.

With that said, let's run npx webpack, which will take our script at src/index.js as the entry point, and will generate dist/main.js as the output. The npx command, which ships with Node 8.2/npm 5.2.0 or higher, runs the webpack binary (./node_modules/.bin/webpack) of the webpack package we installed in the beginning:


https://webpack.js.org/guides/getting-started/


