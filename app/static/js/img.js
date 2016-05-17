function BigImg(bi_action, bi_url)
{
  	msg_prev = "prev";
  	msg_next = "next";
  	msg_close = "close";

  	if(bi_action == "open")
  	{
  		document.getElementById("big_img").style.visibility = "visible";
  		if(typeof(arr_images) != "undefined")
  		{
  			bi_prev = "";
  			bi_next = "";
  			bi_select = "";


            for (i=0; i<arr_images.length; i++)
                if (arr_images[i] == bi_url)
                    j=i;

            if (j!=arr_images.length-1)
                bi_next = "<a href=javascript:BigImg('open','"+arr_images[j+1]+"')>" + msg_next + "</a>";
            if (j!=0)
                bi_prev = "<a href=javascript:BigImg('open','"+arr_images[j-1]+"')>" + msg_prev + "</a>";


  			document.getElementById("here_img").innerHTML = "<img src='"+arr_images[j]+"' border=0  OnClick=BigImg('open','"+arr_images[j+1]+"'); ><br><div class='nav_l'>"+bi_prev+bi_next+"</div><div class='nav_r'><a href=javascript:BigImg('close');>"+msg_close+"</a></div>";
  		}
  		else
  		{
  			document.getElementById("here_img").innerHTML = "<img src="+bi_url+" border=0><br><div class='nav_r'><a href=javascript:BigImg('close');>"+msg_close+"</a></div>";
  		}
  	}
  	else
  	{
  		document.getElementById("here_img").innerHTML = "";
  		document.getElementById("big_img").style.visibility = "hidden";
  	}
  }


var arr_images = new Array(

    "static/images/p1.jpg",
    "static/images/p2.jpg",
    "static/images/p3.jpg",
    "static/images/p4.jpg",
    "static/images/p5.jpg",
    "static/images/p6.jpg",
    "static/images/p7.jpg",
    "static/images/p8.jpg",
    "static/images/p9.jpg",
    "static/images/p10.jpg",
    "static/images/p11.jpg",
    "static/images/p12.jpg",
    "static/images/p13.jpg",
    "static/images/p14.jpg",
    "static/images/p15.jpg",
    "static/images/p16.jpg",
    "static/images/p17.jpg",
    "static/images/p18.jpg",
    "static/images/p19.jpg",
    "static/images/p20.jpg",
    "static/images/p21.jpg",
    "static/images/p22.jpg",
    "static/images/p23.jpg",
    "static/images/p24.jpg");

