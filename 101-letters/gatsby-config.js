module.exports = {
  plugins: [
    {
      resolve: `gatsby-theme-blog`,
      options: {
        contentPath: 'content/posts/101xin'
      },
    },
  ],
  // ➜  posts git:(master) ✗ ln -snf /home/zhangolve/github/my-blog/101xin ./
  // Customize your site metadata:

  // cp -r dir1/* dir2

  siteMetadata: {
    title: `My Blog Title`,
    author: `My Name`,
    description: `My site description...`,
    social: [
      {
        name: `twitter`,
        url: `https://twitter.com/gatsbyjs`,
      },
      {
        name: `github`,
        url: `https://github.com/gatsbyjs`,
      },
    ],
  },
}
