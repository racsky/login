// 等待文档加载完毕后执行
$(function(){

	// 图片轮播
	var imgIndex = 0;  //图片下标
	var timerId;    //保存定时器ID
	timerId = setInterval(autoPlay,1800);   //开启定时器

	// 定时器方法，每隔一秒执行一次
	function autoPlay(){
		
		// 获取图片，根据下标设置元素显示与隐藏
		// 隐藏当前下标对应的图片
		$('.banner img').eq(imgIndex).css('display','none');

		// 更新下标，防止越界
		imgIndex = ++ imgIndex == $('.banner img').length ? 0 : imgIndex;
		
		// 显示下一张图片
		$('.banner img').eq(imgIndex).css('display','block');
	};

});


