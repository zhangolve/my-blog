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

