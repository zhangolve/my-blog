webpack 5升級

webpack ^5.22.0
webpack-cli ^4.5.0
webpack-dev-server ^3.11.2


https://github.com/webpack/webpack-dev-server/issues/2759

遇到了这个问题，怎样解决呢？


webpack serve

更改脚本：


"start": "rimraf ./dist && webpack webpack-dev-server --config ./scripts/start.babel.js",

"start": "rimraf ./dist && webpack serve --config ./scripts/start.babel.js",


 Error: Unique ports must be specified for each devServer option in your webpack configuration. Alternatively, run only 1 devServer config using the --config-name flag to specify your desired config.
    at Object.startDevServer [as default] (/home/zhangolve/github/fe-crisis-management/node_modules/@webpack-cli/serve/lib/startDevServer.js:94:23)
    at Command.<anonymous> (/home/zhangolve/github/fe-c

解决办法：

暂时先用这样一个东西来搞：

export default getConfigs({
    mode: 'development',
    version: `${packageVersion}-${gitBranchName}`,
}).map((modules) => ({ ...modules, devServer }))[0];




错误提示：

 Error: Compiling RuleSet failed: Exclamation mark separated loader lists has been removed in favor of the 'use' property with arrays (at ruleSet[1].rules[5].loader: style-loader!css-loader)

 解决办法：

https://stackoverflow.com/questions/64785244/webpack-config-problems

style-loader!css-loader

{ test: /\.css$/, use: ['style-loader', 'css-loader'] },



[DEP_WEBPACK_COMPILATION_ASSETS] DeprecationWarning: Compilation.assets will be frozen in future, all modifications are deprecated.
BREAKING CHANGE: No more changes should happen to Compilation.assets after sealing the Compilation.
        Do changes to assets earlier, e. g. in Compilation.hooks.processAssets.
        Make sure to select an appropriate stage from Compilation.PROCESS_ASSETS_STAGE_*.
/home/zhangolve/github/fe-crisis-management/node_modules/extract-text-webpack-plugin/dist/index.js:211
          extractedChunk.index = i;
                               ^

TypeError: Cannot set property 'index' of undefined



升级 MiniCssExtractPlugin

const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
  plugins: [new MiniCssExtractPlugin()],
  module: {
    rules: [
      {
        test: /\.css$/i,
        use: [MiniCssExtractPlugin.loader, 'css-loader'],
      },
    ],
  },
};

https://webpack.js.org/plugins/mini-css-extract-plugin/

这些参数又都是什么意思呢？！！

所有用到的



This package has been deprecated
Author message:

Deprecated. Please use https://github.com/webpack-contrib/mini-css-extract-plugin
extract-text-webpack-plugin
DefinitelyTyped icon, indicating that this package has TypeScript declarations provided by the separate @types/extract-text-webpack-plugin package
3.0.2 • Public • Published 3 years ago


以下这些都需要升级到对应的版本：

copy-webpack-plugin@5.0.3 requires a peer of webpack@^4.0.0 but none is installed. You must install peer dependencies yourself.
npm WARN css-loader@3.0.0 requires a peer of webpack@^4.0.0 but none is installed. You must install peer dependencies yourself.
npm WARN eslint-loader@2.2.1 requires a peer of webpack@>=2.0.0 <5.0.0 but none is installed. You must install peer dependencies yourself.
npm WARN extract-text-webpack-plugin@4.0.0-beta.0 requires a peer of webpack@^3.0.0 || ^4.0.0 but none is installed. You must install peer dependencies yourself.
npm WARN file-loader@4.0.0 requires a peer of webpack@^4.0.0 but none is installed. You must install peer dependencies yourself.
npm WARN html-webpack-harddisk-plugin@1.0.1 requires a peer of html-webpack-plugin@^2.0.0 || ^3.0.0 but none is installed. You must install peer dependencies yourself.
npm WARN html-webpack-harddisk-plugin@1.0.1 requires a peer of webpack@^1.0.0 || ^2.0.0 || ^3.0.0 || ^4.0.0 but none is installed. You must install peer dependencies yo
urself.
npm WARN sass-loader@7.1.0 requires a peer of webpack@^3.0.0 || ^4.0.0 but none is installed. You must install peer dependencies yourself.
npm WARN string-replace-loader@2.2.0 requires a peer of webpack@1 || 2 || 3 || 4 but none is installed. You must install peer dependencies yourself.
npm WARN url-loader@2.0.1 requires a peer of webpack@^4.0.0 but none is installed. You must install peer dependencies yourself.

这些warning信息需要调整


https://www.npmjs.com/package/copy-webpack-plugin#transform

升级了一些依赖。。相应地，也需要做一些调整。

globOPtions

ignore


 Module build failed (from ./node_modules/sass-loader/dist/cjs.js):
ValidationError: Invalid options object. Sass Loader has been initialized using an options object that does not match the API schema.
 - options has an unknown property 'includePaths'. These properties are valid:
   object { implementation?, sassOptions?, additionalData?, sourceMap?, webpackImporter? }
    at validate (/home/zhangolve/github/fe-crisis-management/node_modules/webpack/node_modules/schema-utils/dist/validate.js:104:11)


sass-loader 升级之后引起的

https://www.youtube.com/watch?v=rrMGUnBmjwQ

loader 遇到了困难，看个视频了解下。

https://webpack.js.org/guides/asset-modules/


不用file-loader了，有点麻烦。能少用一个loader 就少用一个。

Asset Modules type replaces all of these loaders by adding 4 new module types:

asset/resource emits a separate file and exports the URL. Previously achievable by using file-loader.
asset/inline exports a data URI of the asset. Previously achievable by using url-loader.
asset/source exports the source code of the asset. Previously achievable by using raw-loader.
asset automatically chooses between exporting a data URI and emitting a separate file. Previously achievable by using url-loader with asset size limit.


根据文件类型选择不同的loader

js/ts 选择ts-loader 或者选择babel-loader会有很大的差别。选择ts-loader会更加严格
css, scss , scss-loader, css-loader 对scss文件进行处理，解析，通过minicss 插件将css文件分离出来
image, mp3, eot等资源文件， type='asset'进行处理


: Content not from webpack is served from /home/zhangolve/everbridge/fe-crisis-management/dist
✖ ｢wdm｣: Error: Path doesn't exist '/home/zhangolve/everbridge/fe-crisis-management/dist'
    at MemoryFileSystem.mkdirSync (/home/zhangolve/everbridge/fe-crisis-management/node_modules/memory-fs/lib/MemoryFileSystem.js:130:10)
    at MemoryFileSystem.<computed> [as mkdir] (/home/zhangolve/everbridge/fe-crisis-management/node_modules/memory-fs/lib/MemoryFileSystem.js:193:34)
    at mkdirp (/home/zhangolve/everbridge/fe-crisis-management/node_modules/webpack/lib/util/fs.js:198:5)
    at /home/zhangolve/everbridge/fe-crisis-management/node_modules/webpack/lib/Compiler.js:816:4
    at Hook.eval [as callAsync] (eval at create (/home/zhangolve/everbridge/fe-crisis-management/node_modules/webpack/node_modules/tapable/lib/HookCodeFactory.js:33:10), <anonymous>:4:1)
    at Hook.CALL_ASYNC_DELEGATE [as _callAsync] (/home/zhangolve/everbridge/fe-crisis-management/node_modules/webpack/node_modules/tapable/lib/Hook.js:18:14)
    at Compiler.emitAssets (/home/zhangolve/everbridge/fe-crisis-management/node_modules/webpack/lib/Compiler.js:813:19)
    at /home/zhangolve/everbridge/fe-crisis-management/node_modules/webpack/lib/Watching.js:79:21
    at processTicksAndRejections (internal/process/task_queues.js:79:11)

  
目前看来，没有太多头绪。只能通过排除法筛选错误。

后来通过pull最新代码解决了，我换了台电脑嘛

# next

ERROR in ./src/modules/DragTreeTheme/node-content-renderer.scss
Module build failed (from ./node_modules/mini-css-extract-plugin/dist/loader.js):
ModuleBuildError: Module build failed (from ./node_modules/css-loader/dist/cjs.js):
Error: Can't resolve '/static_cm_mgr/webfonts/fa-solid-900.eot?#iefix' in '/home/zhangolve/everbridge/fe-crisis-management/src/modules/DragTreeTheme'

我改变了，不用绝对路径了，然后使用~module 这样的方式来绕过去。
@font-face {
  font-family: "FontAwesome";
  font-style: normal;
  font-weight: 900;
  font-display:auto;src: url(https://baidu.com~@fortawesome/fontawesome-free/webfonts/fa-solid-900.eot);
  src: url(~@fortawesome/fontawesome-free/webfonts/fa-solid-900.eot?#iefix) format("embedded-opentype"),url(~@fortawesome/fontawesome-free/webfonts/fa-solid-900.woff2) format("woff2"),url(~@fortawesome/fontawesome-free/webfonts/fa-solid-900.woff) format("woff"),url(~@fortawesome/fontawesome-free/webfonts/fa-solid-900.ttf) format("truetype"),url(~@fortawesome/fontawesome-free/webfonts/fa-solid-900.svg#fontawesome) format("svg")
}


# next

Level 5: Runtime Errors.


npm start 出现了两个warning，然后正常的运行了。能够跑起来，但是到了浏览器端，却出现了问题。

ebGlobal.js?8723:7 Uncaught ReferenceError: process is not defined


https://stackoverflow.com/questions/41359504/webpack-bundle-js-uncaught-referenceerror-process-is-not-defined



Webpack 5 removes the ability to access environment variables using the notation process.env.MY_ENV_VAR. I had this same problem because I was getting a Uncaught ReferenceError: process is not defined error in my browser console. From the documentation of porting from v4 to v5 of Webpack, they mention the following:

1. Before upgrading to v5, verify that you can easily do it

Try to set the following options in your webpack 4 configuration and check if build still works correctly.

module.exports = {
   // ...
   node: {
       Buffer: false,
       process: false
   }
};
webpack 5 removes these options from the configuration schema and will always use false.

You have to remove these options again when upgrading your configuration for webpack 5.

2. Handling env vars because process was removed

Regarding Runtime Errors:
process is not defined.
webpack 5 does no longer include a polyfill for this Node.js variable. Avoid using it in the frontend code.
Want to support frontend and browser usage? Use the exports or imports package.json field to use different code depending on the environment.
Also use the browser field to support older bundlers,.
Alternative: Wrap code blocks with the typeof process checks. Note that this will have a negative impact on the bundle size.
Want to use environment variables with process.env.VARIABLE? You need to use the DefinePlugin or EnvironmentPlugin to define these variables in the configuration.
Consider using VARIABLE instead and make sure to check typeof VARIABLE !== 'undefined' too. process.env is Node.js specific and should be avoided in frontend code.
Therefore, given the above information, it is possible to use environment variables using one of the two plugins below.

const webpack = require("webpack");

module.exports = {
    ...
    plugins: [
        new webpack.DefinePlugin({
            "process.env.MY_ENV_VAR": JSON.stringify(process.env.MY_ENV_VAR)
        }),
        new webpack.EnvironmentPlugin(['MY_ENV_VAR']); // <--This is shorthand, does the same thing as the DefinePlugin
    ],
};

Then in your production code it's still feasable to refer to the environment variable in the same way, example:

console.log(process.env.MY_ENV_VAR);
However, as they said in the documentation included above, using process.env is NOT the recommended way since that is Node.js specific.

所以，为什么webpack 要做这些改动呢？！！

干净

# next
StyledComponent.js:265 Uncaught Error: Element type is invalid: expected a string (for built-in components) or a class/function (for composite components) but got: undefined. You likely forgot to export your component from the file it's defined in, or you might have mixed up default and named imports.
    at createFiberFromTypeAndProps (StyledComponent.js:265)
    at createFiberFromElement (StyledComponent.js:265)
    at reconcileSingleElement (StyledComponent.js:265)
    at reconcileChildFibers (StyledComponent.js:265)
    at reconcileChildren (StyledComponent.js:265)
    at updateHostRoot (StyledComponent.js:265)
    at beginWork (StyledComponent.js:265)
    at HTMLUnknownElement.callCallback (StyledComponent.js:265)
    at Object.invokeGuardedCallbackDev (StyledComponent.js:265)
    at invokeGuardedCallback (StyledComponent.js:265)

    这个错误，怀疑和之前start成功后报出的warning信息有关。

    