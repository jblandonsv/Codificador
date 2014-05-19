/**
 * Created by ocaceres on 11-07-13.
 */
// Get the ul that holds the collection of tags
var collectionHolder = $('ul.preguntas');

// setup an "add a tag" link
var $addPreguntaLink = $('<a href="#" class="add_pregunta_link">Agregar Expediente o Documentos</a>');
var $newLinkLi = $('<li></li>').append($addPreguntaLink);


$(document).ready(function(){
	
	
    // add a delete link to all of the existing tag form li elements
    collectionHolder.find('li').each(function() {
        addPreguntaFormDeleteLink($(this));
    });

    // add the "add a tag" anchor and li to the tags ul
    collectionHolder.append($newLinkLi);

    // count the current form inputs we have (e.g. 2), use that as the new
    // index when inserting a new item (e.g. 2)
    collectionHolder.data('index', collectionHolder.find(':input').length);

    $addPreguntaLink.on('click', function(e) {
        // prevent the link from creating a "#" on the URL
        e.preventDefault();

        // add a new tag form (see next code block)
        addPreguntaForm(collectionHolder, $newLinkLi);
    });


});

function addPreguntaForm(collectionHolder, $newLinkLi) {
    // Get the data-prototype explained earlier
    var prototype = collectionHolder.data('prototype');

    // get the new index
    var index = collectionHolder.data('index');

    // Replace '__name__' in the prototype's HTML to
    // instead be a number based on how many items we have
    var newForm = prototype.replace(/__name__/g, index);

    // increase the index with one for the next item
    collectionHolder.data('index', index + 1);

    // Display the form in the page in an li, before the "Add a tag" link li
    var $newFormLi = $('<li></li>').append(newForm);
    $newLinkLi.before($newFormLi);

    // add a delete link to the new form
    addPreguntaFormDeleteLink($newFormLi);
}
function addPreguntaFormDeleteLink($tagFormLi) {
    var $removeFormA = $('<a href="#">Borrar</a><br /><br /><hr /><br />');
    $tagFormLi.append($removeFormA);

    $removeFormA.on('click', function(e) {
        // prevent the link from creating a "#" on the URL
        e.preventDefault();

        // remove the li for the tag form
        $tagFormLi.remove();
    });
}