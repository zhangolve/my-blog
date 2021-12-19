module.exports = {
  plugins: [
    {
      resolve: `@zhangolve/gatsby-theme-blog`,
      options: {
        contentPath: 'content/posts'
      },
    },
  ],
  // ➜  posts git:(master) ✗ ln -snf /home/zhangolve/github/my-blog/101xin ./
  // Customize your site metadata:

  // cp -r dir1/* dir2

  siteMetadata: {
    title: `101封信`,
    author: `爱你的zxw`,
    description: `写给宝贝的101封信`,
    social: [
     
    ],
  },
}
