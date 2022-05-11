function mason(){
	var $grid = $('.grid').masonry({});
	$grid.imagesLoaded().progress( function() {
		$grid.masonry('layout')
	})
}

Promise.all(Array.from(document.images).filter(img => !img.complete).map(img => new Promise(resolve => { img.onload = img.onerror = resolve; }))).then(() => {
    mason()
});

document.addEventListener('DOMContentLoaded', () => {
	document.querySelectorAll('button.store-card').forEach(button => {
		button.onclick = redirect
	});
});