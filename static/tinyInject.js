var script= document.createElement('script');
script.type='text/javascript';
script.src="https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js";
document.head.appendChild(script);

script.onload=function(){

    tinymce.init({
    selector: "#id_content",
    width:800,
    height:500,
    plugins: [
        'advlist autolink link image lists charmap print preview hr anchor pagebreak',
        'searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking',
        'table emoticons template paste help','image code'
      ],
      toolbar: 'undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | ' +
        'bullist numlist outdent indent | link image | print preview media fullpage | ' +
        'forecolor backcolor emoticons | help',
      menu: {
        favs: {title: 'My Favorites', items: 'code visualaid | searchreplace | emoticons'}
      },
      menubar: 'favs file edit view insert format tools table help',
      content_css: 'css/content.css',
      images_upload_url: 'postAcceptor.php',
      images_upload_credentials: true,
      automatic_uploads: false,
      images_reuse_filename: true,
      block_unsupported_drop: false,
      file_picker_callback: function(callback, value, meta) {
        // Provide file and text for the link dialog
        if (meta.filetype == 'file') {
          callback('mypage.html', {text: 'My text'});
        }
    
        // Provide image and alt text for the image dialog
        if (meta.filetype == 'image') {
          callback('myimage.jpg', {alt: 'My alt text'});
        }
    
        // Provide alternative source and posted for the media dialog
        if (meta.filetype == 'media') {
          callback('movie.mp4', {source2: 'alt.ogg', poster: 'image.jpg'});
        }
      }
    });


   
}
