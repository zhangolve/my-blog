cd hexo-blog
cp ../hexo/_next_theme_config.yml themes/next/_config.yml
env_variable="valine"
valine="$($env_variable)"
echo "$valine" >> themes/next/_config.yml
echo "hexo clean start"
hexo clean
echo "hexo clean end"
echo "hexo g start"
hexo g
echo "hexo g end"
