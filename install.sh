npm install hexo-cli gulp -g

directory="hexo-blog"

rm -rf hexo-blog

mkdir hexo-blog
cd hexo-blog
hexo init
npm install hexo-deployer-git --save
npm install hexo-generator-feed --save
npm install hexo-generator-sitemap --save
npm install hexo-next-giscus --save
npm install hexo-theme-next --save

rm -rf source/_posts/*
        
cp ../hexo/* . -r
cp -r ../20{20..99}/ source/_posts/
