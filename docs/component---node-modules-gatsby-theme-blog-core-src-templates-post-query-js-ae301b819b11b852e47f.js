(self.webpackChunkgatsby_starter_blog_theme=self.webpackChunkgatsby_starter_blog_theme||[]).push([[177],{6558:function(t,e,r){"use strict";r.r(e),r.d(e,{default:function(){return w}});var n=r(6552),o=r(7294),u=r(9285),l=r(6725),i=r(6746),a=r(3739),c=r(2877),s=r(3431),p=function(t){return(0,s.tZ)(c.Ge.h1,t)},f=r(4038),x=r(4804),d=function(t){return(0,x.tZ)(c.Ge.p,(0,f.Z)({sx:{fontSize:1,mt:-3,mb:3}},t))},b=r(5444),y=r(7825),m=r(4123),g=r(6900),v=function(t){var e=t.previous,r=t.next;return(0,s.tZ)("footer",{css:(0,y.iv)({mt:4,pt:3})},(0,s.tZ)(c.Ge.hr,null),(0,s.tZ)(g.Z,null),(e||r)&&(0,s.tZ)(m.kC,{as:"ul",css:(0,y.iv)({flexWrap:"wrap",justifyContent:"space-between",listStyle:"none",padding:0})},(0,s.tZ)("li",null,e&&(0,s.tZ)(c.Ge.a,{as:b.rU,to:e.slug,rel:"prev"},"← ",e.title)),(0,s.tZ)("li",null,r&&(0,s.tZ)(c.Ge.a,{as:b.rU,to:r.slug,rel:"next"},r.title," →"))))},O=function(t){var e=t.text,r=t.url;return(0,s.tZ)(o.Fragment,null,e&&(0,s.tZ)(m.kC,null,r?(0,s.tZ)(c.Ge.a,{css:(0,y.iv)({margin:"auto",fontStyle:"italic"}),href:r,target:"_blank"},e):(0,s.tZ)(c.Ge.i,{css:(0,y.iv)({margin:"auto"})},e)))},Z=function(t){var e,r=t.post;return(0,s.tZ)(o.Fragment,null,(null==r||null===(e=r.image)||void 0===e?void 0:e.childImageSharp)&&(0,s.tZ)(o.Fragment,null,(0,s.tZ)(u.G,{image:(0,u.d)(r.image),alt:r.imageAlt?r.imageAlt:r.excerpt}),(0,s.tZ)(O,{text:r.imageCaptionText,url:r.imageCaptionLink})))},_=function(t){var e=t.data,r=e.post,n=e.site.siteMetadata.title,o=t.location,c=t.previous,f=t.next;return(0,s.tZ)(i.Z,{location:o,title:n},(0,s.tZ)(a.Z,{title:r.title,description:r.excerpt,imageSource:r.socialImage?(0,u.e)(r.socialImage):(0,u.e)(r.image),imageAlt:r.imageAlt}),(0,s.tZ)("main",null,(0,s.tZ)("article",null,(0,s.tZ)("header",null,(0,s.tZ)(Z,{post:r}),(0,s.tZ)(p,null,r.title),(0,s.tZ)(d,null,r.date)),(0,s.tZ)("section",null,(0,s.tZ)(l.MDXRenderer,null,r.body)))),(0,s.tZ)(v,{previous:c,next:f}))};function h(t,e){var r=Object.keys(t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(t);e&&(n=n.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),r.push.apply(r,n)}return r}function j(t){for(var e=1;e<arguments.length;e++){var r=null!=arguments[e]?arguments[e]:{};e%2?h(Object(r),!0).forEach((function(e){(0,n.Z)(t,e,r[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(r)):h(Object(r)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(r,e))}))}return t}var w=function(t){var e=t.location,r=t.data,n=r.blogPost,o=r.previous,u=r.next;return(0,s.tZ)(_,{data:j(j({},r),{},{post:n}),location:e,previous:o,next:u})}},6725:function(t,e,r){var n=r(3395);t.exports={MDXRenderer:n}},3395:function(t,e,r){var n=r(6191),o=r(1309),u=r(4176),l=r(3246),i=["scope","children"];function a(t,e){var r=Object.keys(t);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(t);e&&(n=n.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),r.push.apply(r,n)}return r}function c(t){for(var e=1;e<arguments.length;e++){var r=null!=arguments[e]?arguments[e]:{};e%2?a(Object(r),!0).forEach((function(e){u(t,e,r[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(r)):a(Object(r)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(r,e))}))}return t}var s=r(7294),p=r(4983).mdx,f=r(9480).useMDXScope;t.exports=function(t){var e=t.scope,r=t.children,u=l(t,i),a=f(e),x=s.useMemo((function(){if(!r)return null;var t=c({React:s,mdx:p},a),e=Object.keys(t),u=e.map((function(e){return t[e]}));return n(Function,["_fn"].concat(o(e),[""+r])).apply(void 0,[{}].concat(o(u)))}),[r,e]);return s.createElement(x,c({},u))}},6322:function(t){t.exports=function(t,e){(null==e||e>t.length)&&(e=t.length);for(var r=0,n=new Array(e);r<e;r++)n[r]=t[r];return n},t.exports.default=t.exports,t.exports.__esModule=!0},2771:function(t,e,r){var n=r(6322);t.exports=function(t){if(Array.isArray(t))return n(t)},t.exports.default=t.exports,t.exports.__esModule=!0},6191:function(t,e,r){var n=r(4675),o=r(5460);function u(e,r,l){return o()?(t.exports=u=Reflect.construct,t.exports.default=t.exports,t.exports.__esModule=!0):(t.exports=u=function(t,e,r){var o=[null];o.push.apply(o,e);var u=new(Function.bind.apply(t,o));return r&&n(u,r.prototype),u},t.exports.default=t.exports,t.exports.__esModule=!0),u.apply(null,arguments)}t.exports=u,t.exports.default=t.exports,t.exports.__esModule=!0},4176:function(t){t.exports=function(t,e,r){return e in t?Object.defineProperty(t,e,{value:r,enumerable:!0,configurable:!0,writable:!0}):t[e]=r,t},t.exports.default=t.exports,t.exports.__esModule=!0},5460:function(t){t.exports=function(){if("undefined"==typeof Reflect||!Reflect.construct)return!1;if(Reflect.construct.sham)return!1;if("function"==typeof Proxy)return!0;try{return Boolean.prototype.valueOf.call(Reflect.construct(Boolean,[],(function(){}))),!0}catch(t){return!1}},t.exports.default=t.exports,t.exports.__esModule=!0},1840:function(t){t.exports=function(t){if("undefined"!=typeof Symbol&&null!=t[Symbol.iterator]||null!=t["@@iterator"])return Array.from(t)},t.exports.default=t.exports,t.exports.__esModule=!0},9439:function(t){t.exports=function(){throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")},t.exports.default=t.exports,t.exports.__esModule=!0},1309:function(t,e,r){var n=r(2771),o=r(1840),u=r(4866),l=r(9439);t.exports=function(t){return n(t)||o(t)||u(t)||l()},t.exports.default=t.exports,t.exports.__esModule=!0},4866:function(t,e,r){var n=r(6322);t.exports=function(t,e){if(t){if("string"==typeof t)return n(t,e);var r=Object.prototype.toString.call(t).slice(8,-1);return"Object"===r&&t.constructor&&(r=t.constructor.name),"Map"===r||"Set"===r?Array.from(t):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?n(t,e):void 0}},t.exports.default=t.exports,t.exports.__esModule=!0}}]);
//# sourceMappingURL=component---node-modules-gatsby-theme-blog-core-src-templates-post-query-js-ae301b819b11b852e47f.js.map