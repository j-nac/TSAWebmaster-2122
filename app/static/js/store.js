function mason(){
	var $grid = $('.grid').masonry({});
	$grid.imagesLoaded().progress( function() {
		$grid.masonry('layout')
	})
}
document.addEventListener('DOMContentLoaded',()=>mason())