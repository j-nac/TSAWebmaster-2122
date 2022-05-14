function mason(){
	var $grid = $('.grid').masonry({'isFitWidth': true});
	$grid.imagesLoaded().progress( function() {
		$grid.masonry('layout')
	})
}

function loadstore(){
	Promise.all(Array.from(document.images).filter(img => !img.complete).map(img => new Promise(resolve => { img.onload = img.onerror = resolve; }))).then(() => {
		mason()
	});

	document.querySelectorAll('button.store-card').forEach(button => {
		button.onclick = redirect
	});
	document.getElementById('searchbox').onsubmit = function(){
		$.ajax({
			url:'/store?'+$('#searchbox').serializeArray().map(e=>e['name']+'='+e['value']).join('&'),
			type: 'STATIC',
			success: function(data){
				let group = document.getElementById('page')
				let newpage = document.createElement('div')
				newpage.innerHTML = data
				group.children[0].remove()
				newpage.id = 'newpage'
				group.appendChild(newpage)
				loadstore()
			}
		})
		return false
	}
}
