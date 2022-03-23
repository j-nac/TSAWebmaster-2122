var $grid = $('.grid').masonry({
	itemSelector: '.visible-item'
});
function mason(){
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
			$(this).addClass('visible-item')
			return
		}
		$(this).css('display', 'none')
		$(this).removeClass('visible-item')
	});
	$grid.isotope({itemSelector:'.visible-item'})
}
searched_tags = []
function toggle_tag(id){
	for(i in searched_tags){
		if (searched_tags[i] == id){
			searched_tags.pop(i)
			return
		}
	}
	searched_tags.push(id)
}
function apply_tag(id){
	toggle_tag(id.toLowerCase())
	$('div[tags]').each(function(){
		tags = $(this).attr('tags').split(/\s+/)
		for(tag of tags){
			if(searched_tags.includes(tag.toLowerCase()) || searched_tags.length==0){
				console.log('found')
				$(this).css('display', 'block')
				$(this).addClass('visible-item')
				return
			}
		}
		$(this).css('display', 'none')
		$(this).removeClass('visible-item')
	});
	$grid.isotope({itemSelector:'.visible-item'})
}

window.onload = mason