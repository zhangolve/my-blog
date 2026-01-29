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
cp ../2020/  source/_posts/ -r
cp ../2021/  source/_posts/ -r
cp ../2022/  source/_posts/ -r
cp ../2023/  source/_posts/ -r
cp ../2024/  source/_posts/ -r
cp ../2025/  source/_posts/ -r
