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

	$('item[id]').each( function(){ 
		console.log(Object.keys(this))
		console.log(this.className)
		ids = this.id.split(/\s+/)
		for (let id of ids){
			if(regex.test(id)){
				this.css('display', 'block')
				continue
			}
		}
		this.css('display', 'none')
	});
}
function apply_tags(tag){
	$(`div[class]`).each(function(){
		classes = this.className.split(/\s+/)
		for (let name of classes){
			if(name == tag){
				this.css('display', 'block')
			}
		}
		this.css('display', 'none')
	});
}