window.onload = function(){
	var $grid = $('.grid').masonry({
    	// options...
	});
	// layout Masonry after each image loads
	$grid.imagesLoaded().progress( function() {
		$grid.masonry('layout');
	});
}
function search_items(search){
  	let regex = search ? (new RegExp(`.*${search}.*`)) : (new RegExp(".*"));

	$('div[searchable]').each( function(){
		if(regex.test($(this).attr('searchable').toLowerCase())){
			$(this).css('display', 'block')
			return
		}
		$(this).css('display', 'none')
	});
}
function apply_tags(id){
	$('div[tags]').each(function(){
		tags = $(this).attr('tags').split(/\s+/)
		for (let tag of tags){
			if(tag == id){
				$(this).css('display', 'block')
				return
			}
		}
		$(this).css('display', 'none')
	});
}