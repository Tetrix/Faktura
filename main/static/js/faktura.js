function deleteArticle (el)
{   
    $.ajax({
      type: 'POST',
      url: "/articles/delete_article",
      data: {
        article_id:el.value,
        csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
        },
      success: function( returnedData ) {
    $( '#list_articles' ).html( returnedData );
  }
    });
}


function deleteImport (el)
{   
    $.ajax({
      type: 'POST',
      url: "/imports/delete_import",
      data: {
        import_id:el.value,
        csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
        packing_list:$("#id_add_packing_list").val(),
        },
      success: function( returnedData ) {
    $( '#list_imports' ).html( returnedData );
  }
    });
}