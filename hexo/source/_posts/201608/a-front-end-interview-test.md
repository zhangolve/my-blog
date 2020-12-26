title: 一道前端面试题
date: 2016-08-27  16:49:49 
categories: 前端
tags: [算法,javascript] 
description: 



---

前端面试题

这道面试题内容是：

> 给定N个字符串，找出其中重复的字符串和它重复的次数。

<!--more-->

这本身看似简单，但是这里面有一个问题。如果有不止一个重复的字符串怎么办？

当时一时没有思路，后来就是觉得要先找到那个不重复的数组，然后就一直写下去了。

```javascript
function findMax(Arr)
{
  
  var n=[];  //构建一个不重复的数组
  for(var i=0;i<Arr.length;i++)
    {
      if(n.indexOf(Arr[i])==-1)
        {
          n.push(Arr[i]);
          
        }
    }
  
  var count=[];  //构建一个数组，对每一个不重复的数组中的值进行计数，将这些数字填入到这个数组中
 for( var m=0;m<n.length;m++)　　//这个遍历在实际面试中手写代码没有写出来。
   {
  count[m]=0;
   }
  
  
  for( var j=0;j<n.length;j++) //遍历来对每一个不重复的数组中的值进行计数
    {
      for(var k=0;k<Arr.length;k++)
        {
          
          if(n[j]==Arr[k])
            {
              count[j]++;
              
              
            }
        }
      
    }
  var finalArr=[];  //构建一个空数组进行表现最终结果
  for(m=0;m<count.length;m++)
    {
      if(count[m]!=1)  //如果不重复count[m]应当为1
        {
         finalArr.push([n[m],count[m]])//如果不重复，把重复的字符串和重复次数推入到最终数组中
        }
    }
  console.log(finalArr);
}

findMax(['22','33','33','44','55','66','55','66','a','a']);


```


后来我其实尝试着使用forEach()方法来重新构造这个算法，但是发现使用forEach的话并没有想象中那么简洁，例如在这个算法中的二重遍历时就不适宜使用forEach。