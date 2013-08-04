function resizeImages() {
	var wrappers = $('.search-top-wrapper');
	for (var i = 0; i < wrappers.length; i++) {
		var countString = i.toString();
		var wrapperId 	= '#top-'+countString;
		var imageId 	= '#image-'+countString;
		var rowHeight	= $(wrapperId).height();
		// alert(rowHeight);
		// alert(	'wrapperId = ' + wrapperId + '\n' +
		// 		'imageId = ' + imageId + '\n');
				 // + 'rowHeight = ' + rowHeight.toString());
		$(imageId).height(rowHeight);
	}
}