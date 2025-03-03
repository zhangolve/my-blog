npm install hexo-cli gulp -g

directory="hexo-blog"

rm -rf hexo-blog

mkdir hexo-blog
cd hexo-blog
hexo init
npm install hexo-deployer-git --save
npm install hexo-generator-feed --save
npm install hexo-generator-sitemap --save
git clone https://github.com/theme-next/hexo-theme-next themes/next
rm -rf source/_posts/*
        
cp ../hexo/* . -r
cp ../2020/  source/_posts/ -r
cp ../2021/  source/_posts/ -r
cp ../2022/  source/_posts/ -r
cp ../2023/  source/_posts/ -r
cp ../2024/  source/_posts/ -r
cp ../2025/  source/_posts/ -r
