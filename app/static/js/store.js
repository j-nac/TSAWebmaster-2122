function mason(){
	var $grid = $('.grid').masonry({});
	$grid.imagesLoaded().progress( function() {
		$grid.masonry('layout')
	})
}
document.addEventListener('DOMContentLoaded', () => {
	document.querySelectorAll('button.page-nav').forEach(button => {
		button.onclick = redirect
	});
});